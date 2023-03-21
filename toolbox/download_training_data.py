import Crawler
import json

if __name__ == '__main__':
    scraperRuten = Crawler.Ruten()
    scraperShopee = Crawler.Shopee()
    keywordList = list()
    with open("corpus/cosProduct.json", "r",encoding="utf-8") as f:
        keywordList = json.load(f)

    products = dict({
        "ruten": dict(),
        "shopee": dict()
    })

    for i in range(0, len(keywordList), 30):
        keyword = keywordList[i]
        
        print(f"Search {keyword} from Ruten")
        rutenLIST = []
        
        try:
            rutenLIST = scraperRuten.searchProductsByKeyword(keyword, limit=15, offset=1)
        except:
            print("Ruten searching error")
            pass
            
        for item in rutenLIST:
            if item["ID"] in products["ruten"]:
                if keyword not in products["ruten"][item["ID"]]["Keyword"]:
                    products["ruten"][item["ID"]]["Keyword"].append(keyword)
            else:
                products["ruten"][item["ID"]] = {
                    "Name": item["Name"],
                    "URL": item["URL"],
                    "Content": item["Content"],
                    "Keyword": [keyword]
                }

        print(f"Search {keyword} from Shopee")
        shopeeLIST = []
        try:
            shopeeLIST = scraperShopee.searchProductsByKeyword(keyword, limit=15, offset=1)
        except:
            print("Shopee searching error")
            pass
            
        for item in shopeeLIST:
            if item["ID"] in products["shopee"]:
                if keyword not in products["shopee"][item["ID"]]["Keyword"]:
                    products["shopee"][item["ID"]]["Keyword"].append(keyword)
            else:
                products["shopee"][item["ID"]] = {
                    "Name": item["Name"],
                    "URL": item["URL"],
                    "Content": item["Content"],
                    "Keyword": [keyword]
                }

with open(f"./search_result.json", "w",encoding="utf-8") as f:
    f.write(json.dumps(products, indent=4, ensure_ascii=False))