from panda3d.core import BillboardEffect, NodePath, LPoint3f
from .ImmediateTransition import ImmediateTransition
from p3bamboo.BamGlobals import read_vec3, write_vec

# This transition, when applied to an arc, causes that
# arc and everything below it to be rendered so that it
# always faces the camera.  There are all kinds of ways
# that billboards can be set to rotate.
#
# A BillboardTransition is neither on nor off, and it
# does not compose with nested BillboardTransitions.
# Instead, it has an immediate effect.  Once a
# billboard transition is in place, it affects
# everything below it.
class BillboardTransition(ImmediateTransition):

    def __init__(self, bam_file, bam_version):
        ImmediateTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        ImmediateTransition.load(self, di)
        self.up_vector = read_vec3(di)
        self.eye_relative = di.get_uint8() != 0
        self.axial_rotate = di.get_uint8() != 0

    def write(self, write_version, dg):
        ImmediateTransition.write(self, write_version, dg)
        write_vec(dg, self.up_vector)
        dg.add_uint8(int(self.eye_relative))
        dg.add_uint8(int(self.axial_rotate))

    def apply(self, nodePath):
        effect = BillboardEffect.make(self.up_vector, self.eye_relative, self.axial_rotate, 0.0, NodePath(), LPoint3f(0, 0, 0))
        nodePath.setEffect(effect)

    def __str__(self):
        return f'BillboardTransition(up_vector={self.up_vector}, eye_relative={self.eye_relative}, axial_rotate={self.axial_rotate}, {ImmediateTransition.__str__(self)})'
