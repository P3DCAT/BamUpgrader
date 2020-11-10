from p3bamboo.BamObject import BamObject

# This is an abstract class defining the basic
# interface to a Transition--the type of state change
# request that is stored on the arcs of the scene
# graph.
#
# In general, the scene graph represents state by
# encoding transitions between various states on the
# arcs of the graph.  The state of a particular node is
# determined by the composition of all the transitions
# on arcs between that node and the root.
#
# A NodeTransition represents a particular state, or a
# change from any one state to another.  For example,
# it might represent the change from the untextured
# state to rendering with a particular texture, which
# can also be thought of as representing the state of
# rendering with that texture.
class NodeTransition(BamObject):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)

    def load(self, di):
        self.priority = di.get_uint16()

    def write(self, write_version, dg):
        dg.add_uint16(self.priority)

    def __str__(self):
        return f'NodeTransition(priority={self.priority})'
