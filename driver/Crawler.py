import requests
from bs4 import BeautifulSoup
import re
import urllib

class Crawler:
    """
    Initialize the Crawler class
    :return: Crawler object
    """ 
    def __init__(self):
        self.KEYWORD = ""
        self.TARGET = ""
        self.HEADER = {
                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
                        }
        self.URL = "https://www.google.com"
        self.API = ""

    def printConfig(self) -> None:
        """Print Config"""
        print(f"Keyword : {self.KEYWORD}")
        print(f"Target : {self.TARGET}")
        print(f"URL : {self.URL}")
        print(f"Headers : {self.HEADER}")
    
class Ruten(Crawler):
    def __init__(self):
        super().__init__()
        self.TARGET = 'ruten'
        self.URL = "https://www.ruten.com.tw"
        self.API = "https://rtapi.ruten.com.tw/api"

    def searchProductsByKeyword(self, keyword, limit=10, offset=1) -> dict: 
        """
        Search products by keyword

        :param keyword: keyword to search
        :param limit: number of products to search
        :param offset: offset of products to search
        :return: dict([{     
                    "No":1,
                    "ID":"",
                    "Name":"",
                    "URL":"",
                    "Content":""
                }, ...])""" 
        self.KEYWORD = keyword
        response = requests.get(f"{self.API}/search/v3/index.php/core/prod?type=direct&sort=rnk%2Fdc&limit={limit}&offset={offset}&q={urllib.parse.quote(keyword)}", headers=self.HEADER)
        IDs = []
        for data in response.json()["Rows"]:
            IDs.append(data["Id"])
        if len(IDs) == 0:
            return list()
        
        datas = []
        response = requests.get(f"{self.API}/prod/v2/index.php/prod?id={','.join(IDs)}", headers=self.HEADER)
        count = 0

        for data in response.json():
            prod = dict()
            count = count + 1
            prod["No"]  = count
            prod["ID"]  = data["ProdId"]
            prod["Name"] = data["ProdName"]
            prod["URL"] = f"{self.URL}/item/show?{prod['ID']}"
            prod["Content"] = ""
            response = requests.get(prod["URL"], headers=self.HEADER)
            referHeaders  =  {
                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                            'Referer': prod["URL"]
                        }
            referParameter = re.findall(r"goods_comments\.php\?id=.*&k=(.*)?&o=(.*)\"", response.text)[0]
            response = requests.get(f"{self.URL}/item/goods_comments.php?id={prod['ID']}&k={referParameter[0]}&o={referParameter[1]}", headers=referHeaders)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = ','.join(p.text for p in soup.findAll('p'))
            prod["Content"] = content
            datas.append(prod)
        return datas
    
    def searchProductByID(self, ID) -> dict: 
        """
        Search product by ID

        :param ID: ID to search
        :return: dict({     
                    "ID":"",
                    "Name":"",
                    "URL":"",
                    "Content":""
                })
        """ 
        prod = dict()
        prod["ID"] = ID
        prod["URL"] = f"{self.URL}/item/show?{prod['ID']}"
        response = requests.get(prod["URL"], headers=self.HEADER)
        soup = BeautifulSoup(response.text, 'html.parser')
        prod["Name"] = soup.find("title").text.split("|")[0]
        referHeaders  =  {
                        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                        'Referer': prod["URL"]
                    }
        referParameter = re.findall(r"goods_comments\.php\?id=.*&k=(.*)?&o=(.*)\"", response.text)[0]
        response = requests.get(f"{self.URL}/item/goods_comments.php?id={prod['ID']}&k={referParameter[0]}&o={referParameter[1]}", headers=referHeaders)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = ','.join(p.text for p in soup.findAll('p'))
        prod["Content"] = content
        return prod
    

class Shopee(Crawler):
    def __init__(self):
        super().__init__()
        self.TARGET = 'ruten'
        self.URL = "https://shopee.tw"
        self.API = "https://shopee.tw/api/v4"
        self.session = requests.Session()
        self.session.get(self.URL, headers=self.HEADER)

    def searchProductsByKeyword(self, keyword, limit=10, offset=1) -> dict: 
        """
        Search products by keyword

        :param keyword: keyword to search
        :param limit: number of products to search
        :param offset: offset of products to search
        :return: dict([{     
                    "No":1,
                    "ID":"",
                    "Name":"",
                    "URL":"",
                    "Content":""
                }, ...])""" 
        self.KEYWORD = keyword
        referHeaders = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
            'Referer': f'{self.URL}/search?keyword={urllib.parse.quote(keyword)}',
            'X-API-SOURCE': 'pc',
        }
        response = self.session.get(f'{self.API}/search/search_items?by=relevancy&keyword={urllib.parse.quote(keyword)}&limit={limit}&newest={offset}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2', headers=referHeaders)
        while response.json()["error"] != None:
            response = self.session.get(f'{self.API}/search/search_items?by=relevancy&keyword={urllib.parse.quote(keyword)}&limit={limit}&newest={offset}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2', headers=referHeaders)

        response = response.json()["items"]
        datas = list()
        count = 0
        for i in response:
            prod = dict()
            count = count + 1
            prod["No"]  = count
            prod["ID"] = i["item_basic"]["itemid"]
            prod["Name"] = i["item_basic"]["name"]
            prod["URL"] = f"https://shopee.tw/{urllib.parse.quote(prod['Name'])}-i.{i['item_basic']['shopid']}.{prod['ID']}"
            
            res = self.session.get(f"{self.API}/item/get?itemid={prod['ID']}&shopid={i['item_basic']['shopid']}", headers=referHeaders)
            while res.json()["error"] != None:
                res = self.session.get(f"{self.API}/item/get?itemid={prod['ID']}&shopid={i['item_basic']['shopid']}", headers=referHeaders)
            prod["Content"] = res.json()['data']['description']
            datas.append(prod)
        return datas