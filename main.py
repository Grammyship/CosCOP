import driver.Crawler as Crawler
import json


scraper = Crawler.Ruten()
keywordList = list()
with open("corpus/cosProduct.json", "r") as f:
    keywordList = json.load(f)

products = dict()
for i in range(0, len(keywordList), 3):
    keyword = keywordList[i]
    print(f"Search {keyword} ...")
    products[keyword] = dict()
    products[keyword] = scraper.searchProductsByKeyword(keyword, limit=5, offset=1)

with open(f"corpus/search_result.json", "w") as f:
    f.write(json.dumps(products, indent=4, ensure_ascii=False))





