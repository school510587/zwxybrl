# 中文形義點字 (Zhong Wen Xing Yi Braille)

## 簡介

重度視障或全盲者，操作電腦、手機等 3C 裝置讀寫文字時，必須借助螢幕報讀軟體（如 NVDA 及旁白），
透過語音朗讀或點字輸出來讀取資訊。然而，無論透過聽讀或摸讀，他們只能透過讀音去理解文字，
以上下文的語詞組合判斷文意，導致漢字概念一直停留在讀音的程度，產生中文讀寫的困難。即使曾有
字形圖像概念的後天失明者，也因失明後文字閱讀所接收到的資訊只有讀音，漸漸淡忘了文字的奇妙構造。
被此限制，他們也只能使用注音輸入法，導致不斷打出同音異字，沒效率又容易出錯。

有感於此，為加強視障者的中文讀寫技能，我們設計了「形義點字」和「形義詞解」。「點字」和「字詞解釋」
（簡稱詞解）是螢幕報讀軟體提供使用者判斷是哪個字的方式，可是目前的注音點字與造詞為主寫成的詞解
（如「國家的國」），讓使用者幾乎沒機會接觸字形的概念。因此，我們的設計原理就是讓「點字」與「詞解」
呈現字形結構，使用者將不再被動忽略字形概念。

期待「形義點字」的摸讀，配合「形義詞解」的設計，讓視障者更能理解字形，拓展對文字的認知。而藉由自學
字形輸入法，擺脫注音輸入的困局，加強其文字編輯的技巧；還能與明眼人深入探討文字知識、增廣見聞；
甚至因此開發更多元的就學、就業機會與選擇。

使用開源軟體 NVDA, 引入形義點字之點顯器, 能讓您以點顯器閱讀形義點字。

## NVDA+形義點字之安裝方式
我們提供二種方式, 讓您依喜歡的方法, 使用形義點字。

* 方法一: 新手快速法: 直接下載完整壓縮包, 解開就可以用了。
* 方法二: 高手自訂法: 適合很熟悉NVDA的高手, 可以訂製自已的環境。

以下詳細說明:

### 方法一: 最簡單的方式: 下載我們打包好的壓縮檔
您可直接下載這裡的[形義點字NVDA 壓縮檔](http://molerat.net/~goad/ncb/ncb_nvda.7z)。
解壓後執行裡面的nvda.exe程式檔, 配合點顯器, 即可使用形義點字。

### 方法二: 自訂你專屬的NVDA
若您已自行安裝NVDA，可再套用形義點字相關表件，步驟如下：   
(適用於NVDA 2022.4)

https://raw.githubusercontent.com/school510587/zwxybrl/main/src/characterDescriptions.dic
https://raw.githubusercontent.com/school510587/zwxybrl/main/src/zz-tw-cldr.ctb
https://raw.githubusercontent.com/school510587/zwxybrl/main/src/zzh-tw---ncb_che.ctb

1. 安裝好 NVDA 請先到桌面「用右鍵」點NVDA捷徑，選擇「開啟檔案位置(I)」
2. 此時即打開 **「C:\Program Files (x86)\NVDA」** 這個資料夾。
3. 然後請下載這些檔案到以下的資料夾，並且覆蓋原有的檔案：
    1. 進行以下複製動作時, WINDOWS可能要求您:提供系統管理員權限, 請按「繼續」  
        同時您需要對該檔案選:右鍵/另存
    2. [characterDescriptions.dic](https://raw.githubusercontent.com/school510587/zwxybrl/main/src/characterDescriptions.dic)：   
        這是字詞解釋檔，請把這個檔案放到 **「locale\zh_TW」** 資料夾，  
        為與原「字詞解釋檔」的稱呼方式有所區別，日後我們將此檔案  
        稱為「形義詞解檔」。
    3. [zzh-tw---ncb_che.ctb](https://raw.githubusercontent.com/school510587/zwxybrl/main/src/zzh-tw---ncb_che.ctb)：   
        倉頡形義點字表，請將此檔案貼到  
        **「C:\Program Files (x86)\NVDA\louis\tables」**，  
        這才是形義點字表最主要的檔案。
    4. [zz-tw-cldr.ctb](https://raw.githubusercontent.com/school510587/zwxybrl/main/src/zz-tw-cldr.ctb)：  
        表情符號點字表。同樣也請貼到  
        **「C:\Program Files (x86)\NVDA\louis\tables」**  
        這個資料夾。

4. 完成以上檔案放到各自指定的資料夾之後, 才開始設定「引入」形義點字，  
    操作步驟如下：
5. 用記事本編輯 **「locale\zh_TW」** 資料夾中的 zh-tw.ctb 檔案：  
    請在該檔後方加入以下兩條指令：
    ```
    include zzh-tw---ncb_che.ctb # 引入形義點字表
    include zz-tw-cldr.ctb # 引入表情符號點字表
    ```
6. 請注意:
    - 您也可能要先以系統管理員權限開啟記事本, 才能修改本檔案。
    - 存檔編碼請選擇UTF-8, 以免發生亂碼
    - 存檔之後請重新啟動NVDA，正常情況，此時即可摸到形義碼。
    - 也就是各個注音點字之後都有了「以英文字母表示倉頡碼」的形義碼。

## 貢獻者

### 核心團隊

- 笑笑鴿 &lt;<crazy@mail.batol.net>&gt;
- Bo-Cheng Jhan &lt;<school510587@yahoo.com.tw>&gt;
- 黃靖騰 &lt;<hzt07120503@gmail.com>&gt;

### 其他貢獻者
