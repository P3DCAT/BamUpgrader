from .dDrawable import dDrawable
from p3bamboo.BamObject import BamObject
from p3bamboo.BamGlobals import write_vec_arr, write_ushort_arr, write_int_arr

num_GeomAttrTypes = 4

# GeomBindType
G_OFF = 0
G_OVERALL = 1
G_PER_PRIM = 2
G_PER_COMPONENT = 3
G_PER_VERTEX = 4

class Geom(BamObject, dDrawable):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)
        dDrawable.__init__(self)

    def load(self, di):
        BamObject.load(self, di)
        self.coords = self.bam_file.read_vec3_array(di)
        self.norms = self.bam_file.read_vec3_array(di)
        self.colors = self.bam_file.read_vec4_array(di)
        self.texcoords = self.bam_file.read_vec2_array(di)

        self.vindex = self.bam_file.read_ushort_array(di)
        self.nindex = self.bam_file.read_ushort_array(di)
        self.cindex = self.bam_file.read_ushort_array(di)
        self.tindex = self.bam_file.read_ushort_array(di)

        self.num_prims = di.get_uint16()
        self.prim_lengths = self.bam_file.read_int_array(di)

        self.binds = [di.get_uint8() for i in range(num_GeomAttrTypes)] # GeomBindType`

    def write(self, write_version, dg):
        BamObject.write(self, write_version, dg)
        write_vec_arr(dg, self.coords)
        write_vec_arr(dg, self.norms)
        write_vec_arr(dg, self.colors)
        write_vec_arr(dg, self.texcoords)

        write_ushort_arr(dg, self.vindex)
        write_ushort_arr(dg, self.nindex)
        write_ushort_arr(dg, self.cindex)
        write_ushort_arr(dg, self.tindex)

        dg.add_uint16(self.num_prims)
        write_int_arr(dg, self.prim_lengths)

        for bind in self.binds:
            dg.add_uint8(bind)

    def __str__(self):
        return f'Geom(coords={self.coords}, norms={self.norms}, colors={self.colors}, texcoords={self.texcoords}, vindex={self.vindex}, nindex={self.nindex}, cindex={self.cindex}, tindex={self.tindex}, num_prims={self.num_prims}, prim_lengths={self.prim_lengths}, binds={self.binds})'
