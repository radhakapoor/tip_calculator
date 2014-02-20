import sys 



tax_value = float(sys.argv[2]) * float(sys.argv[1])
meal_with_tax = float(sys.argv[1]) + tax_value
tip_value = float(sys.argv[3]) * meal_with_tax
total  = meal_with_tax + tip_value

print "The cost of your meal (without tip or tax) is $", sys.argv[1]
print "The tax rate is", sys.argv[2]
print "Your preferred tip rate is", sys.argv[3]


print "You need to pay " + "$" +'%.2f' % tax_value + " for tax."
print "Without tip but including tax, the cost of your meal is " + "$" + '%.2f' % meal_with_tax
print "Tipping at a rate of " + sys.argv[3] + "," + " you should leave " + "$" + '%.2f' % tip_value + " for a tip." 
print "The grand total for your meal, inclusive of tax and tip, is " + "$" + '%.2f' % total + "."


