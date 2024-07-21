# Quiz
您好，我是現任職於 Reno Studios 再現影像的朱晉毅 !
> 以下是測驗題目 *資料庫測驗* 與 *API 實作測驗* 的作答


## 資料庫測驗
### * 題目一
請寫出一條查詢語句 (SQL)，列出在 2023 年 5 月下訂的訂單，使用台幣付款且5月總金額最多的前 10 筆的旅宿 ID (bnb_id), 旅宿名稱 (bnb_name), 5 月總金額 (may_amount)
```SQL
SELECT 
    orders.bnb_id, 
    bnbs.name as bnb_name, 
    SUM(orders.amount) as amount_in_may
FROM 
    orders
JOIN 
    bnbs on orders.bnb_id = bnbs.id
WHERE 
    orders.created_at between '2023-05-01' and '2023-05-31'
    and orders.currency = 'TWD'
GROUP BY 
    orders.bnb_id, bnbs.name
ORDER BY 
    amount_in_may DESC
LIMIT 10;
```
### * 題目二
在題目一的執行下，我們發現 SQL 執行速度很慢，您會怎麼去優化？請闡述您怎麼判斷與優化的方式
```sql
逐一測試各別 WHERE 的搜尋條件搜尋時間，並為其加上 create index
如:
  create index idx_orders_created_at on orders (created_at);
```
## API 實作測驗
### * SOLID 原則
1. **單一職責原則 (Single Responsibility Principle)**:
   - `Validator` 類別負責驗證傳入值之合法性。
   - `FinanceInspector` 類別負責數值計算之相關函式。

2. **開放封閉原則 (Open/Closed Principle)**:
   - 透過新增 @staticmethod 到 `Validator` 和 `FinanceInspector` 類別來擴展功能，而不需要修改現有代碼。

3. **里氏替換原則 (Liskov Substitution Principle)**:
   - 各個驗證和轉換方法可以獨立替換、使用和抽離，而不影響 `processOrder` 函數的功能。( 需判斷幣種再行計算之功能除外 )

4. **介面隔離原則 (Interface Segregation Principle)**:
   - 將不同細節的驗證和轉換功能分離到不同的 @staticmethod 中。

### * 設計模式

1. **策略模式 (Strategy Pattern)**:
   - 先拆分目標至基礎，再根據小目標建立相同使用方式之函式，以達到方便管理、替換維護之效果。

## API 實作測驗之執行方式
### Requirement
[docker](https://www.docker.com/products/docker-desktop/)
### Installation ( Windows )
```bash
cd path_to\Quiz

docker build -t docker_quiz .
```
### Running unit test
```bash
docker run docker_quiz pytest
```
### Running docker
```bash
docker run -p 5000:5000 docker_quiz
```

