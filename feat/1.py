for n in range(10):
    print(f"Seconds {n+1}:")


name = input("Enter your name: ")
print(f"Hi {name}")


def nested_for_loops():
    for a in range(5):
        for b in range(3):
            for c in range(2):
                print(f"Point({a}, {b}, {c})")


if name:
    nested_for_loops()

# !
