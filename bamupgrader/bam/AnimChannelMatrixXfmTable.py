from .AnimChannelMatrix import AnimChannelMatrix

# i, j, k, h, p, r, x, y, z
# scale, rotation, position
num_tables = 9

# An animation channel that issues a matrix each frame,
# read from a table such as might have been read from
# an egg file.  The table actually consists of nine
# sub-tables, each representing one component of the
# transform: scale, rotate, translate.
class AnimChannelMatrixXfmTable(AnimChannelMatrix):

    def __init__(self, bam_file, bam_version):
        AnimChannelMatrix.__init__(self, bam_file, bam_version)

    def load(self, di):
        AnimChannelMatrix.load(self, di)
        self.compressed = di.get_bool()

        # Those are the default FFT parameters, from config_mathutil.cxx
        self.fft_offset = 0.001
        self.fft_factor = 0.1
        self.fft_exponent = 4

        if self.compressed:
            self.quality = di.get_int8()

            if self.quality < 0:
                self.fft_offset = di.get_float64()
                self.fft_factor = di.get_float64()
                self.fft_exponent = di.get_float64()
        else:
            self.quality = 100.0

        self.tables = []
        return # TODO

        if self.compressed:
            for _ in range(num_tables):
                size = di.get_int32()
                print(size)
                self.tables.append([di.get_float32() for _ in range(size)])
        else:
            for _ in range(num_tables):
                size = di.get_uint16()
                self.tables.append([di.get_float32() for _ in range(size)])

    def write(self, write_version, dg):
        AnimChannelMatrix.write(self, write_version, dg)
        dg.add_bool(self.compressed)

        if self.compressed:
            dg.add_int8(self.quality)

            if self.quality < 0:
                dg.add_float64(self.fft_offset)
                dg.add_float64(self.fft_factor)
                dg.add_float64(self.fft_exponent)

    def __str__(self):
        return f'AnimChannelMatrixXfmTable(compressed={self.compressed}, quality={self.quality}, fft_offset={self.fft_offset}, fft_factor={self.fft_factor}, fft_exponent={self.fft_exponent}, tables={self.tables}, {AnimChannelMatrix.__str__(self)})'
