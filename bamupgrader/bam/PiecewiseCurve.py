from .ParametricCurve import ParametricCurve

# A PiecewiseCurve is a curve made up of several curve
# segments, connected in a head-to-tail fashion.  The
# length of each curve segment in parametric space is
# definable.
class PiecewiseCurve(ParametricCurve):

    def __init__(self, bam_file, bam_version):
        ParametricCurve.__init__(self, bam_file, bam_version)

    def load(self, di):
        ParametricCurve.load(self, di)
        num_segments = di.get_uint32()
        self.segments = [(self.bam_file.read_pointer(di), di.get_float64()) for i in range(num_segments)] # ParametricCurve, tend

    def write(self, write_version, dg):
        ParametricCurve.write(self, write_version, dg)
        dg.add_uint32(len(self.segments))

        for segment in self.segments:
            segment_id, tend = segment
            self.bam_file.write_pointer(dg, segment_id)
            dg.add_float64(tend)

    def __str__(self):
        return f'PiecewiseCurve(segments={self.segments}, {ParametricCurve.__str__(self)})'
