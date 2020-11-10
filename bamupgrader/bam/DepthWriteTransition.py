from panda3d.core import DepthWriteAttrib, DepthTestAttrib
from .OnOffTransition import OnOffTransition

# This enables or disables the writing to the depth
# buffer.
class DepthWriteTransition(OnOffTransition):

    def __init__(self, bam_file, bam_version):
        OnOffTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnOffTransition.load(self, di)

    def write(self, write_version, dg):
        OnOffTransition.write(self, write_version, dg)

    def apply(self, nodePath):
        if self.is_unset():
            return

        attrib = DepthWriteAttrib.make(self.is_on())
        nodePath.setAttrib(attrib)

    def __str__(self):
        return f'DepthWriteTransition({OnOffTransition.__str__(self)})'
