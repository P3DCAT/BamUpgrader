from .NamedNode import NamedNode

# This is a node that contains a pointer to an
# AnimBundle.  Its primary reason to exist is to allow
# the AnimBundles to be stored in the scene graph, so
# they may conveniently be loaded as egg files, for
# instance.
class AnimBundleNode(NamedNode):

    def __init__(self, bam_file, bam_version):
        NamedNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        NamedNode.load(self, di)
        self.anim_bundle = self.bam_file.read_pointer(di) # AnimBundleNode

    def write(self, write_version, dg):
        NamedNode.write(self, write_version, dg)
        self.bam_file.write_pointer(dg, self.anim_bundle) # AnimBundleNode

    def __str__(self):
        return f'AnimBundleNode(anim_bundle={self.anim_bundle}, {NamedNode.__str__(self)})'
