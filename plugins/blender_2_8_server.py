from multiprocessing.connection import Listener
import threading
import queue
import bpy
import bmesh
import mathutils

command_queue = queue.Queue()


class Server(threading.Thread):
    def __init__(self, address):
        threading.Thread.__init__(self)
        self.address = address
        self.main_thread = next(
            th for th in threading.enumerate() if th.__class__.__name__ == "_MainThread"
        )
        self.stay_alive = True

    def run(self):
        serv = Listener(self.address)
        while self.main_thread.is_alive():
            client = Child(serv)
            client.start()
            while self.main_thread.is_alive() and client.is_alive():
                pass
        serv.close()


class Child(threading.Thread):
    def __init__(self, server):
        threading.Thread.__init__(self)
        self.server = server
        self.connected = False

    def run(self):
        try:
            client = self.server.accept()
        except:
            return
        self.connected = True
        while self.connected:
            try:
                msg = client.recv()
                command_queue.put(msg)
            except EOFError:
                self.connected = False


def process_command_queue():
    while not command_queue.empty():
        msg = command_queue.get()
        if isinstance(msg, dict) and msg.get("type", None) == "MESH":
            armature_object = None
            if "bone_id_trm" in msg and isinstance(msg["bone_id_trm"], dict):
                if bpy.ops.object.mode_set.poll():
                    bpy.ops.object.mode_set(mode="OBJECT")

                bpy.ops.object.armature_add()
                armature = bpy.data.armatures[-1]
                armature_object = bpy.data.objects[0]
                armature_object.show_in_front = True

                armature.display_type = "STICK"
                bpy.context.view_layer.update()

                if bpy.ops.object.mode_set.poll():
                    bpy.ops.object.mode_set(mode="EDIT")

                for bone in armature.edit_bones:
                    armature.edit_bones.remove(bone)

                edit_bones = {
                    bone_id: armature.edit_bones.new(bone_id)
                    for bone_id in msg["bone_id_trm"].keys()
                }

                for bone_id, (matrix, _) in msg["bone_id_trm"].items():
                    edit_bone = edit_bones[bone_id]
                    edit_bone.tail = (0, 0, 0.1)
                    edit_bone.transform(mathutils.Matrix(matrix))

                for bone_id, (_, parent_bone_id) in msg["bone_id_trm"].items():
                    if parent_bone_id in edit_bones:
                        edit_bone_ = armature.edit_bones.new(f"{bone_id}_")
                        edit_bone__ = armature.edit_bones.new(f"{bone_id}__")
                        edit_bone = edit_bones[bone_id]

                        edit_bone_.parent = edit_bones[parent_bone_id]
                        edit_bone_.use_connect = True
                        edit_bone_.hide = True
                        edit_bone_.tail = edit_bones[parent_bone_id].head
                        edit_bone__.parent = edit_bone_
                        edit_bone__.use_connect = True
                        edit_bone__.hide = True
                        edit_bone__.tail = edit_bone.head
                        edit_bone.parent = edit_bone__
                        edit_bone.use_connect = True

                if bpy.ops.object.mode_set.poll():
                    bpy.ops.object.mode_set(mode="OBJECT")

            print("loading mesh")
            if bpy.ops.object.mode_set.poll():
                bpy.ops.object.mode_set(mode="OBJECT")

            verts = msg.get("verts", [])
            tverts = msg.get("tverts", [])

            mesh_data = bpy.data.meshes.new("mesh_data")

            bm = bmesh.new()
            # add verts
            [bm.verts.new(v) for v in verts]
            bm.verts.ensure_lookup_table()

            material_index = 0
            for faces in msg.get("faces", []):
                # add faces
                for f in faces:
                    ai, bi, ci = f
                    a = bm.verts[ai]
                    b = bm.verts[bi]
                    c = bm.verts[ci]
                    face = bm.faces.new((a, b, c))
                    face.material_index = material_index
                material_index += 1

            bm.to_mesh(mesh_data)
            bm.free()
            mesh_data.update()

            mesh_object = bpy.data.objects.new("Mesh_Object", mesh_data)

            # weights
            groups = {}
            weights = msg.get("bone_weights", [])
            for vert_index, weight_datas in enumerate(weights):
                for group_name, weight in weight_datas:
                    groups.setdefault(group_name, {})
                    groups[group_name].setdefault(weight, [])
                    groups[group_name][weight].append(vert_index)

            for group_name in groups.keys():
                mesh_object.vertex_groups.new(name=group_name)
                for weight in groups[group_name]:
                    mesh_object.vertex_groups[group_name].add(
                        groups[group_name][weight], weight / 255, "REPLACE"
                    )

            bpy.context.collection.objects.link(mesh_object)

            if armature_object is not None:
                mesh_object.parent = armature_object
                modifier = mesh_object.modifiers.new(type="ARMATURE", name="Armature")
                modifier.object = armature_object
                modifier.use_bone_envelopes = True

        else:
            print("{}\n{}".format(type(msg), msg))

    return 0.2


bpy.app.timers.register(process_command_queue)
s = Server(("", 6163))
s.start()
