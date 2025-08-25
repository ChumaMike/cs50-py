def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    #          $##.##
    #          $50.00 == 50.0
    # TODO
    
    return float(dollars.replace("$", ""))

def percent_to_float(percent):
    #           ##%
    #           15% == 0.15
    # TODO
    
    return float(percent.replace("%", ""))/100

main()