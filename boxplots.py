import pandas
import matplotlib.pyplot as pyplot


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


data = pandas.read_csv(
    './data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)

data[['Valor del Contrato', "Valor Pagado",
      "Valor Pendiente de Pago"]].plot(kind="box")

pyplot.savefig("./assets/boxplot.png")

data[['Rama', "Valor Pagado", "Valor Pendiente de Pago"]
     ].boxplot(by="Rama", rot="45")

pyplot.savefig("./assets/boxplot-agroups.png")
