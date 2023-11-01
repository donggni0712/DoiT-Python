fruits = ["apple", "banana", "mango",
          "watermelon", "melon", "orange"]

for i in range(len(fruits)):
    for j in range(len(fruits)):
        if i == j:
            continue
        print(fruits[i], fruits[j])
