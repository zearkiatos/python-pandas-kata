import random

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

def generate_a_match()->dict:
    teams = 0
    result = {
        
    }
    while teams < 2:
        team
resultsForFix = [
    {
        "local": "Venezuela",
        "visitante": "Argentina",
        "goles_local": random.randrange(0,10),
        "goles_visitante": random.randrange(0,10),
        "resultado": "Argentina"
    },
    {
        "local": "Brazil",
        "visitante": "Paraguay",
        "goles_local": random.randrange(0,10),
        "goles_visitante": random.randrange(0,10),
        "resultado": "empate"
    },
    {
        "local": "Chile",
        "visitante": "Bolivia",
        "goles_local": random.randrange(0,10),
        "goles_visitante": random.randrange(0,10),
        "resultado": "Chile"
    },
    ]
