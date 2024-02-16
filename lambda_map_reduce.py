l1 = [1, 2, 3, 4, 5, 6]

# --- Filter ---

f1 = list(filter(lambda x: x % 2 == 0, l1))
print("Filter:", f1)

# --- Map ---
m1 = list(map(lambda x: x ** 2, l1))
print("Map:", m1)

# --- Reduce ---
from functools import reduce

r1 = reduce(lambda x, y: x + y, l1)
print("Reduce:", r1)
