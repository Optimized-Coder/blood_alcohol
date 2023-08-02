# constants
ML_IN_PINT = 568.2615
MAX_UNITS_OF_ALCOHOL = 14

def get_units(abv, volume):
    '''
    function to get units of alcohol in a drink
    :param abv(float) - %:
    :param volume(float) - ml:
    :return: units of alcohol to 2 decimal places
    '''
    return round(float(abv) * float(volume) / 1000, 2)

def convert_pints_to_ml(pints):
    '''
    function to convert pints to ml
    :param pints(float) - pints:
    :return: ml:
    '''
    return round(float(pints) * ML_IN_PINT)

def get_units_from_beer():
        print("How many pints of beer do you drink per week?")
        pints_of_beer = float(input())
        print("what is the ABV of your favourite beer? If unsure, use 4 as standard.")
        abv = float(input())
        ml_of_beer = convert_pints_to_ml(pints_of_beer)
        units_of_beer = get_units(abv, ml_of_beer)

        return units_of_beer

def get_units_from_spirits():
    print("How many shots of spirits do you drink per week?")
    ml_of_spirits = float(input()) * 25
    print("what is the ABV of your favourite spirits? If unsure, use 40 as standard")
    abv = float(input())
    units_of_spirits = get_units(abv, ml_of_spirits)
    return units_of_spirits


def get_units_from_wines():
     print("How many bottles of wines do you drink per week?")
     ml_of_wines = float(input()) * 750
     print("what is the ABV of your favourite wines? If unsure, use 13.5 as standard")
     abv = float(input())
     units_of_wines = get_units(abv, ml_of_wines)
     return units_of_wines


def get_grams_of_alcohol():
    total_grams_of_alcohol = 0
    print("Have you drank beer? Answer yes or no.")
    drank_beer = input().lower()
    if drank_beer == 'yes':
        grams_from_beer = get_units_from_beer() * 8
        total_grams_of_alcohol += grams_from_beer
    print("Have you drank spirits? Answer yes or no.")
    drinks_spirits = input().lower()
    if drinks_spirits == 'yes':
        grams_from_spirits = get_units_from_spirits() * 8
        total_grams_of_alcohol += grams_from_spirits
    print("Have you drank wines? Answer yes or no.")
    drinks_wines = input().lower()
    if drinks_wines == 'yes':
        grams_from_wines = get_units_from_wines() * 8
        total_grams_of_alcohol += grams_from_wines
    return total_grams_of_alcohol



def get_units_per_week():
    total_units = 0
    print('Hello, what is your name?')
    name = input().title()
    print(f'Hello, {name}')

    print(f"The NHS advise that men and women should not drink more than {MAX_UNITS_OF_ALCOHOL} units of alcohol per week.")
    print("===========")

    print(f"Do you drink beers, {name}? Answer yes or no.")
    drinks_beer = input().lower()
    if drinks_beer == 'yes':
        units_of_beer = get_units_from_beer()
        total_units += units_of_beer
        print(f"You have {units_of_beer} units of alcohol from beer per week.")
    
    print("===========")
    
    print(f"Do you drink spirits, {name}? Answer yes or no.")
    drinks_spirits = input().lower()
    if drinks_spirits == 'yes':
        units_of_spirits = get_units_from_spirits()
        total_units += units_of_spirits
        print(f"You have {units_of_spirits} units of alcohol from spirits per week.")

    print("===========")

    print(f"Do you drink wines, {name}? Answer yes or no.")
    drinks_wines = input().lower()
    if drinks_wines == 'yes':
         units_of_wines = get_units_from_wines()
         total_units += units_of_wines
         print(f"You have {units_of_wines} units of alcohol from wines per week.")

    print(f"You have a total of {total_units} units of alcohol per week.")

def get_blood_alcohol_level():
     alcohol_consumed_in_g = get_grams_of_alcohol()
     print("How much do you weigh in lbs?")
     weight_in_g = round(float(input()) * 453.59237)
     print("Are you male or female?")
     gender = input().lower()
     if gender =='male':
          r = 0.68
     elif gender == 'female':
          r = 0.55
     bac = (alcohol_consumed_in_g / (weight_in_g * r)) * 100
     print(f"Your blood alcohol level is {bac}.")

def main():
     print("Do you want to know how many units of alcohol you have per week? Answer yes or no.")
     answer = input().lower()
     if answer == 'yes':
          get_units_per_week()

     print("Do you want to know your blood alcohol level? Answer yes or no.")
     answer = input().lower()
     if answer == 'yes':
          get_blood_alcohol_level()
     

if __name__ == '__main__':
    main()
