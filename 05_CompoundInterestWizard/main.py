
principle = float(input("Enter the principle amount: "))

while principle <= 0:
    print("Principle amount must be greater than zero.")
    principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the rate of interest: "))

while rate < 0:
    print("Rate of interest must be greater than zero.")
    rate = float(input("Enter the rate of interest: "))

time = float(input("Enter the time period in years: "))

while time <= 0:
    print("Time period must be greater than zero.")
    time = float(input("Enter the time period in years: "))

compound_interest = principle * (1 + (rate / 100)) ** time

print(f"The compound interest is: {compound_interest}")
