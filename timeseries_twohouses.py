#!/usr/bin/env python

##time series for two houses
import pandas as pd

data = { 'datetime' : pd.date_range(start='14/02/2020', end='20/02/2020', freq='D')}

print(data)