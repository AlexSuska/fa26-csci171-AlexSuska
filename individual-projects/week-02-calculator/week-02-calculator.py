"""
CSCI171 Week 02: Friendly Calculator

Start with the required version first. Add the extra credit stretch only
after the required program runs and is easy to explain.
"""


def main():
    # TODO: Build the Week 02 project here.
    print("Week 02: Friendly Calculator")
    
    num1 = float( input("Please give me a number. ") )
    num2 = float( input("One more. ") )
    
    print("The sum is", num1 + num2)
    print("The difference is", num1 - num2)
    print("The product is", num1 * num2)
    print("The quotient is", num1 / num2)
    # Extra!!
    print("The average is", (num1 + num2) / 2)
    print("")
    
    print("If you added both as feet, then converted it to inches it would be", (num1 + num2) * 12, "inches.")
    print("If you added both as inches, then converted it to centimeters it would be", (num1 + num2 * 2.54), "cm.")
    print("If you added both, then split it in half, you would get", (num1 + num2) * .5)
    print("If you added both... and gave a 15% tip, it would be $", (num1 + num2) * .15)

if __name__ == "__main__":
    main()
