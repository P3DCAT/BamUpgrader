from .NodeRelation import NodeRelation

# The arc type specific to renderable scene graphs.
class RenderRelation(NodeRelation):

    def __init__(self, bam_file, bam_version):
        NodeRelation.__init__(self, bam_file, bam_version)

    def load(self, di):
        NodeRelation.load(self, di)

    def write(self, write_version, dg):
        NodeRelation.write(self, write_version, dg)

    def __str__(self):
        return f'RenderRelation({NodeRelation.__str__(self)})'
