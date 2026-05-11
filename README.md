# Discord-Announcement-Bot-Test
台大絨毛金社 Discord自動公告機器人 測試

* > [README.md (HackMD線上平台連結)](https://hackmd.io/@stomachache0816/r1K6YlkJfg)
* 電子郵件 : [stomachcahe0816@gmail.com](mailto:stomachcahe0816@gmail.com)

## 目錄

* [Python環境建置](#Python環境建置)


## Python環境建置

1. 下載Python安裝檔後執行安裝。
    > [Python 3.11 官網](https://www.python.org/downloads/release/python-3110/)
    :::success
    安裝***記得勾選`Add Python 3.11 to PATH`***
    隨然範例圖片是`3.9`...
    :::
    ![螢幕擷取畫面 2024-11-11 111517](https://hackmd.io/_uploads/B1KzGGDEkg.png)

2. 在專案的根目錄空白處以`cmd`開啟。

3. 創建虛擬環境 第一個`venv`是創建虛擬環境的指令 第二個`venv`是指虛擬環境的名字。
    ```
    py -m venv venv
    ```

4. 在IDE內選擇`venv`虛擬環境的Interpreter的路徑。
    ```
    ./venv/Scripts/python.exe
    ```

5. 回到專案根目錄。
    ```
    cd ../..
    ```
6. 在專案根目錄啟用虛擬環境並執行指令安裝`requirements.txt`指定的套件。
    ```
    pip install -r ./requirements.txt
    ```
