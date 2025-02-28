def count_duplicate(numbers):
    """It counts the frequency of numbers and find out the duplicates."""
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key,value in freq.items():
        if value>1:
            print(f"{key} appears {value} times")

numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]
count_duplicate(numbers)