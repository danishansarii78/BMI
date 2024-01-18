name=(input("Enter your name"))
weight=int(input("Enter your weight in pounds"))
height=int(input("Enter your height in inches"))
BMI=(weight*703)/(height*height)
print(BMI)
if BMI>0:
    if(BMI<18.5):
        print("yOU ARE UNDERWEIGHT")
    elif(BMI<=24.9):
        print("your are normal weight")
    elif(BMI<=29.9):
        print("you are overwight")
    elif(BMI<34.9):
        print("you are obese")
    elif(BMI<39.9):
        print("you are severely obese")
    else:
        print("you are moderly obesed")
else:
    print("give valid input")
