def calculate_bmi(mass, height):
    bmi = mass / (height ** 2)
    return bmi

def main():
    print("Body Mass Index (BMI) Calculator")
    mass = float(input("Enter your mass in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(mass, height)
    print(f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 24.9 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()
