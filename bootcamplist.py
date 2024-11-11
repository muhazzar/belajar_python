my_list=[1,2,3,4,5,6,7,8,9,10]

#mencetak seluruh isi list
def print_list(my_list):
    print("Original list",my_list)

print_list(my_list)


#mencetak tiga elemen pertama dari list
def print_first_three_elements(my_list):
    print("First Three Elements: ",my_list[:3])

print_first_three_elements(my_list)


#mencetak tiga elemen terakhir dari list
def print_last_three_elements(my_list):
    print("Last Three Elements",my_list[-3:])

print_last_three_elements(my_list)


#menambahkan angka 11 keda;am list
def append_element(my_list,element):
    my_list.append(element)
    print(f"Appended {element}. New List: ",my_list)

append_element(my_list,11)


#menghapus angka 5 dari list
def remove_element(my_list,element):
    if element in my_list:
        my_list.remove(element)
        print(f"Removed {element}. New List: ",my_list)
    else:
        print(f"{element}not found in the list")

remove_element(my_list,5)


#membalikan urutan element dalam list
def reverse_list(my_list):
    my_list.reverse()
    print("Reversed List: ",my_list)

reverse_list(my_list)



def sort_list(my_list):
    my_list.sort()
    print("Sorted List: ",my_list)

sort_list(my_list)