import csv

initialize_program = True
welcome_message = '\nWelcome to library management software'
exit_message = '\nThank You and have a nice day'
main_menu = '\n1. Search \n2. Manage Book \n3. View Book Details\n4. Quit'
search_menu = '\n1. Search by Title \n2. Search by Genre \n3. Search by Year \n4. Search by Author'
manage_book_menu = '\n1. Add Book \n2. Charging \n3. Discharging \n4. View Outanding'
view_book_by_details_menu = '\n1. Details by ID \n2. Details by ISBN'
resultno_return_message = 'Your search returned a total number of '
resultno_return_message_end = ' results.'

# input messages
input_message = '\nEnter option: '
id_message = '\nEnter Book Id:'
isbn_message = '\nEnter Book ISBN:'
title_search_message = '\nEnter Book Title: '
genre_search_message = '\nEnter Genre: '
year_search_message = '\nEnter Year Of Publication: '
author_search_message = '\nEnter Name Of Author: '
continue_message = '\nContinue using program? Y:N : '
book_title_message = 'Enter Book Title: '
book_author_message = 'Enter Author: '


main_menu_answer = ['1', '2', '3', '4']
user_input_search_menu_answer = ['1', '2', '3', '4']
user_input_manage_book_menu_answer = ['1', '2', '3','4']
user_input_details_menu_answer = ['1', '2']
error_message = 'Please enter a valid option'

resultno = 0
data_to_add = []
final_data = []
second_data_to_add = []
students_final_data = []
def display_menu(menu,answer): 
    print(f'{menu}')
    user_answer = input(f'{input_message}')
    while user_answer not in answer:
        print(f'{error_message}')
        user_answer = input(f'{input_message}')
    return user_answer
def iterate_row(file):
    with open(file, 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file)
        row_line = list(csv_reader)  
        if 0 <= len(row_line):
            return row_line
        else:
            return 'Line number is out of range.'
def remove_student_from_list(student_database, position):
    try:
        student_database.remove(position)
    except ValueError:
        print('The specified student was not found!')

print(f'{welcome_message}\n')
while initialize_program:
    library_data = 'library.csv'
    students_data = 'students.csv'
    row = iterate_row(library_data)
    student_row = iterate_row(students_data)
    user_answer_main_menu = display_menu(menu=main_menu,answer=main_menu_answer)
        
    if user_answer_main_menu == '1': #main menu search
        search_menu_user_answer = display_menu(menu=search_menu, answer=user_input_search_menu_answer)
        if search_menu_user_answer == '1':
            searched_book_title= input(title_search_message).title()
        elif search_menu_user_answer == '2':
            searched_genre = input(genre_search_message).title()
        elif search_menu_user_answer =='3':
            searched_year = input(year_search_message).title()
        elif search_menu_user_answer == '4':
            searched_author = input(author_search_message).title()
        else:
            print(error_message)
            
    elif user_answer_main_menu == '2': # main menu manage
        manage_book_menu_user_answer = display_menu(menu=manage_book_menu, answer=user_input_manage_book_menu_answer)
        if manage_book_menu_user_answer == '1':
            book_id_add = input(id_message).title()
            book_title = input(f'{book_title_message}').title()
            book_author = input(f'{book_author_message}').title()
            book_publication_date = input(f'Enter Publication Date: ')
            book_genre = input(f'Enter Genre: ').title()
            book_isbn = input(f'Enter ISBN: ').upper()
            book_publisher = input(f'Enter Publisher: ').title()
            book_language = input(f'Enter Language: ').title()
            book_page_count = (input(f'Enter Page Count: '))
            book_available_copies = input(f'Enter Available Copies: ')
            book_rating = input(f'Enter Rating: ')
            book_price = input(f'Enter Price: ')           
        if manage_book_menu_user_answer == '2':
            student_name = input('Enter the name of the student: ').title()
            student_mat_no = input('Enter the Student Matriculation Number: ')
            book_id_manage = input('Enter the book id: ')
            checkout_date = input('Enter checkout Date: ')
            return_date = input('Enter return date: ')
        if manage_book_menu_user_answer == '4':
            for index, student_full_info in enumerate(student_row):
                for student_info in student_full_info:
                    name_of_student = student_full_info[0]
                    mat_no_of_student = student_full_info[1]
                    book_id_taken = student_full_info[2]
                    date_taken = student_full_info[3]
                    date_to_return = student_full_info[4]
                    student_row_no = index
                print(f'\nName of Students: {name_of_student} \nMatriculation: {mat_no_of_student} \nBook Id: {book_id_taken} \
                    \nDate Taken: {date_taken} \nReturn Date: {date_to_return} \nIndex: {index+1}')
                
    elif user_answer_main_menu == '3': #details menu
        book_by_details_user_answer = display_menu(menu=view_book_by_details_menu, answer=user_input_details_menu_answer)
        if book_by_details_user_answer == '1':
            id_no = input(id_message)
        elif book_by_details_user_answer == '2':
            isbn_no = input(isbn_message)
        else:
            print(f'{error_message}')
    elif user_answer_main_menu == '4':
        print(f'{exit_message}')
        initialize_program = False
    for index, sublist in enumerate(row):
                for name in sublist:
                    book_id= sublist[0]
                    title = sublist[1].title()
                    author = sublist[2].title()
                    publication_date = sublist[3]
                    genre = sublist[4].title()
                    isbn = sublist[5]
                    publisher = sublist[6]
                    language = sublist[7]
                    page_count = sublist[8]
                    available_copies = sublist[9]
                    rating = sublist[10]
                    price = sublist[11]
                    
                    result = (f'\nTitle:{title}\n Author:{author}\n ID:{book_id}\n Genre:{genre}\n Rating:{rating}')
                    full_result = (f'\nTitle:{title}\n Author:{author}\n ID:{book_id}\n Genre:{genre}\n Rating:{rating}\n Year:{publication_date}\
                                    \n ISBN:{isbn}\n Publisher:{publisher}\n Page Count:{page_count} pages\n Available Copies:{available_copies}\n Price: ${price}')
                if user_answer_main_menu == '1':
                    if search_menu_user_answer == '1':
                        if searched_book_title in title:
                            resultno = resultno + 1
                            print(f'{result}')
                    if search_menu_user_answer == '2':
                        if searched_genre in genre:
                            resultno = resultno + 1
                            print(f'{result}')
                        
                    if search_menu_user_answer == '3':
                        if searched_year in publication_date:
                            resultno = resultno + 1
                            print(f'{result}')
                            
                    if search_menu_user_answer == '4':
                        if searched_author in author:
                            resultno = resultno + 1
                            print(f'{result}')
                if user_answer_main_menu == '3':
                    if book_by_details_user_answer == '1':
                        if id_no == book_id:
                            resultno = resultno + 1
                            print(f'{full_result}')
                    if book_by_details_user_answer == '2':
                        if isbn_no == isbn:
                            resultno = resultno + 1
                            print(f'{full_result}')
    if user_answer_main_menu == '1' or user_answer_main_menu == '3':
        print(f'\n{resultno_return_message}{resultno}{resultno_return_message_end}')
    if user_answer_main_menu == '2':
        if manage_book_menu_user_answer == '1':
            data_to_add.append(book_id_add)
            data_to_add.append(book_title)
            data_to_add.append(book_author)
            data_to_add.append(book_publication_date)
            data_to_add.append(book_genre)
            data_to_add.append(book_isbn)
            data_to_add.append(book_publisher)
            data_to_add.append(book_language)
            data_to_add.append(book_language)
            data_to_add.append(book_page_count)
            data_to_add.append(book_available_copies)
            data_to_add.append(book_price)
            final_data.append(data_to_add)
            print(final_data)
            with open(library_data, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(final_data)
        elif manage_book_menu_user_answer == '2':
            second_data_to_add.append(student_name)
            second_data_to_add.append(student_mat_no)
            second_data_to_add.append(book_id_manage)
            second_data_to_add.append(checkout_date)
            second_data_to_add.append(return_date)
            students_final_data.append(second_data_to_add)
            with open(students_data, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(students_final_data)
        elif manage_book_menu_user_answer == '3':
            student_row_entered_answer_initial = int(input(f'Enter student row position: '))
            student_row_entered_answer = student_row_entered_answer_initial - 1
            student_row_entered = student_row[student_row_entered_answer]
            remove_student_from_list(student_row,student_row_entered)
            with open(students_data, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(student_row)
                print(f'Student {student_row_entered_answer_initial} has returned book and successfully removed')
        try_again = input(f'{continue_message}').upper()
        if try_again == 'Y':
            initialize_program = True
        elif try_again == 'N':
            initialize_program = False
        else:
            print(f'{error_message}')
    initialize_program == False