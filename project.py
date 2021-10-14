
def bmis (weight, height):
    bmi = weight/(height)**2
    print("Your BMI is ",bmi)


def fatty (gender, age):
    bmi = weight / (height) ** 2

    fat = (1.20*bmi)+(0.23*age) - 5.4
    print("Your fat % is ",fat)
    if gender == 'FEMALE':
        if fat>=14 and fat<=16.5:
            print("Excellent ! ")
        elif fat>=16.6 and fat<=19.4:
            print("Good")
        elif fat>=19.5 and fat<=22.7:
            print("Fair")
        elif fat>=22.8 and fat<=27.1:
            print("Poor")
        else:
            print("Dangerously High ! ")
    elif gender == 'MALE':
        if fat>=8 and fat<=10.5:
            print("Excellent ! ")
        elif fat>=10.6 and fat<=14.8:
            print("Good")
        elif fat>=14.9 and fat<=18.6:
            print("Fair")
        elif fat>=21.4 and fat<=24.9:
            print("Poor")
        else:
            print("Dangerously High ! ")

print("WELCOME TO FITNESS CALCULATOR ! !")
print("1. BMI")
print("2. Fat percentage")
print("3. exit")
choice = int(input("What do you want to know? : "))

if choice == 1:
    weight = float(input("Enter your weight in kg : "))
    height = float(input("Enter your height in m : "))
    bmis(weight, height)
elif choice == 2:
    age = int(input("Enter your age : "))
    weight = float(input("Enter your weight in kg : "))
    height = float(input("Enter your height in m : "))
    bmis(weight, height)
    gender = input("Enter your gender : Male or Female : ")
    fatty(gender , age)
elif choice == 3:
    pass
else:
    print("Enter valid choice")
    





