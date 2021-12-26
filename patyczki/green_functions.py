import numpy as np

def green(x, y, x0, y0, w=1.0):
    """
    Greens function to Laplaces equation in semi-infinite strip, with reflective
    walls and absorbing floor.

    Parameters
    ----------
    x : float
        x coordinate of sample point
    y : float
        y coordinate of sample point
    x0 : float
        x coordinate of point source
    y0 : float
        y coordinate of point source
    w : float, default 1.0
        width of the strip

    Returns
    -------
    float
        value of Greens function at loction (x,y) with source located at (x0,y0).

    """

    return 0.5 * np.log(
        (
            (np.cos(np.pi * (x - x0) / w) - np.cosh(np.pi * (y - y0) / w))
            * (np.cos(np.pi * (x + x0) / w) - np.cosh(np.pi * (y - y0) / w))
        )
        / (
            (np.cos(np.pi * (x - x0) / w) - np.cosh(np.pi * (y + y0) / w))
            * (np.cos(np.pi * (x + x0) / w) - np.cosh(np.pi * (y + y0) / w))
        )
    )


def nonsingular_part_green(x, y, w=1.0):
    """
    Nonsingular part of the Greens function evaluated at the location of the
    source. :math:`\lim_{(x,y)\to(x_0,y_0)}G(x,y,x_0,y_0) - 1/2 \log((x-x_0)^2+(y-y_0)^2)`.
    In other words contributions from reflected sources only evaluated at the 
    original source.

    Parameters
    ----------
    x : float
        x coordinate of sample point
    y : float
        y coordinate of sample point
    w : float, default 1.0
        width of the strip

    Returns
    -------
    float
        value of the nonsingular component of the Greens function at source.

    """

    return 0.5 * np.log(
        (np.pi ** 2 * np.sin(np.pi * x / w) ** 2)
        / (
            2
            * w ** 2
            * np.sinh(np.pi * y / w) ** 2
            * (np.cosh(2 * np.pi * y / w) - np.cos(2 * np.pi * x / w))
        )
    )


def singular_part_green(mesh_size):
    """
    Singular asymptotic of Greens function evaluated at the location of the
    source. If the source was smeared on line element of length `mesh_size` then
    this would be the value of the field in the middle of the line segment.

    Parameters
    ----------
    mesh_size : float
        size of the smear line segment

    Returns
    -------
    float
        value of the regularized Greens function evaluated at the source.

    """

    return 0.5 * (-2 + np.log(mesh_size ** 2 / 4))
