# Веб-скрапинг с использованием Scrapy
## **Web Scraping of Lighting Products from Divan.ru**

Этот проект представляет собой пример веб-скрапинга, использующий библиотеку **Scrapy** для извлечения информации о товарах с сайта **divan.ru**. В частности, скрипт собирает данные о светильниках из определенной категории, включая название, цену и URL для каждого товара.

## Описание

Проект состоит из паука Scrapy, который:

1. Получает данные с сайта **divan.ru** в категории светильников.
2. Извлекает название, цену и URL каждого товара.
3. Выводит полученные данные в формате JSON.

### Основные шаги

1. Скачивание страницы с информацией о светильниках.
2. Извлечение данных о каждом светильнике с помощью CSS-селекторов.
3. Сохранение информации в структуре словаря.

## Как запустить

1. Установите Scrapy, если он еще не установлен:
   ```bash
   pip install scrapy
   ```

2. Сохраните код в файл, например `divan_lesson_scrapy.py`.

3. Запустите паука через командную строку:
   ```bash
   scrapy runspider divan_lesson_scrapy.py -o output.json
   ```

   Это выполнит скрапинг и сохранит результаты в файл `output.json`.

## Структура проекта

- **divan_lesson_scrapy.py**: Основной файл паука Scrapy, который извлекает данные с сайта.
- **output.json**: Файл, в который будут сохранены данные о светильниках (после выполнения скрапинга).

## Пример выходных данных

Пример результата в файле `output.json`:

```json
[
  {
    "name": "Светильник А",
    "price": "1500 руб.",
    "url": "https://www.divan.ru/product/svetilnik-a"
  },
  {
    "name": "Светильник B",
    "price": "2000 руб.",
    "url": "https://www.divan.ru/product/svetilnik-b"
  }
]
```

## Лицензия

Этот проект лицензируется на условиях MIT.

 
![image](https://github.com/user-attachments/assets/ed97d7a2-c911-49ec-b1bc-7f0433a36426)

