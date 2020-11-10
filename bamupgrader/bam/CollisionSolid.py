from p3bamboo.BamObject import BamObject

# The abstract base class for all things that can
# collide with other things in the world, and all the
# things they can collide with (except geometry).
#
# This class and its derivatives really work very
# similarly to the way BoundingVolume and all of its
# derivatives work.  There's a different subclass for
# each basic shape of solid, and double-dispatch
# function calls handle the subset of the N*N
# intersection tests that we care about.
# BoundedObject
class CollisionSolid(BamObject):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)

    def load(self, di):
        BamObject.load(self, di)
        self.tangible = di.get_uint8() != 0

    def write(self, write_version, dg):
        BamObject.write(self, write_version, dg)
        dg.add_uint8(int(self.tangible))

    def __str__(self):
        return f'CollisionSolid(tangible={self.tangible})'
