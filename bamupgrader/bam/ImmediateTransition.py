from .NodeTransition import NodeTransition

class ImmediateTransition(NodeTransition):

    def __init__(self, bam_file, bam_version):
        NodeTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        NodeTransition.load(self, di)

    def write(self, write_version, dg):
        NodeTransition.write(self, write_version, dg)

    def __str__(self):
        return f'ImmediateTransition({NodeTransition.__str__(self)})'
