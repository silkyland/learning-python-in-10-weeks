from random import sample
x = list(range(1, 101))

sample_of_x = sample(x, 20)

print(sorted(sample_of_x))
