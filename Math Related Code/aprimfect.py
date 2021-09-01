import sys

try:
    n = int(input("Number:"))
except Exception:
    print("We want a number.")
    sys.exit()

i = 2
factors = []
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        factors.append(i)
if n > 1:
    factors.append(n)

for j in factors:
    print(f"    {j}")