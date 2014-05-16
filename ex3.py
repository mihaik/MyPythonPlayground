#!/usr/bin/env python
# This prints  "I will now count my chickens:"
print "I will now count my chickens:"
# This prints number of Hens. Operation priority is taken into account. Divison will be performed before addition.
# Expected result: 30
print "Hens", 25 + 30 / 6
# This print number of roosters. Again the opration priority is taken into account. 
# Multiplication is performend, then the modulus % and finaly the substraction.
# Expected result: 97
print "Roosters", 100 - 25 * 3 % 4
print "Now I will count the eggs:"
# If integer numbers are used the the result will be 7. 
# If floating point numbers are used the the rerul is more exact 6.75.
# To create folating point numbers replace 1 with 1.0
# Interpreter automaticaly detects type and adjusts calculation
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6
# Boolean logic below. Calculations are done before comparison.
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Oh, that's why it's False."
print "How about some more."
print "Is it greater?", 5 > - 2
print "Is it greater or equal?", 5 >= - 2
print "Is it less or equal?", 5 <= - 2

print "PEMDAS", 10 + 5 - 10 + 5
