from .NamedNode import NamedNode

class SwitchNode(NamedNode):

    def __init__(self, bam_file, bam_version):
        NamedNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        NamedNode.load(self, di)

    def write(self, write_version, dg):
        NamedNode.write(self, write_version, dg)

    def __str__(self):
        return f'SwitchNode({NamedNode.__str__(self)})'
