import patyczki
import numpy as np

def test_green_function_values():

  xpts = np.arange(0.1,0.71,0.1)

  y = 1.4
  y0 = 2.1
  x0 = 1.7
  w = 3.0

  result = np.array([[x, patyczki.green_functions.green(x,y,x0,y0,w)] for x in xpts])

  target = np.array([[0.1,0.00564661],[0.2,0.0055438],[0.3,0.00537652],[0.4,0.00515071],[0.5,0.00487436],[0.6,0.00455722],[0.7,0.00421043]])

  assert np.isclose(result, target, atol=1e-6).all()
  
