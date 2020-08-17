from marching_cubes import edge_index, triangulation, edge_table


def marching_cubes(content, step=1):
    interval = range(0, len(content) - 1, step)
    triangles = []
    for z in interval:
        nxz = z + step if z + step < len(content) else len(content)-1
        for y in interval:
            nxy = y + step if y + step < len(content[z]) else len(content[z])-1
            for x in interval:
                nxx = x + step if x + step < len(content[z][y]) else len(content[z][y])-1
                cube = [content[nxz][nxy][x], content[nxz][nxy][nxx],
                        content[z][nxy][nxx], content[z][nxy][x],
                        content[nxz][y][x], content[nxz][y][nxx],
                        content[z][y][nxx], content[z][y][x]]
                triangles += triangulize(get_edges(cube), step, [x, y, z])
    return triangles


def triangulize(verts, step, base_index):
    triangles = []
    for combination in verts:
        triangle = []
        for edge in combination:
            relative_index = [step * edge_index[edge][i] for i in range(3)]
            triangle.append([relative_index[i] + base_index[i] for i in range(len(base_index))])
        triangles.append(triangle)
    return triangles


def get_edges(verts):
    edges = edge_table[int("".join(map(str, map(int, verts))), 2)]
    return triangulation.get(edges)
