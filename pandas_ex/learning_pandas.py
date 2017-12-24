#!/usr/local/bin/python3.6

import pandas as pd
import numpy as np

# A structured array
my_array = np.ones(3, dtype = ([('foo', int), ('bar', float)]))

# Print the structured array
print(my_array['bar'])

# A record array
my_array2 = my_array.view(np.recarray)

# Print the record array
print(my_array2.foo)
