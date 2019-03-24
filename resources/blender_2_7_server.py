from multiprocessing.connection import Listener
import threading
import bpy


class Server(threading.Thread):
	def __init__(self, address):
		threading.Thread.__init__(self)
		self.address = address
		self.main_thread = next(th for th in threading.enumerate() if th.__class__.__name__ == '_MainThread')
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
				if isinstance(msg, dict) and msg.get('type', None) == 'MESH':
					verts = msg.get('verts', [])
					faces = msg.get('faces', [])
					mesh_data = bpy.data.meshes.new("cube_mesh_data")
					mesh_data.from_pydata(verts, [], faces)
					mesh_data.update()

					obj = bpy.data.objects.new("My_Object", mesh_data)

					scene = bpy.context.scene
					scene.objects.link(obj)
					# obj.select = True
				else:
					print('{}\n{}'.format(type(msg), msg))
			except EOFError:
				self.connected = False


s = Server(('', 6163))
s.start()
