from panda3d.core import PandaNode
from .Node import Node
from .Namable import Namable

class NamedNode(Node, Namable):

    def __init__(self, bam_file, bam_version):
        Node.__init__(self, bam_file, bam_version)
        Namable.__init__(self)

    def load(self, di):
        Node.load(self, di)
        self.name = di.get_string()

    def write(self, write_version, dg):
        Node.write(self, write_version, dg)
        dg.add_string(self.name)

    def create_node(self):
        return PandaNode(self.name)

    def finalize_node(self, nodePath):
        pass

    def __str__(self):
        return f'NamedNode(name={self.name}, {Node.__str__(self)})'
