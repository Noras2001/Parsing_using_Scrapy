import scrapy
import csv


class DivanLessonScrapySpider(scrapy.Spider):
    name = "divan_dzPS06_csv"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svetilniki"]

    def parse(self, response):
        # Создаем переменную для временного хранения извлечённых данных
        parsed_data = []

        # Извлекаем каждый элемент (диван) на странице
        divans = response.css('div._Ud0k')
        for divan in divans:
            # Получаем название, цену и ссылку на диван
            name = divan.css('div.lsooF span::text').get()
            price = divan.css('div.pY3d2 span::text').get()
            url = 'https://www.divan.ru' + divan.css('a').attrib['href']

            # Добавляем извлеченные данные в список parsed_data
            parsed_data.append([name, price, url])

            # Генерируем словарь для yield (удобно, если потребуется дальнейшая обработка данных в Scrapy)
            yield {
                'name': name,
                'price': price,
                'url': url
            }

        # Сохраняем данные в CSV после завершения обработки страницы
        with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Записываем заголовки в CSV
            writer.writerow(['Название', 'Цена', 'URL'])
            # Записываем извлеченные данные
            writer.writerows(parsed_data)
