import sys
args_list =sys.argv[1:]
args_list=[int(i) for i in args_list]
args_list.sort()
args_list=[str(i) for i in args_list]
Sort=','.join(args_list)
print(args_list)