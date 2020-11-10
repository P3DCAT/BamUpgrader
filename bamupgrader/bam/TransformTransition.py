from .Matrix4fTransition import Matrix4fTransition

# This defines a new coordinate system.
class TransformTransition(Matrix4fTransition):

    def __init__(self, bam_file, bam_version):
        Matrix4fTransition.__init__(self, bam_file, bam_version)

    def load(self, di):
        Matrix4fTransition.load(self, di)

    def write(self, write_version, dg):
        Matrix4fTransition.write(self, write_version, dg)

    def apply(self, nodePath):
        nodePath.setMat(self.matrix)

    def __str__(self):
        return f'TransformTransition({Matrix4fTransition.__str__(self)})'
