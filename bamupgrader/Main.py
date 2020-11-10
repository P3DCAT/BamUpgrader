from panda3d.core import Filename, getModelPath, loadPrcFileData
from bamupgrader.UpgradedBamFile import UpgradedBamFile
import argparse, os

# TODO: Characters

def setup_p3bamboo():
    from p3bamboo.BamFactory import BamFactory

    # Nodes
    from bamupgrader.bam.Node import Node
    from bamupgrader.bam.NamedNode import NamedNode
    from bamupgrader.bam.ModelNode import ModelNode
    from bamupgrader.bam.ModelRoot import ModelRoot
    from bamupgrader.bam.NodeRelation import NodeRelation
    from bamupgrader.bam.RenderRelation import RenderRelation
    from bamupgrader.bam.NodeTransition import NodeTransition
    from bamupgrader.bam.OnOffTransition import OnOffTransition
    from bamupgrader.bam.OnTransition import OnTransition
    from bamupgrader.bam.TextureTransition import TextureTransition
    from bamupgrader.bam.TextureApplyTransition import TextureApplyTransition
    from bamupgrader.bam.TransparencyTransition import TransparencyTransition
    from bamupgrader.bam.ImmediateTransition import ImmediateTransition
    from bamupgrader.bam.PruneTransition import PruneTransition
    from bamupgrader.bam.CullFaceTransition import CullFaceTransition
    from bamupgrader.bam.DepthWriteTransition import DepthWriteTransition
    from bamupgrader.bam.DepthTestTransition import DepthTestTransition
    from bamupgrader.bam.GeomBinTransition import GeomBinTransition
    from bamupgrader.bam.BillboardTransition import BillboardTransition
    from bamupgrader.bam.Matrix4fTransition import Matrix4fTransition
    from bamupgrader.bam.TransformTransition import TransformTransition
    from bamupgrader.bam.DecalTransition import DecalTransition
    from bamupgrader.bam.ImageBuffer import ImageBuffer
    from bamupgrader.bam.Texture import Texture
    from bamupgrader.bam.CollisionNode import CollisionNode
    from bamupgrader.bam.CollisionSolid import CollisionSolid
    from bamupgrader.bam.CollisionPlane import CollisionPlane
    from bamupgrader.bam.CollisionPolygon import CollisionPolygon
    from bamupgrader.bam.CollisionSphere import CollisionSphere
    from bamupgrader.bam.Geom import Geom
    from bamupgrader.bam.GeomTri import GeomTri
    from bamupgrader.bam.GeomTristrip import GeomTristrip
    from bamupgrader.bam.GeomTrifan import GeomTrifan
    from bamupgrader.bam.GeomPoint import GeomPoint
    from bamupgrader.bam.GeomNode import GeomNode
    from bamupgrader.bam.SwitchNode import SwitchNode
    from bamupgrader.bam.SwitchNodeOne import SwitchNodeOne
    from bamupgrader.bam.LODNode import LODNode
    from bamupgrader.bam.SequenceNode import SequenceNode
    # Characters
    from bamupgrader.bam.AnimGroup import AnimGroup
    from bamupgrader.bam.AnimBundle import AnimBundle
    from bamupgrader.bam.AnimBundleNode import AnimBundleNode
    from bamupgrader.bam.AnimChannelBase import AnimChannelBase
    from bamupgrader.bam.PartGroup import PartGroup
    from bamupgrader.bam.PartBundleNode import PartBundleNode
    from bamupgrader.bam.Character import Character
    from bamupgrader.bam.MovingPartBase import MovingPartBase
    from bamupgrader.bam.MovingPartMatrix import MovingPartMatrix
    from bamupgrader.bam.CharacterJoint import CharacterJoint
    from bamupgrader.bam.CharacterJointBundle import CharacterJointBundle
    from bamupgrader.bam.ComputedVertices import ComputedVertices
    from bamupgrader.bam.AnimChannelMatrix import AnimChannelMatrix
    from bamupgrader.bam.AnimChannelMatrixXfmTable import AnimChannelMatrixXfmTable
    from bamupgrader.bam.AnimChannelScalar import AnimChannelScalar
    from bamupgrader.bam.AnimChannelScalarTable import AnimChannelScalarTable
    # Curves
    from bamupgrader.bam.ParametricCurve import ParametricCurve
    from bamupgrader.bam.PiecewiseCurve import PiecewiseCurve
    from bamupgrader.bam.ClassicNurbsCurve import ClassicNurbsCurve
    from bamupgrader.bam.CubicCurveseg import CubicCurveseg

    elements = {
        'Node': Node,
        'NamedNode': NamedNode,
        'ModelNode': ModelNode,
        'ModelRoot': ModelRoot,
        'NodeRelation': NodeRelation,
        'RenderRelation': RenderRelation,
        'NodeTransition': NodeTransition,
        'OnOffTransition': OnOffTransition,
        'OnTransition': OnTransition,
        'TextureTransition': TextureTransition,
        'TextureApplyTransition': TextureApplyTransition,
        'TransparencyTransition': TransparencyTransition,
        'ImmediateTransition': ImmediateTransition,
        'PruneTransition': PruneTransition,
        'CullFaceTransition': CullFaceTransition,
        'DepthWriteTransition': DepthWriteTransition,
        'DepthTestTransition': DepthTestTransition,
        'GeomBinTransition': GeomBinTransition,
        'BillboardTransition': BillboardTransition,
        'MatrixTransition<LMatrix4f>': Matrix4fTransition,
        'TransformTransition': TransformTransition,
        'DecalTransition': DecalTransition,
        'ImageBuffer': ImageBuffer,
        'Texture': Texture,
        'CollisionNode': CollisionNode,
        'CollisionSolid': CollisionSolid,
        'CollisionPlane': CollisionPlane,
        'CollisionPolygon': CollisionPolygon,
        'CollisionSphere': CollisionSphere,
        'Geom': Geom,
        'GeomTri': GeomTri,
        'GeomTristrip': GeomTristrip,
        'GeomTrifan': GeomTrifan,
        'GeomPoint': GeomPoint,
        'GeomNode': GeomNode,
        'SwitchNode': SwitchNode,
        'SwitchNodeOne': SwitchNodeOne,
        'LODNode': LODNode,
        'SequenceNode': SequenceNode,
        'AnimGroup': AnimGroup,
        'AnimBundle': AnimBundle,
        'AnimBundleNode': AnimBundleNode,
        'AnimChannelBase': AnimChannelBase,
        'PartGroup': PartGroup,
        'PartBundleNode': PartBundleNode,
        'Character': Character,
        'MovingPartBase': MovingPartBase,
        'MovingPartMatrix': MovingPartMatrix,
        'MovingPart<LMatrix4f>': MovingPartMatrix,
        'CharacterJoint': CharacterJoint,
        'CharacterJointBundle': CharacterJointBundle,
        'ComputedVertices': ComputedVertices,
        'AnimChannelMatrix': AnimChannelMatrix,
        'AnimChannelMatrixXfmTable': AnimChannelMatrixXfmTable,
        'AnimChannelScalar': AnimChannelScalar,
        'AnimChannelScalarTable': AnimChannelScalar,
        'ParametricCurve': ParametricCurve,
        'PiecewiseCurve': PiecewiseCurve,
        'ClassicNurbsCurve': ClassicNurbsCurve,
        'CubicCurveseg': CubicCurveseg
    }

    for name, value in elements.items():
        BamFactory.register_type(name, value)

def main():
    setup_p3bamboo()

    parser = argparse.ArgumentParser(description='This script can be used to convert old Panda3D BAM version 3.3 models to the new BAM system.')
    parser.add_argument('--model-path', help='The model path to convert all BAM files in.')
    parser.add_argument('--bam-version', help='The bam version to use while writing BAM files. For example: 6.24')
    args = parser.parse_args()

    path = args.model_path

    if path:
        path = path.strip('/\\')

    if not path:
        parser.print_help()
        return 1

    getModelPath().appendPath(Filename.from_os_specific(path))
    loadPrcFileData('settings', 'bam-texture-mode unchanged')

    if args.bam_version:
        version = args.bam_version.split('.')

        if len(version) != 2:
            print('Invalid BAM version! For example, a valid BAM version would look like this: 6.24')
            return 1

        print(f'Using BAM version {args.bam_version}.')
        version = ' '.join(version)
        loadPrcFileData('settings', f'bam-version {version}')

    for root, _, files in os.walk(path):
        old_root = os.path.relpath(root, path)
        new_root = os.path.join(path + '-upgraded', old_root)

        for file in files:
            if not file.endswith('.bam'):
                continue

            full_path = os.path.join(root, file)
            bam = UpgradedBamFile()
            bam.set_filename(full_path)

            print(f'Processing {full_path}...')

            with open(full_path, 'rb') as f:
                bam.load(f)

            if bam.version != (3, 3):
                print(f'Invalid BAM version: {bam.version}')
                return 1

            if not os.path.exists(new_root):
                os.makedirs(new_root)

            bam.write_model(os.path.join(new_root, file))

    return 0

if __name__ == '__main__':
    main()
