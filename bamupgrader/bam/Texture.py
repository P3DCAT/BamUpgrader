from .ImageBuffer import ImageBuffer

# FilterType
FT_nearest                = 0 # Point sample the pixel
FT_linear                 = 1 # Bilinear filtering of four neighboring pixels
FT_nearest_mipmap_nearest = 2 # Point sample the pixel from the nearest mipmap level
FT_linear_mipmap_nearest  = 3 # Bilinear filter the pixel from the nearest mipmap level
FT_nearest_mipmap_linear  = 4 # Point sample the pixel from two mipmap levels, and linearly blend
FT_linear_mipmap_linear   = 5 # A.k.a. trilinear filtering: Bilinear filter the pixel from two mipmap levels, and linearly blend the results.

# WrapMode
WM_clamp = 0
WM_repeat = 1

# PixelBuffer Format
F_color_index = 0
F_stencil_index = 1
F_depth_component = 2
F_red = 3
F_green = 4
F_blue = 5
F_alpha = 6
F_rgb = 7                  # any suitable RGB mode, whatever the hardware prefers
F_rgb5 = 8                 # specifically, 5 bits per R,G,B channel
F_rgb8 = 9                 # 8 bits per R,G,B channel
F_rgb12 = 10               # 12 bits per R,G,B channel
F_rgb332 = 11              # 3 bits per R & G, 2 bits for B
F_rgba = 12                # any suitable RGBA mode, whatever the hardware prefers
F_rgbm = 13                # as above, but only requires 1 bit for alpha (i.e. mask)
F_rgba4 = 14               # 4 bits per R,G,B,A channel
F_rgba5 = 15               # 5 bits per R,G,B channel, 1 bit alpha
F_rgba8 = 16               # 8 bits per R,G,B,A channel
F_rgba12 = 17              # 12 bits per R,G,B,A channel
F_luminance = 18
F_luminance_alpha = 19     # 8 bits luminance, 8 bits alpha
F_luminance_alphamask = 20 # 8 bits luminance, only needs 1 bit of alpha

# 2D texture class
class Texture(ImageBuffer):

    def __init__(self, bam_file, bam_version):
        ImageBuffer.__init__(self, bam_file, bam_version)

    def load(self, di):
        ImageBuffer.load(self, di)
        self.historical = di.get_uint32() # For historical purposes
        self.wrap_u = di.get_uint8() # WrapMode
        self.wrap_v = di.get_uint8() # WrapMode
        self.minfilter = di.get_uint8() # FilterType
        self.magfilter = di.get_uint8() # FilterType
        self.magfilter_color = di.get_uint8() # FilterType
        self.magfilter_alpha = di.get_uint8() # FilterType

        self.anisotropic_degree = di.get_int16()

        self.has_pbuffer = False
        self.pbuffer_format = -1
        self.pbuffer_num_components = -1

        if di.get_remaining_size() > 0:
            self.has_pbuffer = di.get_bool()

            if self.has_pbuffer:
                self.pbuffer_format = di.get_uint8()
                self.pbuffer_num_components = di.get_uint8()

    def write(self, write_version, dg):
        ImageBuffer.write(self, write_version, dg)
        dg.add_uint32(self.historical)
        dg.add_uint8(self.wrap_u)
        dg.add_uint8(self.wrap_v)
        dg.add_uint8(self.minfilter)
        dg.add_uint8(self.magfilter)
        dg.add_uint8(self.magfilter_color)
        dg.add_uint8(self.magfilter_alpha)

        dg.add_int16(self.anisotropic_degree)

        dg.add_bool(self.has_pbuffer)

        if self.has_pbuffer:
            dg.add_uint8(self.pbuffer_format)
            dg.add_uint8(self.pbuffer_num_components)

    def __str__(self):
        return f'Texture(wrap_u={self.wrap_u}, wrap_v={self.wrap_v}, minfilter={self.minfilter}, magfilter={self.magfilter}, magfilter_color={self.magfilter_color}, magfilter_alpha={self.magfilter_alpha}, anisotropic_degree={self.anisotropic_degree}, has_pbuffer={self.has_pbuffer}, pbuffer_format={self.pbuffer_format}, pbuffer_num_components={self.pbuffer_num_components}, {ImageBuffer.__str__(self)})'
