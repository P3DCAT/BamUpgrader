from panda3d.core import NodePath, TexturePool, Filename
from p3bamboo.BamFile import BamFile

class UpgradedBamFile(BamFile):

    def add_node(self, obj, node):
        for relation in obj.get_relations():
            child = self.object_map[relation.child_id]
            child_node = child.create_node()

            if not child_node:
                continue

            child_node_path = NodePath(child_node)

            for transition in relation.get_transitions():
                transition.apply(child_node_path)

            child_node_path.reparentTo(node)
            self.add_node(child, child_node_path)

        obj.finalize_node(node)

    def write_model(self, filename):
        model_root = next(self.get_objects_of_type('ModelRoot'))
        root = NodePath(model_root.create_node())

        self.add_node(model_root, root)
        model_root.finalize_node(root)
        root.ls()

        root.write_bam_file(Filename.from_os_specific(filename))
