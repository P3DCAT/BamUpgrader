from .NamedNode import NamedNode

# A virtual base class for parametric curves.
# This encapsulates all curves in 3-d space defined
# for a single parameter t in the range [0,get_max_t()].
class ParametricCurve(NamedNode):

    def __init__(self, bam_file, bam_version):
        NamedNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        NamedNode.load(self, di)
        self.curve_type = di.get_int8()
        self.num_dimensions = di.get_int8()

    def write(self, write_version, dg):
        NamedNode.write(self, write_version, dg)
        dg.add_int8(self.curve_type)
        dg.add_int8(self.num_dimensions)

    def __str__(self):
        return f'ParametricCurve(curve_type={self.curve_type}, num_dimensions={self.num_dimensions}, {NamedNode.__str__(self)})'
