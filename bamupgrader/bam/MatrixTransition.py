from .NodeTransition import NodeTransition

class MatrixTransition(NodeTransition):

    def __init__(self, bam_file, bam_version, matrix_type):
        NodeTransition.__init__(self, bam_file, bam_version)
        self.matrix_name = matrix_type.__name__
        self.matrix = matrix_type()

    def load(self, di):
        NodeTransition.load(self, di)
        self.matrix.read_datagram(di)

    def write(self, write_version, dg):
        NodeTransition.write(self, write_version, dg)
        self.matrix.write_datagram(dg)

    def __str__(self):
        return f'MatrixTransition<{self.matrix_name}>(matrix={self.matrix}, {NodeTransition.__str__(self)})'
