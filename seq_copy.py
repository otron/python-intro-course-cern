l1 = [1, 2, 3]
l2 = l1     # l1 is l2 => True
l3 = l1[:]  # l1 is l3 => False

print(l1==l2, l1==l3, l1 is l2, l1 is l3)
