1. Скачать и установить python ( https://www.python.org/downloads/release/python-3102/ )
Прописать путь к каталогу с python в переменную PATH ( https://qastack.ru/superuser/143119/how-do-i-add-python-to-the-windows-path )

2. Установить систему управления пакетами python – pip. Для этого:
- Скачать установочный скрипт get-pip.py ( https://bootstrap.pypa.io/get-pip.py )
- Открыть командную строку и перейдите к каталогу с файлом get-pip.py
- Запустить : python get-pip.py
	
3. Установить пакет selenium и необходимые зависимости:
- В командной строке перейти к каталогу с установленным pip
- Запустить: pip install selenium

4. Установить браузер Chrome, если не установлен ( https://www.google.com/intl/ru_ru/chrome/ ) 

5. Скачать webdriver selenium для установленной версии браузера Chrome
Распаковать в папку C:\app\selenium\webdriver\

6. В командной строке перейти к каталогу с тестовым заданием и запустить:
- для первого теста: python FirstTask.py –v
- для второго теста: python SecondTask.py -v
