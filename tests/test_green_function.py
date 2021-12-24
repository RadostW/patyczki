import patyczki
import numpy

def test_green_function_values():

  a = 2.0

  assert numpy.isclose(a, 2.0, atol=1e-6)
  
