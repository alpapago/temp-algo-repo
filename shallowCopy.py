# deep copy

A = [[0 for col in range(4)] for row in range(3)]
A[2][1] = 4
print(A) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 0, 0]]

# shallow copy

B = [[0]*4]*3
B[2][1] = 5
print(B) # [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]