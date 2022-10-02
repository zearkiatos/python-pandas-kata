import pandas
import matplotlib.pyplot as pyplot


data = pandas.read_csv(
    './data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)

data.plot(kind="scatter", x="Valor del Contrato", y="Valor Pendiente de Pago")

pyplot.savefig('./assets/dispersion-graph.png')


