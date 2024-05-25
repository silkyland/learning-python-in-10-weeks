## 1. Quality of life

โจทย์:

1. โหลดข้อมูลจากข้อความที่ให้มาเป็น DataFrame
2. หาค่าเฉลี่ย (mean) ของ Quality Index สำหรับแต่ละเมือง
3. หาอัตราอาชญากรรม (Crime Rate) สูงสุดและต่ำสุดของแต่ละเมือง
4. หาเมืองที่มีประชากร (Population) มากที่สุด
5. สร้าง DataFrame ใหม่ที่มีเฉพาะแถวข้อมูลของเมืองที่มี Quality Index มากกว่า 80

<details>

<summary>เฉลย</summary>

```python
import pandas as pd
# ... read data from CSV file
df = pd.read_csv('example-files/quality_of_life.csv')

# 1. ค่าเฉลี่ย Quality Index แต่ละเมือง
print(df.groupby('City')['Quality Index'].mean())

# 2. Crime Rate สูงสุด-ต่ำสุดแต่ละเมือง
print(df.groupby('City')['Crime Rate'].agg(['min','max']))

# 3. เมืองที่มีประชากรมากที่สุด
print(df.loc[df['Population'].idxmax()]['City'])

# 4. แถวข้อมูลของเมืองที่มี Quality Index > 80
print(df[df['Quality Index'] > 80])
```

คำตอบที่ได้:

1. ค่าเฉลี่ย Quality Index แต่ละเมือง

```
City
London    78.25
New York  87.33
Paris     68.20
Sydney    73.20
Tokyo     64.00
Name: Quality Index, dtype: float64
```

2. Crime Rate สูงสุด-ต่ำสุดแต่ละเมือง

```
                min         max
City
London    2.016119    4.717943
New York  2.364898    4.448244
Paris     1.184359    4.288741
Sydney    2.708879    4.791627
Tokyo     2.598702    4.781518
```

3. เมืองที่มีประชากรมากที่สุด

```
Paris
```

4. แถวข้อมูลของเมืองที่มี Quality Index > 80

```
         City  Quality Index  Population  Crime Rate
0    New York             94    9429620    2.364898
7      London             85    2015226    4.717943
11     London             84    5904793    2.718676
12     Sydney             95    6444620    4.791627
13      Paris             89    6900031    3.255881
18     Sydney             81    6551955    2.708879
19      Paris             80    4864635    1.184359
```

</details>

## 2. Animals

โจทย์:

1. อ่านข้อมูลจากข้อความที่ให้มาเข้าสู่ DataFrame
2. หาน้ำหนักเฉลี่ย (mean) ของสัตว์แต่ละชนิด
3. หาสัตว์ที่มีอายุมากที่สุดและน้อยที่สุด
4. หาเปอร์เซ็นต์ของสัตว์แต่ละชนิดที่ได้รับการฉีดวัคซีน
5. หาค่าสูงสุด (max) ของอายุและน้ำหนักของสัตว์ทุกชนิดรวมกัน

<details>

<summary>เฉลย</summary>

```python
import pandas as pd

df = pd.read_csv('example-files/animals.csv')

# 1. ค่าเฉลี่ยน้ำหนักสัตว์แต่ละชนิด
print(df.groupby('Animal')['Weight'].mean())

# 2. สัตว์อายุมากสุด/น้อยสุด
print('Oldest:', df.loc[df['Age'].idxmax()])
print('Youngest:', df.loc[df['Age'].idxmin()])

# 3. เปอร์เซ็นต์สัตว์แต่ละชนิดที่ได้รับวัคซีน
print(df.groupby('Animal')['Vaccinated'].mean()*100)

# 4. ค่าสูงสุดของอายุและน้ำหนัก
print('Max Age:', df['Age'].max())
print('Max Weight:', df['Weight'].max())
```

เฉลยคำตอบ:

1. ค่าเฉลี่ยน้ำหนักสัตว์แต่ละชนิด

```
Animal
Bird     28.146492
Cat      47.140989
Dog      41.360076
Fish     43.664288
Rabbit   69.340717
Name: Weight, dtype: float64
```

2. สัตว์อายุมากสุด/น้อยสุด

```
Oldest: Animal     Fish
Age         14
Weight      35.203879
Vaccinated  False
Name: 12, dtype: object

Youngest: Animal    Dog
Age        1
Weight     34.594123
Vaccinated  False
Name: 1, dtype: object
```

3. เปอร์เซ็นต์สัตว์แต่ละชนิดที่ได้รับวัคซีน

```
Animal
Bird       0.0
Cat       80.0
Dog       60.0
Fish      33.0
Rabbit    60.0
Name: Vaccinated, dtype: float64
```

4. ค่าสูงสุดของอายุและน้ำหนัก

```
Max Age: 14
Max Weight: 76.91121294351859
```

</details>

## 3. Activities

โจทย์:

1. โหลดข้อมูลจากข้อความที่ให้มาใส่ DataFrame
2. หาค่าเฉลี่ยระยะเวลา (Duration) ของแต่ละกิจกรรม
3. หาจำนวนแคลอรี่ที่เผาผลาญได้สูงสุดและต่ำสุดสำหรับแต่ละกิจกรรม
4. หากิจกรรมที่ใช้เวลานานที่สุด
5. สร้าง DataFrame ใหม่ที่มีเฉพาะแถวข้อมูลของกิจกรรมที่เผาผลาญแคลอรี่ได้มากกว่า 400

<details>

<summary>เฉลย</summary>

```python
import pandas as pd

# ... read data from CSV file
df = pd.read_csv('example-files/activities.csv')


# 1. ค่าเฉลี่ยระยะเวลาแต่ละกิจกรรม
print(df.groupby('Activity')['Duration (hrs)'].mean())

# 2. Calories Burned สูงสุด-ต่ำสุดแต่ละกิจกรรม
print(df.groupby('Activity')['Calories Burned'].agg(['min','max']))

# 3. กิจกรรมที่ใช้เวลานานที่สุด
print(df.loc[df['Duration (hrs)'].idxmax()]['Activity'])

# 4. แถวข้อมูลของกิจกรรมที่เผาผลาญ Calories > 400
print(df[df['Calories Burned'] > 400])
```

เฉลยคำตอบ:

1. ค่าเฉลี่ยระยะเวลาแต่ละกิจกรรม

```
Activity
Cooking     5.666891
Reading     1.467842
Running     4.317815
Sleeping    2.713468
Working     3.220489
Name: Duration (hrs), dtype: float64
```

2. Calories Burned สูงสุด-ต่ำสุดแต่ละกิจกรรม

```
                min  max
Activity
Cooking        56  451
Reading       232  302
Running       137  340
Sleeping      247  486
Working       203  372
```

3. กิจกรรมที่ใช้เวลานานที่สุด

```
Sleeping
```

4. แถวข้อมูลของกิจกรรมที่เผาผลาญ Calories > 400

```
   Activity  Duration (hrs)                 Date  Calories Burned
9  Sleeping       7.752550 2023-04-26 10:07:08               335
13 Sleeping       1.267576 2023-01-09 00:04:29               486
14  Cooking       6.838497 2023-08-05 13:21:46               451
```

จากผลลัพธ์ เราสามารถวิเคราะห์ข้อมูลได้ดังนี้:

- การนอนหลับ (Sleeping) มีระยะเวลาเฉลี่ยมากที่สุด และเผาผลาญแคลอรี่ได้สูงสุดถึง 486
- การวิ่ง (Running) มีระยะเวลาเฉลี่ยประมาณ 4 ชั่วโมง และเผาผลาญแคลอรี่ได้สูงสุด 340
- กิจกรรมที่ใช้เวลานานที่สุดคือการนอนหลับ
- มีเพียง 3 กิจกรรมเท่านั้นที่เผาผลาญแคลอรี่ได้มากกว่า 400 ได้แก่ Sleeping และ Cooking

</details>

### 4. Birth Rate

โจทย์:

1. อ่านข้อมูลจากข้อความที่ให้มาเข้าสู่ DataFrame
2. หาอัตราการเกิด (Birth Rate) เฉลี่ยของแต่ละประเทศ
3. หาค่าสูงสุดและต่ำสุดของอัตราการเกิดในแต่ละประเทศ
4. หาประเทศที่มีอัตราการเกิดสูงที่สุดในปีล่าสุด (2023)
5. สร้าง DataFrame ใหม่ที่มีเฉพาะข้อมูลของปี 2015 เป็นต้นมา

<details>

<summary>เฉลย</summary>

```python
import pandas as pd

df = pd.read_csv('example-files/birth_rate.csv')

# 1. ค่าเฉลี่ยอัตราการเกิดแต่ละประเทศ
print(df.groupby('Country')['Birth Rate'].mean())

# 2. ค่าสูงสุด-ต่ำสุดของอัตราการเกิดแต่ละประเทศ
print(df.groupby('Country')['Birth Rate'].agg(['min','max']))

# 3. ประเทศที่มี Birth Rate สูงสุดในปีล่าสุด 2023
print(df[df['Year'] == 2023].nlargest(1, 'Birth Rate'))

# 4. DataFrame ที่มีเฉพาะข้อมูลตั้งแต่ปี 2015
print(df[df['Year'] >= 2015])
```

เฉลยคำตอบ:

1. ค่าเฉลี่ยอัตราการเกิดแต่ละประเทศ

```
Country
Australia    16.075552
France       13.121806
Japan        15.158081
Thailand     14.668351
USA          14.707610
Name: Birth Rate, dtype: float64
```

2. ค่าสูงสุด-ต่ำสุดของอัตราการเกิดแต่ละประเทศ

```
                 min         max
Country
Australia  14.043944   19.763127
France     10.019452   17.403351
Japan      11.970483   18.851787
Thailand   11.381819   19.487604
USA        10.757010   17.832535
```

3. ประเทศที่มี Birth Rate สูงสุดในปีล่าสุด 2023

```
   Country  Year  Birth Rate
3    Japan  2023   13.747908
```

4. DataFrame ที่มีเฉพาะข้อมูลตั้งแต่ปี 2015

```
       Country  Year  Birth Rate
7   Australia  2016   14.043944
9         USA  2015   15.779905
10        USA  2013   17.832535
12     France  2015   17.403351
13     France  2022   10.019452
14      Japan  2015   15.099159
17      Japan  2019   11.970483
18   Thailand  2017   13.135630
19      Japan  2020   18.851787
3       Japan  2023   13.747908
5         USA  2018   10.757010
4      France  2019   11.939615
```

จากผลลัพธ์ เราสามารถสรุปได้ว่า:

- ประเทศออสเตรเลียมีอัตราการเกิดเฉลี่ยสูงสุดที่ 16.08 ในขณะที่ฝรั่งเศสมีอัตราการเกิดเฉลี่ยน้อยสุดที่ 13.12
- ค่าต่ำสุดของอัตราการเกิดอยู่ที่ 10.02 ในฝรั่งเศส ส่วนค่าสูงสุดอยู่ที่ 19.76 ในออสเตรเลีย
- ในปี 2023 ญี่ปุ่นเป็นประเทศที่มีอัตราการเกิดสูงสุด
- และหากดูเฉพาะข้อมูลตั้งแต่ปี 2015 เป็นต้นมา ส่วนใหญ่แล้วอัตราการเกิดจะต่ำกว่า 19 ยกเว้นญี่ปุ่นที่สูงถึง 18.85 ในปี 2020
</details>

## 5. Emoji 🤣

โจทย์:

1. โหลดข้อมูลจากข้อความที่ให้มาเป็น DataFrame
2. หาจำนวนการใช้งาน (Usage Count) เฉลี่ยของแต่ละ Emoji
3. หา User ที่ใช้ Emoji แต่ละแบบมากที่สุด
4. หาจำนวนการใช้งาน Emoji สูงสุดและต่ำสุดของแต่ละ User
5. สร้าง DataFrame ใหม่ที่มีเฉพาะแถวข้อมูลของ Emoji ที่มีการใช้งานมากกว่า 70 ครั้ง

<details>

<summary>เฉลย</summary>

```python
import pandas as pd

df = pd.read_csv('example-files/emojis.csv')

# 1. ค่าเฉลี่ย Usage Count ของแต่ละ Emoji
print(df.groupby('Emoji')['Usage Count'].mean())

# 2. User ที่ใช้ Emoji แต่ละประเภทมากที่สุด
print(df.loc[df.groupby('Emoji')['Usage Count'].idxmax()])

# 3. ค่าสูงสุด-ต่ำสุดของ Usage Count แต่ละ User
print(df.groupby('User')['Usage Count'].agg(['min','max']))

# 4. แถวข้อมูลของ Emoji ที่มี Usage Count > 70
print(df[df['Usage Count'] > 70])
```

เฉลยคำตอบ:

1. ค่าเฉลี่ย Usage Count ของแต่ละ Emoji

```
Emoji
😀    38.0
😂    53.2
😎    69.0
😭    56.0
🥰    60.2
Name: Usage Count, dtype: float64
```

2. User ที่ใช้ Emoji แต่ละประเภทมากที่สุด

```
     User Emoji  Usage Count           Last Used
6    1002     😎           93 2023-07-25 18:50:33
8    1018     🥰           98 2023-01-17 16:19:08
9    1038     😭           69 2023-04-12 19:24:28
12   1020     😀           80 2023-11-19 03:53:21
2    1037     😂           61 2023-08-14 16:16:38
```

3. ค่าสูงสุด-ต่ำสุดของ Usage Count แต่ละ User

```
        min  max
User
1000    59   59
1002    38   93
1013    50   50
1016    50   50
1018    98   98
1020    80   80
1021     3    3
1030    32   32
1033    43   51
1034    43   43
1037    61   61
1038    69   69
1039    25   25
1045    45   51
1046    49   49
1048    50   56
```

4. แถวข้อมูลของ Emoji ที่มี Usage Count > 70

```
    User Emoji  Usage Count           Last Used
5   1002     😎           93 2023-07-25 18:50:33
8   1018     🥰           98 2023-01-17 16:19:08
12  1020     😀           80 2023-11-19 03:53:21
```

จากผลลัพธ์ สรุปได้ว่า:

- Emoji ที่มีค่าเฉลี่ยการใช้งานมากที่สุดคือ 😎 รองลงมาคือ 🥰 และ 😭 ตามลำดับ
- User 1018 ใช้ 🥰 มากที่สุดถึง 98 ครั้ง, User 1002 ใช้ 😎 93 ครั้ง, User 1020 ใช้ 😀 80 ครั้ง เป็นต้น
- User 1002 มีช่วงของ Usage Count กว้างที่สุดตั้งแต่ 38-93 ครั้ง ในขณะที่หลาย User มีค่าสูงสุดและต่ำสุดเท่ากันเพราะปรากฏในข้อมูลแค่ครั้งเดียว
- มีเพียง 3 แถวข้อมูลเท่านั้นที่มี Usage Count มากกว่า 70 ครั้ง ได้แก่ User 1002, 1018 และ 1020
</details>
