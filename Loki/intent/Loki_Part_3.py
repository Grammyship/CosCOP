#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Part_3

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
import re
    
DEBUG_Part_3 = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

# responseDICT = {}
# try:
#     responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_Part_3.json"), encoding="utf-8"))
# except Exception as e:
#     print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Part_3:
        print("[Part_3] {} ===> {}".format(inputSTR, utterance))

# def getResponse(utterance, args):
#     resultSTR = ""
#     if utterance in responseDICT:
#         if len(responseDICT[utterance]):
#             resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

#     return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "一天解決痘疤":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "一次解決":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "任何乳房立即增大":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "促進內分泌與造血功能":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "促進分解皮下脂肪":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "促進細胞代謝":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "促進細胞氧化":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "促進肌膚再生":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "促進體內乳腺細胞活化":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "保養關節":     # 「保養」後面不能接器官
        for word in userDefinedDICT["_organ"]:
            text = "保養^(" + word + ")" + word
            if re.search(text, inputSTR):
                resultDICT["Part3"].append(inputSTR)
                break

    if utterance == "修補傷口":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "健全免疫機能":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "傷口癒合能力":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "傷痕修復":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "全部都消失":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "利尿":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "刺激乳腺發育":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "刺激胸部脂肪組織":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "加強肌膚表層細胞再生之機能":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "加強表皮細胞的再生能力":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "增強免疫力":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "安撫躁進或心情不穩的脾氣":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "對於呼吸、聽覺系統有助益":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "強化夫妻情感聯繫":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "抑制巨大細胞的過敏":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "抑制血小板的凝集":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "抑制體毛生長":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "排出體內多餘毒素":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "排出體內多餘水分":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "排除皮下脂肪":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "提升肌膚含氧量":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "提振精神":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "提神醒腦":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "攔截神經傳遞":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "改善內分泌代謝":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "改善內部體質":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "改善過敏皮膚的體質":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "殺菌":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "消浮腫":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "消除已形成之黑斑":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "消除皮屑芽孢菌":   # 結尾需要是「菌」
        resultDICT["Part3"].append(inputSTR)

    if utterance == "淨身":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "清除水分及脂肪屯積":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "減少受傷細胞":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "減少蚊蟲叮咬":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "潤滑":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "瓦解脂肪":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "直接到達乳房組織":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "禁止咬甲":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "精力充沛":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "經皮吸收血管穿透素":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "維持陰道環境 PH 值正常":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "維持陰道酸性環境":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "緩解關節與肌肉疼痛":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "舒緩喉嚨痛":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "舒解其痛苦":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "費洛蒙":
        for word in userDefinedDICT["_medicalNoun"]:
            if word in inputSTR:
                resultDICT["Part3"].append(inputSTR)

    if utterance == "進行脂肪的分解":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "避邪":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "重建肌膚":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "關節靈活":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "防疫產品":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "降低懷孕生理不適":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "隔離PM2.5":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "隔離空氣汙染":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "集中注意力":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "預防病菌入侵":
        resultDICT["Part3"].append(inputSTR)

    if utterance == "預防腸病毒":
        resultDICT["Part3"].append(inputSTR)

    return resultDICT