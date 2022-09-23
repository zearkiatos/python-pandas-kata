import pandas

a1 = {"time": 9.58, "athletes": "Usain Bolt",
      "country": "Jamaica", "date": "16/08/2009", "city": "Berlin"}

a2 = {"time": 9.69, "athletes": "Usain Bolt",
      "country": "Jamaica", "date": "16/09/2008", "city": "Beijing"}

a3 = {"time": 9.72, "athletes": "Usain Bolt",
      "country": "Jamaica", "date": "31/05/2008", "city": "New York"}

a4 = {"time": 9.74, "athletes": "Asafa Powell",
      "country": "Jamaica", "date": "09/09/2007", "city": "Reiti"}

a5 = {"time": 9.77, "athletes": "Asafa Powell",
      "country": "Jamaica", "date": "18/08/2006", "city": "Zurich"}

records = [a1, a2, a3, a4, a5]

dataFrame_records = pandas.DataFrame(records)

print(dataFrame_records)

times = [9.58, 9.69, 9.72, 9.74, 9.77]

athletes = ["Usain Bolt", "Usain Bolt",
            "Usain Bolt", "Asafa Powell", "Asafa Powell"]

countries = ["Jamaica", "Jamaica", "Jamaica", "Jamaica", "Jamaica"]

dates = ["16/08/2009", "16/09/2008", "31/05/2008", "09/09/2007", "18/08/2006"]

cities = ["Berlin", "Beijing", "New York", "Rieti", "Zurich"]

data = {
    "time": times,
    "athlete": athletes,
    "country": countries,
    "date": dates,
    "city": cities
}

dataFrame_records = pandas.DataFrame(dates)

print(dataFrame_records)

times = pandas.Series([9.58, 9.69, 9.72, 9.74, 9.77])

athletes = pandas.Series(["Usain Bolt", "Usain Bolt",
                          "Usain Bolt", "Asafa Powell", "Asafa Powell"])

countries = pandas.Series(
    ["Jamaica", "Jamaica", "Jamaica", "Jamaica", "Jamaica"])

dates = pandas.Series(
    ["16/08/2009", "16/09/2008", "31/05/2008", "09/09/2007", "18/08/2006"])

cities = pandas.Series(["Berlin", "Beijing", "New York", "Rieti", "Zurich"])

data_series = {
    "time": times,
    "athlete": athletes,
    "country": countries,
    "date": dates,
    "city": cities
}

dataFrame_records = pandas.DataFrame(data_series)

print(dataFrame_records)

dataFrame_records = pandas.read_csv('./data/records.csv')

print(dataFrame_records)

data = pandas.read_csv('./data/SECOP_II_-_Contratos_Electr_nicos.csv')

print(data.columns)

columns_values = ["Valor del Contrato", "Valor de pago adelantado",
                  "Valor Pendiente de Pago", "Valor Pagado", "Sector"]

values = data[columns_values].copy()

categories = values.copy()

print(values)

print(categories.head(5))

print(categories.tail())

print(categories.info())

print(categories.describe())

print(categories["Sector"].unique())

print(categories["Sector"].value_counts())

print(values.mean())

print(values["Valor Pagado"].mean())

print(values.max())

print(values.idmax())

print(values.quantile(0.50))

print(values.quantile(0.95))

print(values.sum())

print(values.div(1000000))

print(values.sum(axis=1))
