import pandas
import random

STUDENT_PERCENTAGE = 0.25

names = [
"Ariel Olmedo Herranz",
"Calisto Peña Dávila",
"Maite Antón Cerezo",
"Fabio Jerez Lorenzo",
"Cipriano Páez Sierra",
"Elisabet Agustina Portero Ayala",
"Jose Francisco Mario Perelló Nicolau",
"Daniela Ariza Sedano",
"Eligio Hervás Piña",
"Ámbar Garrido Escribano",
"Prudencia de Zamora",
"Roxana Cortina-Leal",
"Roxana Jódar Rosado",
"Maribel Ferrero Giralt",
"Anselmo Carro-Fernández",
"Brenda Curry",
"Andrew Maxwell",
"John Soto",
"Stephen Stuart",
"Kelly Cole",
"Taylor Hammond",
"Susan Reyes",
"Deanna Allison",
"Abigail Hunt",
"Alexis Becker",
"Lucas King",
"Dr. Daniel Thompson DDS",
"Amanda Deleon",
"Kevin King",
"Elizabeth Allen"
]

def get_a_name(index:int)->str:
    return names[index]


def generate_a_students(student_quantity: int) -> list:
    student_notes = []
    count = 0

    while count < student_quantity:
        notes = {
            "nombre": get_a_name(random.randrange(0,30)),
            "matematicas": round(random.uniform(0.0,5.0),2),
            "ingles": round(random.uniform(0.0,5.0),2),
            "ciencias": round(random.uniform(0.0,5.0),2),
            "literatura": round(random.uniform(0.0,5.0),2),
            "arte": round(random.uniform(0.0,5.0),2),
        }
        count += 1
        student_notes.append(notes)
    return student_notes


def best_students(students: pandas.DataFrame) -> pandas.DataFrame:
    columns = students.columns[1:6].copy()

    data = students[columns].copy()
    students_column = students.columns[0]

    names = students[students_column].copy()

    data = data.values.tolist()
    names_list = names.values.tolist()

    size = len(data)

    student_average = []

    for i in range(size):
        average = {
            "nombre": names_list[i],
            "promedio": round((data[i][0] + data[i][1] + data[i][2] + data[i][3] + data[i][4]) / 5,2)
        }
        student_average.append(average)


    student_average_dataframe = pandas.DataFrame(student_average)

    student_ordered = student_average_dataframe.sort_values("promedio",ascending=False)
    

    quantity = int(size*STUDENT_PERCENTAGE)

    best_students = student_ordered.iloc[0:quantity]
    
    
    return best_students


students = generate_a_students(19)

students_dataframes = pandas.DataFrame(students)

best_students = best_students(students_dataframes)

print(best_students)

