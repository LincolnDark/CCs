list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
intersection_set = set.intersection(set(list_a), set(list_b))
# source https://www.kite.com/python/answers/how-to-find-the-intersection-of-two-lists-in-python

#AD had to add a print statement

print(intersection_set)

#Only got overlapping, where are the none overlapping?

non_inter_test = set(list_a) ^ set(list_b)
print(non_inter_test)

# source https://stackoverflow.com/questions/40185258/find-elements-not-in-the-intersection-of-two-lists