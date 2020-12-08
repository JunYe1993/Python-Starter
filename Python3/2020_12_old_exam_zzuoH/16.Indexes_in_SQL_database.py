# Question 1:
# Please explain usage and pros/cons of indexes in SQL database. 

# Question 2:
# Write a function
# which takes a string as input and return the string that has matched parentheses.
# The original string has non-matched parentheses Can you use constant place
# complexity to solve it? ex1. "so(m(e)t)hi)ng" should return "so(m(e)t)hing" ex2.
# "a(bcd(" should return "abcd" ex3. "))((" should return ""

# Answer 1
# If you want to find a piece of information that is within a large database. 
# To get this information out of the database the computer will look through every row until it finds it.
# If the table is sorted, it will be more faster to find that imformation.
# Indexes allow us to create sorted lists without having to create all new sorted tables
# , which would take up a lot of storage space.

### 適合使用索引
### 頻繁作為查詢條件的字段應該創建索引
### 多表查詢中與其它表進行關聯的字段,外鍵關係建立索引
### 單列索引/複合索引的選擇,高併發下傾向於創建複合索引
### 查詢中經常用來排序的字段
### 查詢中經常用來統計或者分組字段
###
### 不適合使用索引
### 頻繁更新的字段: 每次更新都會影響索引樹
### where條件查詢中用不到的字段
### 表記錄太少
### 經常增刪改的表: 更新了表,索引也得更新才行
### 注意: 如果一張表中,重複的記錄非常多,為它建立索引就沒有太大意義

### https://dataschool.com/sql-optimization/how-indexing-works/
### https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/689476/