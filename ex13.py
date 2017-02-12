from sys import argv #argv --argument variable（参数变量）

script, first, second, third = argv #参数变量保存着运行脚本时传递给python的参数，这一步将其解包分别赋予之前的变量

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third