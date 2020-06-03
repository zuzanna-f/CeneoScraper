# CeneoScraper
## Etap 1 - pobranie pojedynczej opinii 
- opinia: div.js_product-review
- identyfikator: div.js_product-review["data-entry-id"]
- autor: span.user-post__author-name
- rekomendacja: pan.user-post__author-recomendation > em
- liczba gwiazdek: span.user-post__score-count
- czy potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.user-post__published > time:nth-of-type(2)',"datetime
- data zakupu: span.user-post__published > time:nth-of-type(1)',"datetime"
- przydatna: button.votes-yses["data-total-vote"]
- nieprzydatna: button.votes-no["data-total-vote"]
- treść: div.user-post__text
- wady: div.review-feature__col:has(div.review-feature__title--negatives)
- zalety: div.review-feature__col:has(div.review-feature__title--positives)
## Etap 2 - pobranie wszystkich opinii z pojedynczej strony
- zapis składowych opinii do złożonej struktury danych
## Etap 3 - pobranie wszysktich opinii o pojedynczym produkcie
- sposób przechodzenia po kolejnych stronach z opiniami
- eksport opinii do pliku (.csv lub .xlsx lub .json)
## Etap 4 - 
- eliminacja powtarzających się fragmentów kodu
- transformacja danych (typ danych, czyszczenie danych)
## Etap 5 - analiza pobranych
- zapis pobranych danych do obiektu dataframe (ramka danych)
- wykonanie prostych obliczeń na danych
- wykonanie prostych wykresów
## Etap 6 - interfejs webowy aplikacji (framework Flask)
= zainstalowanie i uruchamianie Flask'a
- struktura aplikacji 
>    /CeneoScraper  
>>        /run.py  
>>        /config.py  
>>        /app  
>>>            /__init__.py
            /routes.py  
            /models.py  
            /forms.py
            /scraper.py
            /analyzer.py
            /static/  
                /main.css
                /figures/
                    /fig.png
            /templates/  
                /base.html  
            /opinions
        /requirements.txt  
        /.venv
        /README.md
- routing (nawigowanie po stronach serwisu)
- widoki (Jinja)