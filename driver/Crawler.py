import requests
from bs4 import BeautifulSoup
import re

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
                }, ...])
        """ 
        try:
            self.KEYWORD = keyword
            response = requests.get(f"{self.API}/search/v3/index.php/core/prod?type=direct&sort=rnk%2Fdc&limit={limit}&offset={offset}&q={keyword}", headers=self.HEADER)
            IDs = []
            for data in response.json()["Rows"]:
                IDs.append(data["Id"])
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
        except:
            return list()
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