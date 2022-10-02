import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as pyplot

data = pandas.read_csv(
    './data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)


numbers = data[["Valor Pagado", "Valor Pendiente de Pago"]]

scatter_matrix(numbers, alpha=0.7, figsize=(8, 8), diagonal="hist")

pyplot.savefig('./assets/dispersion-matrix.png')

columns = numbers[["Valor Pagado", "Valor Pendiente de Pago"]]

columns.plot(kind="hist", figsize=(10, 4), xlim=(-1, 30), bins=10, subplots=True,
             layout=(1, 2), sharey=True, title="Valores pagados y pendientes")

pyplot.savefig('./assets/dispersion-matrix-multiple.png')
