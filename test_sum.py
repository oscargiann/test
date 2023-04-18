from .sum_numbers import sum_two, operation
from pytest import raises
import xarray as xr
import numpy as np
import pandas as pd

def test_sum():
    a = 10
    b = 1
    c = sum_two(a, b)

    assert c == a + b


def test_operation():
    assert isinstance(operation(), xr.DataArray)
