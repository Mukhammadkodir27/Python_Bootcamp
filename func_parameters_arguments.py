# ---------- Function Parameters & Arguments ----------

# Example 4
def arithmetic_operations(x, y):
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")


arithmetic_operations(20, 5)
print("-----------")
arithmetic_operations(5, 20)


def legal_age(name, age, allowed_age):
    if age >= allowed_age:
        print(f"{name} is allowed to drive.")
    else:
        print(f"{name} is not allowed to drive.")


legal_age("Tom", 21, 18)
legal_age("Sarah", 17, 18)
