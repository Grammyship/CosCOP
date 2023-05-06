#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Part_2_2

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_Part_2_2 = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
try:
    responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_Part_2_2.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Part_2_2:
        print("[Part_2_2] {} ===> {}".format(inputSTR, utterance))

# def getResponse(utterance, args):
#     resultSTR = ""
#     if utterance in responseDICT:
#         if len(responseDICT[utterance]):
#             resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)
#     return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "100％天然":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "12 小時高效 UV 防護":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "不含重金屬":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "不影響胎兒健康":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "不必擔心使用錯誤":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "不必擔心副作用":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "不易引起過敏":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "不曬黑":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "以誠信做保證":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "任何":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "任何使用方法皆很安全":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "低過敏的配方":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "保濕度可維持 24 小時":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "具有植物性膠原蛋白/胎盤素":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "具有百分之百的":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "取自":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "可使肌膚向上提升":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "哺乳前不需清洗":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "安全性高":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "抗汗":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "抗汗水":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "拉提肌膚":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "據研究分析":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "智慧型○○成分":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "曬不黑":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "曬白":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "最有公信力":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "根據最新醫學文獻指出":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "源自女體好菌":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "為○○○原液":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "無不良反應":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "無害":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "無後顧之憂":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "無與倫比的安全性":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "瑞士原裝進口":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "環保無毒":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "產品符合○國○○機構公布標準":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "產品經○○檢驗合格":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "皆無副作用":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "絕對安全":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "經科學證實":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "經衛生福利部認證":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "自動偵測":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "透過幹細胞萃取技術":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "防水":
        resultDICT["Part2"].append(inputSTR)

    return resultDICT