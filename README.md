# Telegram bot 農地調查照片上傳系統使用手冊

各位農地調查的夥伴大家好，因為我覺得農地環境照上傳之前再重新命名的時候很容易輸入錯誤，所以寫了一個可以在現場上傳照片的 Telegram 機器人。這份教學系統會讓你申請一個屬於你自己的 Telegram bot，然後將我寫好的執行檔直接在你自己的電腦當系統伺服器。雖然設定會有一點點小繁瑣，但不需要任何程式語言背景，也可以很方便的直接上傳照片，並且自動將照片命名完成。

## 1. 下載 Telegram app

建議你使用電腦操作，可以使用電腦使用網頁版 [Telegram](https://web.telegram.org/)，或者是下載[桌面版](https://desktop.telegram.org/)，沒有帳號的話可以很簡單申請一個。

但還是要去下載手機的 Telegram app，現場使用還是要用手機喔。

這邊我會用桌面版示範

## 2. 申請一個 Telegram bot
可以參考 [Telegram](https://core.telegram.org/bots) 官方的教學

1. 在搜尋欄搜尋 @botfather 並點選他按下 start 。
![](https://i.imgur.com/yz1UvVi.png)
![](https://i.imgur.com/6Wg88y6.png)

2. 輸入 /newbot 或者是直接按 BotFather 提供的指令
![](https://i.imgur.com/3iI8yjb.png)

3. 輸入你的機器人的名字，這便要輸入什麼都可以，例如我就先叫他 Chendada Demo Bot。
![](https://i.imgur.com/zWEYs4P.png)

4. 輸入機器人的 username，結尾一定要是 "bot"，例如我就用 chendada_demo_bot。

5. 這樣就申請成功囉！這時候 BotFather 會給你一組很像亂碼的東西，這串東西叫做 "token"，可以當作是跟 Telegram server 溝通獨一無二的鑰匙。<font color="#f00">請記住這串數字要自己記好，不可以外流，不然只要知道這串 toen，大家都可以使用你的機器人</font>
![](https://i.imgur.com/iIR1ph2.png)

## 3. 查看你的 chat_id

1. 搜尋 @userinfobot
![](https://i.imgur.com/H4MtqY7.png)

2. 一樣按 start 他就會告訴你你的 chat_id，就是那個 id。
![](https://i.imgur.com/Un9eXl7.png)

## 下載並執行 tg-farm-env-img-server.exe
[下載連結](https://drive.google.com/drive/folders/1dpXyW31bBHU9U48RzysWnFdahBVtNqfU?usp=sharing)

1. 執行 tg-farm-env-img-server.exe 檔案，依序輸入 token、chat_id 最後選擇特生提供的路線 kml 檔，不要選網格那一個喔。
![](https://i.imgur.com/K1JG8Ak.png)

![](https://i.imgur.com/2WtO88R.png)

![](https://i.imgur.com/I7sMsq5.png)

![](https://i.imgur.com/DiD4awN.png)

2. 輸入完之後 server 就成功運行囉！

![](https://i.imgur.com/9632qv7.png)

## 使用 Telegram 手機 app

1. 先依序拍好目前樣線 東 南 西 北 的照片。

2. 下載好手機 app 之後請在搜尋欄中搜尋你剛剛設定的機器人名字。

![](https://i.imgur.com/NFfX53k.png)

3. 一樣按下 start 開始上傳。之後要再上傳的話輸入 /start 就可以再上傳了。

![](https://i.imgur.com/8JSVzst.png)

4. 先分享一個你目前的點位，系統會依照你給的 kml 抓最近的點，意思就是你正在調查的樣線。

![](https://i.imgur.com/a3rlZN8.png)

![](https://i.imgur.com/eX3FWGe.png)

5. 依序上傳 東 南 西 北 的照片。

![](https://i.imgur.com/IhcSGTR.png)

![](https://i.imgur.com/292O6bL.png)

6. 按下上傳照片就會自動命名好，並且存到你的電腦囉！

![](https://i.imgur.com/M7AaYxb.png)

![](https://i.imgur.com/rF2gSyl.png)

![](https://i.imgur.com/I8H4Fz5.png)

## 使用 .txt 設定 token 跟 chat_id
如果不想要每次都輸入 token 跟 chat_id，可以像這樣建兩個 txt 文字檔，分別命名為 "token.txt" 跟 "chat_id.txt"，裡面寫剛剛的 token 跟 chat_id，且將路線的 kml 檔案命名為 "route.kml"。將這幾個檔跟 tg-farm-env-img-server.exe 放在同一個資料夾內，系統就會自動抓這幾個檔案的內容。

![](https://i.imgur.com/9oUKYRN.png)

![](https://i.imgur.com/JOfVQoE.png)

![](https://i.imgur.com/uu26eXi.png)
