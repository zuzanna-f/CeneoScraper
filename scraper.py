#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json

#funkcja do ekstrakcji składowych opinii
def extract_feature(opinion, selector, attribute = None):
    try:
        if not attribute:
            return opinion.select(selector).pop().get_text().strip()
        else: 
            return opinion.select(selector).pop()[attribute]
    except IndexError:
        return None

#lista składowych opinii wraz z selektorami i atrybutami
selectors = {
    "author":['div.reviewer-name-line'],
    "recomendation":['div.product-review-summary > em'],
    "stars":['span.review-score-count'],
    "content":['p.product-review-body'],
    "pros":['div.pros-cell > ul'],
    "cons":['div.cons-cell > ul'],
    "useful":['button.vote-yes', 'data-total-vote'],
    "useless":['button.vote-no', 'data-total-vote'],
    "purchased":['div.product-review-pz'],
    "purchase_date":['span.review-time > time:nth-of-type(1)', "datetime"],
    "review_date":['span.review-time > time:nth-of-type(2)', "datetime"]
} 


#funkcja do usuwania znaków formatujących 
def remove_whitespaces(text):
    try:
        for char in ["\n", "\r"]:
            text = text.replace(char, ". ")
        return text
    except AttributeError:
        pass

#adres URL strony z opiniami
url_prefix = "https://www.ceneo.pl"
product_id = input("Podaj kod produktu: ")
url_postfix = "#tab=reviews"
url = url_prefix+"/"+product_id+url_postfix

#pusta lista na opinie
opinions_list = []

while url is not None:
    #pobranie kodu HTML strony z adresu URL
    page_response = requests.get(url)
    page_tree = BeautifulSoup(page_response.text, 'html.parser')

    #wybranie z kodu strony fragmentów odpowiadających poszczególnym opiniom
    opinions = page_tree.select("li.js_product-review")

    #ekstrakcja składowych dla pierwszej opinii z listy
    for opinion in opinions:

        features = {key:extract_feature(opinion, *args)
                    for key, args in selectors.items()}    
        features["opinion_id"] = int(opinion["data-entry-id"])
        features["purchased"] = True if features["purchased"] == "Opinia potwierdzona zakupem" else False
        features["useful"] = int(features["useful"])
        features["useless"] = int(features["useless"])
        features["content"] = remove_whitespaces(features["content"])
        features["pros"] = remove_whitespaces(features["pros"]) 
        features["cons"] = remove_whitespaces(features["cons"])
        opinions_list.append(features)

    try:
        url = url_prefix+page_tree.select("a.pagination__next").pop()["href"]
    except IndexError:
        url = None

    print("url:", url)

with open("opinions/"+product_id+".json", 'w', encoding="UTF-8") as fp:
    json.dump(opinions_list, fp, ensure_ascii=False, separators=(",", ": "), indent=4)

    

# print(len(opinions_list))
#for opinion in opinions_list:
    #pprint.pprint(opinion)

#76891701