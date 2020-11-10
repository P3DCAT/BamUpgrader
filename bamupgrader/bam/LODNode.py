from panda3d import core
from .SwitchNodeOne import SwitchNodeOne
from p3bamboo.BamGlobals import read_vec2, read_vec3, write_vec

class LODNode(SwitchNodeOne):

    def __init__(self, bam_file, bam_version):
        SwitchNodeOne.__init__(self, bam_file, bam_version)

    def load(self, di):
        SwitchNodeOne.load(self, di)
        self.center = read_vec3(di)

        num_switches = di.get_uint16()
        self.switches = [read_vec2(di) for i in range(num_switches)]

    def write(self, write_version, dg):
        SwitchNodeOne.write(self, write_version, dg)
        write_vec(dg, self.center)
        dg.add_uint16(len(self.switches))

        for switch in self.switches:
            write_vec(dg, switch)

    def create_node(self):
        node = core.LODNode(self.name)
        node.set_center(self.center)

        for switch in self.switches:
            switch1, switch2 = switch

            if switch1 < switch2:
                switch3 = switch1
                switch1 = switch2
                switch2 = switch3

            node.add_switch(switch1, switch2)

        return node

    def __str__(self):
        return f'LODNode(center={self.center}, switches={self.switches}, {SwitchNodeOne.__str__(self)})'
