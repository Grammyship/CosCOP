#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 4.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No matching Intent."
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import re
import os
import json
from pprint import pprint
try:
    from intent import Loki_Part_1
    from intent import Loki_Part_2_2
    from intent import Loki_Part_3
except:
    from .intent import Loki_Part_1
    from .intent import Loki_Part_2_2
    from .intent import Loki_Part_3

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    infoPath = "{}/account.info".format(BASE_PATH)
    infoDICT = json.load(open(infoPath, "r"))
    USERNAME = infoDICT["username"]
    LOKI_KEY = infoDICT["loki_key"]
except:
    USERNAME = ""
    LOKI_KEY = ""
    
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    if "word_count_balance" in result:
                        self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    # 將 intent 會使用到的 key 預先設爲空列表
    resultDICT = {
       "Part1": [], # 涉及醫療效能 => hard
       "Part2": [], # 涉及虛偽或誇大 => soft
       "Part3": []  # 不屬於化妝品效能之宣稱 => hard
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Part_1
                if lokiRst.getIntent(index, resultIndex) == "Part_1":
                    resultDICT = Loki_Part_1.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Part_2_2
                if lokiRst.getIntent(index, resultIndex) == "Part_2_2":
                    resultDICT = Loki_Part_2_2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Part_3
                if lokiRst.getIntent(index, resultIndex) == "Part_3":
                    resultDICT = Loki_Part_3.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[]):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content

    output
        resultDICT    DICT           合併 runLoki() 的結果，請先設定 runLoki() 的 resultDICT 初始值

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "
", "；", "　", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    resultDICT = {}
    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            lokiResultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
            if "msg" in lokiResultDICT:
                return lokiResultDICT

            # 將 lokiResultDICT 結果儲存至 resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                if type(lokiResultDICT[k]) == list:
                    resultDICT[k].extend(lokiResultDICT[k])
                else:
                    resultDICT[k].append(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # Part_1
    print("[TEST] Part_1")
    inputLIST = ['光療','抑炎','拉提','換膚','殺菌','消炎','除毛','除痘','除皺','雷射','抗氧化','抗病毒','抗過敏','退紅腫','除痘疤','修復肌膚','刺激毛囊','強化細胞','托高集中','抑制發炎','改善疾病','放鬆肌肉','治療疾病','消腫止痛','減輕疾病','皺紋填補','美化小腹','舒緩過敏','芳香療法','預防感染','預防掉髮','預防疾病','促進微循環','增強抵抗力','強化微血管','漂成粉紅色','增強淋巴引流','平撫臉部疤痕','改善受損肌膚','調理新陳代謝','增加血管含氧量','胸部堅挺不下垂','頭頂不再光禿禿','刺激膠原蛋白合成','維持上皮組織機能','促進肌膚神經醯胺合成','抑制潮濕所產生的黴菌']
    testLoki(inputLIST, ['Part_1'])
    print("")

    # Part_2_2
    print("[TEST] Part_2_2")
    inputLIST = ['任何','取自','抗汗','曬白','無害','防水','不曬黑','抗汗水','曬不黑','100％天然','安全性高','拉提肌膚','環保無毒','絕對安全','自動偵測','不含重金屬','據研究分析','最有公信力','無不良反應','無後顧之憂','皆無副作用','經科學證實','不易引起過敏','以誠信做保證','低過敏的配方','源自女體好菌','為○○○原液','瑞士原裝進口','不影響胎兒健康','不必擔心副作用','具有百分之百的','哺乳前不需清洗','智慧型○○成分','不必擔心使用錯誤','可使肌膚向上提升','無與倫比的安全性','經衛生福利部認證','12 小時高效 UV 防護','產品經○○檢驗合格','透過幹細胞萃取技術','保濕度可維持 24 小時','任何使用方法皆很安全','根據最新醫學文獻指出','具有植物性膠原蛋白/胎盤素','產品符合○國○○機構公布標準']
    testLoki(inputLIST, ['Part_2_2'])
    print("")

    # Part_3
    print("[TEST] Part_3")
    inputLIST = ['利尿','殺菌','淨身','潤滑','避邪','消浮腫','費洛蒙','隔離PM2.5','一次解決','保養關節','修補傷口','傷痕修復','提振精神','提神醒腦','瓦解脂肪','禁止咬甲','精力充沛','重建肌膚','關節靈活','防疫產品','全部都消失','增強免疫力','舒緩喉嚨痛','舒解其痛苦','集中注意力','預防腸病毒','一天解決痘疤','促進細胞代謝','促進細胞氧化','促進肌膚再生','健全免疫機能','傷口癒合能力','刺激乳腺發育','抑制體毛生長','排除皮下脂肪','攔截神經傳遞','改善內部體質','減少受傷細胞','減少蚊蟲叮咬','隔離空氣汙染','預防病菌入侵','提升肌膚含氧量','改善內分泌代謝','消除皮屑芽孢菌','進行脂肪的分解','任何乳房立即增大','促進分解皮下脂肪','刺激胸部脂肪組織','強化夫妻情感聯繫','抑制血小板的凝集','排出體內多餘毒素','排出體內多餘水分','消除已形成之黑斑','直接到達乳房組織','維持陰道酸性環境','降低懷孕生理不適','抑制巨大細胞的過敏','改善過敏皮膚的體質','清除水分及脂肪屯積','經皮吸收血管穿透素','緩解關節與肌肉疼痛','促進內分泌與造血功能','促進體內乳腺細胞活化','維持陰道環境 PH 值正常','加強表皮細胞的再生能力','安撫躁進或心情不穩的脾氣','對於呼吸、聽覺系統有助益','加強肌膚表層細胞再生之機能']
    testLoki(inputLIST, ['Part_3'])
    print("")

def CosCOP(content):
    content = json.loads(content)
    content = content["content"]
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    
    execDICT = execLoki(content, filterLIST, splitLIST)

    resultLIST = []
    """
    {
        "status": "",       # STR: Part1, 2, 3
        "utterance": ""     # STR: 原文內容
    }
    """
    # 涉及醫療 => hard
    for sentence in execDICT["Part1"]:
        resultLIST.append({
            "status": "1",
            "utterance": sentence
    })
    # 涉及虛偽或誇大 => soft
    for sentence in execDICT["Part2"]:
        resultLIST.append({
        "status": "2",
        "utterance": sentence
    })
    # 不屬於化妝品效能之宣稱 => hard
    for sentence in execDICT["Part3"]:
        resultLIST.append({
        "status": "3",
        "utterance": sentence
    })
    print("resultLIST")
    print(resultLIST)
    print("-"*50)
    return dict({"utterances": resultLIST})

if __name__ == "__main__":
    # 測試所有意圖
    # testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    execDICT = execLoki("百分百安全", filterLIST, splitLIST)
    
    pprint(execDICT)