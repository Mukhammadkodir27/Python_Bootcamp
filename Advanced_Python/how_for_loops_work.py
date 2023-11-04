# ----- how for loops work -----

# the for loop, whenever the iteration ends, it is going to raise StopIteration exception and handle it
# internally all by itself
# it means, num = [1, 2, 3]  and when it reaches last element it stops automatically.


# the for loop is actually an infinite while loop
# the infinite while loop says, as loong as the situation or condition holds true, I am going to run
# if any iteration holds false then I am not going to run


numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#  print(num)

iterator_obj = numbers.__iter__()

# infinite while loop
while True:
    try:
        # get the next item
        element = next(iterator_obj)  # or element = iterator_obj.__next__()

        # do smth with the element
        # print(element)
        print(f"Element: {element}")
    except StopIteration:
        break
