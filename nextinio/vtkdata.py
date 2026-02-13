import vtk
import numpy as np
from vtk.util.numpy_support import vtk_to_numpy

def read_vtk_file(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()
    polydata = reader.GetOutput()

    points = np.array([polydata.GetPoint(i) for i in range(polydata.GetNumberOfPoints())])
    velocity = vtk_to_numpy(polydata.GetPointData().GetArray("velocity"))
    mass = vtk_to_numpy(polydata.GetPointData().GetArray("mass"))
    ptype = vtk_to_numpy(polydata.GetPointData().GetArray("type"))

    return {
        "points": points,
        "point_data": {
            "velocity": velocity,
            "mass": mass,
            "type": ptype
        }
    }
