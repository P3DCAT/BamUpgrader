from panda3d.core import LMatrix4f
from .MovingPartMatrix import MovingPartMatrix

# This represents one joint of the character's
# animation, containing an animating transform matrix.
class CharacterJoint(MovingPartMatrix):

    def __init__(self, bam_file, bam_version):
        MovingPartMatrix.__init__(self, bam_file, bam_version)
        self.net_arcs = []
        self.local_arcs = []
        self.initial_net_transform_inverse = LMatrix4f()

    def load(self, di):
        MovingPartMatrix.load(self, di)
        num_net_arcs = di.get_uint16()
        self.net_arcs = [self.bam_file.read_pointer(di) for i in range(num_net_arcs)] # NodeRelation
        num_local_arcs = di.get_uint16()
        self.local_arcs = [self.bam_file.read_pointer(di) for i in range(num_local_arcs)] # NodeRelation
        self.initial_net_transform_inverse.read_datagram(di)

    def write(self, write_version, dg):
        MovingPartMatrix.write(self, write_version, dg)
        dg.add_uint16(len(self.net_arcs))

        for arc in self.net_arcs:
            self.bam_file.write_pointer(dg, arc) # NodeRelation

        dg.add_uint16(len(self.local_arcs))

        for arc in self.local_arcs:
            self.bam_file.write_pointer(dg, arc) # NodeRelation

        self.initial_net_transform_inverse.write_datagram(dg)

    def __str__(self):
        return f'CharacterJoint(net_arcs={self.net_arcs}, local_arcs={self.local_arcs}, initial_net_transform_inverse={self.initial_net_transform_inverse}, {MovingPartMatrix.__str__(self)})'
