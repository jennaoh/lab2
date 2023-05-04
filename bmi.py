
def calculate_bmi(height, weight):

    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height*height)

    print("Your BMI is "+str(bmi))
    print("Your bmi is", bmi)

    if bmi < 18.5:
        print("under weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("normal weight")
        return 0
    else:
        print("over weight")
        return 1


calculate_bmi(weight=57, height=1.73)



