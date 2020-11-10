from p3bamboo.BamObject import BamObject
from .Namable import Namable

# This is the base class for PartRoot and
# MovingPart.  It defines a hierarchy of MovingParts.
class PartGroup(BamObject, Namable):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)
        Namable.__init__(self)

    def load(self, di):
        self.name = di.get_string()

        num_children = di.get_uint16()
        self.children = [self.bam_file.read_pointer(di) for i in range(num_children)] # PartGroup

    def write(self, write_version, dg):
        dg.add_string(self.name)
        dg.add_uint16(len(self.children))

        for child in self.children:
            self.bam_file.write_pointer(dg, child) # PartGroup

    def __str__(self):
        return f'PartGroup(name={self.name}, children={self.children})'
