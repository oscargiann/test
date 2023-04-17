import xarray as xr
import numpy as np
import pandas as pd
 

def sum_two(a, b):
    return a + b
    

def operation():
    data = xr.DataArray(np.random.randn(2, 3), dims=("x", "y"), coords={"x": [10, 20]})
    return data
