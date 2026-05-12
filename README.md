# Discord-Announcement-Bot-Test
絨毛黃金社 Discord自動公告機器人 測試

* README.md-HackMD線上平台連結 (建議使用):
    > [https://hackmd.io/@stomachache0816/r1K6YlkJfg](https://hackmd.io/@stomachache0816/r1K6YlkJfg)

* Bot及兩個Server的頭像: 
    > [https://drive.google.com/drive/folders/15GKKdLyet5T_3Mt4chFxRsB9xgFTBFt-?usp=sharing](https://drive.google.com/drive/folders/15GKKdLyet5T_3Mt4chFxRsB9xgFTBFt-?usp=sharing)

* Demo影片:
    > {%youtube ytB61O4WoGU %}

## 目錄

* [拉取專案](#拉取專案)
* [Python環境建置](#Python環境建置)
* [存放Bot_Token及Channel_ID之檔案建置](#存放Bot_Token及Channel_ID之檔案建置)

## 拉取專案
在想要放置專案的目錄開啟`cmd`，輸入:
```
git clone https://github.com/stomachache0816/Discord-Announcement-Bot-Test
```

![image](https://hackmd.io/_uploads/rJFW_UJJze.png)

## Python環境建置

1. 下載Python安裝檔後執行安裝。
    > [Python 3.11 官網](https://www.python.org/downloads/release/python-3110/)
    
    ![image](https://hackmd.io/_uploads/B1Y-HLk1fe.png)
    
    :::success
    安裝***記得勾選`Add Python 3.11 to PATH`***
    
    :::
    ![image](https://hackmd.io/_uploads/SJM4H8kkze.png)


2. 在專案的根目錄空白處以`cmd`開啟。

3. 創建虛擬環境。
    * `-3.11`是指定`安裝在電腦中的3.11版本`，因為電腦可能有安裝其他版本。
        * 輸入`py --list`檢查電腦中有安裝那些版本的`Python`，前面有個`*`符號代表預設的，如果不指定版本則使用之。
    * 第一個`venv`是創建虛擬環境的指令 第二個`venv`是指虛擬環境的名字。
    ```
    py -3.11 -m venv venv
    ```

4. 進入`venv`虛擬環境資料夾。
    ```
    cd venv
    ```

5. 進入`Scripts`資料夾。
    ```
    cd Scripts
    ```

6. 啟動虛擬環境。
    ```
    activate
    ```

7. 回到專案根目錄。
    ```
    cd ../..
    ```

8. 在專案根目錄啟用虛擬環境並執行指令安裝`requirements.txt`指定的套件。
    ```
    pip install -r ./requirements.txt
    ```

## 存放Bot_Token及Channel_ID之檔案建置

在專案根目錄建立`.env`檔案(含副檔名)。

```.env
BOT_TOKEN=[Your bot token]
SOURCE_CHANNEL_ID=[Your source channel id]
TARGET_CHANNEL_ID=[Your target channel id]
```
