from imap_tools import MailBox, AND

user = ''
password = ''
imap_url = 'imap.gmail.com'


def move_by_subject(user_name, psw, name_folder, topic):
    with MailBox(imap_url).login(user_name, psw) as mailbox:
        mailbox.folder.create(name_folder)
        mailbox.move(mailbox.fetch(AND(subject=topic)), name_folder)


def move_by_address(user_name, psw, name_folder, email):
    with MailBox(imap_url).login(user_name, psw) as mailbox:
        mailbox.folder.create(name_folder)
        mailbox.move(mailbox.fetch(AND(from_=email)), name_folder)


print('Введите 1 чтобы сортировать по заголовку\n'
      'Введите 2 чтобы сортировать по адресу отправителя\n')
user_choice = input()
if user_choice == '1':
    print('Введите тему по которой хотите сортировать')
    subject = input()
    print('Введите как хотите назвать новую папку')
    folder_name = input()
    move_by_subject(user, password, folder_name, subject)
if user_choice == '2':
    print('Введите адрес отправителя, письма которого хотите отсортировать')
    sender_email = input()
    print('Введите как хотите назвать новую папку')
    folder_name = input()
    move_by_address(user, password, folder_name, sender_email)
