from panda3d.core import DecalEffect
from .OnOffTransition import OnOffTransition

# When this transition is in effect, the first GeomNode
# encountered is rendered in a special mode, such that
# all of its *children* (indeed, the whole subtree
# beginning at the top GeomNode under the transition)
# are rendered as decals of the GeomNode.
#
# This means that the decal geometry (i.e. all geometry
# in GeomNodes parented somewhere below the top
# GeomNode) is assumed to be coplanar with the base
# geometry, and will be rendered so that no z-fighting
# will occur between it and the base geometry.
#
# The render behavior is undefined if the decal
# geometry is *not* coplanar with the base geometry.
class DecalTransition(OnOffTransition):

    def __init__(self, bam_file, bam_version):
        OnOffTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnOffTransition.load(self, di)

    def write(self, write_version, dg):
        OnOffTransition.write(self, write_version, dg)

    def apply(self, nodePath):
        if self.is_unset():
            return

        effect = DecalEffect.make()
        nodePath.setEffect(effect)

    def __str__(self):
        return f'DecalTransition({OnOffTransition.__str__(self)})'
