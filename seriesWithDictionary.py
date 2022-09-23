import pandas

pairs = {
    "5/11/20": 19,
    "6/11/20": 18,
    "7/11/20": 29,
    "8/11/20": 14,
    "9/11/20": 20,
    "10/11/20": 20,
    "11/11/20": 20,
    "12/11/20": 20,
    "13/11/20": 19,
}

temperatures = pandas.Series(pairs)

print(temperatures)

temperatures = temperatures.reset_index(drop=True)

print(temperatures)

dataFrame_records = pandas.read_csv("./data/records.csv")

print(dataFrame_records)