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
        *half* width of the strip

    Returns
    -------
    float
        value of Greens function at loction (x,y) with source located at (x0,y0).

    """

    return (
        (np.cos(np.pi * (x - x0) / w) - np.cosh(np.pi * (y - y0) / w))
        * (np.cos(np.pi * (x + x0) / w) - np.cosh(np.pi * (y - y0) / w))
    ) / (
        (np.cos(np.pi * (x - x0) / w) - np.cosh(np.pi * (y + y0) / w))
        * (np.cos(np.pi * (x + x0) / w) - np.cosh(np.pi * (y + y0) / w))
    )
