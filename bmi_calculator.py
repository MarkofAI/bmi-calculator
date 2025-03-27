# A BMI (Body Mass Index) calculator to determine if person is underweight, normal weight, overweight, or obese.

# Get User Input
try:
    weight = input('Enter your weight, in pounds: ')
    lbs = float(weight)
    height = input('Enter your height, in inches: ')
    ht = float(height)

# Calculate BMI (need to handle input properly ): BMI = weight (lbs?) / height (inches?)
    bmi = (lbs / (ht **2)) * 703
    rbmi = round(bmi, 2)    # Round BMI to two decimal points.
    print('Your BMI is:', rbmi)

# Use Conditional Statements: Based on BMI, categorize into underweight (< 18.5), 
# normal weight (>= 18.5 - 24.9), overweight (>= 25 - 29.9), or obese (>=30).
    if rbmi < 18.5:
        print("You are underweight. It's time to put on some pounds!")
    elif rbmi >= 18.5 and rbmi < 24.9:
        print("You are normal weight. Keep up the great work!")
    elif rbmi >= 25.0 and rbmi < 29.9:
        print("You are overweight. It's time to shed some pounds!")
    elif rbmi >= 30:
        print("You are obese. Things are getting serious. You need to lose weight ASAP!")

except:
    print("That's not a valid number!")




#Handle bad inputs