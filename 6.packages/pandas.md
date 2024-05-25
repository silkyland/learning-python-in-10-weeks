# Pandas

Pandas (Python Data Analysis Library) เป็น open-source library ใน Python ที่ใช้สำหรับการจัดการและวิเคราะห์ข้อมูล โดยเฉพาะอย่างยิ่งข้อมูลที่อยู่ในรูปแบบตาราง (tabular data) และ time series data

Pandas ถูกพัฒนาขึ้นมาเพื่อช่วยให้การทำงานกับข้อมูลใน Python เป็นไปได้อย่างมีประสิทธิภาพและง่ายดายขึ้น โดยมีเป้าหมายหลักเพื่อนำเสนอโครงสร้างข้อมูลที่ยืดหยุ่นและเครื่องมือที่หลากหลายสำหรับการวิเคราะห์ข้อมูลแบบต่างๆ

โครงสร้างข้อมูลหลักใน Pandas มีสองประเภท ได้แก่:

1. Series: อาร์เรย์ 1 มิติที่สามารถเก็บข้อมูลประเภทต่างๆ (เช่น integers, floats, strings) และมี index กำกับ

2. DataFrame: โครงสร้างข้อมูลแบบ 2 มิติคล้ายตาราง ประกอบด้วยแถวและคอลัมน์ โดยแต่ละคอลัมน์เป็น Series

นอกจากนี้ Pandas ยังมีฟังก์ชันและเมธอดต่างๆมากมายในการจัดการและปรับแต่งข้อมูล เช่น การกรองข้อมูล การสร้างคอลัมน์ใหม่ การรวมตาราง การจัดกลุ่มและสรุปข้อมูล และอื่นๆ ทำให้สะดวกต่อการทำความสะอาด จัดระเบียบ และวิเคราะห์ข้อมูลอย่างมีประสิทธิภาพ

ด้วยความสามารถที่หลากหลายและใช้งานง่าย Pandas จึงกลายเป็นเครื่องมือยอดนิยมสำหรับนักวิทยาศาสตร์ข้อมูล นักวิเคราะห์ และผู้ที่ทำงานด้านข้อมูลในภาษา Python

### 1.การสร้าง Series และ DataFrame

การสร้าง Series และ DataFrame เป็นหัวข้อแรกและพื้นฐานที่สำคัญในการทำงานกับ Pandas ใน Python มาดูรายละเอียดและตัวอย่างของแต่ละส่วนกัน

1. Series
   Series คืออาร์เรย์ 1 มิติที่สามารถเก็บข้อมูลประเภทต่างๆ เช่น integers, floats และ strings โดยมี index (ป้ายชื่อ) สำหรับแต่ละเอลิเมนต์ สามารถสร้าง Series ได้โดยใช้ pd.Series() และส่งอาร์กิวเมนต์เป็นลิสต์หรือ NumPy array ดังตัวอย่าง:

```python
import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)
```

ผลลัพธ์:

```
0    1
1    2
2    3
3    4
4    5
dtype: int64
```

นอกจากนี้ยังสามารถกำหนด index ให้กับ Series ได้ดังนี้:

```python
data = [1, 2, 3, 4, 5]
labels = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=labels)
print(series)
```

ผลลัพธ์:

```
a    1
b    2
c    3
d    4
e    5
dtype: int64
```

2. DataFrame
   DataFrame เป็นโครงสร้างข้อมูลแบบ 2 มิติ ประกอบด้วยแถวและคอลัมน์เหมือนตาราง แต่ละคอลัมน์เป็น Series ที่มี index ร่วมกัน DataFrame จึงเหมาะสำหรับเก็บข้อมูลที่มีหลายตัวแปรหรือฟีลด์ สามารถสร้าง DataFrame ได้โดยใช้ pd.DataFrame() และส่งอาร์กิวเมนต์เป็น dictionary ของลิสต์ หรือ dictionary ของ Series ดังตัวอย่าง:

```python
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print(df)
```

ผลลัพธ์:

```
      name  age      city
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
3    David   40     Tokyo
```

สามารถกำหนด index ให้กับ DataFrame ได้เช่นเดียวกับ Series:

```python
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df)
```

ผลลัพธ์:

```
       name  age      city
a    Alice   25  New York
b      Bob   30    London
c  Charlie   35     Paris
d    David   40     Tokyo
```

การสร้าง Series และ DataFrame เป็นพื้นฐานสำคัญในการทำงานกับข้อมูลใน Pandas เมื่อสร้างแล้วจะสามารถใช้ฟังก์ชันและเมธอดต่างๆ ของ Pandas ในการเลือก แก้ไข และวิเคราะห์ข้อมูลได้อย่างมีประสิทธิภาพ

### 2. การอ่านและเขียนข้อมูลจากไฟล์ต่างๆ เช่น CSV, Excel, SQL databases

Pandas มีฟังก์ชันในการอ่านและเขียนข้อมูลจากไฟล์หลากหลายรูปแบบ ทำให้สะดวกในการนำเข้าและส่งออกข้อมูลระหว่าง Pandas กับแหล่งข้อมูลภายนอก มาดูตัวอย่างการใช้งานกัน

1. CSV (Comma-Separated Values)

- การอ่านไฟล์ CSV:

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```

- การเขียนไฟล์ CSV:

```python
df.to_csv('output.csv', index=False)
```

2. Excel

- การอ่านไฟล์ Excel:

```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(df.head())
```

- การเขียนไฟล์ Excel:

```python
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
```

3. SQL Databases

- การเชื่อมต่อและอ่านข้อมูลจาก SQL database (ตัวอย่างใช้ SQLite):

```python
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM table_name", conn)
print(df.head())
```

- การเขียนข้อมูลลงใน SQL database:

```python
df.to_sql('table_name', conn, if_exists='replace', index=False)
```

นอกจากนี้ Pandas ยังรองรับการอ่านและเขียนข้อมูลจากไฟล์ประเภทอื่นๆ เช่น JSON, HTML, HDFStore, Feather เป็นต้น

ข้อควรระวังในการอ่านและเขียนไฟล์ คือการตั้งค่าพารามิเตอร์ต่างๆ ให้เหมาะสม เช่น delimiter (ตัวคั่นข้อมูล), encoding (รูปแบบการเข้ารหัสอักขระ), header (การระบุแถวที่เป็นหัวตาราง), index_col (คอลัมน์ที่ใช้เป็น index) และ na_values (ค่าที่ถือเป็น missing data) เป็นต้น เพื่อให้ Pandas สามารถอ่านและเขียนข้อมูลได้อย่างถูกต้อง

การอ่านและเขียนข้อมูลเป็นขั้นตอนสำคัญในการทำงานกับข้อมูลจริง ซึ่ง Pandas ช่วยให้การนำเข้าและส่งออกข้อมูลเป็นเรื่องง่ายและมีประสิทธิภาพ

### 3.การเลือกและกรองข้อมูลโดยใช้ indexing และ slicing

การเลือกและกรองข้อมูลเป็นหนึ่งในการทำงานหลักกับ DataFrame ใน Pandas ซึ่งมีวิธีการหลายแบบในการเลือกข้อมูลที่ต้องการ เช่น การใช้ index, boolean indexing และ conditional selection มาดูตัวอย่างแต่ละวิธีกัน

สมมติเรามี DataFrame ดังนี้:

```python
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)
print(df)
```

ผลลัพธ์:

```
     name  age      city
0   Alice   25  New York
1     Bob   30    London
2Charlie   35     Paris
3   David   40     Tokyo
4     Eve   45    Sydney
```

1. การเลือกข้อมูลโดยใช้ index และ column names:

- เลือกคอลัมน์เดียว:

```python
print(df['name'])
```

- เลือกหลายคอลัมน์:

```python
print(df[['name', 'age']])
```

- เลือกแถวโดยใช้ index:

```python
print(df.loc[0]) # เลือกแถวแรก
print(df.iloc[1:4]) # เลือกแถวที่ 2-4
```

2. Boolean indexing:

- เลือกแถวที่ตรงกับเงื่อนไข:

```python
print(df[df['age'] > 30])
```

- เลือกแถวที่ตรงกับหลายเงื่อนไข:

```python
print(df[(df['age'] > 30) & (df['city'] == 'Paris')])
```

3. Conditional selection:

- เลือกค่าตามเงื่อนไข:

```python
print(df.loc[df['age'] > 30, 'name'])
```

- เลือกแถวและคอลัมน์ตามเงื่อนไข:

```python
print(df.loc[df['age'] > 30, ['name', 'city']])
```

การเลือกและกรองข้อมูลเป็นทักษะสำคัญในการทำงานกับข้อมูลขนาดใหญ่ ช่วยให้เราสามารถเลือกเฉพาะส่วนที่สนใจมาวิเคราะห์ได้อย่างมีประสิทธิภาพ Pandas มีเครื่องมือที่หลากหลายและยืดหยุ่นสำหรับการเลือกและกรองข้อมูล ซึ่งเป็นพื้นฐานสำคัญในการทำความเข้าใจและจัดการกับข้อมูล

### 4.การจัดการ missing data

ในการทำงานกับข้อมูลจริง เราหลีกเลี่ยงไม่ได้ที่จะพบกับปัญหา missing data หรือข้อมูลที่ขาดหายไป ซึ่งอาจเกิดจากหลายสาเหตุ เช่น การเก็บข้อมูลผิดพลาด ข้อมูลไม่สมบูรณ์ หรือไม่มีข้อมูลในบางช่วงเวลา Pandas มีเครื่องมือและเทคนิคที่หลากหลายในการจัดการกับ missing data มาดูตัวอย่างกัน

สมมติเรามี DataFrame ที่มี missing data ดังนี้:

```python
import numpy as np
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, np.nan, 35, np.nan, 45],
    'city': ['New York', 'London', None, 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)
print(df)
```

ผลลัพธ์:

```
     name   age      city
0   Alice  25.0  New York
1     Bob   NaN    London
2Charlie  35.0      None
3   David   NaN     Tokyo
4     Eve  45.0    Sydney
```

1. การตรวจสอบ missing data:

- ตรวจสอบค่า null หรือ NaN ในแต่ละคอลัมน์:

```python
print(df.isnull().sum())
```

- ตรวจสอบแถวที่มี missing data:

```python
print(df[df.isnull().any(axis=1)])
```

2. การลบแถวหรือคอลัมน์ที่มี missing data:

- ลบแถวที่มี missing data:

```python
print(df.dropna())
```

- ลบคอลัมน์ที่มี missing data:

```python
print(df.dropna(axis=1))
```

3. การแทนค่า missing data:

- แทนด้วยค่าคงที่:

```python
print(df.fillna(0))
```

- แทนด้วยค่าเฉลี่ยของคอลัมน์:

```python
print(df.fillna(df.mean()))
```

- แทนด้วยค่าก่อนหน้าหรือถัดไป (forward/backward fill):

```python
print(df.fillna(method='ffill'))
print(df.fillna(method='bfill'))
```

การจัดการ missing data เป็นขั้นตอนสำคัญในการเตรียมและทำความสะอาดข้อมูลก่อนการวิเคราะห์ ซึ่งมีผลต่อคุณภาพและความน่าเชื่อถือของผลการวิเคราะห์ การเลือกวิธีการจัดการที่เหมาะสมขึ้นอยู่กับบริบทของข้อมูลและเป้าหมายของการวิเคราะห์ Pandas มีเครื่องมือที่ยืดหยุ่นและหลากหลายในการจัดการ missing data ช่วยให้เราสามารถจัดการกับปัญหานี้ได้อย่างมีประสิทธิภาพ

### 5. การสร้างและจัดการ datetime data

ในการวิเคราะห์ข้อมูล เรามักจะต้องทำงานกับข้อมูลที่เกี่ยวข้องกับวันที่และเวลา เช่น ข้อมูลการซื้อขาย ข้อมูลการเข้าใช้งานเว็บไซต์ หรือข้อมูลสภาพอากาศ Pandas มีเครื่องมือที่มีประสิทธิภาพในการจัดการกับข้อมูลประเภท datetime มาดูตัวอย่างการทำงานกัน

1. การสร้าง datetime Series หรือ column:

- สร้าง datetime Series จาก string:

```python
import pandas as pd

dates = pd.Series(['2023-01-01', '2023-01-02', '2023-01-03'])
dt_series = pd.to_datetime(dates)
print(dt_series)
```

- สร้าง datetime column ใน DataFrame:

```python
data = {'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'value': [100, 200, 300]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)
```

2. การดึงค่าต่างๆ จาก datetime Series:

- ดึงปี เดือน วัน:

```python
print(dt_series.dt.year)
print(dt_series.dt.month)
print(dt_series.dt.day)
```

- ดึงชื่อวันในสัปดาห์ และชื่อเดือน:

```python
print(dt_series.dt.day_name())
print(dt_series.dt.month_name())
```

3. การเลือกข้อมูลตามเงื่อนไขของวันที่และเวลา:

- เลือกข้อมูลตามช่วงวันที่:

```python
print(df[(df['date'] >= '2023-01-01') & (df['date'] <= '2023-01-02')])
```

- เลือกข้อมูลตามปีหรือเดือน:

```python
print(df[df['date'].dt.year == 2023])
print(df[df['date'].dt.month == 1])
```

4. การคำนวณและจัดการช่วงเวลา:

- คำนวณระยะเวลาระหว่างวันที่:

```python
delta = df['date'].max() - df['date'].min()
print(delta)
```

- เลื่อนวันที่ไปข้างหน้าหรือย้อนหลัง:

```python
print(df['date'] + pd.Timedelta(days=1))
print(df['date'] - pd.Timedelta(weeks=1))
```

การทำงานกับข้อมูล datetime อย่างมีประสิทธิภาพเป็นสิ่งสำคัญในหลายโดเมน เช่น การวิเคราะห์อนุกรมเวลา (time series analysis) การตรวจจับเหตุการณ์ผิดปกติ หรือการสร้างรายงานตามช่วงเวลา Pandas มีฟีเจอร์ที่ครอบคลุมและใช้งานง่ายในการจัดการข้อมูล datetime ช่วยให้เราสามารถวิเคราะห์และสร้างข้อมูลเชิงลึกจากข้อมูลที่เกี่ยวข้องกับเวลาได้อย่างมีประสิทธิภาพ

### 6. การรวมและเชื่อมต่อ DataFrames (concatenation และ merging)

ในการวิเคราะห์ข้อมูล เรามักจะต้องรวมข้อมูลจากหลายแหล่งเข้าด้วยกัน เพื่อให้ได้ชุดข้อมูลที่สมบูรณ์และพร้อมสำหรับการวิเคราะห์ Pandas มีฟังก์ชันที่มีประสิทธิภาพในการรวมและเชื่อมต่อ DataFrames เข้าด้วยกัน มาดูตัวอย่างการใช้งานกัน

สมมติเรามี DataFrames สองชุดดังนี้:

```python
import pandas as pd

data1 = {'A': ['A0', 'A1', 'A2'],
         'B': ['B0', 'B1', 'B2']}
df1 = pd.DataFrame(data1)

data2 = {'A': ['A3', 'A4', 'A5'],
         'B': ['B3', 'B4', 'B5']}
df2 = pd.DataFrame(data2)
```

1. การต่อ DataFrames ในแนวแกน (concatenation):

- ต่อ DataFrames ในแนวแกน 0 (แถว):

```python
concat_df = pd.concat([df1, df2])
print(concat_df)
```

- ต่อ DataFrames ในแนวแกน 1 (คอลัมน์):

```python
concat_df = pd.concat([df1, df2], axis=1)
print(concat_df)
```

2. การรวม DataFrames ตามคอลัมน์ที่กำหนด (merging):
   สมมติเรามี DataFrames สองชุดที่มีคอลัมน์ร่วมกัน:

```python
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'A': ['A0', 'A1', 'A2', 'A3']}
df1 = pd.DataFrame(data1)

data2 = {'key': ['K0', 'K1', 'K4', 'K5'],
         'B': ['B0', 'B1', 'B4', 'B5']}
df2 = pd.DataFrame(data2)
```

- รวม DataFrames ตามคอลัมน์ 'key':

```python
merged_df = pd.merge(df1, df2, on='key')
print(merged_df)
```

- รวม DataFrames ตามคอลัมน์ 'key' และเก็บแถวที่ไม่มีข้อมูลตรงกัน:

```python
merged_df = pd.merge(df1, df2, on='key', how='outer')
print(merged_df)
```

- รวม DataFrames ตามคอลัมน์ 'key' และเก็บแถวที่มีข้อมูลตรงกันใน DataFrame ทางซ้าย:

```python
merged_df = pd.merge(df1, df2, on='key', how='left')
print(merged_df)
```

การรวมและเชื่อมต่อ DataFrames เป็นทักษะสำคัญในการทำงานกับข้อมูลจริง ที่มักจะมาจากหลายแหล่งและมีรูปแบบที่แตกต่างกัน Pandas มีฟังก์ชันที่ยืดหยุ่นและมีประสิทธิภาพในการจัดการกับเรื่องนี้ ช่วยให้เราสามารถรวมและเชื่อมต่อข้อมูลได้อย่างง่ายดายและรวดเร็ว เพื่อให้ได้ชุดข้อมูลที่สมบูรณ์และพร้อมสำหรับการวิเคราะห์ต่อไป

### 7 การจัดกลุ่มและรวมข้อมูล (grouping และ aggregation)

ในการวิเคราะห์ข้อมูล เรามักจะต้องการสรุปหรือรวมข้อมูลตามกลุ่มที่กำหนด เพื่อให้เห็นภาพรวมหรือเปรียบเทียบระหว่างกลุ่มต่างๆ Pandas มีเครื่องมือที่มีประสิทธิภาพในการจัดกลุ่มและรวมข้อมูล ด้วยฟังก์ชัน `groupby()` และเมท็อดต่างๆ ที่ใช้ในการรวมข้อมูล มาดูตัวอย่างการใช้งานกัน

สมมติเรามี DataFrame ของยอดขายสินค้าดังนี้:

```python
import pandas as pd

data = {'product': ['A', 'B', 'C', 'A', 'B', 'C'],
        'store': ['X', 'X', 'X', 'Y', 'Y', 'Y'],
        'sales': [100, 200, 150, 120, 180, 200]}
df = pd.DataFrame(data)
print(df)
```

1. การจัดกลุ่มข้อมูลด้วย `groupby()`:

- จัดกลุ่มตามคอลัมน์ 'store':

```python
store_group = df.groupby('store')
print(store_group)
```

- จัดกลุ่มตามหลายคอลัมน์:

```python
store_product_group = df.groupby(['store', 'product'])
print(store_product_group)
```

2. การรวมข้อมูลด้วยฟังก์ชันต่างๆ:

- รวมข้อมูลด้วยฟังก์ชัน `sum()`:

```python
sales_sum = df.groupby('store')['sales'].sum()
print(sales_sum)
```

- รวมข้อมูลด้วยฟังก์ชัน `mean()`:

```python
sales_mean = df.groupby('store')['sales'].mean()
print(sales_mean)
```

- รวมข้อมูลด้วยฟังก์ชัน `agg()` และกำหนดหลายฟังก์ชัน:

```python
sales_stats = df.groupby('store')['sales'].agg(['sum', 'mean', 'min', 'max'])
print(sales_stats)
```

3. การกรองข้อมูลหลังจากจัดกลุ่ม:

- กรองกลุ่มที่มียอดขายรวมมากกว่า 300:

```python
high_sales_stores = df.groupby('store')['sales'].sum()
high_sales_stores = high_sales_stores[high_sales_stores > 300]
print(high_sales_stores)
```

การจัดกลุ่มและรวมข้อมูลเป็นหนึ่งในการทำงานที่สำคัญและใช้บ่อยที่สุดในการวิเคราะห์ข้อมูล ช่วยให้เราสามารถสรุปข้อมูลในระดับที่ต้องการ และเปรียบเทียบระหว่างกลุ่มต่างๆ ได้อย่างมีประสิทธิภาพ Pandas มีฟังก์ชัน `groupby()` ที่ยืดหยุ่นและใช้งานง่าย ร่วมกับฟังก์ชันรวมข้อมูลที่หลากหลาย ช่วยให้เราสามารถจัดกลุ่มและรวมข้อมูลได้ตามความต้องการ และนำไปใช้ในการวิเคราะห์และสร้างข้อมูลเชิงลึกต่อไป

### 8 การ reshape ข้อมูลด้วย pivoting, melting, stacking และ unstacking

ในการวิเคราะห์ข้อมูล บางครั้งเราอาจต้องการ reshape ข้อมูลให้อยู่ในรูปแบบที่เหมาะสมกับการวิเคราะห์หรือนำเสนอ Pandas มีฟังก์ชันต่างๆ ที่ช่วยให้เราสามารถ reshape ข้อมูลได้อย่างยืดหยุ่นและมีประสิทธิภาพ มาดูตัวอย่างการใช้งานกันครับ

สมมติเรามี DataFrame ของยอดขายสินค้าแยกตามปีและไตรมาสดังนี้:

```python
import pandas as pd

data = {'year': [2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022],
        'quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
        'sales': [100, 120, 130, 150, 110, 130, 140, 160]}
df = pd.DataFrame(data)
print(df)
```

1. การ reshape ข้อมูลด้วย `pivot()`:

- สร้าง pivot table โดยใช้คอลัมน์ 'year' เป็น index และคอลัมน์ 'quarter' เป็น columns:

```python
pivot_df = df.pivot(index='year', columns='quarter', values='sales')
print(pivot_df)
```

2. การ reshape ข้อมูลด้วย `melt()`:

- แปลง pivot table กลับเป็น DataFrame แบบเดิมด้วย `melt()`:

```python
melted_df = pivot_df.reset_index().melt(id_vars='year', var_name='quarter', value_name='sales')
print(melted_df)
```

3. การ reshape ข้อมูลด้วย `stack()` และ `unstack()`:

- ใช้ `stack()` เพื่อแปลง DataFrame ให้เป็น Series ที่มี MultiIndex:

```python
stacked_df = df.set_index(['year', 'quarter']).stack()
print(stacked_df)
```

- ใช้ `unstack()` เพื่อแปลง Series กลับเป็น DataFrame:

```python
unstacked_df = stacked_df.unstack()
print(unstacked_df)
```

การ reshape ข้อมูลเป็นทักษะสำคัญในการจัดการและวิเคราะห์ข้อมูล เพราะข้อมูลที่มีรูปแบบเหมาะสมจะช่วยให้การวิเคราะห์และนำเสนอข้อมูลเป็นไปได้อย่างมีประสิทธิภาพ Pandas มีฟังก์ชันอย่าง `pivot()`, `melt()`, `stack()` และ `unstack()` ที่ช่วยให้เราสามารถ reshape ข้อมูลได้ตามความต้องการ ทำให้การทำงานกับข้อมูลในรูปแบบต่างๆ เป็นเรื่องที่ง่ายและสะดวกยิ่งขึ้น

### 9 การใช้ string methods กับข้อมูลประเภท string

ในการทำงานกับข้อมูล เรามักจะต้องจัดการกับข้อมูลประเภท string เช่น การแยกหรือรวมคำ การแทนที่หรือลบอักขระ หรือการสร้างคอลัมน์ใหม่จากคอลัมน์ที่เป็น string Pandas มี string methods ที่หลากหลายและใช้งานง่าย ช่วยให้เราสามารถจัดการกับข้อมูลประเภท string ได้อย่างมีประสิทธิภาพ มาดูตัวอย่างการใช้งานกัน

สมมติเรามี DataFrame ของข้อมูลพนักงานดังนี้:

```python
import pandas as pd

data = {'name': ['John Doe', 'Jane Doe', 'John Smith', 'Jane Smith'],
        'email': ['john.doe@example.com', 'jane.doe@example.com', 'john.smith@example.com', 'jane.smith@example.com']}
df = pd.DataFrame(data)
print(df)
```

1. การแยกคำหรืออักขระด้วย `split()`:

- สร้างคอลัมน์ 'first_name' และ 'last_name' จากการแยกคำในคอลัมน์ 'name':

```python
df[['first_name', 'last_name']] = df['name'].str.split(' ', expand=True)
print(df)
```

2. การรวมคำหรืออักขระด้วย `cat()`:

- สร้างคอลัมน์ 'username' จากการรวมคำในคอลัมน์ 'first_name' และ 'last_name':

```python
df['username'] = df['first_name'].str.cat(df['last_name'], sep='_').str.lower()
print(df)
```

3. การแทนที่อักขระหรือลำดับอักขระด้วย `replace()`:

- แทนที่อักขระ '.' ในคอลัมน์ 'email' ด้วย '\_':

```python
df['email'] = df['email'].str.replace('.', '_')
print(df)
```

4. การตรวจสอบว่ามีลำดับอักขระใดๆ ปรากฏในสตริงหรือไม่ด้วย `contains()`:

- ตรวจสอบว่าคอลัมน์ 'email' มี '@example.com' หรือไม่:

```python
mask = df['email'].str.contains('@example.com')
print(df[mask])
```

การใช้ string methods ใน Pandas ช่วยให้เราสามารถจัดการกับข้อมูลประเภท string ได้อย่างสะดวกและมีประสิทธิภาพ ไม่ว่าจะเป็นการสร้างคอลัมน์ใหม่ การแยกหรือรวมคำ การแทนที่หรือลบอักขระ หรือการตรวจสอบเงื่อนไขต่างๆ ในข้อมูล string methods เป็นเครื่องมือที่มีประโยชน์อย่างยิ่งในการทำความสะอาดและเตรียมข้อมูลก่อนการวิเคราะห์

### การวาดกราฟและ data visualization

การวาดกราฟและ data visualization เป็นส่วนสำคัญในการวิเคราะห์และนำเสนอข้อมูล ช่วยให้เราสามารถสื่อสารข้อมูลเชิงลึกและแสดงความสัมพันธ์ระหว่างตัวแปรต่างๆ ได้อย่างชัดเจน Pandas มีความสามารถในการวาดกราฟและ data visualization ในตัวโดยใช้ matplotlib ทำให้สะดวกในการสร้างกราฟจาก DataFrame หรือ Series มาดูตัวอย่างการใช้งานกัน

สมมติเรามี DataFrame ของยอดขายรายเดือนดังนี้:

```python
import pandas as pd

data = {'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'sales': [100, 120, 150, 200, 180]}
df = pd.DataFrame(data)
print(df)
```

1. การวาดกราฟเส้น (line plot):

- สร้างกราฟเส้นของยอดขายรายเดือน:

```python
df.plot(x='month', y='sales', kind='line')
```

2. การวาดกราฟแท่ง (bar plot):

- สร้างกราฟแท่งของยอดขายรายเดือน:

```python
df.plot(x='month', y='sales', kind='bar')
```

3. การวาดกราฟวงกลม (pie chart):

- สร้างกราฟวงกลมของยอดขายรายเดือน:

```python
df.set_index('month')['sales'].plot(kind='pie', autopct='%1.1f%%')
```

4. การวาดกราฟการกระจาย (scatter plot) ระหว่างสองตัวแปร:

- สมมติเรามีข้อมูลความสัมพันธ์ระหว่างอายุและรายได้:

```python
data = {'age': [25, 30, 35, 40, 45],
        'income': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)
df.plot(x='age', y='income', kind='scatter')
```

นอกจากนี้ เรายังสามารถปรับแต่งรูปแบบของกราฟ เช่น สี ขนาด ป้ายกำกับ และชื่อแกนต่างๆ ได้ตามต้องการ การวาดกราฟและ data visualization ใน Pandas ช่วยให้เราสามารถสำรวจและทำความเข้าใจข้อมูลได้ง่ายขึ้น รวมทั้งนำเสนอข้อมูลได้อย่างมีประสิทธิภาพ

อย่างไรก็ตาม สำหรับกราฟที่ซับซ้อนหรือต้องการควบคุมรูปแบบอย่างละเอียด เราอาจต้องใช้ matplotlib หรือ seaborn โดยตรงเพื่อสร้างกราฟ โดยใช้ Pandas ร่วมกับไลบรารีเหล่านี้ในการเตรียมและจัดการข้อมูลสำหรับการวาดกราฟ

### 11 การใช้ Pandas กับ time series data

Time series data หรือข้อมูลอนุกรมเวลา เป็นข้อมูลที่มีการบันทึกค่าตามลำดับเวลา เช่น ราคาหุ้นรายวัน ยอดขายรายเดือน หรือปริมาณฝนรายปี การวิเคราะห์ time series data มีความสำคัญในหลายสาขา เช่น การเงิน เศรษฐศาสตร์ และการพยากรณ์ Pandas มีเครื่องมือและฟังก์ชันที่ออกแบบมาเพื่อทำงานกับ time series data โดยเฉพาะ ทำให้สะดวกในการจัดการและวิเคราะห์ข้อมูลประเภทนี้ มาดูตัวอย่างการใช้งานกัน

สมมติเรามีข้อมูลราคาปิดรายวันของหุ้นดังนี้:

```python
import pandas as pd

data = {'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'close': [100, 110, 105, 115, 120]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
print(df)
```

1. การกำหนด datetime index:

- กำหนดคอลัมน์ 'date' เป็น index ของ DataFrame:

```python
df = df.set_index('date')
print(df)
```

2. การเลือกข้อมูลตามช่วงเวลา:

- เลือกข้อมูลระหว่างวันที่ 2023-01-02 ถึง 2023-01-04:

```python
print(df.loc['2023-01-02':'2023-01-04'])
```

3. การ resample ข้อมูล:

- ลดความถี่ข้อมูลจากรายวันเป็นรายสัปดาห์:

```python
weekly_df = df.resample('W').last()
print(weekly_df)
```

4. การเลื่อนข้อมูล (shift) และการคำนวณผลต่าง:

- คำนวณผลต่างของราคาปิดเทียบกับวันก่อนหน้า:

```python
df['diff'] = df['close'].diff()
print(df)
```

5. การคำนวณค่าเฉลี่ยเคลื่อนที่ (rolling mean):

- คำนวณค่าเฉลี่ยเคลื่อนที่ของราคาปิดในช่วง 3 วัน:

```python
df['rolling_mean'] = df['close'].rolling(window=3).mean()
print(df)
```

การใช้ Pandas กับ time series data ช่วยให้เราสามารถจัดการและวิเคราะห์ข้อมูลอนุกรมเวลาได้อย่างมีประสิทธิภาพ ไม่ว่าจะเป็นการกำหนด datetime index การเลือกข้อมูลตามช่วงเวลา การ resample ข้อมูล การคำนวณผลต่างและค่าเฉลี่ยเคลื่อนที่ และอื่นๆ ฟีเจอร์เหล่านี้ทำให้การทำงานกับ time series data ใน Pandas เป็นเรื่องง่ายและสะดวกยิ่งขึ้น

### 12 Performance optimization และ best practices

การทำงานกับข้อมูลขนาดใหญ่ใน Pandas อาจต้องใช้ทรัพยากรของเครื่องคอมพิวเตอร์สูง ดังนั้นการเพิ่มประสิทธิภาพในการประมวลผลและการปฏิบัติตาม best practices จึงเป็นสิ่งสำคัญ เพื่อให้การทำงานกับข้อมูลเป็นไปอย่างรวดเร็วและมีประสิทธิภาพ มาดูเทคนิคและข้อแนะนำบางส่วนในการปรับปรุง performance และปฏิบัติตาม best practices ใน Pandas กัน

1. การใช้ `vectorization` แทนการวนลูป:

- ใช้ `vectorized operations` เช่น การใช้ `apply()`, `map()`, `applymap()` แทนการเขียนลูปด้วย `iterrows()` หรือ `itertuples()` เพื่อเพิ่มความเร็วในการประมวลผล

2. การเลือกใช้ `data types` ที่เหมาะสม:

- เลือกใช้ `data types` ที่เหมาะสมกับข้อมูลแต่ละประเภท เช่น การใช้ `int` แทน `float` เมื่อเป็นไปได้ เพื่อประหยัดหน่วยความจำ
- ใช้ `Categorical` data type สำหรับข้อมูลที่มีค่าซ้ำกันมาก เพื่อลดการใช้หน่วยความจำ

3. การลด memory usage ด้วย `downcast`:

- ใช้ `downcast` เพื่อลดขนาดของ `data types` ลงตามความเหมาะสม เช่น การ `downcast` จาก `int64` เป็น `int8` เมื่อค่าในคอลัมน์ไม่เกินขอบเขตของ `int8`

4. การใช้ `chunk` สำหรับข้อมูลขนาดใหญ่:

- ใช้เทคนิค `chunking` โดยแบ่งข้อมูลขนาดใหญ่ออกเป็นส่วนๆ และประมวลผลทีละส่วน เพื่อลดการใช้หน่วยความจำ

5. การใช้ libraries อื่นๆ เพื่อเพิ่มประสิทธิภาพ:

- ใช้ libraries เช่น `NumPy` และ `Numba` ในการเร่งความเร็วของการคำนวณทางคณิตศาสตร์
- ใช้ `Cython` หรือ `Numba` ในการเขียน `custom functions` ที่ต้องการประสิทธิภาพสูง

6. การใช้ `built-in functions` และ `methods` ของ Pandas:

- ใช้ `built-in functions` และ `methods` ของ Pandas ให้เป็นประโยชน์ เพราะส่วนใหญ่ได้รับการออกแบบมาให้มีประสิทธิภาพสูง เช่น การใช้ `value_counts()` ในการนับจำนวนค่าที่ซ้ำกัน หรือการใช้ `read_csv()` ในการอ่านไฟล์ CSV แทนการเขียนโค้ดเอง

นอกจากนี้ การทำความเข้าใจกับโครงสร้างข้อมูลและ APIs ของ Pandas รวมถึงการออกแบบและวางแผนขั้นตอนการประมวลผลข้อมูลอย่างเหมาะสม ก็เป็นส่วนสำคัญในการพัฒนาโค้ดที่มีประสิทธิภาพและง่ายต่อการบำรุงรักษา

การปรับปรุง performance และการปฏิบัติตาม best practices อาจต้องอาศัยประสบการณ์และความเข้าใจในระบบของเราเอง อย่างไรก็ตาม Pandas และ community ของ Pandas ได้ให้คำแนะนำและตัวอย่างที่เป็นประโยชน์มากมาย ซึ่งสามารถนำมาปรับใช้ให้เข้ากับบริบทและความต้องการของเราได้

### 13 รวบรวมฟังก์ชั่นการใช้งานที่เป็นประโยชน์ใน Pandas

1. การอ่านและเขียนไฟล์:

- `pd.read_csv()`: อ่านไฟล์ CSV เข้ามาเป็น DataFrame
- `pd.read_excel()`: อ่านไฟล์ Excel เข้ามาเป็น DataFrame
- `df.to_csv()`: เขียน DataFrame ไปเป็นไฟล์ CSV
- `df.to_excel()`: เขียน DataFrame ไปเป็นไฟล์ Excel

ตัวอย่าง:

```python
import pandas as pd

# อ่านไฟล์ CSV
df = pd.read_csv('data.csv')

# เขียน DataFrame ไปเป็นไฟล์ Excel
df.to_excel('output.xlsx', index=False)
```

2. การเลือกข้อมูล:

- `df.loc[]`: เลือกข้อมูลตามดัชนีหรือเงื่อนไข
- `df.iloc[]`: เลือกข้อมูลตามตำแหน่งของแถวและคอลัมน์
- `df['column_name']`: เลือกคอลัมน์ตามชื่อ

ตัวอย่าง:

```python
# เลือกแถวที่มีค่า 'A' ในคอลัมน์ 'category'
selected_rows = df.loc[df['category'] == 'A']

# เลือกแถวที่ 0 ถึง 4 และคอลัมน์ที่ 1 ถึง 3
selected_data = df.iloc[0:5, 1:4]
```

3. การสร้างคอลัมน์ใหม่:

- `df['new_column'] = ...`: สร้างคอลัมน์ใหม่และกำหนดค่า

ตัวอย่าง:

```python
# สร้างคอลัมน์ใหม่ 'total_score' จากผลรวมของคอลัมน์ 'score1' และ 'score2'
df['total_score'] = df['score1'] + df['score2']
```

4. การกรองข้อมูล:

- `df[condition]`: กรองข้อมูลตามเงื่อนไข

ตัวอย่าง:

```python
# กรองเฉพาะแถวที่มีค่า 'age' มากกว่า 30
filtered_df = df[df['age'] > 30]
```

5. การจัดกลุ่มและสรุปข้อมูล:

- `df.groupby()`: จัดกลุ่มข้อมูลตามคอลัมน์ที่กำหนด
- `df.agg()`: ใช้ฟังก์ชันเพื่อสรุปข้อมูลในแต่ละกลุ่ม

ตัวอย่าง:

```python
# จัดกลุ่มตามคอลัมน์ 'category' และหาผลรวมของคอลัมน์ 'value'
grouped_sum = df.groupby('category')['value'].sum()
```

6. การจัดเรียงข้อมูล:

- `df.sort_values()`: จัดเรียงข้อมูลตามคอลัมน์ที่กำหนด

ตัวอย่าง:

```python
# จัดเรียงข้อมูลตามคอลัมน์ 'age' จากน้อยไปมาก
sorted_df = df.sort_values('age')
```

7. การรวมข้อมูล:

- `pd.concat()`: รวม DataFrame หรือ Series แนวแกนเดียวกัน
- `pd.merge()`: รวม DataFrame ตามคอลัมน์ที่กำหนด

8. `df.drop()`: ลบแถวหรือคอลัมน์ที่ระบุ

ตัวอย่าง:

```python
# ลบคอลัมน์ 'column1' และ 'column2'
df = df.drop(['column1', 'column2'], axis=1)
```

Input DataFrame:

```
   column1  column2  column3
0        1        4        7
1        2        5        8
2        3        6        9
```

Output DataFrame:

```
   column3
0        7
1        8
2        9
```

9. `df.fillna()`: เติมค่าที่หายไป (missing values) ด้วยค่าที่กำหนด

ตัวอย่าง:

```python
# เติมค่าที่หายไปด้วย 0
df = df.fillna(0)
```

Input DataFrame:

```
   column1  column2
0      1.0      NaN
1      NaN      5.0
2      3.0      6.0
```

Output DataFrame:

```
   column1  column2
0      1.0      0.0
1      0.0      5.0
2      3.0      6.0
```

10. `df.rename()`: เปลี่ยนชื่อคอลัมน์

ตัวอย่าง:

```python
# เปลี่ยนชื่อคอลัมน์ 'old_name' เป็น 'new_name'
df = df.rename(columns={'old_name': 'new_name'})
```

Input DataFrame:

```
   old_name  column2
0         1        4
1         2        5
2         3        6
```

Output DataFrame:

```
   new_name  column2
0         1        4
1         2        5
2         3        6
```

11. `df.astype()`: เปลี่ยนประเภทข้อมูล (data type) ของคอลัมน์

ตัวอย่าง:

```python
# เปลี่ยนประเภทข้อมูลของคอลัมน์ 'column1' เป็น int
df['column1'] = df['column1'].astype(int)
```

Input DataFrame:

```
  column1  column2
0    1.0        4
1    2.0        5
2    3.0        6
```

Output DataFrame:

```
   column1  column2
0        1        4
1        2        5
2        3        6
```

12. `df.shift()`: เลื่อนข้อมูลในแถวตามจำนวนที่กำหนด

ตัวอย่าง:

```python
# เลื่อนข้อมูลในแถวขึ้น 1 แถว
df = df.shift(1)
```

Input DataFrame:

```
   column1  column2
0        1        4
1        2        5
2        3        6
```

Output DataFrame:

```
   column1  column2
0      NaN      NaN
1      1.0      4.0
2      2.0      5.0
```

13. `df.rolling()`: สร้าง rolling window สำหรับการคำนวณค่าเฉลื่อนต่าง ๆ

ตัวอย่าง:

```python
# คำนวณค่าเฉลี่ยเคลื่อนที่ (moving average) ของคอลัมน์ 'column1' ด้วย window size เท่ากับ 2
df['rolling_mean'] = df['column1'].rolling(window=2).mean()
```

Input DataFrame:

```
   column1  column2
0        1        4
1        2        5
2        3        6
```

Output DataFrame:

```
   column1  column2  rolling_mean
0        1        4           NaN
1        2        5           1.5
2        3        6           2.5
```

14. `df.melt()`: แปลง DataFrame จากรูปแบบ wide เป็น long

ตัวอย่าง:

```python
# แปลง DataFrame จากรูปแบบ wide เป็น long โดยใช้คอลัมน์ 'id' เป็น identifier variable และคอลัมน์ที่เหลือเป็น value variables
df_long = df.melt(id_vars=['id'], value_vars=['column1', 'column2', 'column3'])
```

Input DataFrame:

```
   id  column1  column2  column3
0   1        a        d        g
1   2        b        e        h
2   3        c        f        i
```

Output DataFrame:

```
   id variable value
0   1  column1     a
1   2  column1     b
2   3  column1     c
3   1  column2     d
4   2  column2     e
5   3  column2     f
6   1  column3     g
7   2  column3     h
8   3  column3     i
```

15. `df.merge()`: รวม DataFrame ตามคอลัมน์ที่กำหนด

ตัวอย่าง:

```python
# รวม DataFrame df1 และ df2 โดยใช้คอลัมน์ 'key' เป็นตัวเชื่อม
merged_df = pd.merge(df1, df2, on='key', how='inner')
```

Input DataFrames:

```
df1:
   key  value1
0   A       1
1   B       2
2   C       3

df2:
   key  value2
0   B       4
1   C       5
2   D       6
```

Output DataFrame:

```
   key  value1  value2
0   B       2       4
1   C       3       5
```

16. `df.groupby().transform()`: ใช้ฟังก์ชันกับแต่ละกลุ่มและคืนค่าที่มีขนาดเท่ากับ DataFrame เดิม

ตัวอย่าง:

```python
# คำนวณผลรวมของคอลัมน์ 'value' สำหรับแต่ละกลุ่มที่แบ่งตามคอลัมน์ 'category'
df['group_sum'] = df.groupby('category')['value'].transform('sum')
```

Input DataFrame:

```
   category  value
0        A      1
1        B      2
2        A      3
3        B      4
4        A      5
```

Output DataFrame:

```
   category  value  group_sum
0        A      1          9
1        B      2          6
2        A      3          9
3        B      4          6
4        A      5          9
```

17. `pd.pivot_table()`: สร้าง pivot table จาก DataFrame

ตัวอย่าง:

```python
# สร้าง pivot table ที่แสดงผลรวมของคอลัมน์ 'value' โดยใช้คอลัมน์ 'category' เป็น index และคอลัมน์ 'type' เป็น columns
pivot_table = pd.pivot_table(df, values='value', index='category', columns='type', aggfunc='sum')
```

Input DataFrame:

```
   category  type  value
0        A     X      1
1        B     Y      2
2        A     Y      3
3        B     X      4
4        A     X      5
```

Output DataFrame (Pivot Table):

```
type        X    Y
category
A           6    3
B           4    2
```

เหล่านี้เป็นเพียงตัวอย่างเพิ่มเติมของฟังก์ชันที่มีประโยชน์ใน Pandas ยังมีฟังก์ชันอื่น ๆ อีกมากมายที่สามารถใช้ในการจัดการและวิเคราะห์ข้อมูลได้อย่างมีประสิทธิภาพ ลองศึกษาเพิ่มเติมและทดลองใช้งานฟังก์ชันต่าง ๆ เพื่อให้คุ้นเคยกับการใช้งาน Pandas นะครับ

ตัวอย่าง:

```python
# รวม DataFrame df1 และ df2 ในแนวแถว
combined_df = pd.concat([df1, df2])

# รวม DataFrame df1 และ df2 โดยใช้คอลัมน์ 'key' เป็นตัวเชื่อม
merged_df = pd.merge(df1, df2, on='key')
```

## แบบฝึกหัด

ข้อ 1: วิเคราะห์ยอดขายของร้านค้าปลีก
ไฟล์ CSV: sales_data.csv

```
date,product,category,quantity,price
2023-01-01,A,Electronics,10,50.0
2023-01-01,B,Clothing,5,20.0
2023-01-02,C,Electronics,8,80.0
2023-01-02,D,Clothing,12,15.0
2023-01-03,A,Electronics,5,50.0
```

คำสั่ง:

1. อ่านไฟล์ CSV เข้ามาใน DataFrame
2. คำนวณยอดขายรวมของแต่ละวัน
3. หาสินค้าที่ขายดีที่สุดในแต่ละหมวดหมู่ (category)

<details>
<summary>เฉลย</summary>

```python
import pandas as pd

df = pd.read_csv('sales_data.csv')
df['total_sales'] = df['quantity'] * df['price']

daily_sales = df.groupby('date')['total_sales'].sum()
print("Daily Sales:")
print(daily_sales)

best_selling_products = df.groupby(['category', 'product'])['quantity'].sum().sort_values(ascending=False).groupby(level=0).head(1)
print("\nBest Selling Products by Category:")
print(best_selling_products)
```

</details>
<br>
ข้อ 2: วิเคราะห์ข้อมูลพนักงานในบริษัท
ไฟล์ CSV: employee_data.csv

```
id,name,department,salary,hire_date
1,John Doe,Sales,50000,2020-01-01
2,Jane Smith,Marketing,60000,2019-05-15
3,Bob Johnson,Sales,55000,2021-03-10
4,Alice Brown,Engineering,80000,2018-07-20
5,Charlie Davis,Marketing,62000,2020-11-05
```

คำสั่ง:

1. อ่านไฟล์ CSV เข้ามาใน DataFrame
2. คำนวณจำนวนพนักงานและค่าเฉลี่ยเงินเดือนในแต่ละแผนก
3. หาพนักงานที่ทำงานกับบริษัทนานที่สุด

<details>

<summary>เฉลย</summary>

```python
import pandas as pd

df = pd.read_csv('employee_data.csv')
df['hire_date'] = pd.to_datetime(df['hire_date'])

dept_stats = df.groupby('department').agg({'id': 'count', 'salary': 'mean'})
dept_stats.columns = ['num_employees', 'avg_salary']
print("Department Statistics:")
print(dept_stats)

longest_serving_employee = df.loc[df['hire_date'].idxmin()]
print("\nLongest Serving Employee:")
print(longest_serving_employee)
```

</details>
<br>
ข้อ 3: วิเคราะห์ข้อมูลสภาพอากาศ
ไฟล์ CSV: weather_data.csv

```
date,city,temperature,humidity,windspeed
2023-01-01,New York,5.0,0.6,10.0
2023-01-01,London,8.0,0.8,12.0
2023-01-02,New York,7.0,0.7,8.0
2023-01-02,London,6.0,0.9,15.0
2023-01-03,New York,9.0,0.5,5.0
2023-01-03,London,10.0,0.6,10.0
```

คำสั่ง:

1. อ่านไฟล์ CSV เข้ามาใน DataFrame
2. หาค่าเฉลี่ยอุณหภูมิและความชื้นในแต่ละเมือง
3. หาวันที่มีความเร็วลมสูงสุดในแต่ละเมือง

<details>

<summary>เฉลย</summary>

```python
import pandas as pd

df = pd.read_csv('weather_data.csv')

city_stats = df.groupby('city').agg({'temperature': 'mean', 'humidity': 'mean'})
print("City Statistics:")
print(city_stats)

max_windspeed_dates = df.loc[df.groupby('city')['windspeed'].idxmax()]
print("\nDates with Maximum Windspeed:")
print(max_windspeed_dates)
```

แบบฝึกหัดเหล่านี้ครอบคลุมการใช้งาน Pandas ในการวิเคราะห์ข้อมูลจากหลากหลายสถานการณ์จริง เช่น การวิเคราะห์ยอดขาย ข้อมูลพนักงาน และข้อมูลสภาพอากาศ ซึ่งสามารถนำไปประยุกต์ใช้กับข้อมูลในชีวิตจริงได้

</details>

<br>
ข้อ 4: มีไฟล์ CSV ชื่อ "sales_data.csv" ที่บันทึกข้อมูลยอดขายรายวันของร้านค้าแห่งหนึ่งในปี 2023 ให้อ่านไฟล์เข้ามาใน DataFrame และทำการวิเคราะห์ข้อมูลดังนี้:

คำสั่ง:

1. หายอดขายรวมของแต่ละเดือน
2. หาสินค้าที่ขายดีที่สุด 5 อันดับแรกของแต่ละเดือน
3. หาวันที่มียอดขายสูงสุดและต่ำสุดของแต่ละเดือน

ตัวอย่างไฟล์ CSV (sales_data.csv):

```
date,product,price,quantity
2023-01-01,A,100,5
2023-01-01,B,200,3
2023-01-02,A,100,2
2023-01-02,C,150,4
2023-01-03,B,200,1
2023-01-03,C,150,3
2023-02-01,A,100,4
2023-02-01,B,200,2
2023-02-02,C,150,5
2023-02-02,D,120,3
2023-02-03,A,100,3
2023-02-03,D,120,2
```

<details>

<summary>เฉลย</summary>

```python
import pandas as pd

# อ่านไฟล์ CSV เข้ามาใน DataFrame
df = pd.read_csv('sales_data.csv')

# แปลงคอลัมน์ date ให้เป็น datetime
df['date'] = pd.to_datetime(df['date'])

# สร้างคอลัมน์ใหม่สำหรับเดือนและปี
df['month'] = df['date'].dt.to_period('M')

# 1. หายอดขายรวมของแต่ละเดือน
monthly_sales = df.groupby('month')['price'].sum()
print("ยอดขายรวมของแต่ละเดือน:")
print(monthly_sales)

# 2. หาสินค้าที่ขายดีที่สุด 5 อันดับแรกของแต่ละเดือน
top_products = df.groupby(['month', 'product'])['quantity'].sum().groupby('month').nlargest(5)
print("\nสินค้าที่ขายดีที่สุด 5 อันดับแรกของแต่ละเดือน:")
print(top_products)

# 3. หาวันที่มียอดขายสูงสุดและต่ำสุดของแต่ละเดือน
df['total_sales'] = df['price'] * df['quantity']
min_max_sales_dates = df.groupby(['month', 'date'])['total_sales'].sum().groupby('month').agg(['idxmin', 'idxmax'])
min_max_sales_dates.columns = ['min_date', 'max_date']
print("\nวันที่มียอดขายสูงสุดและต่ำสุดของแต่ละเดือน:")
print(min_max_sales_dates)
```

ผลลัพธ์:

```
ยอดขายรวมของแต่ละเดือน:
month
2023-01    2150
2023-02    1840
Name: price, dtype: int64

สินค้าที่ขายดีที่สุด 5 อันดับแรกของแต่ละเดือน:
month    product
2023-01  C          7
         A          7
         B          4
2023-02  A          7
         C          5
Name: quantity, dtype: int64

วันที่มียอดขายสูงสุดและต่ำสุดของแต่ละเดือน:
               min_date            max_date
month
2023-01 5   2023-01-03 0   2023-01-01
2023-02 10  2023-02-03 8   2023-02-02
```

โค้ดนี้แสดงให้เห็นวิธีการใช้ Pandas ในการวิเคราะห์ข้อมูลยอดขายจากไฟล์ CSV ตามที่โจทย์กำหนด เราสามารถใช้ฟังก์ชัน `groupby()`, `sum()`, `nlargest()`, และ `agg()` เพื่อคำนวณและสรุปข้อมูลตามเงื่อนไขที่ต้องการได้อย่างง่ายดาย

</details>
<br>

ข้อ 5: มีไฟล์ CSV ชื่อ "weather_data.csv" ที่บันทึกข้อมูลสภาพอากาศรายวันของเมืองหนึ่งในปี 2023 ให้อ่านไฟล์เข้ามาใน DataFrame และทำการวิเคราะห์ข้อมูลดังนี้:

1. หาอุณหภูมิเฉลี่ย, สูงสุด, และต่ำสุดของแต่ละเดือน
2. หาจำนวนวันที่ฝนตกในแต่ละเดือน
3. สร้างกราฟแสดงการเปลี่ยนแปลงของอุณหภูมิตลอดทั้งปี

ตัวอย่างไฟล์ CSV (weather_data.csv):

```
date,temperature,humidity,rainfall
2023-01-01,25.5,60,0
2023-01-02,26.0,65,10
2023-01-03,24.8,70,5
2023-02-01,28.2,55,0
2023-02-02,27.8,60,0
2023-02-03,29.1,50,0
2023-03-01,30.5,45,0
2023-03-02,31.2,40,0
2023-03-03,32.0,35,0
```

<details>

<summary>เฉลย</summary>

```python
import pandas as pd
import matplotlib.pyplot as plt

# อ่านไฟล์ CSV เข้ามาใน DataFrame
df = pd.read_csv('weather_data.csv')

# แปลงคอลัมน์ date ให้เป็น datetime
df['date'] = pd.to_datetime(df['date'])

# สร้างคอลัมน์ใหม่สำหรับเดือนและปี
df['month'] = df['date'].dt.to_period('M')

# 1. หาอุณหภูมิเฉลี่ย, สูงสุด, และต่ำสุดของแต่ละเดือน
monthly_temp = df.groupby('month')['temperature'].agg(['mean', 'max', 'min'])
print("อุณหภูมิเฉลี่ย, สูงสุด, และต่ำสุดของแต่ละเดือน:")
print(monthly_temp)

# 2. หาจำนวนวันที่ฝนตกในแต่ละเดือน
monthly_rainy_days = df[df['rainfall'] > 0].groupby('month').size()
print("\nจำนวนวันที่ฝนตกในแต่ละเดือน:")
print(monthly_rainy_days)

# 3. สร้างกราฟแสดงการเปลี่ยนแปลงของอุณหภูมิตลอดทั้งปี
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temperature'])
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Change Throughout the Year')
plt.grid(True)
plt.show()
```

ผลลัพธ์:

```
อุณหภูมิเฉลี่ย, สูงสุด, และต่ำสุดของแต่ละเดือน:
            mean   max   min
month
2023-01  25.4333  26.0  24.8
2023-02  28.3667  29.1  27.8
2023-03  31.2333  32.0  30.5

จำนวนวันที่ฝนตกในแต่ละเดือน:
month
2023-01    2
2023-02    0
2023-03    0
dtype: int64
```

</details>

<br>

โค้ดนี้แสดงให้เห็นวิธีการใช้ Pandas ในการวิเคราะห์ข้อมูลสภาพอากาศจากไฟล์ CSV ตามที่โจทย์กำหนด เราสามารถใช้ฟังก์ชัน `groupby()`, `agg()`, และ `size()` ในการคำนวณค่าสถิติและนับจำนวนวันที่ฝนตกได้ นอกจากนี้ยังมีการใช้ Matplotlib ในการสร้างกราฟแสดงการเปลี่ยนแปลงของอุณหภูมิตลอดทั้งปีอีกด้วย

การฝึกทำแบบฝึกหัดแบบนี้จะช่วยให้เราคุ้นเคยกับการใช้ Pandas และ Matplotlib ในการวิเคราะห์และนำเสนอข้อมูลได้ดียิ่งขึ้น
