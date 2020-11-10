from panda3d.core import TexturePool
from .OnOffTransition import OnOffTransition

# This controls the assignment of the primary texture
# to a piece of geometry.  If there is no
# TextureTransition or the transition is off, the
# geometry is rendered untextured; if there is an 'on'
# TextureTransition affecting a piece of geometry it
# will be rendered with the indicated texture.
#
# At one time this was a MultiTransition because we
# were thinking of using this interface to support
# multitexturing.  But on reflection that is a flawed
# idea because MultiTransitions don't support any
# ordering, and we don't yet have an interface for
# specifying multiple layers of UV coordinates anyway.
# Until this is fully worked out, this will be a simple
# OnOffTransition: either there is a texture or there
# isn't.
class TextureTransition(OnOffTransition):

    def __init__(self, bam_file, bam_version):
        OnOffTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        OnOffTransition.load(self, di)
        self.texture_id = self.bam_file.read_pointer(di) # Texture

    def write(self, write_version, dg):
        OnOffTransition.write(self, write_version, dg)
        self.bam_file.write_pointer(dg, self.texture_id)

    def get_texture(self):
        if self.texture_id:
            return self.bam_file.object_map[self.texture_id]

    def apply(self, nodePath):
        texture = self.get_texture()

        if not texture:
            return

        #if 'palette' in texture.name and not getattr(texture, 'edited', False):
        #    texture.name = texture.name.replace('palette', 'palette_converted')

        if texture.alpha_name:
            #if 'palette' in texture.alpha_name and not getattr(texture, 'edited', False):
            #    texture.alpha_name = texture.alpha_name.replace('palette', 'palette_converted')

            tex = TexturePool.load_texture(texture.name, texture.alpha_name)
        else:
            tex = TexturePool.load_texture(texture.name)

        if not tex:
            print('Texture missing!', texture.name, texture.alpha_name)
            return

        #texture.edited = True
        tex.set_wrap_u(texture.wrap_u)
        tex.set_wrap_v(texture.wrap_v)
        tex.set_minfilter(texture.minfilter)
        tex.set_magfilter(texture.magfilter)
        tex.set_anisotropic_degree(texture.anisotropic_degree)
        nodePath.setTexture(tex, 0)

    def __str__(self):
        return f'TextureTransition(texture_id={self.texture_id}, {OnOffTransition.__str__(self)})'
