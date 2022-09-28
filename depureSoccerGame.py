import random
import pandas
import numpy

TIE = 'empate'
conmebol_teams = [
    "Argentina",
    "Bolivia",
    "Brazil",
    "Chile",
    "Colombia",
    "Ecuador",
    "Paraguay",
    "Peru",
    "Uruguay",
    "Venezuela"
]

fake_data = [
    "efrefere",
    "frfr",
    "Brfrfrazil",
    "erfer",
    "Colgergombia",
    "hrtrhtr",
    "rthtrhrh",
    "rthrthrt",
    "hrtrthr",
    "hrthrhyunju"
]

def generate_a_match() -> dict:
    local = ''
    guest = ''
    teams_match = []
    while local == guest:
        local = conmebol_teams[random.randrange(0, 9)]
        guest = conmebol_teams[random.randrange(0, 9)]
    teams_match.append(local)
    teams_match.append(guest)
    teams_match.append(TIE)
    result = {
        "local": local,
        "visitante": guest,
        "goles_local": random.randrange(0,9),
        "goles_visitante": random.randrange(0,9),
        "resultado": teams_match[random.randrange(0, 2)]
    }

    return result


def generate_a_match_fake() -> dict:
    local = ''
    guest = ''
    teams_match = []
    local = conmebol_teams[random.randrange(0, 9)]
    guest = conmebol_teams[random.randrange(0, 9)]
    teams_match.append(local)
    teams_match.append(guest)
    teams_match.append('deded')
    result = {
        "local": local,
        "visitante": guest,
        "goles_local": numpy.NaN,
        "goles_visitante": numpy.NaN,
        "resultado": teams_match[random.randrange(0, 2)]
    }

    return result


def generate_wrong_data(match_quantity: int) -> pandas.DataFrame:
    hacked_list = []
    quantity = 0

    while (quantity < match_quantity):
        hacked_list.append(generate_a_match_fake())
        quantity += 1

    return pandas.DataFrame(hacked_list)

def fix_result(result):
    if (result['goles_local'] > result['goles_visitante']):
        result['resultado'] = result['goles_local']
    elif (result['goles_local'] < result['goles_visitante']):
        result['resultado'] = result['goles_visitante']
    elif (result['goles_local'] == result['goles_visitante']):
        result['resultado'] = TIE
    return result

def fix_result(result):
    if (result['goles_local'] > result['goles_visitante']):
        result['resultado'] = result['goles_local']
    elif (result['goles_local'] < result['goles_visitante']):
        result['resultado'] = result['goles_visitante']
    elif (result['goles_local'] == result['goles_visitante']):
        result['resultado'] = TIE
    return result

def fix_goals(goals:any)->int:
    result = goals
    if (numpy.isnan(goals)):
        result = 0
    
    return result

def drop_duplicate_teams(data):
    if(data["local"] == data["visitante"]):
        data = data.drop("local", axis=0)
    return data



def match_depurator(wrong_dataframe:pandas.DataFrame)->pandas.DataFrame:

    wrong_dataframe = wrong_dataframe.apply(lambda result: fix_result(result), axis=1)

    wrong_dataframe['goles_local'] = wrong_dataframe['goles_local'].apply(fix_goals)

    wrong_dataframe['goles_visitante'] = wrong_dataframe['goles_visitante'].apply(fix_goals)

    wrong_dataframe = wrong_dataframe.apply(lambda data: drop_duplicate_teams(data), axis=1).dropna()
    return wrong_dataframe

wrong_data = generate_wrong_data(20)

print(wrong_data)

print(match_depurator(wrong_data))