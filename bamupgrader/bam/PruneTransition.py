from .ImmediateTransition import ImmediateTransition

# This transition, when encountered in the scene graph,
# causes rendering to stop at this point and not
# traverse anything below.  In effect, it causes all
# the geometry at this level and below to become
# invisible.
class PruneTransition(ImmediateTransition):

    def __init__(self, bam_file, bam_version):
        ImmediateTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        ImmediateTransition.load(self, di)

    def write(self, write_version, dg):
        ImmediateTransition.write(self, write_version, dg)

    def apply(self, nodePath):
        # Nothing has to be applied.
        pass

    def __str__(self):
        return f'PruneTransition({ImmediateTransition.__str__(self)})'
