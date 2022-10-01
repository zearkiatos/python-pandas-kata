import pandas
import matplotlib.pyplot as pyplot


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


data = pandas.read_csv(
    './data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)

colors = {
    "boxes": "#9965DD",
    "whiskers": "#FFA010",
    "medians": "#1010A0",
    "caps": "#FF0000"
}

data.boxplot(by="Departamento", column=["Valor del Contrato"], rot="90", figsize=(
    8, 4), color=colors, notch=True, sym="*", widths=0.5, showmeans=True, fontsize="small")

pyplot.savefig("./assets/customBoxplots.png")
