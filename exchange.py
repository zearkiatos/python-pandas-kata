import pandas


def convert_to_dollars(number: float) -> int:
    return round(number / 3600)


values = pandas.read_csv(
    './data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)

print(values["Valor del Contrato"])
print(values["Valor del Contrato"].apply(convert_to_dollars))

print("Use a lambda function \n")


def lambda_function(number): return round(number/3600)


print(values["Valor del Contrato"].apply(lambda_function))

print(values["Valor del Contrato"].apply(lambda number: round(number/3600)))

values["Alto valor"] = values["Valor del Contrato"].apply(
    lambda value: "Yes" if value > 100000000 else "No")


print(values["Alto valor"])

print(values["Alto valor"].value_counts())

print("Conditional instructions \n")

value = 20
result = "Yes" if value > 10 else "No"

print(result)

values["Alto valor bool"] = values["Alto valor"].apply(
    lambda value: True if value == "Yes" else False)

print(values["Alto valor bool"])

values = values.drop("Alto valor", axis=1)

values = values.drop("Alto valor bool", axis=1)

print(values)

print(values.apply(sum))

print(values.apply(sum, axis=1))

print(values.apply(lambda x: (x.max()-x.min()), axis=0))

print(values.apply(lambda x: (x.max()-x.min()), axis=1))


def count_zeros(column_values) -> int:
    zeros = 0
    quantity = column_values.value_counts()
    if 0 in quantity:
        zeros = quantity.loc[0]
    return zeros


print(values.apply(count_zeros))


def calculate_next_percentaje(registry) -> float:
    total = registry["Valor del Contrato"]
    next_value = registry["Valor de pago adelantado"]

    if total > 0:
        percentaje = next_value / total
    else:
        percentaje = 0

    return round(percentaje, 2)


values["Porcentaje adelantado"] = values.apply(
    calculate_next_percentaje, axis=1)

values["Porcentaje adelantado"].quantile(0.999)

values_dollars = values.applymap(lambda x: x/3600)

print(values_dollars)
