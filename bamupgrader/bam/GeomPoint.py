from panda3d import core
from .Geom import Geom

class GeomPoint(Geom):

    def __init__(self, bam_file, bam_version):
        Geom.__init__(self, bam_file, bam_version)

    def load(self, di):
        Geom.load(self, di)
        self.size = di.get_uint32()

    def write(self, write_version, dg):
        Geom.write(self, write_version, dg)
        dg.add_uint32(self.size)

    def create_primitive(self):
        return core.GeomPoints(core.Geom.UH_static)

    def __str__(self):
        return f'GeomPoint(size={self.size}, {Geom.__str__(self)})'
