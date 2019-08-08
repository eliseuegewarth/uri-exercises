
s = int(input())
h = s//3600
s = s%3600
m = s//60
s = s%60

print("{}:{}:{}".format(h,m,s))
