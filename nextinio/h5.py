import meshio
import h5py
import numpy as np
from .vtkdata import read_vtk_file

def vtk_to_gadget_hdf5(vtk_filename, hdf5_filename):
    mesh = meshio.read(vtk_filename)

    points = mesh.points
    velocity = mesh.point_data.get("velocity")
    mass = mesh.point_data.get("mass")
    ptype = mesh.point_data.get("type")

    if velocity is None or mass is None or ptype is None:
        raise ValueError("Missing required point_data fields: velocity, mass, or type")

    with h5py.File(hdf5_filename, "w") as f:
        for ptype_id in np.unique(ptype):
            mask = (ptype == ptype_id)
            group = f.create_group(f"PartType{ptype_id}")

            group.create_dataset("Coordinates", data=points[mask])
            group.create_dataset("Velocities", data=velocity[mask])
            group.create_dataset("Masses", data=mass[mask])

            # Optional: add dummy IDs
            group.create_dataset("ParticleIDs", data=np.arange(np.sum(mask), dtype=np.uint64))