from panda3d.core import LVecBase4f, NurbsCurve
from .PiecewiseCurve import PiecewiseCurve

# A Nonuniform Rational B-Spline.
#
# This class is actually implemented as a
# PiecewiseCurve made up of several CubicCurvesegs,
# each of which is created using the nurbs_basis()
# method.  The list of CV's and knots is kept here,
# within the ClassicNurbsCurve class.
#
# This class is the original Panda-native
# implementation of a NURBS curve.  It is typedeffed as
# "NurbsCurve" and performs all NURBS curve functions
# if we do not have the NURBS++ library available.
#
# However, if we *do* have the NURBS++ library, another
# class exists, the NurbsPPCurve, which is a wrapper
# around that library and provides some additional
# functionality.  In that case, the other class is
# typedeffed to "NurbsCurve" instead of this one, and
# performs most of the NURBS curve functions.  This
# class then becomes vestigial.
class ClassicNurbsCurve(PiecewiseCurve):

    def __init__(self, bam_file, bam_version):
        PiecewiseCurve.__init__(self, bam_file, bam_version)

    def load(self, di):
        PiecewiseCurve.load(self, di)
        self.order = di.get_int8()
        num_cvs = di.get_uint32()
        self.points = []
        self.knots = []

        for i in range(num_cvs):
            point = LVecBase4f()
            point.read_datagram(di)
            self.points.append(point)
            self.knots.append(di.get_float64())

    def write(self, write_version, dg):
        PiecewiseCurve.write(self, write_version, dg)
        dg.add_int8(self.order)
        dg.add_uint32(len(self.cvs))

        for point in self.points:
            point.write_datagram(dg)

        for knot in self.knots:
            dg.add_float64(knot)

    def create_node(self):
        node = NurbsCurve()

        for point in self.points:
            node.append_cv(point)

        for i, knot in enumerate(self.knots):
            node.set_knot(i, knot)

        return node

    def __str__(self):
        return f'ClassicNurbsCurve(order={self.order}, points={self.points}, knots={self.knots}, {PiecewiseCurve.__str__(self)})'
