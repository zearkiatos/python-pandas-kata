import pandas


countries = [
    {
        "Pais": "Venezuela",
        "Poblacion": 1000000,
        "Edad_mediana": 31
    },
    {
        "Pais": "Chile",
        "Poblacion": 6000000,
        "Edad_mediana": 40
    },
    {
        "Pais": "Colombia",
        "Poblacion": 8400000,
        "Edad_mediana": 38
    },
    {
        "Pais": "Australia",
        "Poblacion": 25000000,
        "Edad_mediana": 50
    }
]

universities = [
    {
        "country": "Venezuela",
        "university_name": "UNEFA",
        "num_students": 1000
    },
    {
        "country": "Venezuela",
        "university_name": "Universidad de Carabobo",
        "num_students": 3500
    },
    {
        "country": "Chile",
        "university_name": "Universidad Tecnica Federico Santa Maria",
        "num_students": 3000
    },
    {
        "country": "Colombia",
        "university_name": "Universidad de los Andes",
        "num_students": 4000
    },
    {
        "country": "Australia",
        "university_name": "National Australia University",
        "num_students": 185000
    },
    {
        "country": "Australia",
        "university_name": "Melbourne University",
        "num_students": 185000
    },
    {
        "country": "Australia",
        "university_name": "Sydney University",
        "num_students": 185000
    },
    {
        "country": "Australia",
        "university_name": "South New Gales University",
        "num_students": 185000
    }
]

countriesDataFrame = pandas.DataFrame(countries)

universitiesDataFrame = pandas.DataFrame(universities)


def calculate_university_capacity(countriesDataFrame: pandas.DataFrame, universitiesDataframe: pandas.DataFrame) -> pandas.DataFrame:
    universities = universitiesDataframe.groupby("country")
    university_capacity = []

    for name, group in universities:
        data = countriesDataFrame[countriesDataFrame["Pais"] == name]
        citizen_quantity = data["Poblacion"].values[0]
        university = {
            "Pais": name,
            "habitantes_por_puesto": round(citizen_quantity/(group["num_students"].sum()), 1)
        }
        university_capacity.append(university)


    

    return pandas.DataFrame(university_capacity)


print(calculate_university_capacity(countriesDataFrame, universitiesDataFrame))
