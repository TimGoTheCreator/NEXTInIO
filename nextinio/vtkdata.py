import meshio

def read_vtk_file(filename=None):
    if filename is None:
        return None

    mesh = meshio.read(filename)

    # If POLYDATA, convert to unstructured grid with vertex cells
    if mesh.cells and any(c.type == "vertex" for c in mesh.cells):
        cells = [("vertex", np.arange(len(mesh.points)).reshape(-1, 1))]
        mesh = meshio.Mesh(points=mesh.points, cells=cells, point_data=mesh.point_data)

    return {
        "points": mesh.points,
        "cells": mesh.cells,
        "point_data": mesh.point_data,
        "cell_data": mesh.cell_data,
    }
