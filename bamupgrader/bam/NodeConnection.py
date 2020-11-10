# This class represents the table, stored within each
# Node, of all the connected NodeRelations (arcs) of a
# particular graph type.
class NodeConnection(object):

    def __init__(self):
        self.graph_type = None
        self.down_pointers = []

    def set_graph_type(self, graph_type):
        self.graph_type = graph_type

    def get_graph_type(self):
        return self.graph_type

    def add_down_pointer(sel, pointerf):
        self.down_pointers.append(pointer)

    def get_relations(self, bam_file):
        return [bam_file.object_map[obj_id] for obj_id in self.down_pointers]

    def __str__(self):
        return f'NodeConnection(graph_type={self.graph_type}, down_pointers={self.down_pointers})'
