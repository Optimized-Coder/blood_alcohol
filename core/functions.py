from flask import request

# constants
ML_IN_PINT = 568.2615

def get_units(abv, volume):
    return round(float(abv) * float(volume) / 1000, 2)

def convert_pints_to_ml(pints):
    return round(float(pints) * ML_IN_PINT)

def get_units_from_beer():
    pint_or_half = float(request.args.get('pint-or-half'))
    abv = request.args.get('abv')
    ml_of_beer = pint_or_half * ML_IN_PINT
    units_of_beer = get_units(abv, ml_of_beer)

    return units_of_beer

def get_units_from_spirits():
    num_of_shots = float(request.args.get('num-of-shots'))
    abv = request.args.get('abv')
    units_of_spirits = get_units(abv, num_of_shots * 25)
    return units_of_spirits


def get_units_from_wines():
    ml_of_wines = float(request.args.get('ml-of-wines'))
    abv = request.args.get('abv')
    units_of_wines = get_units(abv, ml_of_wines)
    return units_of_wines

def get_grams_of_alcohol(units):
    return float(units) * 8

def get_blood_alcohol(gender, weight, grams_of_alcohol):
    weight_in_grams = weight * 453.59237

    if gender =='male':
        r = 0.68
    if gender =='female':
        r = 0.55

    return round(grams_of_alcohol / (weight_in_grams * r) * 100, 5)

