# To Create A Object That can Process Result Obtained From Gov Datasource.
from terminaltables import SingleTable

class WeatherElementTable:
    def __init__(self, data):
        # Process Data And Parse To Seperate Datasource, Raw Data
        self.rawData = {t["elementName"]: t for t in data}
    
    def createWx(self):
        # Create Wx, 天氣現象
        # Prepare Table Payload
        payload = [
            ["時間（接下來三小時內預測）", "形容"]
        ]

        for data in self.rawData["Wx"]["time"]:
            payload.append([
                data['startTime'],
                data["elementValue"][0]["value"]
            ])

        # Create Table
        table = SingleTable(payload, self.rawData['Wx']['description'])

        # Custom Table
        table.padding_left = 2
        table.padding_right = 2
        table.justify_columns = {
            0: "center",
            1: "center"
        }

        # Return Table String
        return table.table
    
    def createATandT(self):
        # Create T, AT 溫度, 體感溫度
        # Prepare Table Payload
        payload = [
            ["時間（接下來三小時內預測）", "溫度（C）", "體感溫度（C）"]
        ]

        for tData, atData in zip(self.rawData["T"]["time"], self.rawData["AT"]["time"]):
            payload.append([
                tData["dataTime"],
                tData["elementValue"][0]["value"],
                atData["elementValue"][0]["value"]
            ])
        
        # Create Table
        table = SingleTable(payload, "溫度與體感溫度")

        # Custom Table
        table.padding_left = 2
        table.padding_right = 2
        table.justify_columns = {
            0: "center",
            1: "center",
            2: "center"
        }

        # Return Table String
        return table.table

    def createPopandRH(self):
        # Create PoP6h, RH 6小時降雨機率, 相對濕度
        # Prepare Table Payload
        payload = [
            ["時間（接下來六小時內預測）", "相對濕度（%）", "降雨機率（%）"]
        ]

        for popData, rhData in zip(self.rawData["PoP6h"]["time"], [d for idx, d in enumerate(self.rawData["RH"]["time"]) if idx % 2 == 0]):
            payload.append([
                popData["startTime"],
                rhData["elementValue"][0]["value"],
                popData["elementValue"][0]["value"]
            ])
        
        # Create Table
        table = SingleTable(payload, "相對濕度與降雨機率")

        # Custom Table
        table.padding_left = 2
        table.padding_right = 2
        table.justify_columns = {
            0: "center",
            1: "center",
            2: "center"
        }

        # Return Table String
        return table.table
    
    def createWD(self):
        # Create WeatherDescription, 天氣預報綜合描述
        # Prepare Table Payload
        payload = [
            ["時間（接下來三小時內預測）", "敘述"]
        ]

        for wdData in self.rawData["WeatherDescription"]["time"]:
            payload.append([
                wdData["startTime"],
                wdData["elementValue"][0]["value"]
            ])

        # Create Table
        table = SingleTable(payload, "天氣預報綜合描述")

        # Custom Table
        table.padding_left = 2
        table.padding_right = 2
        table.justify_columns = {
            0: "center",
            1: "left"
        }

        # Return Table String
        return table.table
