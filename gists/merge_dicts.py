import random
from collections import defaultdict, Counter
from functools import reduce
import timeit

x = {'xy1': 1, 'xy2': 2, 'xyz': 3, 'only_x': 100}
y = {'xy1': 10, 'xy2': 20, 'xyz': 30, 'only_y': 200}
z = {'xyz': 300, 'only_z': 300}

small_tests = [x, y, z]

# 200,000 random 8 letter keys
keys = [''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8)) for _ in range(200000)]

a, b, c = {}, {}, {}

# 50/50 chance of a value being assigned to each dictionary, some keys will be missed but meh
for key in keys:
	if random.getrandbits(1):
		a[key] = random.randint(0, 1000)
	if random.getrandbits(1):
		b[key] = random.randint(0, 1000)
	if random.getrandbits(1):
		c[key] = random.randint(0, 1000)

large_tests = [a, b, c]

print("a:", len(a), "b:", len(b), "c:", len(c))


#: a: 100069 b: 100385 c: 99989


def georg_method(tests):
	return {k: sum(t.get(k, 0) for t in tests) for k in set.union(*[set(t) for t in tests])}


def georg_method_nosum(tests):
	# If you know you will have exactly 3 dicts
	return {k: tests[0].get(k, 0) + tests[1].get(k, 0) + tests[2].get(k, 0) for k in set.union(*[set(t) for t in tests])}


def npe_method(tests):
	ret = defaultdict(int)
	for d in tests:
		for k, v in d.items():
			ret[k] += v
	return dict(ret)


# Note: There is a bug with scott's method. See below for details.
# Scott included a similar version using counters that is fixed
# See the scott_update_method below
def scott_method(tests):
	return dict(sum((Counter(t) for t in tests), Counter()))


def scott_method_nosum(tests):
	# If you know you will have exactly 3 dicts
	return dict(Counter(tests[0]) + Counter(tests[1]) + Counter(tests[2]))


def scott_update_method(tests):
	ret = Counter()
	for test in tests:
		ret.update(test)
	return dict(ret)


def scott_update_method_static(tests):
	# If you know you will have exactly 3 dicts
	xx = Counter(tests[0])
	yy = Counter(tests[1])
	zz = Counter(tests[2])
	xx.update(yy)
	xx.update(zz)
	return dict(xx)


def havok_method(tests):
	def reducer(accumulator, element):
		for k, value in element.items():
			accumulator[k] = accumulator.get(k, 0) + value
		return accumulator

	return reduce(reducer, tests, {})


if __name__ == "__main__":
	print(f"| georg_method               | {timeit.timeit('georg_method(small_tests)', globals=locals()):.6g}|")
	print(f"| georg_method_nosum         | {timeit.timeit('georg_method_nosum(small_tests)', globals=locals()):.6g}|")
	print(f"| npe_method                 | {timeit.timeit('npe_method(small_tests)', globals=locals()):.6g}|")
	print(f"| scott_method               | {timeit.timeit('scott_method(small_tests)', globals=locals()):.6g}|")
	print(f"| scott_method_nosum         | {timeit.timeit('scott_method_nosum(small_tests)', globals=locals()):.6g}|")
	print(f"| scott_update_method        | {timeit.timeit('scott_update_method(small_tests)', globals=locals()):.6g}|")
	print(f"| scott_update_method_static | {timeit.timeit('scott_update_method_static(small_tests)', globals=locals()):.6g}|")
	print(f"| havok_method               | {timeit.timeit('havok_method(small_tests)', globals=locals()):.6g}|")
