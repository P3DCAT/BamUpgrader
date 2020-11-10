from panda3d import core
from .ParametricCurve import ParametricCurve

# A CubicCurveseg is any curve that can be completely
# described by four 4-valued basis vectors, one for
# each dimension in three-space, and one for the
# homogeneous coordinate.  This includes Beziers,
# Hermites, and NURBS.
#
# This class encapsulates a single curve segment of the
# cubic curve.  Normally, when we think of Bezier and
# Hermite curves, we think of a piecewise collection of
# such segments.
#
# Although this class includes methods such as
# hermite_basis() and nurbs_basis(), to generate a
# Hermite and NURBS curve segment, respectively, only
# the final basis vectors are stored: the product of
# the basis matrix of the corresponding curve type, and
# its geometry vectors.  This is the minimum
# information needed to evaluate the curve.  However,
# the individual CV's that were used to compute these
# basis vectors are not retained; this might be handled
# in a subclass (for instance, HermiteCurve).
class CubicCurveseg(ParametricCurve):

    def __init__(self, bam_file, bam_version):
        ParametricCurve.__init__(self, bam_file, bam_version)
        self.bx = core.LVecBase4f()
        self.by = core.LVecBase4f()
        self.bz = core.LVecBase4f()
        self.bw = core.LVecBase4f()

    def load(self, di):
        ParametricCurve.load(self, di)
        self.bx.read_datagram(di)
        self.by.read_datagram(di)
        self.bz.read_datagram(di)
        self.bw.read_datagram(di)
        self.rational = di.get_bool()

    def write(self, write_version, dg):
        ParametricCurve.write(self, write_version, dg)
        self.bx.write_datagram(dg)
        self.by.write_datagram(dg)
        self.bz.write_datagram(dg)
        self.bw.write_datagram(dg)
        dg.add_bool(self.rational)

    def create_node(self):
        mat = core.LMatrix4f(self.bx, self.by, self.bz, self.bw)
        node = core.CubicCurveseg(mat)
        return node

    def __str__(self):
        return f'CubicCurveseg(bx={self.bx}, by={self.by}, bz={self.bz}, bw={self.bw}, rational={self.rational}, {ParametricCurve.__str__(self)})'
