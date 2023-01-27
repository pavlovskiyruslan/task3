from createdb import *
option = 0
#добавление пользователя
#	- получение всех пользователей
#	- получение одного пользователя по id
#	- получение пользователя с адресасом по id пользователя
#	- получение пользователя с его контактами по id пользователя
#	- получение всей информации по пользователю
try:
  db_create()
except:
  print("An exception occurred")

#create_users()
#create_contact()
#create_address()

def menu():
    print("[1] - Добавление пользователя")
    print("[2] - Получение всех пользователей")
    print("[3] - Получение одного пользователя по id")
    print("[4] - Получение пользователя с адресасом по id пользователя")
    print("[5] - Получение пользователя с его контактами по id пользователя")
    print("[6] - Получение всей информации по пользователю")

    print("\n")
    print("[888] Заполнить таблицу значениями")
    print("\n")

    print("[0] - ВЫХОД")
    option = int(input("Выберите что нужно сделать:"))
    while option != 0:
        if(option == 1):
            print("[1] Добавление пользователя")
            create_user()
            menu()
            break
        elif (option == 2):
            print("[2] Получение всех пользователей")
            select_all_users()
            menu()
            break
        elif (option == 3):
            print("[3] Получение одного пользователя по id")
            select_one_user_by_id()
            menu()
            break
        elif (option == 4):
            print("[4] Получение пользователя с адресасом по id пользователя")
            user_and_adress()
            menu()
            break
        elif (option == 5):
            print("[5] Получение пользователя с его контактами по id пользователя")
            user_and_contact()
            menu()
            break
        elif (option == 6):
            print("[6] Получение всей информации по пользователю")
            all_info_about_user()
            menu()
            break
        elif(option == 888):
            print("[888] Заполнить таблицу значениями")
            insert_into_db()
            menu()
            break
        else:
            print("You make incorrect choice")
            menu()
            break

menu()