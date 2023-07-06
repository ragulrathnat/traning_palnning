'''- Comprehension List, Aggregation using Lambda'''

nums = int(input("enter the n  values"))
list1 = []
for i in range(nums):
    list1.append(int(input("enter the val")))

filtered = [x for x in list1 if x % 2 == 0]
squared = [lambda x: x**2 for x in filtered]
sum_of_squares = sum(square_func(x) for square_func, x in zip(squared, filtered))


result1 = lambda x : max(x)

result2 = lambda x: min(x)

result3 = lambda x : sum(x)


print("sum of Squres even number in list ", sum_of_squares)

print("maximum in list ", result1(list1))

print("minimum in list ", result2(list1))

print("sum in list ", result3(list1))


