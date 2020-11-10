from panda3d import core
from p3bamboo.BamGlobals import read_vec3, write_vec
from .CollisionSolid import CollisionSolid

class CollisionSphere(CollisionSolid):

    def __init__(self, bam_file, bam_version):
        CollisionSolid.__init__(self, bam_file, bam_version)

    def load(self, di):
        CollisionSolid.load(self, di)
        self.center = read_vec3(di)
        self.radius = di.get_float32()

    def write(self, write_version, dg):
        CollisionSolid.write(self, write_version, dg)
        write_vec(dg, self.center)
        dg.add_float32(self.radius)

    def create_node(self):
        return core.CollisionSphere(self.center, self.radius)

    def __str__(self):
        return f'CollisionSphere(center={self.center}, radius={self.radius}, {CollisionSolid.__str__(self)})'
