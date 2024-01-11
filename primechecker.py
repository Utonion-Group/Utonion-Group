def prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**.5)+1):
    if n % i == 0:
      return False
  return True

choice = int(input("Number here: "))
if prime(choice):
  print(f"{choice} is prime")
else:
  print(f"{choice} isn't prime")
