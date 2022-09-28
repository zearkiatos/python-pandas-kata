import pandas

data = pandas.read_csv('./data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)

by_branch = data.groupby("Rama")

print(len(by_branch))

for name, group in by_branch:
    print(name, len(group))

executive = by_branch.get_group('Ejecutivo')

print(executive)

print(by_branch["Valor Pagado"])

print(by_branch["Valor Pagado"].mean())

print(by_branch.describe())

multiply = data.groupby(["Rama", "Sector"])

print(multiply)

print(multiply.sum())

print(multiply.apply(max))
