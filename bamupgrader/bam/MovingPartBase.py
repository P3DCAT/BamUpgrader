from .PartGroup import PartGroup

# This is the base class for a single animatable piece
# that may be bound to one channel (or more, if
# blending is in effect).  It corresponds to, for
# instance, a single joint or slider of a character.
#
# MovingPartBase does not have a particular value type.
# See the derived template class, MovingPart, for this.
class MovingPartBase(PartGroup):

    def __init__(self, bam_file, bam_version):
        PartGroup.__init__(self, bam_file, bam_version)

    def load(self, di):
        PartGroup.load(self, di)

    def write(self, write_version, dg):
        PartGroup.write(self, write_version, dg)

    def __str__(self):
        return f'MovingPartBase({PartGroup.__str__(self)})'
