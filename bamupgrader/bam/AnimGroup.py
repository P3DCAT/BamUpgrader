from p3bamboo.BamObject import BamObject
from .Namable import Namable

# This is the base class for AnimChannel and
# AnimBundle.  It implements a hierarchy of
# AnimChannels.  The root of the hierarchy must be an
# AnimBundle.
class AnimGroup(BamObject, Namable):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)
        Namable.__init__(self)

    def load(self, di):
        self.name = di.get_string()
        self.root = self.bam_file.read_pointer(di) # AnimGroup

        num_children = di.get_uint16()
        self.children = [self.bam_file.read_pointer(di) for i in range(num_children)] # AnimGroup

    def write(self, write_version, dg):
        dg.add_string(self.name)
        self.bam_file.write_pointer(dg, self.root)
        dg.add_uint16(len(self.children))

        for child in self.children:
            self.bam_file.write_pointer(dg, child)

    def __str__(self):
        return f'AnimGroup(name={self.name}, root_id={self.root}, children={self.children})'
