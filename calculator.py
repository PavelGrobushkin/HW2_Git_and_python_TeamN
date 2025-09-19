def slo(x,y):
  return x+y

def minus (x,y):
  return x-y

def divide(x, y):
    if y == 0:
        return "Деление на ноль не допустимо"
    else:
        return x / y
      
def main():
  calc = input("Введите ваше выражение (например: 5 - 3): ")
  parts = calc.split()
  operator = parts[1]
  x = parts[0]
  y = parts[2]
  if '.' in x:
    x=float(x)
  else:
    x=int(x)
  if '.' in y:
    y=float(y)
  else:
    y=int(y)

  if operator == '+':
    return slo(x,y)
  elif operator == '-':
    return minus(x,y)
  elif operator == '*':
    return umn(x,y)
  elif operator == '/':
    return divide(x,y)
  

main()