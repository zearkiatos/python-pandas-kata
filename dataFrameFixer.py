import pandas
import numpy

dataframe = pandas.DataFrame([{
    "number": numpy.nan,
    "date": pandas.NaT,
    "string": None
}])

print(dataframe)

print(dataframe.info())

print(dataframe.isna())

data = pandas.read_csv('./data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)

print(data)

date = data.loc[15, "Fecha de Fin del Contrato"]

print(date)

print(type(date))

print(pandas.to_datetime(date, infer_datetime_format=True, errors="coerce"))

print(pandas.to_datetime("2020-02-30", infer_datetime_format=True, errors="coerce"))

date["fechas corregidas"] = pandas.to_datetime(
    data["Fecha de Fin del Contrato"], infer_datetime_format=True, errors="coerce")

print(date["fechas corregidas"].isna().value_counts())

print(date[(data["Fecha de Fin del Contrato"].notna()) & (date["fechas corregidas"].isna())] [["Fecha de Fin del Contrato"], "fechas corregidas"])

date["Años"] = date["fechas corregidas"].dt.year
print(data.loc[0:5, "Año"])

date["Año"] = date["Año"].fillna(0)

print(date.loc[0:5, "Año"])
