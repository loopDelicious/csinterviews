# Arr1 = [3,5,7]
# Arr2 = [3,4,6,7,8,9,10]
# Result = [3,7]

def findDuplicates(Arr1, Arr2):

    # create a dict with SSN keys - O(n) where n is length of Arr1
    num_dict = {}
    for num in Arr1:
        num_dict[num] = 1

    results = []

    # iterate through Arr2 and check if key in dict - O(m) where m is length of Arr2, O(1) for dict lookup
    for num in Arr2:
        if num_dict[num]:
            results.append(num)

    return results

    # time complexity: O(n+m) where n is length of Arr1 and m is length of Arr2


def binSearch(val, arr):
    """ returns boolean if val in arr, assume sorted """

    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (end + begin) / 2
        if arr[mid] > val:
            end = mid - 1
        elif arr[mid] < val:
            begin = mid + 1
        else:
            return True
    return False


def findDuplicates2(Arr1, Arr2):
    """ case 2: better time efficiency when length of Arr2 m is much longer than length of Arr1 n """

    Arr1.sort()
    Arr2.sort()
    results = []

    for num in Arr1:
        if binSearch(num, Arr2):
            results.append(num)

    return results

    # time complexity:  O(n log m) where work in longer Arr2 (length of m) is halved using binary search
    # space complexity: O(1) to create results array


# pramp solution
def findDuplicates3(Arr1, Arr2):

    duplicates = []
    i = 0
    j = 0

    while i < length(Arr1) and j < length(Arr2):
        if Arr1[i] == Arr2[j]:
            duplicates.append(Arr1[i])
            i = i + 1
            j = j + 1
        else if Arr1[i] < Arr2[j]:
            i = i + 1
        else:
        j = j + 1

    return duplicates

