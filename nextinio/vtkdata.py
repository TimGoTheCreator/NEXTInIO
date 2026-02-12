import meshio

def read_vtk_file(filename=None):
    """
    Read a VTK file if a filename is provided.
    If no filename is given, just return None.
    """
    if filename is None:
        # Nothing to do if you don't want to use it
        return None
    
    # We use meshio cause its lightweight to type
    mesh = meshio.read(filename)
    return {
        "points": mesh.points,
        "cells": mesh.cells,
        "point_data": mesh.point_data,
        "cell_data": mesh.cell_data,
    }
