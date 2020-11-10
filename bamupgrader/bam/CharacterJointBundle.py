from .PartBundle import PartBundle

class CharacterJointBundle(PartBundle):

    def __init__(self, bam_file, bam_version):
        PartBundle.__init__(self, bam_file, bam_version)

    def load(self, di):
        PartBundle.load(self, di)

    def write(self, write_version, dg):
        PartBundle.write(self, write_version, dg)

    def __str__(self):
        return f'CharacterJointBundle({PartBundle.__str__(self)})'
