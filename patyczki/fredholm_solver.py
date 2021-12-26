import patyczki.green_functions
import numpy as np
import numpy.linalg


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
    w : float, default 1.0
        width of the strip


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

    np.fill_diagonal(offdiag_entries, 0.0)  # Fix diagonal entries inplace.

    diag_entries = np.diag(
        patyczki.green_functions.nonsingular_part_green(mesh[:, 0], mesh[:, 1], w=w)
        + patyczki.green_functions.singular_part_green(mesh_sizes)
    )

    return offdiag_entries + diag_entries


def weights(mesh, mesh_sizes, mesh_values, w=1.0):
    """
    Give solution for weights that result in Laplace field with values
    `mesh_values` at `mesh` locations.

    Parameters
    ----------
    mesh : np.array
        A 2-n array containing (x,y) coordinates of the mesh points.
    mesh_sizes : np.array
        A 1-n array containing sizes of segments surrounding corresponding
    mesh_values : np.array
        A 1-n array containing target values at the mesh points.
        points of the discretization.
    w : float, default 1.0
        width of the strip


    Returns
    -------
    np.array
        A 1-n array of weights.

    """

    return numpy.linalg.solve(coupling_matrix(mesh, mesh_sizes, w=w), -mesh_values)
