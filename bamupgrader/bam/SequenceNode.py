from panda3d import core
from .SwitchNodeOne import SwitchNodeOne

class SequenceNode(SwitchNodeOne):

    def __init__(self, bam_file, bam_version):
        SwitchNodeOne.__init__(self, bam_file, bam_version)

    def load(self, di):
        SwitchNodeOne.load(self, di)
        self.cycle_time = di.get_float32()
        self.element_count = di.get_uint16()

    def write(self, write_version, dg):
        SwitchNodeOne.write(self, write_version, dg)
        dg.add_float32(self.cycle_time)
        dg.add_uint16(self.element_count)

    def create_node(self):
        node = core.SequenceNode(self.name)
        node.set_frame_rate(1.0 / self.cycle_time)
        return node

    def finalize_node(self, nodePath):
        nodePath.node().loop(False, 0, nodePath.getNumChildren() - 1)

    def __str__(self):
        return f'SequenceNode(cycle_time={self.cycle_time}, element_count{self.element_count}, {SwitchNodeOne.__str__(self)})'
