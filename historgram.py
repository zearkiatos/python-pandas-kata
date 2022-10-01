import pandas
import matplotlib.pyplot as pyplot
import matplotlib


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


data = pandas.read_csv(
    './data/SECOP_II_-_Contratos_Electr_nicos.csv').head(20)


payments = data["Valor Pagado"]

payments.plot(kind="hist", figsize=(10, 4))

pyplot.savefig('./assets/histogram.png')

show_image('./assets/histogram.png')

payments.plot.hist(figsize=(10, 4))

pyplot.savefig('./assets/histogram-second-way.png')

show_image('./assets/histogram-second-way.png')


payments.plot(kind="hist", figsize=(10, 4), xlim=(-1, 30), bins=20)

pyplot.savefig('./assets/histogram-custom.png')

show_image('./assets/histogram-custom.png')

payments.plot(kind="hist", figsize=(10, 4), xlim=(2, 30),
              ylim=(0.70), bins=20, title="Payment values")

pyplot.savefig('./assets/histogram-y.png')

show_image('./assets/histogram-y.png')

matplotlib.style.use('seaborn-darkgrid')
payments.plot(kind="hist", figsize=(10, 4), xlim=(2, 30),
              ylim=(0.70), bins=20, title="Payment values")

pyplot.savefig('./assets/histogram-with-custom-color.png')

show_image('./assets/histogram-with-custom-color.png')

ax = payments.plot(kind="hist", figsize=(10, 4), xlim=(2, 30),
                   ylim=(0.70), bins=20, title="Payment values")

ax.set_xlabel("Value in millions of COP", fontsize=9)

ax.xaxis.set_label_coords(0.5, -0.07)

ax.set_ylabel("Contract quantity", fontsize=9)

figure = ax.get_figure()

figure.savefig('./assets/histogram.svg')
