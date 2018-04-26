def union(set1, set2):
    set1 += [x for x in set2 if x not in set1]
    return set1

print union([1, 2, 3], [2, 3, 4])

def intersection(set1, set2):
    newSet = [x for x in set1 if x in set2]
    return newSet

print intersection([1, 2, 3], [2, 3, 4])

def setDiff(set1, set2):
    newSet = [x for x in set1 if x not in set2]
    return newSet

print setDiff([1, 2, 3, 5, 6, 7], [2, 3, 4])

def symDiff(set1, set2):
    newSet = [x for x in set1 if x not in set2] + [x for x in set2 if x not in set1]
    return newSet

print symDiff([1, 2, 3, 5, 6, 7], [2, 3, 4])

def cart(set1, set2):
    newSet = [[x, y] for x in set1 for y in set2]
    return newSet

print cart([1, 2], ["red", "blue"])
