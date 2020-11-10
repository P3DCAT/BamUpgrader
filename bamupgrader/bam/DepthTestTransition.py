from .OnTransition import OnTransition

# DepthTestProperty
M_none          = 0 # No depth test; may still write to depth buffer.
M_never         = 1 # Never draw.
M_less          = 2 # incoming < stored
M_equal         = 3 # incoming == stored
M_less_equal    = 4 # incoming <= stored
M_greater       = 5 # incoming > stored
M_not_equal     = 6 # incoming != stored
M_greater_equal = 7 # incoming >= stored
M_always        = 8 # Always draw.  Same effect as none, more expensive.

# This transition controls the nature of the test
# against the depth buffer.  It does not affect whether
# the depth buffer will be written to or not; that is
# handled by a separate transition, DepthWriteTransition.
class DepthTestTransition(OnTransition):

    def __init__(self, bam_file, bam_version):
        OnTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnTransition.load(self, di)
        self.mode = di.get_uint8() # DepthTestProperty

    def write(self, write_version, dg):
        OnTransition.write(self, write_version, dg)
        dg.add_uint8(self.mode)

    def __str__(self):
        return f'DepthTestTransition(mode={self.mode}, {OnTransition.__str__(self)})'
