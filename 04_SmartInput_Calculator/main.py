calc = input("Enter the calculation you need to do (only /, *, -, + , ** ,// operations allowed): ")

try:
    result = eval(calc)
    print("Result:", round(result, 2))
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")
except (SyntaxError, NameError):
    print("❌ Error: Invalid expression. Please use valid numbers and operators.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
