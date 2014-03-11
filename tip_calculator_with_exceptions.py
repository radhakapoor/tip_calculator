import sys
 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tax_value=tax_value,
                    tip_value=tip_value,
                    total = total)
    return meal_info
 
 
def main():
    meal_input = sys.argv[1]
    while True:
        try:
            meal_input = float(meal_input)
            break
            meal_input = raw_input("Please enter a number as an input parameter for the meal")
        except ValueError:
            meal_input =raw_input("Please enter a number as an input parameter for the meal")
            
    tax_rate_input = sys.argv[2]
    while True:
        try:
            tax_rate_input = float(tax_rate_input)
            break
            tax_rate_input = raw_input("Please enter a number as an input parameter for the tax rate")
        except ValueError:
            tax_rate_input = raw_input("Please enter a number as an input parameter for the tax rate")
            
    tip_rate_input = sys.argv[3]
    while True:
        try:
            tip_rate_input = float(tip_rate_input)
            break
            tip_rate_input = raw_input("Please enter a number as an input parameter for the tip rate")
        except ValueError:
            tip_rate_input = raw_input("Please enter a number as an input parameter for the tip rate")
        
            

        
    meal_info = calculate_meal_costs(meal_input, tax_rate_input, 
                                    tip_rate_input)
 
    print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
    print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        int(100*meal_info['tip_rate']), 
                                        meal_info['tip_value'])
    print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])
 
if __name__ == '__main__':
    main()