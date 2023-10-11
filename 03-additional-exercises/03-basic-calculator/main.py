def calculator(num1, op, num2):
  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  elif op == "*":
    return num1 * num2
  else:
    return num1 / num2
  
x = 5
y = 2
op = "*"

result = calculator(x, op, y)
print(result)