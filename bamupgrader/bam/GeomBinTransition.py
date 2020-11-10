from panda3d.core import CullBinAttrib
from .OnOffTransition import OnOffTransition

class GeomBinTransition(OnOffTransition):

    def __init__(self, bam_file, bam_version):
        OnOffTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnOffTransition.load(self, di)
        self.value = di.get_string()
        self.draw_order = di.get_int32()

    def write(self, write_version, dg):
        OnOffTransition.write(self, write_version, dg)
        dg.add_string(self.value)
        dg.add_int32(self.draw_order)

    def apply(self, nodePath):
        attrib = CullBinAttrib.make(self.value, self.draw_order)
        nodePath.setAttrib(attrib)

    def __str__(self):
        return f'GeomBinTransition(value={self.value}, draw_order={self.draw_order}, {OnOffTransition.__str__(self)})'
