meal = 50
tax = 0.08
tip = 0.15

tax_value = tax * meal
meal_with_tax = meal + tax_value
tip_value = tip * meal_with_tax
total  = meal_with_tax + tip_value

print "The base cost of your meal was " + "$" + '%.2f' % meal
print "You need to pay " + "$" + '%.2f' % tax_value + " for tax."
print "Tipping at a rate of 15%, you should leave " + "$" + '%.2f' % tip_value + " for a tip." 
print "The grand total for your meal, inclusive of tax and tip is " + "$" + '%.2f' % total + "."