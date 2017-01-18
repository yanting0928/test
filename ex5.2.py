# the use of % and the auxiliary identifier of * + - ...

num = 100

print "%d to hex is %x." % (num,num)
# %x is means hexadecimal.

print "%d to hex is %o." % (num,num)
# %u is means octonary number system

# # means display 0 if the result is octonary number system,display 0x before hexadecimal.

print "%d to hex is %#x." % (num,num)
print "%d to hex is %#o." % (num,num)

# float
f = 3.1415926
print "value of f is :%.4f" % f

# specify the width and aligning

students = [{"name":"Willber","age":27},{"name":"Will","age":28},{"name":"June","age":27}]
# %[width]typecode
print "name: %10s, age: %10d" %(students[0]["name"],students[0]["age"])
# - means left aligning
print "name: %-10s, age: %-10d" %(students[1]["name"],students[1]["age"])
# * define width or precision after dot.
print "name: %*s, age: %0*d" %( 10, students[2]["name"], 10, students[2]["age"])