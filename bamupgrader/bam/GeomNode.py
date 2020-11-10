from panda3d import core
from .NamedNode import NamedNode
from .GeomPoint import GeomPoint

norms = 0
no_norms = 0

class GeomNode(NamedNode):

    def __init__(self, bam_file, bam_version):
        NamedNode.__init__(self, bam_file, bam_version)

    def load(self, di):
        NamedNode.load(self, di)

        num_geoms = di.get_uint16()
        self.geom_ids = [self.bam_file.read_pointer(di) for i in range(num_geoms)]

    def write(self, write_version, dg):
        NamedNode.write(self, write_version, dg)
        dg.add_uint16(len(self.geom_ids))

        for geom in self.geom_ids:
            self.bam_file.write_pointer(dg, geom)

    def get_geoms(self):
        return [self.bam_file.object_map[obj_id] for obj_id in self.geom_ids]

    def create_node(self):
        node = core.GeomNode(self.name)

        for geom in self.get_geoms():
            self.add_geom(node, geom)

        return node

    def add_geom(self, node, geom_obj):
        if geom_obj.norms:
            if geom_obj.texcoords:
                if geom_obj.colors:
                    gformat = core.GeomVertexFormat.get_v3n3c4t2()
                else:
                    gformat = core.GeomVertexFormat.get_v3n3t2()
            else:
                gformat = core.GeomVertexFormat.get_v3n3()
        elif geom_obj.texcoords:
            if geom_obj.colors:
                gformat = core.GeomVertexFormat.get_v3c4t2()
            else:
                gformat = core.GeomVertexFormat.get_v3t2()
        elif geom_obj.colors:
            gformat = core.GeomVertexFormat.get_v3c4()
        else:
            gformat = core.GeomVertexFormat.get_v3()

        data = core.GeomVertexData(node.getName(), gformat, core.Geom.UH_static)
        vertexWriter = core.GeomVertexWriter(data, 'vertex')

        for coord in geom_obj.coords:
            vertexWriter.addData3f(coord)

        if geom_obj.norms:
            normalWriter = core.GeomVertexWriter(data, 'normal')

            for coord in geom_obj.coords:
                normalWriter.addData3f(coord)

        if geom_obj.colors:
            colorWriter = core.GeomVertexWriter(data, 'color')

            for coord in geom_obj.colors:
                colorWriter.addData4f(coord)
            for i in range(len(geom_obj.coords) - len(geom_obj.colors)):
                colorWriter.addData4f(geom_obj.colors[-1])

        if geom_obj.texcoords:
            texCoordWriter = core.GeomVertexWriter(data, 'texcoord')

            for coord in geom_obj.texcoords:
                texCoordWriter.addData2f(coord)

        tris = geom_obj.create_primitive()

        if not tris:
            return

        k = 0

        if isinstance(geom_obj, GeomPoint):
            default_length = 1
        else:
            default_length = 3

        geom = core.Geom(data)

        for i in range(geom_obj.num_prims):
            if geom_obj.prim_lengths:
                length = geom_obj.prim_lengths[i]
            else:
                length = default_length

            if geom_obj.vindex:
                for j in range(length):
                    tris.addVertex(geom_obj.vindex[k + j])
            else:
                for j in range(length):
                    tris.addVertex(k + j)

            tris.closePrimitive()
            geom.addPrimitive(tris)
            tris = geom_obj.create_primitive()
            k += length

        node.addGeom(geom)

    def __str__(self):
        return f'GeomNode(geom_ids={self.geom_ids}, {NamedNode.__str__(self)})'
