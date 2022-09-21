import pandas
import numpy

serie = pandas.Series(numpy.random.normal(100, 20, 1000))

print(serie)

print(serie.sort_values())

print(serie.sort_index())

copy = serie.copy()

copy[500] = 180

print(copy)

copy[0:100] = 20

print(copy)

copy[900:1000] = [40]*100

print(copy)

copy = serie.sort_values().copy()

print(copy)

copy[500] = 180

print(copy)

copy[0:100] = 20

print(copy)

copy[900:1000] = [40]*100

print(copy)

copy = serie.copy()

copy.loc[500] = 180

print(copy)

copy.loc[0:100] = 20

print(copy)

copy.loc[900:1000] = [40]*100

print(copy)

copy = serie.copy()

copy.iloc[500] = 180

print(copy)

copy.iloc[0:100] = 20

print(copy)

copy.iloc[900:1000] = [40]*100

print(copy)
