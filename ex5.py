my_name = 'Jerry'
my_age = 35.0 * 2.54 # a lie
my_height = 74.0  #inch
my_weight = 180.0 * 0.4826 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He is %0.2f cm tall." % my_height 
print "He is %0.2f kg heavy." % my_weight
print "Actually that is not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on ther coffee." % my_teeth

# this line is tricky, try to get it exactly right
print " If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight) 
