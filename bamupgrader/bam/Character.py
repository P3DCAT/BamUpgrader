from panda3d import core
from p3bamboo.BamGlobals import write_vec_arr
from .PartBundleNode import PartBundleNode

class Character(PartBundleNode):

    def __init__(self, bam_file, bam_version):
        PartBundleNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        PartBundleNode.load(self, di)
        # Dynamic Vertices
        self.coords = self.bam_file.read_vec3_array(di)
        self.norms = self.bam_file.read_vec3_array(di)
        self.colors = self.bam_file.read_vec4_array(di)
        self.texcoords = self.bam_file.read_vec2_array(di)

        self.computed_vertices = self.bam_file.read_pointer(di)

        num_parts = di.get_uint16()
        self.parts = [self.bam_file.read_pointer(di) for i in range(num_parts)] # PartGroup

    def write(self, write_version, dg):
        PartBundleNode.write(self, write_version, dg)
        write_vec_arr(dg, self.coords)
        write_vec_arr(dg, self.norms)
        write_vec_arr(dg, self.colors)
        write_vec_arr(dg, self.texcoords)
        self.bam_file.write_pointer(dg, self.computed_vertices)
        dg.add_uint16(len(self.parts))

        for part in self.parts:
            self.bam_file.write_pointer(dg, part) # PartGroup

    def create_node(self):
        node = core.Character(self.name)
        bundle_obj = self.get_part_bundle()
        bundle = core.CharacterJointBundle(bundle_obj.name)
        #TODO
        #print(self)
        #print(self.get_computed_vertices())
        #print([str(part) for part in self.get_parts()])
        #print(self.get_part_bundle())
        #print(bundle)
        return node

    def get_computed_vertices(self):
        return self.bam_file.object_map[self.computed_vertices]

    def get_parts(self):
        return [self.bam_file.object_map[part_id] for part_id in self.parts]

    def __str__(self):
        return f'Character(coords={self.coords}, norms={self.norms}, colors={self.colors}, texcoords={self.texcoords}, computed_vertices={self.computed_vertices}, parts={self.parts}, {PartBundleNode.__str__(self)})'
