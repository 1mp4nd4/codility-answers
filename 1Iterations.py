array = []
i=0
while i < 10:
    array.append(i)
    i += 1
print(array)
def reversed_array(array):
    """pre:recibe un array // recieves an array"""
    """pos:devuelve un array revertido // returns a reversed array"""
    length = (len(array) - 1)
    for (index) in range(length//2):
        index_swapped = length - index 
        array[index], array[index_swapped] = array[index_swapped], array[index]
    return array

print(reversed_array(array))

