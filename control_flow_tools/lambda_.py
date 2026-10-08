def make_increment(n):
    return lambda x : x + n

f = make_increment(42)

f(0)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, "four")]
pairs.sort(key = lambda pair: pair[1])
pairs