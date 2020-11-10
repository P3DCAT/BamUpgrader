from panda3d import core
from .ModelNode import ModelNode

class ModelRoot(ModelNode):

    def __init__(self, bam_file, bam_version):
        ModelNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        ModelNode.load(self, di)

    def write(self, write_version, dg):
        ModelNode.write(self, write_version, dg)

    def create_node(self):
        return core.ModelRoot(self.name)

    def __str__(self):
        return f'ModelRoot({ModelNode.__str__(self)})'
