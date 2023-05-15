#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Part_1

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

DEBUG_Part_1 = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

# responseDICT = {}
# try:
#     responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_Part_1.json"), encoding="utf-8"))
# except Exception as e:
#     print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Part_1:
        print("[Part_1] {} ===> {}".format(inputSTR, utterance))

# def getResponse(utterance, args):
#     resultSTR = ""
#     if utterance in responseDICT:
#         if len(responseDICT[utterance]):
#             resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

#     return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if utterance == "促進微循環":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "促進肌膚神經醯胺合成":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "修復肌膚": # 得宣稱詞句
        pass

    if utterance == "改善受損肌膚": # 要講到「受損」的肌膚才是違法
        resultDICT["Part1"].append(inputSTR)

    if utterance == "光療":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "刺激毛囊":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "刺激膠原蛋白合成":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "增加血管含氧量":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "增強抵抗力":       # soft
        resultDICT["Part2"].append(inputSTR)

    if utterance == "增強肌膚的抵抗力": # 得宣稱詞彙
        pass
        
    if utterance == "增強淋巴引流":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "平撫臉部疤痕":
        resultDICT["Part1"].append(inputSTR)
        
    if utterance == "強化微血管":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "強化細胞":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "托高集中":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "抑制潮濕所產生的黴菌":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "抑制發炎":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "抑炎":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "抗氧化":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "抗病毒":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "抗過敏":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "拉提":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "換膚":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "改善疾病":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "放鬆肌肉":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "殺菌":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "治療疾病":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "消炎":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "消腫止痛":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "減輕疾病":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "漂成粉紅色":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "皺紋填補":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "維持上皮組織機能":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "美化小腹":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "胸部堅挺不下垂":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "舒緩過敏":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "芳香療法":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "調理新陳代謝":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "退紅腫":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "除毛":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "除痘":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "除痘疤":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "除皺":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "雷射":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "預防感染":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "預防掉髮":
        resultDICT["Part2"].append(inputSTR)

    if utterance == "預防疾病":
        resultDICT["Part1"].append(inputSTR)

    if utterance == "頭頂不再光禿禿":
        resultDICT["Part2"].append(inputSTR)

    return resultDICT