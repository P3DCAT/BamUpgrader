from panda3d import core
from .NamedNode import NamedNode

class ModelNode(NamedNode):

    def __init__(self, bam_file, bam_version):
        NamedNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        NamedNode.load(self, di)

        if self.bam_version >= (3, 2):
            self.preserve_transform = di.get_bool()
        else:
            self.preserve_transform = False

    def write(self, write_version, dg):
        NamedNode.write(self, write_version, dg)

        if write_version >= (3, 2):
            dg.add_bool(self.preserve_transform)

    def create_node(self):
        return core.ModelNode(self.name)

    def __str__(self):
        return f'ModelNode(preserve_transform={self.preserve_transform}, {NamedNode.__str__(self)})'
