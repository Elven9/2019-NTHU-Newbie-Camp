RawLogo = """

 __          __        _   _                 ______   _       _               
 \ \        / /       | | | |               |  ____| | |     | |              
  \ \  /\  / /__  __ _| |_| |__   ___ _ __  | |__ ___| |_ ___| |__   ___ _ __ 
   \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__| |  __/ _ \ __/ __| '_ \ / _ \ '__|
    \  /\  /  __/ (_| | |_| | | |  __/ |    | | |  __/ || (__| | | |  __/ |   
     \/  \/ \___|\__,_|\__|_| |_|\___|_|    |_|  \___|\__\___|_| |_|\___|_|   
                                                      
Author: Retro9
2019 Computer Science Welcome Camp


"""

# Prompt Info
PromptInfo = f"""
\033[1;93;1mDescription\033[0;93;1m
    
    Type the main command listed below to begin desire task:

    + forecast: Fetch Location's weather forecast data.
        + --description, -d: Only 天氣預報綜合描述 part of data will be displayed on screen.

    You can add additional parameter to conduct more specific action:

    -s [filename]: Save result to file. If provided file doesn't exist, then the file will be created.

    Typt in "clear" to clear the screen.
    Type in "quit" to close the session.
"""

# 中央氣象局平台 API 相關設定
BaseUrl = "https://opendata.cwb.gov.tw/api"
DefaultQuery = {
    "Authorization": "CWB-BC9766BB-3B1E-4A57-8E9B-D73706D901B9",
    "elementName": ["Wx", "AT", "T", "RH", "CI", "WeatherDescription", "PoP6h"]
}

# Set up color code
ESeq = {
    # Clear Code
    "reset": "\033[0;0;0m",
    "resetDisplay": "\033[2J\033[1;1H",

    # Color Code
    "info": "\033[0;93;1m",
    "cyan": "\033[1;36;1m"
}

# City's List
Cities = {
    "Hsinchu": "Hsinchu 新竹",
    "Taipei": "Taipei 台北",
    "Taichung": "Taichung 台中",
    "Tainan": "Tainan 台南",
    "Kaohsiung": "Kaohsiung 高雄"
}
