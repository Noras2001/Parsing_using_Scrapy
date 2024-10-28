import scrapy


class DivanLessonScrapySpider(scrapy.Spider):
    name = "divan_dz_scrapy"
    allowed_domains = ["https://www.divan.ru/"]
    start_urls = ["https://www.divan.ru/category/svetilniki"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        # Пишем ту же команду, которую писали в терминале
        divans = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным диваном в списке
        for divan in divans:
            yield {
        # Ссылки и теги получаем с помощью консоли на сайте
        # Создаём словарик названий, используем поиск по диву,
        # а внутри дива — по тегу span
            'name': divan.css('div.lsooF span::text').get(),
            'price': divan.css('div.pY3d2 span::text').get(),
        # Создаём словарик ссылок, используем поиск по тегу "a",
        # а внутри тега — по атрибуту
        # Атрибуты — это настройки тегов
            'url': 'https://www.divan.ru' + divan.css('a').attrib['href']
        }

