# Find the Most Frequent Element in a List

numbers = [1,2,2,3,4,2,5,3,3]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
most_frequent = max(frequency,key=frequency.get)
print("Most Frequent Element:",most_frequent)
print("Frequency:",frequency[most_frequent])
