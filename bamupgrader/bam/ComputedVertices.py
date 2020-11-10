from panda3d.core import LVecBase2f, LVecBase3f, LVecBase4f
from p3bamboo.BamObject import BamObject
from p3bamboo.BamGlobals import write_vec_arr

# These are the vertices that must be animated as part
# of the normal character animation.  This includes
# vertices animated into one or more joints, as well as
# morph vertices.
class VertexTransform(object):

    def __init__(self, di):
        self.load(di)

    def load(self, di):
        self.joint_index = di.get_int16()
        self.effect = di.get_float32()

        vindex_length = di.get_uint16()
        self.vindex = [di.get_uint16() for i in range(vindex_length)]

        nindex_length = di.get_uint16()
        self.nindex = [di.get_uint16() for i in range(nindex_length)]

    def write(self, dg):
        dg.add_int16(self.joint_index)
        dg.add_float32(self.effect)
        dg.add_uint16(len(self.vindex))

        for vertex in self.vindex:
            dg.add_uint16(vertex)

        dg.add_uint16(len(self.nindex))

        for normal in self.nindex:
            dg.add_uint16(normal)

    def __str__(self):
        return f'VertexTransform(joint_index={self.joint_index}, effect={self.effect}, vindex={self.vindex}, nindex={self.nindex})'

class ComputedVerticesMorph(object):

    def __init__(self, vector_type, di):
        self.vector = vector_type()
        self.load(di)

    def load(self, di):
        self.index = di.get_uint16()
        self.vector.read_datagram(di)

    def write(self, dg):
        dg.add_uint16(self.index)
        self.vector.write_datagram(dg)

    def __str__(self):
        return f'ComputedVerticesMorph(index={self.index}, vector={self.vector})'

class ComputedVertices(BamObject):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)

    def load(self, di):
        BamObject.load(self, di)
        num_transforms = di.get_uint16()
        self.transforms = [VertexTransform(di) for i in range(num_transforms)]
        num_vertex_morphs = di.get_uint16()
        self.vertex_morphs = [ComputedVerticesMorph(di, LVecBase3f) for i in range(num_vertex_morphs)]
        num_normal_morphs = di.get_uint16()
        self.normal_morphs = [ComputedVerticesMorph(di, LVecBase3f) for i in range(num_normal_morphs)]
        num_texcoord_morphs = di.get_uint16()
        self.texcoord_morphs = [ComputedVerticesMorph(di, LVecBase2f) for i in range(num_texcoord_morphs)]
        num_color_morphs = di.get_uint16()
        self.color_morphs = [ComputedVerticesMorph(di, LVecBase4f) for i in range(num_color_morphs)]

        self.orig_coords = self.bam_file.read_vec3_array(di)
        self.orig_norms = self.bam_file.read_vec3_array(di)
        self.orig_colors = self.bam_file.read_vec4_array(di)
        self.orig_texcoords = self.bam_file.read_vec2_array(di)

    def write(self, write_version, dg):
        BamObject.write(self, write_version, dg)
        dg.add_uint16(len(self.transforms))

        for transform in self.transforms:
            transform.write(dg)

        dg.add_uint16(len(self.vertex_morphs))

        for morph in self.vertex_morphs:
            morph.write(dg)

        dg.add_uint16(len(self.normal_morphs))

        for morph in self.normal_morphs:
            morph.write(dg)

        dg.add_uint16(len(self.texcoord_morphs))

        for morph in self.texcoord_morphs:
            morph.write(dg)

        dg.add_uint16(len(self.color_morphs))

        for morph in self.color_morphs:
            morph.write(dg)

        write_vec_arr(dg, self.orig_coords)
        write_vec_arr(dg, self.orig_norms)
        write_vec_arr(dg, self.orig_colors)
        write_vec_arr(dg, self.orig_texcoords)

    def conv(self, list):
        return [str(element) for element in list]

    def __str__(self):
        return f'ComputedVertices(transforms={self.conv(self.transforms)}, vertex_morphs={self.conv(self.vertex_morphs)}, normal_morphs={self.conv(self.normal_morphs)}, texcoord_morphs={self.conv(self.texcoord_morphs)}, color_morphs={self.conv(self.color_morphs)}, orig_coords={self.orig_coords}, orig_norms={self.orig_norms}, orig_colors={self.orig_colors}, orig_texcoords={self.orig_texcoords})'
