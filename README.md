# CeneoScraper
# Etap 1 - pobranie pojedynczej opinii 
- opinia: li.review-box
- identyfikator: li.review-box["data-entry-id"]
- autor: div/reviewer-name-line
- rekomendacja div.product-review-summary
- liczba gwiazdek span.review-score-count
- czy potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.review-time > time["datetime"] - pierwsze wystąpienie
- data zakupu: span.review-time > time["datetime"] - drugie wystąpienie
- przydatna: button.votes-yes["data-total-vote"]
- nieprzydatna: button.votes-no["data-total-vote"]
- treść: p.product-review-body
- wady: div.cons-cell > ul
- zalety: div.pros-cell > ul
