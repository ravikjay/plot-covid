# COVID-19 ANALYSIS

## Overview
A python script that aggregates data from the Humanitarian Data Exchange.

### Terminology

#### Pandas
- the most convenient installation strategy leverages Anaconda
- __Series__
  - a one dimensional (1-D) array that can store any data types
    - eg. `a = pandas.Series(Data, index = Index)`
  - `Data` can be:
    - a `Scalar` value (`int` or `string`)
      - in which case the default index used is `[0, 1, ... , n-1]`
    - a Python `dictionary` (`<key, value>` pair)
      - in which case the keys will form the index
      - eg. `dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}`
        - the index will be `['a', 'b', 'c', ...]`
    - a Ndarray (N-dimensional)
      - in which case the cardinality of the (N-1)th dimension will form the index
      - eg. `Data = [[2, 3, 4], [5, 6, 7]]`
        ```
          index   values
            0    [2, 3, 4]
            1    [5, 6, 7]
        ```
- __DataFrames__
  - a two-dimensional (2-D) data structure with rows & columns (essentially a table)
  - we can leverage this structure to do things like:
    - calculate statistics & answer questions about the data
      - average, median, min, max of each column?
      - does column A correlate with column B?
      - what does the distribution of data in column C look like?
    - clean the data
      - an underrated but essential component of analysis
      - remove missing values & filter rows / columns by selected criteria
    - visualize the data (with [Plotly](#plotly) perhaps)
    - export the munged data back to a CSV, file, or database
  - `Data` can be:
    - one or more `dictionaries`
      ```
      dict1 = {'a':1, 'b':2, 'c':3, 'd':4}           # Define Dictionary 1
      dict2 = {'a':5, 'b':6, 'c':7, 'd':8, 'e':9}    # Define Dictionary 2
      Data  = {'first':dict1, 'second':dict2}        # Define Data with dict1 and dict2
      df    = pandas.DataFrame(Data)                 # Create DataFrame

      /render
      index    first      second
        a       1.0         5
        b       2.0         6
        c       3.0         7
        d       4.0         8
        e       NaN         9

        ** NaN = Not a Number **  
      ```
    - one or more `Series`
      ```
      s1 = pandas.Series([1, 3, 4, 5, 6, 2, 9])             # Define series 1
      s2 = pandas.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])    # Define series 2
      s3 = pandas.Series(['a', 'b', 'c', 'd', 'e'])         # Define series 3

      Data = {'first':s1, 'second':s2, 'third':s3}          # Define Data
      dfseries = pandas.DataFrame(Data)                     # Create DataFrame

      /render
      index    first      second    third
        0        1         1.1        a
        1        3         3.5        b
        2        4         4.7        c
        3        5         5.8        d
        4        6         2.9        e
        5        2         9.3       NaN
        6        9         NaN       NaN

        ** NaN = Not a Number **  
      ```
    - `2D-numpy Ndarray`
      ```
      d1   = [[2, 3, 4], [5, 6, 7]]       # Define 2d array 1
      d2   = [[2, 4, 8], [1, 3, 9]]       # Define 2d array 2
      Data = {'first': d1, 'second': d2}  # Define Data  
      df2d = pandas.DataFrame(Data)       # Create DataFrame

      /render
      index    first       second
        0    [2, 3, 4]    [2, 4, 8]
        1    [5, 6, 7]    [1, 3, 9]
      ```
    -

<!-- TODO write this up -->
#### Plotly
