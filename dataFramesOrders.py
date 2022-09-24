import pandas

data = pandas.read_csv('./data/SECOP_II_-_Contratos_Electr_nicos.csv')

columns_values = ["Sector", "Estado Contrato",
                  "Fecha de Firma", "Es Pyme"]

categories = data[columns_values].copy()

categories_orders = categories.sort_values("Estado Contrato")

print(categories_orders)

print(categories_orders.iloc[5])

print(categories_orders.iloc[5:10])

print(categories_orders.loc[5])

print(categories_orders.loc[5:10, ["Sector", "Es Pyme"]])

show = categories_orders.iloc[0:4]

print(show)


print(categories_orders["Estado Contrato"] == 'Activo')

print(categories_orders[categories_orders["Estado Contrato"] == 'Activo'])

print(categories_orders[(categories_orders["Estado Contrato"] == 'Activo') | (
    categories_orders["Estado Contrato"] == 'En ejecución')])

february_contract = categories_orders[(
    categories_orders["Fecha de Firma"] >= "2020-02-01") & (categories_orders["Fecha de Firma"] < "2020-03-01")]

print(february_contract)

print(categories[categories["Sector"].isin(["Servicio Público", "deportes"])])