# O(1)

print("Hi")

# O(n)
a_small_list = ["n", "y", 4]

counter = 0

for item in a_small_list:
    counter += 1
    print(item, counter)

# O(log(n))

# O(n^2)

counter = 0

for item in a_small_list:
    for thing in a_small_list:
        counter += 1
        print(item, thing, counter)

# O(n^3)

counter = 0

for item in a_small_list:
    for thing in a_small_list:
        for demon in a_small_list:
            counter += 1
            print(item, thing, demon, counter)
