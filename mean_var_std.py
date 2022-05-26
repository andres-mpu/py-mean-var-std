# Mean-Variance-Standard Deviation Calculator

# https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer

# https://docs.python.org/3/tutorial/errors.html#exceptions
# https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html
# https://numpy.org/doc/stable/reference/generated/numpy.matrix.std.html

# How to Use Numpy Variance [AKA, np.var]
# https://www.sharpsightlabs.com/blog/numpy-variance/#example-2

import numpy as np

def calculate(_numbers):
  if len(_numbers) < 9:
    raise ValueError("List must contain nine numbers.")

  _matrix = np.asarray(_numbers).reshape(3,3)

  column_mean     = np.mean(_matrix, 0)
  row_mean        = np.mean(_matrix, 1)
  matrix_mean     = np.mean(_matrix)

  column_variance = np.var(_matrix, 0)
  row_variance    = np.var(_matrix, 1)
  matrix_variance = np.var(_matrix)

  column_standard_deviation = np.std(_matrix, 0)
  row_standard_deviation    = np.std(_matrix, 1)
  matrix_standard_deviation = np.std(_matrix)

  column_max = np.max(_matrix, 0)
  row_max    = np.max(_matrix, 1)
  matrix_max = np.max(_matrix)

  column_min = np.min(_matrix, 0)
  row_min    = np.min(_matrix, 1)
  matrix_min = np.min(_matrix)

  column_sum = np.sum(_matrix, 0)
  row_sum    = np.sum(_matrix, 1)
  matrix_sum = np.sum(_matrix)

  calculations = {
    'mean' : [column_mean.tolist(), row_mean.tolist(), matrix_mean],
    'variance' : [column_variance.tolist(), row_variance.tolist(), matrix_variance],
    'standard deviation' : [column_standard_deviation.tolist(), row_standard_deviation.tolist(), matrix_standard_deviation],
    'max' : [column_max.tolist(), row_max.tolist(), matrix_max],
    'min' : [column_min.tolist(), row_min.tolist(), matrix_min],
    'sum' : [column_sum.tolist(), row_sum.tolist(), matrix_sum]
    }

  return calculations
