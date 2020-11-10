from .AnimGroup import AnimGroup

# Parent class for all animation channels.  An
# AnimChannel is an arbitrary function that changes
# over time (actually, over frames), usually defined by
# a table read from an egg file (but possibly computed
# or generated in any other way).
class AnimChannelBase(AnimGroup):

    def __init__(self, bam_file, bam_version):
        AnimGroup.__init__(self, bam_file, bam_version)

    def load(self, di):
        AnimGroup.load(self, di)
        self.last_frame = di.get_uint16()

    def write(self, write_version, dg):
        AnimGroup.write(self, write_version, dg)
        dg.add_uint16(self.last_frame)

    def __str__(self):
        return f'AnimChannelBase(last_frame={self.last_frame}, {AnimGroup.__str__(self)})'
