from .Namable import Namable
from .dDrawable import dDrawable
from p3bamboo.BamObject import BamObject

class ImageBuffer(BamObject, Namable, dDrawable):

    def __init__(self, bam_file, bam_version):
        BamObject.__init__(self, bam_file, bam_version)
        Namable.__init__(self)
        dDrawable.__init__(self)

    def load(self, di):
        BamObject.load(self, di)
        self.name = di.get_string()
        self.alpha_name = di.get_string()

    def write(self, write_version, dg):
        BamObject.write(self, write_version, dg)
        dg.add_string(self.name)
        dg.add_string(self.alpha_name)

    def __str__(self):
        return f'ImageBuffer(name={self.name}, alpha_name={self.alpha_name})'
