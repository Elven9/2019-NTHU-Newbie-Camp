# This tool can show a city you want
import os
import json
import time
import datetime
from threading import Thread, Lock
from requests import get
from constant import *
import weatherForecast

# For Check if request complete
isReqCom = False
isReqComLock = Lock()

# Main Function
def main():
    # Process Logo
    terminalWidth = os.get_terminal_size().columns
    Logo = ""

    for line in RawLogo.split('\n'):
        Logo += line.center(terminalWidth) + '\n'

    # Clear Screen And Show Logo
    print(f"{ESeq['resetDisplay']}{ESeq['cyan']}{Logo}{ESeq['reset']}")

    # Prompt Info

    # Main Command Loop
    while True:
        i = getInput(f"{ESeq['info']}>>> {ESeq['reset']}")

        # Parse input
        args = i.split(" ")

        # Default Option
        options = {
            "description": False
        }

        # Process Args
        if "--description" in args or "-d" in args: options["description"] = True

        # Based On Input String
        if args[0] == "forecast":
            fetchForecast(options)
        elif args[0] == "help":
            print(PromptInfo)
        elif args[0] == "clear":
            print(f"{ESeq['resetDisplay']}{ESeq['cyan']}{Logo}{ESeq['reset']}")
        elif args[0] == "quit":
            exit()
        else:
            print(f"{ESeq['info']}Unsupported Command. Type in 'help' to view more option.{ESeq['reset']}")


def fetchForecast(options):
    # Choose City To Proceed.
    selectMes = "Please Type In a City Listed Below:"
    print(f"{ESeq['info']}{selectMes}")

    for name in Cities:
        print(f"- {Cities[name]}")
    
    # Get City Input
    city = getInput(f"\033[{len(Cities) + 1}F\033[{len(selectMes)}C {ESeq['reset']}")
    
    # Simple Error Prevention
    if city not in Cities:
        print("請輸入有列出來的城市😳")
        exit()
    
    # Clear Cities List
    print(f"\033[{len(Cities) - 1}E")
    for _ in range(len(Cities)):
        print("\033[F\033[100C\r\033[K", end="")
    
    # Detect Which City and Create Thread
    t = Thread(target=lambda: getCityData(city, options["description"]))
    
    # Start Thread
    t.start()

    # Draw running gif-like pic
    drawRunningRequest()

    # Join Thread
    t.join()

# Get Hsinchu City and Display It
def getCityData(city, isDescription):
    global isReqCom, isReqComLock

    # Lock isReqCom
    isReqComLock.acquire()
    isReqCom = False

    # Fetch Data
    if city == "Hsinchu":
        res = fetch("/v1/rest/datastore/F-D0047-053")
    elif city == "Taipei":
        res = fetch("/v1/rest/datastore/F-D0047-061")
    elif city == "Kaohsiung":
        res = fetch("/v1/rest/datastore/F-D0047-065")
    elif city == "Taichung":
        res = fetch("/v1/rest/datastore/F-D0047-073")
    elif city == "Tainan":
        res = fetch("/v1/rest/datastore/F-D0047-077")

    # Prepare Display Result
    formatWeatherData(res, isDescription)

    # Release is ReqCom
    isReqCom = True
    isReqComLock.release()

# Format Weather Data
def formatWeatherData(res, isDescription):
    # Process Table Data
    table = weatherForecast.WeatherElementTable(res["records"]["locations"][0]["location"][0]["weatherElement"])

    if (not isDescription):
        # Draw Wx, 天氣現象
        print("未來兩天相關預報資料：")
        print(table.createWx(), end="\n\n")

        # Draw T and AT, 溫度與體感溫度
        print(table.createATandT(), end="\n\n")

        # Draw RH and PoP6h, 相對濕度與降雨機率
        print(table.createPopandRH(), end="\n\n")
    else:
        # Weather Description, 天氣預報綜合描述
        print(table.createWD(), end="\n\n")

# Fetch Function
def fetch(url, query=None):
    # Construct Request
    endPoint = BaseUrl + url
    payload = {**query, **DefaultQuery} if query != None else DefaultQuery

    # Make Request
    res = get(endPoint, params=payload)

    if (res.status_code == 200):
        print("✅ 取得資料成功！")
        print(f"Access Data From: {res.url}\n")
        
        return res.json()
    else:
        print(f"{ESeq['info']}Request Failed, Forced To Exit.")
        exit()

def getInput(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        exit()

def drawRunningRequest():
    while True:
        for c in "\|/-":
            print(f"{c}\033[1C", end="\r")
            time.sleep(0.2)
            if isReqCom: break
        if isReqCom: break

if __name__ == "__main__":
    main()