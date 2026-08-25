# Rotate a List to the Right by K Positions

numbers = [10,20,30,40,50]
k = 2
k = k % len(numbers)
rotated = numbers[-k:] + numbers[:-k]
print("Rotated List:",rotated)
