import pandas
import random


def increase_notes(notes: pandas.Series) -> pandas.Series:
    if notes.mean() > 2.5:
        notes = notes + round(notes.std(), 2)
    
    for i in range(notes.size):
        current_notes = notes.iloc[i]

        if current_notes > 5:
            notes.iloc[i] = 5.0
    return notes

notes = []

for i in range(15):
    generated_notes = random.normalvariate(3.25,0.98)
    generated_notes = round(generated_notes, 2)
    valid = False
    while not valid:
        if generated_notes >= 1.5 and generated_notes <=5.0:
            valid = True
        else:
            generated_notes = random.normalvariate(3.25, 0.98)
            generated_notes = round(generated_notes, 2)

    notes.append(generated_notes)
    note_serie = pandas.Series(notes)

print(note_serie)
print("-"*15)
print(increase_notes(note_serie))
