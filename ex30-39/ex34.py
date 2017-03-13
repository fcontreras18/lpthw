print "1. The 2nd animal is at 1 is a python"
print "2. The third animal is at 2 is a peacock"
print "3. The first animal is at 0 is a bear"
print "4. The 4th animal is at 3 is a kangaroo"
print "5. The fifth animal is at 4 is a whale"
print "6. The 3rd animal is at 2 is a peacock"
print "7. The sixth animal is at 5 is a platypus"
print "8. The 5th animal at 4 is a whale"


def check_place(ordinal):
    animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
    if ordinal >= 1 and ordinal <= len(animals):
        print "The # %s animal is %s and is at %s" % (ordinal, animals[ordinal -1], ordinal - 1)
    else:
        print "Entered an invalid number!"

check_place(1)