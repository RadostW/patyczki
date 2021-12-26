import patyczki.green_functions
import numpy as np


def coupling_matrix(mesh, mesh_sizes, w=1.0):
    """
    Create coupling matrix out of locations of discretization points and sizes
    of the discretized segments. A discretization of Green-Fredholm equation for
    the solution of Laplaces problem. When you apply this matrix to a vector of
    weights you get values of Laplace-field at discretization points.

    Parameters
    ----------
    mesh : np.array
        A 2-n array containing (x,y) coordinates of the mesh points.
    mesh_sizes : np.array
        A 1-n array containing sizes of segments surrounding corresponding
    points of the discretization.

    Returns
    -------
    np.array
        A n-n array of coupling terms.

    """

    offdiag_entries = patyczki.green_functions.green(
        mesh[:, np.newaxis, 0],
        mesh[:, np.newaxis, 1],
        mesh[np.newaxis, :, 0],
        mesh[np.newaxis, :, 1],
        w=w,
    )
    
    np.fill_diagonal(offdiag_entries,0.0) # Fix diagonal entries inplace.

    diag_entries = np.diag(
        patyczki.green_functions.nonsingular_part_green(mesh[:, 0], mesh[:, 1], w=w)
        + patyczki.green_functions.singular_part_green(mesh_sizes)
    )

    return offdiag_entries + diag_entries


