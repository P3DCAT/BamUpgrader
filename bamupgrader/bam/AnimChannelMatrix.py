from .AnimChannelBase import AnimChannelBase

class AnimChannelMatrix(AnimChannelBase):

    def __init__(self, bam_file, bam_version):
        AnimChannelBase.__init__(self, bam_file, bam_version)

    def load(self, di):
        AnimChannelBase.load(self, di)

    def write(self, write_version, dg):
        AnimChannelBase.write(self, write_version, dg)

    def __str__(self):
        return f'AnimChannelMatrix({AnimChannelBase.__str__(self)})'
