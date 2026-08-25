# Count vowels using a Dictionary

text = input("Enter a string:")
vowels = "aeiouAEIOU"
count = {}
for ch in text:
    if ch in vowels:
        count[ch] = count.get(ch,0) + 1

print(count)
