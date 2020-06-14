from xml.etree import ElementTree as XML
from xml.etree.ElementTree import Element, ElementTree

ASSET = """
    <asset>
        <contributor>
            <author>ACExplorer</author>
        </contributor>
        <unit name="meter" meter="1"/>
        <up_axis>Z_UP</up_axis>
    </asset>
"""


class Collada:
    def __init__(self):
        self._collada = Element(
            "COLLADA",
            {
                "xmlns": "http://www.collada.org/2005/11/COLLADASchema",
                "version": "1.4.1",
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"
            }
        )
        self._collada.append(XML.fromstring(ASSET))
        self._dae = ElementTree(self._collada)
        self._collada.append(Element("library_effects"))
        self._collada.append(Element("library_images"))
        self._collada.append(Element("library_materials"))
        self._collada.append(Element("library_geometries"))
        self._collada.append(Element("library_controllers"))
        self._collada.append(Element("library_visual_scenes"))
        self._collada.append(Element("scene"))

    def to_string(self):
        return XML.tostring(self._collada, "unicode")

    def save(self, path: str):
        self._dae.write(path, "unicode")


if __name__ == '__main__':
    print(Collada().to_string())
