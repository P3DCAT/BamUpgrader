from .NodeTransition import NodeTransition

# This is an abstract class that encapsulates a family
# of transitions for states that are always on, in one
# state or another.  It's similar to OnOffTransition,
# except the state can never be 'off'; it is always on
# in some sense.
#
# Most scene graph attributes that have an enumerated
# set of states fall into this category.
#
# There is no explicit identity transition.  Each
# transition always changes the state.
class OnTransition(NodeTransition):

    def __init__(self, bam_file, bam_version):
        NodeTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        NodeTransition.load(self, di)

    def write(self, write_version, dg):
        NodeTransition.write(self, write_version, dg)

    def __str__(self):
        return f'OnTransition({NodeTransition.__str__(self)})'
