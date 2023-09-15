# ---------- Set Operations ----------

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# ---> Set Union
print(A | B)  # operator
print(B | A)

print(A.union(B))  # method
print(B.union(A))

# ---> Set Intersection
print(A & B)
print(B & A)

print(A.intersection(B))
print(B.intersection(A))

# ---> Set Difference
print(A - B)
print(B - A)

print(A.difference(B))
print(B.difference(A))

# ---> Set Symmetric Difference
print(A ^ B)
print(B ^ A)

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

...
