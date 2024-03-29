import patyczki
import numpy as np


def test_green_function_values():

    xpts = np.arange(0.1, 2.51, 0.1)

    y = 1.4
    y0 = 2.1
    x0 = 1.7
    w = 3.0

    result = np.array(
        [[x, patyczki.green_functions.green(x, y, x0, y0, w)] for x in xpts]
    )

    target = np.array(
        [
            [0.1, -2.58835],
            [0.2, -2.59754],
            [0.3, -2.61286],
            [0.4, -2.63431],
            [0.5, -2.66188],
            [0.6, -2.69552],
            [0.7, -2.73509],
            [0.8, -2.78035],
            [0.9, -2.83084],
            [1.0, -2.88579],
            [1.1, -2.94399],
            [1.2, -3.00363],
            [1.3, -3.06211],
            [1.4, -3.11602],
            [1.5, -3.16135],
            [1.6, -3.19408],
            [1.7, -3.21115],
            [1.8, -3.21143],
            [1.9, -3.19613],
            [2.0, -3.1684],
            [2.1, -3.13235],
            [2.2, -3.09209],
            [2.3, -3.05112],
            [2.4, -3.0121],
            [2.5, -2.97696],
        ]
    )

    assert np.isclose(result, target, atol=1e-6).all()


def test_green_function_singularity_removed_values():

    xpts = np.arange(0.1, 2.51, 0.1)

    y = 2.1
    w = 3.0

    result = np.array(
        [[x, patyczki.green_functions.nonsingular_part_green(x, y, w)] for x in xpts]
    )

    target = np.array(
        [
            [0.1, -5.89279],
            [0.2, -5.20594],
            [0.3, -4.81098],
            [0.4, -4.53796],
            [0.5, -4.33363],
            [0.6, -4.17424],
            [0.7, -4.04715],
            [0.8, -3.94481],
            [0.9, -3.86239],
            [1.0, -3.79662],
            [1.1, -3.74525],
            [1.2, -3.7067],
            [1.3, -3.67987],
            [1.4, -3.66404],
            [1.5, -3.65881],
            [1.6, -3.66404],
            [1.7, -3.67987],
            [1.8, -3.7067],
            [1.9, -3.74525],
            [2.0, -3.79662],
            [2.1, -3.86239],
            [2.2, -3.94481],
            [2.3, -4.04715],
            [2.4, -4.17424],
            [2.5, -4.33363],
        ]
    )

    assert np.isclose(result, target, atol=1e-6).all()

def test_green_function_singularity_requilarized():
    result = patyczki.green_functions.singular_part_green(0.1)
    target = -3.99573
    
    assert np.isclose(result,target, atol=1e-6).all()


