from .NodeConnection import NodeConnection
from p3bamboo.BamObject import BamObject

max_node_graphs = 2

class Node(BamObject):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)

    def load(self, di):
        self.connections = [NodeConnection(), NodeConnection()]
        num_connections = di.get_uint16()

        if num_connections > max_node_graphs:
            raise Exception('Max node graph exceeded:', num_connections)

        for i in range(num_connections):
            graph_type = self.bam_file.read_handle(di)
            conn = self.connections[i]
            num_arcs = di.get_uint16()
            arcs = [self.bam_file.read_pointer(di) for j in range(num_arcs)]

            if i < max_node_graphs:
                conn.set_graph_type(graph_type)

                for arc in arcs:
                    conn.down_pointers.append(arc)

    def get_relations(self):
        relations = []

        for connection in self.connections:
            if connection.down_pointers:
                relations += connection.get_relations(self.bam_file)

        return relations

    def write(self, write_version, dg):
        pass

    def __str__(self):
        return f'Node(connections=[{", ".join([str(conn) for conn in self.connections])}])'
