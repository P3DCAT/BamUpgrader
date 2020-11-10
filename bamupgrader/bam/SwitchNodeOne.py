from .SwitchNode import SwitchNode

class SwitchNodeOne(SwitchNode):

    def __init__(self, bam_file, bam_version):
        SwitchNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        SwitchNode.load(self, di)

    def write(self, write_version, dg):
        SwitchNode.write(self, write_version, dg)

    def __str__(self):
        return f'SwitchNodeOne({SwitchNode.__str__(self)})'
