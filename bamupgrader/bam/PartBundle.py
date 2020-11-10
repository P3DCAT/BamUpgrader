from .PartGroup import PartGroup

# This is the base class for PartRoot and
# MovingPart.  It defines a hierarchy of MovingParts.
class PartBundle(PartGroup):

    def __init__(self, bam_file, bam_version):
        PartGroup.__init__(self, bam_file, bam_version)

    def load(self, di):
        PartGroup.load(self, di)

    def write(self, write_version, dg):
        PartGroup.write(self, write_version, dg)

    def __str__(self):
        return f'PartBundle({PartGroup.__str__(self)})'
