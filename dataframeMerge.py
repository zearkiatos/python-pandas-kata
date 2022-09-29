import pandas

data = pandas.read_csv('./data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)

activated = data[data["Estado Contrato"] == "Activo"].head()

print(activated)

canceled = data[data["Estado Contrato"] == "Cerrado"].head()

print(canceled)

activated_canceled = pandas.concat([activated, canceled])

print(activated_canceled)

average_by_sector = data.groupby("Sector").mean()

print(average_by_sector)
