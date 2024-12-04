# s = (a + b + c)/2
# A = sqrt((s-a)(s-b)(s-c)s)


a = float(input("enter a value for a:"))
b = float(input("enter a value for b:"))
c = float(input("enter a value for c:"))
s = (a + b + c)/2

A = (s-a) * (s-b) * (s-c) ** 0.5

print(f"area the triangle is {A}")

# %d -> Integer
# %e -> exponential
# %f -> Float
# %o -> Octal
# %x -> Hexadecimal
