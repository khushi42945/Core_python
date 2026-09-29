def second_max_F(numbers):
    max1 = None
    max2 = None
    unique_list = []

    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
     
        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        elif num < max1 and (max2 is None or num > max2):
            max2 = num

    return max2, unique_list


user_input = input("Apni list ke numbers space dekar enter karein")
if user_input.strip() == "":
    print("Aapne koi number enter nahi kiya. Empty list banegi.")
    user_list = []
else:
    user_list = [int(x) for x in user_input.split()]

second_max, unique = second_max_F(user_list)

print(f"\nAapki List: {user_list}")
print(f"Second Max: {second_max}")
print(f"Unique List: {unique}")
