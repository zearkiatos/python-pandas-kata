import pandas
import matplotlib.pyplot as pyplot
import matplotlib


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


data = pandas.read_csv(
    './data/SECOP_II_-_Contratos_Electr_nicos.csv').head(50)

contract_quantities = data["Sector"].value_counts()


contract_quantities.plot(kind="bar", figsize=(10, 3), fontsize="small", xlabel="Sectors",
                         ylabel="Contract Quantity", title="Contract quantity by sectors")

pyplot.savefig('./assets/bars.png')

show_image('./assets/bars.png')

contract_quantities.plot(kind="bar", figsize=(10, 3), fontsize="small", xlabel="Sectors",
                         ylabel="Contract Quantity", logy=True, title="Contract quantity by sectors")

pyplot.savefig('./assets/bars-logy.png')

show_image('./assets/bars-logy.png')

