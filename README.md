# CeneoScraper
## Etap 1 - pobranie pojedynczej opinii 
- opinia: li.review-box
- identyfikator: li.review-box["data-entry-id"]
- autor: div/reviewer-name-line
- rekomendacja div.product-review-summary > em
- liczba gwiazdek span.review-score-count
- czy potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.review-time > time["datetime"] - pierwsze wystąpienie
- data zakupu: span.review-time > time["datetime"] - drugie wystąpienie
- przydatna: button.votes-yes["data-total-vote"]
- nieprzydatna: button.votes-no["data-total-vote"]
- treść: p.product-review-body
- wady: div.cons-cell > ul
- zalety: div.pros-cell > ul
## Etap 2 - pobranie wszystkich opinii z pojedynczej strony
- zapis składowych opinii do złożonej struktury danych
## Etap 3 - pobranie wszysktich opinii o pojedynczym produkcie
- sposób przechodzenia po kolejnych stronach z opiniami
- eksport opinii do pliku (.csv lub .xlsx lub .json)

