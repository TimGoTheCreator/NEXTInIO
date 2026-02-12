import meshio

def read_vtk_file(filename=None):
    """
    Read a VTK file if a filename is provided.
    If POLYDATA, convert to a point-only mesh so downstream
    code can treat it like an unstructured grid.
    """
    if filename is None:
        return None
    
    mesh = meshio.read(filename)

    # Detect POLYDATA with vertex cells
    if mesh.cells and any(c.type == "vertex" for c in mesh.cells):
        # Re-wrap as point-only mesh (ignore connectivity)
        mesh = meshio.Mesh(points=mesh.points, point_data=mesh.point_data)

    return {
        "points": mesh.points,
        "cells": mesh.cells,
        "point_data": mesh.point_data,
        "cell_data": mesh.cell_data,
    }
