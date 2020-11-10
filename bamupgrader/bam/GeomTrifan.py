from panda3d import core
from .Geom import Geom

class GeomTrifan(Geom):

    def __init__(self, bam_file, bam_version):
        Geom.__init__(self, bam_file, bam_version)

    def load(self, di):
        Geom.load(self, di)

    def write(self, write_version, dg):
        Geom.write(self, write_version, dg)

    def create_primitive(self):
        return core.GeomTrifans(core.Geom.UH_static)

    def __str__(self):
        return f'GeomTrifan({Geom.__str__(self)})'
