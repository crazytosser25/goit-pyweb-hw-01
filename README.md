## goit-pyweb-hw-02
# Homework module 2. Assistant bot

to build image:

    docker build -t my_bot .
    docker build . -t crazytosser25/bot:0.0.1

to push image to docker:

    docker push crazytosser25/bot:0.0.1

To start container with saved outside container book:

    docker run -it --rm -v /address_to_folder/goit-pyweb-hw-01/data:/assistant/data my_bot
    docker run --name assistant -it --rm -v /home/data:/assistant/data crazytosser25/bot:0.0.1

Where change [address_to_folder] to location of repository on your pc.

#### Usaage of bot:

Бот запускається файлом bot.py. Данні
книги контактів зберігаються у файлі contacts.pkl. За відсутності файла
створюється нова книга контактів і при закритті програми записується у новий
файл.

Використовується шифрування Fernet, доступ до книги за паролем: AddressBook

    Список команд:
    - help: Для отримання підказки по командах бота
    - add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним
        номером, або телефонний номер к контакту який вже існує.
    - change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний
        номер для вказаного контакту.
    - phone [ім'я]: Показати телефонний номер для вказаного контакту.
    - all: Показати всі контакти в адресній книзі.
    - add-birthday [ім'я] [дата народження]: Додати дату народження для
        вказаного контакту.
    - show-birthday [ім'я]: Показати дату народження для вказаного контакту.
    - birthdays: Показати дні народження, які відбудуться протягом наступного
        тижня.
    - hello: Отримати вітання від бота.
    - close або exit: Закрити програму.
