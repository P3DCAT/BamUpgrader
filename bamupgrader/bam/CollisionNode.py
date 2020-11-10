from panda3d import core
from .NamedNode import NamedNode

class CollisionNode(NamedNode):

    def __init__(self, bam_file, bam_version):
        NamedNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        NamedNode.load(self, di)

        num_solids = di.get_uint16()
        self.solid_ids = [self.bam_file.read_pointer(di) for i in range(num_solids)]

        self.from_collide_mask = di.get_uint32()
        self.into_collide_mask = di.get_uint32()
        self.collide_geom = di.get_bool()

    def write(self, write_version, dg):
        NamedNode.write(self, write_version, dg)
        dg.add_uint16(len(self.solid_ids))

        for solid_id in self.solid_ids:
            self.bam_file.write_pointer(dg, solid_id)

        dg.add_uint32(self.from_collide_mask)
        dg.add_uint32(self.into_collide_mask)
        dg.add_bool(self.collide_geom)

    def get_solids(self):
        return [self.bam_file.object_map[obj_id] for obj_id in self.solid_ids]

    def create_node(self):
        node = core.CollisionNode(self.name)
        node.set_from_collide_mask(self.from_collide_mask)
        node.set_into_collide_mask(self.into_collide_mask)

        for solid in self.get_solids():
            solid = solid.create_node()

            if solid:
                node.addSolid(solid)

        return node

    def __str__(self):
        return f'CollisionNode(solid_ids={self.solid_ids}, from_collide_mask={self.from_collide_mask}, into_collide_mask={self.into_collide_mask}, collide_geom={self.collide_geom}, {NamedNode.__str__(self)})'
