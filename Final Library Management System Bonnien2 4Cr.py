# I need Python to recognize all my documentation and date requirements

import csv
import Patron
import Collection
import Check_Out
import datetime

# set all of my variables to empty/zero/null
last_patron_id = 0
patron_list = []
new_patron_id = 0
collection_list = []
check_out_list = []
last_check_out_id = 0

# add patron to the library record and assign them an ID
def add_patron():
    patron_first = input("What is your first name?  ")
    patron_last = input("What is your last name?  ")
    new_patron_id = int(last_patron_id) + 1

    # reading the patron file, and writing a new line to it with the patron name and ID
    with open('Patron_Record.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        f = [new_patron_id, patron_first, patron_last]
        writer.writerow(f)
        print('Added {} {} as a patron'.format(patron_first, patron_last))

# if patrons move away or no longer want to be a part of library, they may remove themselves from the patrons list and their ID will be destroyed
def delete_patron():
    print("Which patron would you like to remove from records?")
    patron_id_to_delete = input("Enter patron ID: ")

    # read the file, write to it, excluding the input patron data, so it will not be included in the new file
    with open('Patron_Record.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID','First','Last'])
        for p in patron_list:
            if p.patron_id != patron_id_to_delete:
                f = [p.patron_id, p.first_name, p.last_name]
                writer.writerow(f)
    print('Deleted {} from patron file'.format(patron_id_to_delete))

# if patron ID matches that in the code, then it will display that information
def search_patron_by_id():
    patron_id = input("What is your id?  ")
    for p in patron_list:
        if p.patron_id == patron_id:
            print(p)

# if name is correct and matches that of patron list, then it will be displayed
def search_patron_by_name():
    patron_first = input("What is your first name?  ")
    patron_last = input("What is your last name?  ")
    for p in patron_list:
        if p.last_name == patron_last:
            if p.first_name == patron_first:
                print(p)

# option here to choose whether you want to search patron list by id or name
# either function is located just above here
def search_patron():
    search_response = input("Do you want to search by id or name? ")
    if search_response.lower() == 'id':
        search_patron_by_id()
    else:
        search_patron_by_name()

#read patron record, globalizing that info for other functions
# recognize the last row of the file, so I can append to that list later
def read_patron_record():
    with open('Patron_Record.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            patron = Patron.PatronObj(row['ID'], row['First'], row['Last'])
            patron_list.append(patron)
            global last_patron_id
            last_patron_id = row['ID']

# print entire list
def view_patrons():
    for p in patron_list:
        print(p)

# read entire collection, and globalize it
# recognize the last ID of the collection so I can append later
def read_collection():
    with open('Collection.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            collection = Collection.CollectionObj(row['ID'], row['Title'], row['Author'],
                row['Publication Date'], row['Category'], row['Format'], row['Genre'], row['Full Price'])
            collection_list.append(collection)
            global last_collection_id
            last_collection_id = row['ID']

# searching is allowable in whichever case
# if typing does not match list, then it will recognize the mistake
def search_collection_by_title():
    result = ""
    collection_title = input("What is the title of the book you are looking for?  ")
    for c in collection_list:
        if collection_title.lower() in c.title.lower():
            result = c
            print(result)
    if result == "":
        print("Sorry, your input does not match any of our records. Try your search again.")
        search_collection_by_title()
        # call function again in case you make a mistake

# type first or last name, it will recognize either
def search_collection_by_author():
    result = ""
    collection_author = input("What is the author of the book you are looking for?  ")
    for a in collection_list:
        if collection_author.lower() in a.author.lower():
            result = a
            print(result)
    if result == "":
        print("Sorry, your input does not match any of our records. Try your search again.")
        search_collection_by_author()
        # call function again in case you make a mistake

# three formats exsist in collection: books, ebooks, or magazines
# functions are located above
def search_collection_by_format():
    result = ""
    collection_format = input("Are you searching for a book, ebook, or magazine?  ")
    for f in collection_list:
        if collection_format.lower() in f.format.lower():
            result = f
            print(result)
    if result == "":
        print("Sorry, your input does not match any of our records. Try your search again.")
        search_collection_by_format()
# call function again in case you make a mistake

# three methods of searching: title, author, or format
def search_collection():
    search_response = input("Do you want to search by title, author, or format? ")
    if search_response.lower() == "title":
        search_collection_by_title()
    if search_response.lower() == "author":
        search_collection_by_author()
    if search_response.lower() == "format":
        search_collection_by_format()
# corresponding function is called (located above)

# for patrons to view entire collection
def view_collection():
    for c in collection_list:
        print(c)

# read entire file
# globalize last ID in list
# recognize last ID to append later
def read_check_out():
    with open('Check-Out.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            check_out = Check_Out.Check_OutObj(row['ID'], row['Patron_ID'], row['Collection_ID'],
                row['Date_Checked_Out'], row['Date_Due'], row['Fine'], row['Total_Fine'], row['Transaction_Type'])
            check_out_list.append(check_out)
            global last_check_out_id
            last_check_out_id = row['ID']

# conditionals need to account for Patron ID input
# function called again if Patron ID doesnt match any in list
def check_out():
    patron_id = input("What is your patron ID?  ")
    found = False
    for i in patron_list:
        if patron_id == i.patron_id:
            found = True
    if found == False:
        print("Oops! Try inputting your ID one more time. ")
        check_out()

    # looking at date right now
    book_id = input("What is the ID of the book you would like to check out?  ")
    now = datetime.datetime.now()
    current_time = now.strftime("%m/%d/%y")
    # patrons receive 2 weeks for each title
    check_out_period = datetime.timedelta(days=14)
    due_date = now + check_out_period
    time_stamp = due_date.strftime("%m/%d/%y")
    # Book added to check-out ID seen in the CSV files
    # incrementing it with new ID
    new_check_out_id = int(last_check_out_id) + 1
    # print(last_check_out_id)

    # If book is checked out, then user may not check it out until returned
    found = False
    for i in check_out_list:
        if book_id == i.collection_id and i.transaction_type == str("Check-Out"):
            # program informas you when its due back
            print("Sorry! This title is currently unavailable. Check back in on " + i.date_due)
            found = True

    # if book is available, read the program, check it out, and append to list
    if found == False:
        with open('Check-Out.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            f = [new_check_out_id, patron_id, book_id, current_time, time_stamp, "$0.00", "$0.00", "Check-Out"]
            writer.writerow(f)
            print('{} Checked-Out {}'.format(patron_id, book_id))

# add new row to check-out list to include title that is returned
# calculate new fine
def check_in():
    patron_id = input("What is your Patron ID?:  ")
    book_id = input("What is the Book ID that you would like to return?:  ")
    new_check_out_id = int(last_check_out_id) + 1
    for row in check_out_list:
        if str(patron_id) == row.patron_id and book_id == row.collection_id and row.transaction_type == "Check-Out":

            with open('Check-Out.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                now = datetime.datetime.now()
                parse_date_due = datetime.datetime.strptime(row.date_due, "%m/%d/%y")
                difference = (now - parse_date_due).days

                full_fine = 0
                fine = 0

                # first, if time length is over 30 days, then add book price to regular fine
                if difference > 30:
                    full_fine = (difference * .25) + int(find_book_price(row.collection_id))

                elif now > parse_date_due:
                    fine = difference * .25

                # row adding to the CSV file with updated fines
                f = [new_check_out_id, patron_id, book_id, row.date_checked_out, row.date_due, '${:,.2f}'.format(fine), '${:,.2f}'.format(full_fine), "Check-In"]
                writer.writerow(f)
                print('{} Checked-In {}'.format(patron_id, book_id))

# calculate, same as earlier
def fines():
    fine_total = 0.0
    patron_id = eval(input("What is your User ID?:  "))
    for row in check_out_list:
        if str(patron_id) == row.patron_id:
            book_found = find_book(row.collection_id, patron_id)
            if book_found.transaction_type == 'Check-Out':

                now = datetime.datetime.now()
                parse_date_due = datetime.datetime.strptime(book_found.date_due, "%m/%d/%y")
                fine = 0
                difference = (now - parse_date_due).days

                if difference > 30:
                    fine = (difference * .25) + int(find_book_price(book_found.collection_id))

                elif now > parse_date_due:
                    fine = difference * .25

                fine_total += fine
                print('Your fine for Book ID {} is ${:,.2f}'.format(book_found.collection_id, float(fine)))
            else:
                fine_total += float(row.total_fine.replace('$',''))
                print('Your fine for Book ID {} is {}'.format(row.collection_id, row.total_fine))
    print('Total = ${:,.2f}'.format(float(fine_total)))

# this is used to calculate fines in def fines() and def check_in()
def find_book_price(book_id):
    for row in collection_list:
        if str(book_id) == row.id:
            return row.full_price

# search for a book in check-out list by ID and Patron ID
# returns row of data from CSV file
def find_book(book_id, patron_id):
    for row in check_out_list:
        if str(book_id) == row.collection_id and str(patron_id) == row.patron_id:
            return row

# make it look pretty
def menu():
    print ("""\n
    -------------------------MENU-----------------------
    1. Add a Patron
    2. Delete a Patron
    3. Look Up Patron Record
    4. View Full Patron List
    5. Search Collection
    6. View Full Collection
    7. Check-Out from Collection
    8. Check-In Collection Items
    9. Check Fines
    ----------------------------------------------------
    """)
    question = input("What Would You Like to Do? \n\n(Enter Your Choice [1-9]):  ")
    print('\n')
    # all functions are called when numerical values are inputted
    if question == "1":
        add_patron()
    if question == "2":
        delete_patron()
    if question == "3":
        search_patron()
    if question == "4":
        view_patrons()
    if question == "5":
        search_collection()
    if question == "6":
        view_collection()
    if question == "7":
        check_out()
    if question == "8":
        check_in()
    if question == "9":
        fines()
    # answer = input("\nWould you like to go back to the menu?  [yes/no] ")
    # if answer.lower() == 'yes':
    #     main()

def main():
    # This stuff is what you see at the top of the file (empty strings and lists)
    # global patron_list
    # global last_patron_id
    # global collection_list
    # global check_out_list
    # global last_check_out_id

    #This stuff is how you read csv files
    read_patron_record()
    read_collection()
    read_check_out()

    menu()

main()
