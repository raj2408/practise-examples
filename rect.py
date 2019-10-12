n=int(input("Enter the lenght of the rectangle: "))
m=int(input("Enter the width: "))
c="c"
def print_rect(n, m, c):
    row=n*c
    for a in range(m):
        print (row)

print((n * c + '\n') * m, end="")