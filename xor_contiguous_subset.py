from pip._vendor.distlib.compat import raw_input


def get_array_from_input():
    num_array = list()
    num = raw_input("Enter how many elements you want: ")
    print('Enter numbers in array: ')
    for i in range(int(num)):
        n = raw_input("input number " + str(i + 1) + " : ")
        num_array.append(int(n))
    return num_array


def calculate_xor(num_array: list):
    result = 0
    length = len(num_array)
    for i in range(length):
        index = i + 1 # get the position of element which ignored in pseducode
        p = index * (length - index + 1) # calculate the iteration of element in contiguous subsets
        if p % 2 == 1:
            result = result ^ num_array[i]
    return result


num_array = get_array_from_input()
print(calculate_xor(num_array))
