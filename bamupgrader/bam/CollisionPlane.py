from panda3d import core
from .CollisionSolid import CollisionSolid

class CollisionPlane(CollisionSolid):

    def __init__(self, bam_file, bam_version):
        CollisionSolid.__init__(self, bam_file, bam_version)
        self.plane = core.LPlanef()

    def load(self, di):
        CollisionSolid.load(self, di)
        self.plane.read_datagram(di)

    def write(self, write_version, dg):
        CollisionSolid.write(self, write_version, dg)
        self.plane.write_datagram(dg)

    def create_node(self):
        return core.CollisionPlane(self.plane)

    def __str__(self):
        return f'CollisionPlane(plane={self.plane}, {CollisionSolid.__str__(self)})'
