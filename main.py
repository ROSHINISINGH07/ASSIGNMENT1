def fun(n):
  return n % 3 == 0 or n % 5 == 0

li = (52,27,85,35,40,15,6,9,18)

print(list(filter(fun,li)))

# program for divisibility of 3 or 5 using lambda

li = (52,27,85,35,40,15,6,9,18)
print(list(filter(lambda n : n % 3 == 0 or n % 5 == 0 ,li)))