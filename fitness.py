# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Please enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in US pounds: "))
    inches = float(input("Enter your height in US inches: "))


    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.
    computeAge = compute_age(birthdate)
    kgToLb = kg_from_lb(pounds)
    cmToIn = cm_from_in(inches)
    body = body_mass_index(kgToLb, cmToIn)
    basal = basal_metabolic_rate(gender,kgToLb, cmToIn, computeAge )
    # def      basal_metabolic_rate(gender, weight, height, age)}

    # Print the results for the user to see.
    print(f"Age (years): {computeAge}")
    print(f"Weight (kg): {kgToLb:.2f}")
    print(f"Height (cm): {cmToIn:.1f}")
    print(f"Body mass index: {body:.1f} ")
    print(f"Basal metabolic rate (kcal/day): {basal:.0f}")
    


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    lb_to_kg_constant = 0.45359237
    kg = lb * lb_to_kg_constant
    
    return kg


def cm_from_in(inch):
   i = inch * 2.54
   cm_from_in = round(i, 1)
   return cm_from_in

    


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    body_mass_index = (10000 * weight) / (height ** 2)
    return body_mass_index
    


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if(gender == "F"):
      bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
      bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr

main()
# Call the main function so that
# this program will start executing.