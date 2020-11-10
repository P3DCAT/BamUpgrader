from .AnimChannelScalar import AnimChannelScalar

class AnimChannelScalarTable(AnimChannelScalar):

    def __init__(self, bam_file, bam_version):
        AnimChannelScalar.__init__(self, bam_file, bam_version)

    def load(self, di):
        AnimChannelScalar.load(self, di)
        self.compressed = di.get_bool()

    def write(self, write_version, dg):
        AnimChannelScalar.write(self, write_version, dg)
        dg.add_bool(self.compressed)

    def __str__(self):
        return f'AnimChannelScalarTable(compressed={self.compressed}, {AnimChannelScalar.__str__(self)})'
