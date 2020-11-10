from panda3d import core
from p3bamboo.BamGlobals import read_vec2, write_vec
from .CollisionPlane import CollisionPlane

# AxisType
AT_x = 0
AT_y = 1
AT_z = 2

class CollisionPolygon(CollisionPlane):

    def __init__(self, bam_file, bam_version):
        CollisionPlane.__init__(self, bam_file, bam_version)

    def load(self, di):
        CollisionPlane.load(self, di)

        num_points = di.get_uint16()
        self.points = [read_vec2(di) for i in range(num_points)]

        self.median = read_vec2(di)
        self.axis = di.get_uint8() # AxisType
        self.reversed = di.get_uint8() != 0

    def write(self, write_version, dg):
        CollisionPlane.write(self, write_version, dg)
        dg.add_uint16(len(self.points))

        for point in self.points:
            write_vec(dg, point)

        write_vec(dg, self.median)
        dg.add_uint8(self.axis)
        dg.add_uint8(int(self.reversed))

    def create_node(self):
        if not self.points:
            return None

        zero = core.LPoint3f(0, 0, 0)
        polygon = core.CollisionPolygon(zero, zero, zero)
        a, b, c, d = self.plane

        if self.axis == AT_x:
            points = [core.LPoint3f(-(b * point[0] + c * point[1] + d) / a, point[0], point[1]) for point in self.points]
        elif self.axis == AT_y:
            points = [core.LPoint3f(point[0], -(a * point[0] + c * point[1] + d) / b, point[1]) for point in self.points]
        elif self.axis == AT_z:
            points = [core.LPoint3f(point[0], point[1], -(a * point[0] + b * point[1] + d) / c) for point in self.points]
        else:
            raise Exception(f'Invalid axis for CollisionPolygon: {self.axis}')

        if self.reversed:
            points.reverse()

        polygon.setup_points(points)
        return polygon

    def __str__(self):
        return f'CollisionPolygon(points={self.points}, median={self.median}, axis={self.axis}, reversed={self.reversed}, {CollisionPlane.__str__(self)})'
