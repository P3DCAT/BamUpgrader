from panda3d.core import TransparencyAttrib
from .OnTransition import OnTransition

# TransparencyProperty
M_none             = 0 # No transparency in effect.
M_alpha            = 1 # Writes to depth buffer of transp objects disabled
M_alpha_sorted     = 2 # Assumes transp objects are depth sorted
M_multisample      = 3 # Source alpha values modified to 1.0 before writing
M_multisample_mask = 4 # Source alpha values not modified
M_binary           = 5 # Only writes pixels with alpha = 1.0

def transparency_to_panda(property):
    if property == M_none:
        return TransparencyAttrib.M_none
    elif property == M_alpha:
        return TransparencyAttrib.M_alpha
    elif property == M_alpha_sorted:
        # No real equivalent
        return TransparencyAttrib.M_dual
    elif property == M_multisample:
        return TransparencyAttrib.M_multisample
    elif property == M_multisample_mask:
        return TransparencyAttrib.M_multisample_mask
    elif property == M_binary:
        return TransparencyAttrib.M_binary

    raise Exception(f'Invalid transparency mode: {property}')

# This controls the enabling of transparency. Simply
# setting an alpha component to non-1 does not in
# itself make an object transparent; you must also
# enable transparency mode with a suitable
# TransparencyTransition.  Similarly, it is wasteful to
# render an object with a TransparencyTransition in
# effect unless you actually want it to be at least
# partially transparent (and it has alpha components
# less than 1).
class TransparencyTransition(OnTransition):

    def __init__(self, bam_file, bam_version):
        OnTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnTransition.load(self, di)
        self.mode = di.get_uint8() # TransparencyProperty

    def write(self, write_version, dg):
        OnTransition.write(self, write_version, dg)
        dg.add_uint8(self.mode)

    def get_panda_transparency(self):
        return transparency_to_panda(self.mode)

    def apply(self, nodePath):
        attrib = TransparencyAttrib.make(self.get_panda_transparency())
        nodePath.setAttrib(attrib)

    def __str__(self):
        return f'TransparencyTransition(mode={self.mode}, {OnTransition.__str__(self)})'
