# Finding List Items Index

# numbers = ["m", "nnn", "", 1, 1] * 5
# print(numbers)

ft_group = ['Kadir', 'Adil', 'Fozil', 'Hasan', 'Hasan', 'Kadir']  # * 2

print(ft_group.index('Fozil'))
selected_user_index = ft_group.index("Kadir")
print(selected_user_index)


def change_selection(user):
    global selected_user_index
    if user in ft_group:
        selected_user_index = ft_group.index(user)


for i in ft_group:
    if ft_group.count(i) < 2:
        change_selection(i)
        print(
            f"The selected users index is: {selected_user_index} and he is {ft_group[selected_user_index]}")
        print(f"{ft_group[selected_user_index]} appeared",
              ft_group.count(i), "time")
    else:
        print(
            f"The selected users index is: {selected_user_index} and he is {ft_group[selected_user_index]}")
        print(f"{ft_group[selected_user_index]} appeared",
              ft_group.count(i), "times")
        continue
        # break could be used but not recommended!



#1111
#1111