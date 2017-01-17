# the example is about format string
my_name = 'Yanting Xu'

my_age = 22 # not a lie

my_height = 163 # cm

my_weight = 50 #kg It's real,a little fat? I feel good.

my_eyes = 'Brown'

my_teeth = 'White'

my_hair = 'Black'

print "Let's talk about %s." % my_name
print "She's %d cm tall." % my_height
print "She's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "She's got %s eys and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the tea." % my_teeth

# this line is tricky,try to fet it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)