a = 0
b = 10
try:
  res = a/b
  print(res)
except ZeroDivisionError:
  print("Cant devide by zero")
