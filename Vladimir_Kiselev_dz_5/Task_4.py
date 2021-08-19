# Task_4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([num for i, num in enumerate(src) if src[i] > src[i - 1] and src[i] != src[0]])