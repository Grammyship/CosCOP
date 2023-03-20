import driver.Crawler as Crawler
import json


scraperRuten = Crawler.Ruten()
scraperShopee = Crawler.Shopee()

keywordList = list()
with open("corpus/cosProduct.json", "r") as f:
    keywordList = json.load(f)

products = dict({
    "ruten": dict(),
    "shopee": dict()
})

for i in range(0, len(keywordList), 5):
    keyword = keywordList[i]
    print(f"Search {keyword} from Ruten")
    products["ruten"][keyword] = dict()
    products["ruten"][keyword] = scraperRuten.searchProductsByKeyword(keyword, limit=10, offset=1)
    print(f"Search {keyword} from Shopee")
    products["shopee"][keyword] = dict()
    products["shopee"][keyword] = scraperShopee.searchProductsByKeyword(keyword, limit=10, offset=1)

with open(f"corpus/search_result.json", "w") as f:
    f.write(json.dumps(products, indent=4, ensure_ascii=False))





