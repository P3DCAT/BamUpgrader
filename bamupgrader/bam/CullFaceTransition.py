from panda3d.core import CullFaceAttrib
from .OnTransition import OnTransition

# CullFaceProperty
M_cull_none              = 0 # Cull no polygons
M_cull_clockwise         = 1 # Cull clockwise-oriented polygons
M_cull_counter_clockwise = 2 # Cull counter-clockwise-oriented polygons
M_cull_all               = 3 # Cull all polygons (other primitives are still drawn)

# This controls how polygons are culled according to
# the ordering of their vertices after projection (and,
# hence, according to their facing relative to the
# camera).
class CullFaceTransition(OnTransition):

    def __init__(self, bam_file, bam_version):
        OnTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnTransition.load(self, di)
        self.mode = di.get_uint8() # CullFaceProperty

    def write(self, write_version, dg):
        OnTransition.write(self, write_version, dg)
        dg.add_uint8(self.mode)

    def apply(self, nodePath):
        if self.mode == M_cull_all:
            raise Exception('All polygons are culled in this mode...')

        attrib = CullFaceAttrib.make(self.mode)
        nodePath.setAttrib(attrib)

    def __str__(self):
        return f'CullFaceTransition(mode={self.mode}, {OnTransition.__str__(self)})'
