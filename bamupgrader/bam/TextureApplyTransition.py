from panda3d.core import TextureAttrib, TextureStage
from .OnTransition import OnTransition

# TextureApplyProperty Mode
M_modulate = 0
M_decal = 1
M_blend = 2
M_replace = 3
M_add = 4

# This controls the way textures modify the colors
# assigned to geometry.
class TextureApplyTransition(OnTransition):

    def __init__(self, bam_file, bam_version):
        OnTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnTransition.load(self, di)
        self.mode = di.get_uint8() # TextureApplyProperty

    def write(self, write_version, dg):
        OnTransition.write(self, write_version, dg)
        dg.add_uint8(self.mode)

    def apply(self, nodePath):
        attrib = nodePath.getAttrib(TextureAttrib)
        stage = TextureStage('tex')
        stage.setMode(self.mode)
        # TODO
        #nodePath.setAttrib(attrib.add_on_stage(stage, attrib.getTexture(), 0))

    def __str__(self):
        return f'TextureApplyTransition(mode={self.mode}, {OnTransition.__str__(self)})'
