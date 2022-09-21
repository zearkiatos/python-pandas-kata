import pandas

data = [19, 18, 29, 14, 20, 20, 20, 20, 19]

dates = ["5/11/20", "6/11/20", "7/11/20", "8/11/20",
         "9/11/20", "10/11/20", "11/11/20", "12/11/20", "13/11/20"]


temperatures = pandas.Series(data, index=dates, name="Temperatures in Bogota")

print(temperatures)
