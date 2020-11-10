from p3bamboo.BamObject import BamObject

# The base class for all scene graph arcs.  This is the
# glue between Nodes that defines the scene graph.
# There are no arcs of type NodeRelation per se, but
# there may be any number of types of arcs that inherit
# from NodeRelation.
#
# All arcs are directed binary relations, from a parent
# node to a child node, and may include any number of
# NodeTransitions which affect the attributes of the
# child node and later descendants.
class NodeRelation(BamObject):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)

    def load(self, di):
        self.graph_type = self.bam_file.read_handle(di)
        self.parent_id = self.bam_file.read_pointer(di)
        self.child_id = self.bam_file.read_pointer(di)
        self.sort = di.get_uint16()

        num_transitions = di.get_uint16()
        self.transitions = [self.bam_file.read_pointer(di) for i in range(num_transitions)]

    def write(self, write_version, dg):
        self.bam_file.write_handle(dg, self.graph_type, self.bam_file.written_handles)
        self.bam_file.write_pointer(dg, self.parent_id)
        self.bam_file.write_pointer(dg, self.child_id)
        di.add_uint16(self.sort)
        di.add_uint16(len(self.transitions))

        for transition in self.transitions:
            self.bam_file.write_pointer(dg, transition)

    def get_transitions(self):
        return [self.bam_file.object_map[obj_id] for obj_id in self.transitions]

    def __str__(self):
        return f'NodeRelation(graph_type={self.graph_type}, parent_id={self.parent_id}, child_id={self.child_id}, sort={self.sort}, transition_ids={self.transitions})'
