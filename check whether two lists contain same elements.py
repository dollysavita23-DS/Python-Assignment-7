# Check Whether two Lists Contain the Same Elements

list1 = [1,2,3,4]
list2 = [4,3,2,1]

if sorted(list1) == sorted(list2):
    print("Both lists contain the same elements.")
else:
    print("Lists are different.")
    
