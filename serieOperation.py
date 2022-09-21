import pandas

serie_2 = pandas.Series([2, 4, 8, 16, 32])

serie_3 = pandas.Series([1, 8, 27, 64, 125])

serie_4 = pandas.Series([1, 16, 81, 256, 625, 1296])

print(serie_2)

print("Extract a value use an index\n")

print(serie_2.get(2))

print("Extract a value use the indexes: loc[init:end]\n")

print(serie_2.loc[2:4])

print("Extract a value use the positions: iloc[init:end]\n")

print(serie_2.iloc[2:4])

print(serie_2.values)

numbers = serie_2.to_list()

for number in numbers:
    print(number)

copy = serie_2.copy()

print(copy)

print(serie_2+1)

print(serie_3 - 1)

print(serie_4 * 1)

print(serie_2/1)

print(serie_3//2)

print(serie_4 % 2)

print(serie_2 + serie_3)

print(serie_2 + serie_4)

print(serie_2.add(serie_4, fill_value=0))


print(serie_2.max())

print(serie_3.min())

print(serie_4.mean())

print(serie_2.std())

print(serie_3.median())
