from .AnimGroup import AnimGroup

# This is the root of an AnimChannel hierarchy.  It
# knows the frame rate and number of frames of all the
# channels in the hierarchy (which must all match).
class AnimBundle(AnimGroup):

    def __init__(self, bam_file, bam_version):
        AnimGroup.__init__(self, bam_file, bam_version)

    def load(self, di):
        AnimGroup.load(self, di)
        self.fps = di.get_float32()
        self.num_frames = di.get_uint16()

    def write(self, write_version, dg):
        AnimGroup.write(self, write_version, dg)
        dg.add_float32(self.fps)
        dg.add_uint16(self.num_frames)

    def __str__(self):
        return f'AnimBundle(fps={self.fps}, num_frames={self.num_frames}, {AnimGroup.__str__(self)})'
