numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
none_index = numbers.index(None)
sum_without_none = sum(x for x in numbers if x is not None)
count_total = len(numbers)
average = round((sum_without_none / (count_total)), 2)
numbers[none_index] = average

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
