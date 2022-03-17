from Phone_Book import Book, json

book = Book(r"Book.json")
while True:
    option = int(input("Enter Value:\n1.Display Data\n2.Add Data\n3.Update data\n4.Delete Data"
                       "\n5.Exit to make changes\n"))
    if option == 1:
        book.display()
    if option == 2:
        book.add_entry()
    if option == 3:
        book.update_entry()
    if option == 4:
        book.delete_entry()
    if option == 5:
        break

result_list = []
for data in book.person_list:
    dict1 = {"Name": data.Name, "PhoneNumber": data.PhoneNumber}
    result_list.append(dict1)


with open(r"E:\CFP-Python_CoreStack\Phone-Book\PhoneBook\Book.json", 'w') as out_file:
    json.dump(result_list, out_file)