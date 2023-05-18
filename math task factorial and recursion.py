"""
num = int(input("type your factorial number: "))

result = 1

for N in range(num, 0, -1):
    result *= N

print(f"for {num} factoreal is {result}")
"""

def factoreal(n):
    if n > 0:
        return n * factoreal(n - 1)
    elif n < 0:
        return "Infinite"
    else:
        return 1

print(factoreal(int(input("type your factoreal Number: "))))

