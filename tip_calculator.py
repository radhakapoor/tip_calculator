from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--first", dest="first_arg", help="the first argument")
parser.add_option("-s", "--second", dest="second_arg", help="the second argument")
parser.add_option("-t", "--third", dest="third_arg", help="the third argument", default="0.15")

(options, args) = parser.parse_args()

if not (options.first_arg):
    parser.error("You need to provide the meal value")
if not (options.second_arg):
    parser.error("Your need to provide a tax rate")
    
meal = format(options.first_arg)
tax = format(options.second_arg)
tip = format(options.third_arg)
tax_value = float(tax) * float(meal)
meal_with_tax = float(meal) + tax_value
tip_value = float(meal) * float(tip)
total = meal_with_tax + tip_value

print "The price of the meal is $" + meal
print "The tax rate is " + tax + "."
print "The tip rate is " + tip + "."

print "You need to pay " + "$" +'%.2f' % tax_value + " for tax."
print "Without tip but including tax, the cost of your meal is " + "$" + '%.2f' % meal_with_tax
print "Tipping at a rate of " + tip + "," + " you should leave " + "$" + '%.2f' % tip_value + " for a tip." 
print "The grand total for your meal, inclusive of tax and tip, is " + "$" + '%.2f' % total + "."


#type in shell python optionparser.py -f 50
