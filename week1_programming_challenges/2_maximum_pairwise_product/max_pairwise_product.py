n = int(input())
a = [ int(e) for e in input().split() ]


first = second = float("-inf")

for e in a:
  if e > first:
    second = first
    first = e
  elif e > second:
    second = e

print(first * second)