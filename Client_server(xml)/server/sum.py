import sys

length= len(sys.argv)
arg_list=sys.argv[1:]
sum=0
for i in arg_list:
    sum+=int(i)
print(sum)
