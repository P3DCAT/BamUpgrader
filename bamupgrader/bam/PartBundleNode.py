from .NamedNode import NamedNode

# This is a node that contains a pointer to an
# PartBundle.  Like AnimBundleNode, it exists solely to
# make it easy to store PartBundles in the scene graph.
class PartBundleNode(NamedNode):

    def __init__(self, bam_file, bam_version):
        NamedNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        NamedNode.load(self, di)
        self.part_bundle = self.bam_file.read_pointer(di) # PartBundleNode

    def write(self, write_version, dg):
        NamedNode.write(self, write_version, dg)
        self.bam_file.write_pointer(dg, self.part_bundle) # PartBundleNode

    def get_part_bundle(self):
        return self.bam_file.object_map[self.part_bundle]

    def __str__(self):
        return f'PartBundleNode(part_bundle={self.part_bundle}, {NamedNode.__str__(self)})'
