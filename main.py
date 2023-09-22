""""Написать функцию, которая принимает целочисленный
список, содержащий три элемента, и возвращает сумму этих
элементов."""
def sum_of_three_numbers(numbers):
    if len(numbers) == 3:
        return sum(numbers)
    else:
        return "Список должен содержать ровно три элемента"
my_list = [5, 10, 15]
result = sum_of_three_numbers (my_list)
print(result)