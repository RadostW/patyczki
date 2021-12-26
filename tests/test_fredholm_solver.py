import patyczki
import numpy as np


def test_coupling_matrix():

    mesh = np.array([[1.0, 2.77778], [1.0, 7.22222], [1.0, 9.44444]])
    mesh_sizes = np.array([5.55556, 3.33333, 1.11111])


    result = patyczki.fredholm_solver.coupling_matrix(mesh, mesh_sizes, w=2.0)

    target = np.array([[-7.56027,-8.72665,-8.72665],[-8.72665,-22.0337,-22.6902],[-8.72665,-22.6902,-30.1137]])

    assert np.isclose(result, target, atol=1e-6).all()


def test_weight_solver():

    mesh = np.array([[1.0, 2.77778], [1.0, 7.22222], [1.0, 9.44444]])
    mesh_sizes = np.array([5.55556, 3.33333, 1.11111])
    mesh_values = np.array([2.77778, 7.22222, 9.44444])

    result = patyczki.fredholm_solver.weights(mesh, mesh_sizes, mesh_values, w=2.0)

    target = [-0.00129594, 0.0220288, 0.297404]

    assert np.isclose(result, target, atol=1e-6).all()
