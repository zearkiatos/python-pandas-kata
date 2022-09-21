import pandas

data = [19, 18, 29, 14, 20, 20, 20, 19]

temperatures = pandas.Series(data, name="Temperatures in Bogota")

print(temperatures)

print(type(temperatures))

print(temperatures.dtypes)

print(type(temperatures.values))
