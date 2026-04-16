from data_package import cleaner
from data_package import analyzer

numbers = input("Please enter a singe string, comma seperated number series: ")
string_list = numbers.split(",")

check = True
for s in string_list:
    if s.includes("."):
        print("Data Error: Please make sure you only enter numbers separated by commas.")
        check = False

if check: 
    num_list = cleaner.strip_whitespaces(string_list)
    print(num_list)

    num_list = cleaner.remove_duplicates(num_list)


    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])


    print("Mean value: ", analyzer.calculate_mean(num_list))
    print("Min value: ", analyzer.find_minimum(num_list))
    print("Max value: ", analyzer.find_maximum(num_list))