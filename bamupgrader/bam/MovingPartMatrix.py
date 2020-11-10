from panda3d.core import LMatrix4f
from .MovingPartBase import MovingPartBase

# This is a particular kind of MovingPart that accepts
# a matrix each frame.
class MovingPartMatrix(MovingPartBase):

    def __init__(self, bam_file, bam_version):
        MovingPartBase.__init__(self, bam_file, bam_version)
        self.matrix = LMatrix4f()
        self.initial_matrix = LMatrix4f()

    def load(self, di):
        MovingPartBase.load(self, di)
        self.matrix.read_datagram(di)
        self.initial_matrix.read_datagram(di)

    def write(self, write_version, dg):
        MovingPartBase.write(self, write_version, dg)
        self.matrix.write_datagram(dg)
        self.initial_matrix.write_datagram(dg)

    def __str__(self):
        return f'MovingPartMatrix(matrix={self.matrix}, initial_matrix={self.initial_matrix}, {MovingPartBase.__str__(self)})'
