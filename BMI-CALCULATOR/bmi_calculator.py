def calculate_bmi(weight, height):
    """Calculate BMI = weight (kg) / height (m)^2"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """Classify BMI based on WHO standard"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI CALCULATOR ===")
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        
        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be positive numbers.")
            return
        
        bmi = calculate_bmi(weight, height)
        status = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Health Status: {status}")
    except ValueError:
        print("❌ Please enter valid numerical inputs.")

if __name__ == "__main__":
    main()
