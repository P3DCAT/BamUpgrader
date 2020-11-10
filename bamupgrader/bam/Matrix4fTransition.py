from panda3d.core import LMatrix4f
from .MatrixTransition import MatrixTransition

class Matrix4fTransition(MatrixTransition):

    def __init__(self, bam_file, bam_version):
        MatrixTransition.__init__(self, bam_file, bam_version, LMatrix4f)
