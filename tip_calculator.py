



print "Enter the cost of your meal" 
meal = raw_input()
print "Enter the tax rate as a decimal"
tax = raw_input()
print "Enter your preferred tip rate"
tip = raw_input()

tax_value = float(tax) * float(meal)
print "You need to pay " + "$" + '%.2f' % tax_value + " for tax."

meal_with_tax = float(meal) + tax_value
tip_value = float(tip) * meal_with_tax
total  = meal_with_tax + tip_value
print "Without tip but including tax, the cost of your meal is " + "$" + '%.2f' % meal_with_tax
print "Tipping at a rate of " + tip +  " you should leave " + "$" + '%.2f' % tip_value + " for a tip." 
print "The grand total for your meal, inclusive of tax and tip is " + "$" + '%.2f' % total + "."


