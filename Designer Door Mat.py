N, M = input().split()

N = int(N)
M = int(M)

str = ".|."

for i in range(1, N, 2):
    print((str*i).center(M, "-"))

print("WELCOME".center(M, "-"))


for i in range(N-2, 0, -2):
    print((str*i).center(M, "-"))