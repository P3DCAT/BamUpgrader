from .NodeTransition import NodeTransition

# TransitionDirection
TD_identity = 0
TD_on = 1
TD_off = 2

# This is an abstract class that encapsulates a family
# of transitions for states that are either on or off
# (and, when on, may or may not have some particular
# value).  This is typically useful for things like
# Texture, which have a definite value when on, and
# also have a definite off condition.
#
# See also OnTransition, which is used for states that
# are always on in some sense, or whose value itself
# can encode the case of being off.
#
# The transition may be either 'on', turning on a
# particular state, 'off', turning *off* a state that
# was previously turned on, or 'identity', not
# affecting the state.  If two 'on' transitions are
# composed together, the second one overrides the
# first.
class OnOffTransition(NodeTransition):

    def __init__(self, bam_file, bam_version):
        NodeTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        NodeTransition.load(self, di)
        self.direction = di.get_uint8() # TransitionDirection

    def write(self, write_version, dg):
        NodeTransition.write(self, write_version, dg)
        dg.add_uint8(self.direction)

    def is_unset(self):
        return self.direction == TD_identity

    def is_on(self):
        return self.direction == TD_on

    def __str__(self):
        return f'OnOffTransition(direction={self.direction}, {NodeTransition.__str__(self)})'
