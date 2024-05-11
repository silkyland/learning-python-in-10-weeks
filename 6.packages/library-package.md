# Library Package in Python

## Library and Package

ในบริบทของ Python คำว่า "library" และ "package" มักใช้แทนกันได้ โดยทั่วไปหมายถึงชุดของโมดูลหรือโค้ดที่ถูกจัดระเบียบไว้ด้วยกันเพื่อให้สามารถนำไปใช้งานได้ง่าย อย่างไรก็ตาม มีความแตกต่างเล็กน้อยระหว่างสองคำนี้ ดังนี้

### Library (ไลบรารี):

เป็นคำที่ใช้อ้างถึงชุดของโมดูลหรือโค้ดที่เกี่ยวข้องกัน และถูกนำไปใช้เพื่อวัตถุประสงค์เฉพาะ เช่น การจัดการวันที่และเวลา (datetime) หรือการสร้างกราฟ (matplotlib) โดยไลบรารีอาจประกอบด้วยหลายๆ package หรือโมดูลย่อยๆ ก็ได้

### Package (แพ็คเกจ):

เป็นไดเรกทอรีที่รวบรวมโมดูลที่เกี่ยวข้องกันเอาไว้ โดยจะมีไฟล์พิเศษชื่อ **init**.py เพื่อระบุว่าไดเรกทอรีนั้นเป็น package และอาจมีโมดูลย่อย (submodule) หรือ subpackage อยู่ภายใน package ได้อีก

สรุปคือ package เป็นวิธีการจัดระเบียบโค้ดให้เป็นโครงสร้างที่ชัดเจน ส่วน library อ้างถึงชุดของโค้ดที่ใช้งานร่วมกันเพื่อวัตถุประสงค์บางอย่าง ซึ่งอาจอยู่ในรูปแบบของ package เดียวหรือหลาย package ก็ได้

## Built-in Package

### 1.Math

ไลบรารี math เป็น built-in package ใน Python ที่ให้ฟังก์ชันทางคณิตศาสตร์มากมาย ครอบคลุมทั้งคณิตศาสตร์พื้นฐานและขั้นสูง ตัวอย่างฟังก์ชันที่สำคัญใน math ได้แก่

1. math.ceil(x) และ math.floor(x) - ปัดเศษขึ้นและลงของ x
2. math.pow(x, y) - คำนวณ x ยกกำลัง y
3. math.sqrt(x) - คำนวณรากที่สองของ x
4. math.pi - ค่าคงที่ pi (π)
5. math.sin(x), math.cos(x), math.tan(x) - คำนวณ sine, cosine และ tangent ของมุม x เรเดียน
6. math.log(x) - คำนวณ natural logarithm ของ x
7. math.gcd(a, b) - หา greatest common divisor (หรือ highest common factor) ของ a และ b
8. math.radians(x) และ math.degrees(x) - แปลงหน่วยมุมระหว่างองศาและเรเดียน

ตัวอย่างการใช้งาน math:

```python
import math

# ปัดเศษขึ้นและลง
x = 4.2
print(math.ceil(x))  # ผลลัพธ์: 5
print(math.floor(x))  # ผลลัพธ์: 4

# ยกกำลังและรากที่สอง
y = 3
print(math.pow(x, y))  # ผลลัพธ์: 74.08800000000002
print(math.sqrt(x))  # ผลลัพธ์: 2.0493901531919196

# ค่า pi
print(math.pi)  # ผลลัพธ์: 3.141592653589793

# ฟังก์ชันตรีโกณมิติ
angle_rad = math.pi / 4
print(math.sin(angle_rad))  # ผลลัพธ์: 0.7071067811865476
print(math.cos(angle_rad))  # ผลลัพธ์: 0.7071067811865476
print(math.tan(angle_rad))  # ผลลัพธ์: 0.9999999999999999

# หา greatest common divisor
a, b = 24, 36
print(math.gcd(a, b))  # ผลลัพธ์: 12

# แปลงหน่วยมุม
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(angle_rad)  # ผลลัพธ์: 0.7853981633974483
print(math.degrees(angle_rad))  # ผลลัพธ์: 45.0
```

ไลบรารี math ยังมีฟังก์ชันอื่นๆ อีกมากมายที่ใช้ในการคำนวณทางคณิตศาสตร์ สามารถศึกษาเพิ่มเติมได้จากเอกสารของ Python โดยรวมแล้ว math นับเป็น built-in package ที่มีประโยชน์อย่างมากในการเขียนโปรแกรมที่ต้องอาศัยการคำนวณทางคณิตศาสตร์

### 2.Random

ต่อไปเป็น package random ซึ่งเป็น built-in package ที่ใช้ในการสร้างค่าสุ่ม (random) ในรูปแบบต่างๆ ทั้งจำนวนเต็ม จำนวนจริง รวมถึงการสุ่มเลือกข้อมูลจากลิสต์หรือคอลเล็กชันอื่นๆ ตัวอย่างฟังก์ชันที่สำคัญใน random ได้แก่

1. random.random() - สร้างค่าจำนวนจริงสุ่มระหว่าง 0.0 ถึง 1.0
2. random.randint(a, b) - สร้างค่าจำนวนเต็มสุ่มระหว่าง a ถึง b (รวม a และ b)
3. random.uniform(a, b) - สร้างค่าจำนวนจริงสุ่มระหว่าง a ถึง b
4. random.choice(seq) - สุ่มเลือกหนึ่งรายการจากลำดับ seq
5. random.shuffle(seq) - สลับลำดับข้อมูลใน seq แบบสุ่ม
6. random.sample(population, k) - เลือกข้อมูลจาก population แบบสุ่มโดยไม่ซ้ำกัน จำนวน k รายการ

ตัวอย่างการใช้งาน random:

```python
import random

# สร้างค่าสุ่ม
print(random.random())  # ผลลัพธ์: ค่าสุ่มระหว่าง 0.0 ถึง 1.0
print(random.randint(1, 10))  # ผลลัพธ์: เลขจำนวนเต็มสุ่มระหว่าง 1 ถึง 10
print(random.uniform(1.0, 10.0))  # ผลลัพธ์: ค่าจำนวนจริงสุ่มระหว่าง 1.0 ถึง 10.0

# สุ่มเลือกจากลิสต์
fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))  # ผลลัพธ์: สุ่มเลือกผลไม้ 1 ชนิด

# สลับลำดับแบบสุ่ม
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # ผลลัพธ์: ลิสต์ numbers ที่ถูกสลับลำดับแล้ว เช่น [3, 1, 5, 2, 4]

# เลือกข้อมูลแบบสุ่มไม่ซ้ำ
letters = ['a', 'b', 'c', 'd', 'e']
print(random.sample(letters, 3))  # ผลลัพธ์: เลือกตัวอักษร 3 ตัวแบบสุ่ม เช่น ['e', 'b', 'd']
```

นอกจากนี้ random ยังมีฟังก์ชันอื่นๆ อีกมากมาย และเป็น package ที่มีประโยชน์ในการสร้างค่าสุ่มสำหรับจำลองสถานการณ์ต่างๆ ทำเกม หรือใช้ในการทดสอบโปรแกรม สามารถศึกษาเพิ่มเติมได้จากเอกสารของ Python เช่นกัน

### 3. Datetime

ต่อไปเป็นเรื่องของ package datetime ซึ่งใช้ในการจัดการกับวันที่และเวลาใน Python โดย datetime มีคลาสและฟังก์ชันที่ช่วยให้สามารถสร้าง จัดรูปแบบ และคำนวณเกี่ยวกับวันที่และเวลาได้อย่างสะดวก

คลาสหลักๆ ใน datetime ได้แก่

1. datetime.date - แทนวันที่ (ปี, เดือน, วัน)
2. datetime.time - แทนเวลา (ชั่วโมง, นาที, วินาที, ไมโครวินาที)
3. datetime.datetime - แทนวันที่และเวลา (ปี, เดือน, วัน, ชั่วโมง, นาที, วินาที, ไมโครวินาที)
4. datetime.timedelta - แทนช่วงหรือระยะเวลา

ตัวอย่างการใช้งาน datetime:

```python
from datetime import date, time, datetime, timedelta

# วันที่ปัจจุบัน
today = date.today()
print(today)  # ผลลัพธ์: วันที่ปัจจุบัน เช่น 2023-07-04

# สร้างวันที่
birth_date = date(1990, 12, 25)
print(birth_date)  # ผลลัพธ์: 1990-12-25

# เวลาปัจจุบัน
current_time = datetime.now().time()
print(current_time)  # ผลลัพธ์: เวลาปัจจุบัน เช่น 14:30:45.123456

# กำหนดเวลา
alarm_time = time(6, 30)
print(alarm_time)  # ผลลัพธ์: 06:30:00

# จัดรูปแบบวันที่และเวลา
now = datetime.now()
format_string = "%Y-%m-%d %H:%M:%S"
print(now.strftime(format_string))  # ผลลัพธ์: วันที่และเวลาปัจจุบันในรูปแบบ เช่น 2023-07-04 14:35:20

# บวกลบวันที่และเวลา
delta = timedelta(days=30, hours=2, minutes=15)
future_date = now + delta
print(future_date)  # ผลลัพธ์: วันที่และเวลาในอนาคตที่บวกเพิ่ม 30 วัน 2 ชั่วโมง 15 นาที
```

#### Format codes หรือ directives

ในการแสดงผลหรือจัดรูปแบบวันที่และเวลาใน Python เราสามารถใช้รูปแบบพิเศษที่เรียกว่า "format codes" หรือ "directives" ร่วมกับฟังก์ชัน `strftime()` ของออบเจ็กต์ datetime เพื่อกำหนดรูปแบบการแสดงผลตามที่ต้องการ

ตัวอย่างของ format codes ที่นิยมใช้กับ `strftime()` มีดังนี้:

- `%Y`: ปีแบบเต็ม (4 หลัก)
- `%m`: เดือนเป็นตัวเลข (01-12)
- `%d`: วันที่ (01-31)
- `%H`: ชั่วโมงในรูปแบบ 24 ชั่วโมง (00-23)
- `%I`: ชั่วโมงในรูปแบบ 12 ชั่วโมง (01-12)
- `%M`: นาที (00-59)
- `%S`: วินาที (00-59)
- `%p`: AM หรือ PM
- `%a`: ชื่อวันในสัปดาห์แบบย่อ (เช่น Sun, Mon, ...)
- `%A`: ชื่อวันในสัปดาห์แบบเต็ม (เช่น Sunday, Monday, ...)
- `%b`: ชื่อเดือนแบบย่อ (เช่น Jan, Feb, ...)
- `%B`: ชื่อเดือนแบบเต็ม (เช่น January, February, ...)

เราสามารถใช้ format codes เหล่านี้ในการสร้างรูปแบบวันที่และเวลาตามที่ต้องการได้ เช่น:

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))  # 2023-04-19
print(now.strftime("%A, %B %d, %Y"))  # Wednesday, April 19, 2023
print(now.strftime("%I:%M %p"))  # 02:30 PM
```

นอกจากนี้ เรายังสามารถใช้ format codes เหล่านี้ร่วมกับฟังก์ชัน `datetime.strptime()` เพื่อแปลงสตริงวันที่และเวลาให้เป็นออบเจ็กต์ datetime ได้อีกด้วย เช่น:

```python
date_str = "2023-04-19 14:30:00"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
```

ในตัวอย่างนี้ เราใช้ format codes `%Y`, `%m`, `%d`, `%H`, `%M` และ `%S` เพื่อระบุรูปแบบของสตริงวันที่และเวลาที่ต้องการแปลงให้ตรงกับสตริงที่ป้อนเข้ามา

การทำความเข้าใจ format codes และวิธีการใช้งานร่วมกับฟังก์ชัน `strftime()` และ `strptime()` จะช่วยให้สามารถจัดรูปแบบและแปลงวันที่และเวลาในรูปแบบต่างๆ ได้อย่างยืดหยุ่น ซึ่งเป็นทักษะที่สำคัญในการทำงานกับข้อมูลวันที่และเวลาในภาษา Python

#### การเปรียบเทียบวันที่และเวลา

ในการเปรียบเทียบวันที่และเวลาใน Python สามารถใช้ตัวดำเนินการเปรียบเทียบ (comparison operators) เช่น <, <=, >, >=, ==, != ได้โดยตรง ลองดูตัวอย่างการเปรียบเทียบด้วย datetime นี้ครับ

```python
from datetime import date, time, datetime

# เปรียบเทียบวันที่
date1 = date(2023, 7, 1)
date2 = date(2023, 7, 4)

print(date1 < date2)  # ผลลัพธ์: True
print(date1 > date2)  # ผลลัพธ์: False
print(date1 == date2)  # ผลลัพธ์: False

# เปรียบเทียบเวลา
time1 = time(8, 30)
time2 = time(9, 45)

print(time1 < time2)  # ผลลัพธ์: True
print(time1 >= time2)  # ผลลัพธ์: False
print(time1 != time2)  # ผลลัพธ์: True

# เปรียบเทียบวันที่และเวลา
dt1 = datetime(2023, 7, 4, 10, 0)
dt2 = datetime(2023, 7, 4, 12, 30)
dt3 = datetime(2023, 7, 5, 8, 15)

print(dt1 < dt2)  # ผลลัพธ์: True
print(dt2 > dt3)  # ผลลัพธ์: False
print(dt1 == dt2)  # ผลลัพธ์: False

# เปรียบเทียบกับวันที่และเวลาปัจจุบัน
now = datetime.now()
past_date = datetime(2022, 12, 31)
future_date = datetime(2024, 1, 1)

print(past_date < now < future_date)  # ผลลัพธ์: True
```

ในตัวอย่างนี้ เราสามารถเปรียบเทียบวันที่ (date), เวลา (time) และวันที่และเวลา (datetime) โดยใช้ตัวดำเนินการเปรียบเทียบได้โดยตรง ซึ่ง Python จะเปรียบเทียบตามลำดับของปี, เดือน, วัน, ชั่วโมง, นาที, วินาที ตามลำดับ

### 4. os

ต่อไปเป็นเรื่องของ package os ซึ่งใช้ในการทำงานกับระบบปฏิบัติการ (operating system) เช่น การจัดการไฟล์และไดเรกทอรี, การดึงข้อมูลสภาพแวดล้อม (environment) ของระบบ และการรันคำสั่งของระบบปฏิบัติการผ่านทาง Python

ตัวอย่างฟังก์ชันที่น่าสนใจใน os:

1. os.getcwd() - คืนค่าไดเรกทอรีปัจจุบันที่ Python กำลังทำงานอยู่
2. os.chdir(path) - เปลี่ยนไดเรกทอรีทำงานปัจจุบันไปยัง path ที่กำหนด
3. os.listdir(path) - คืนค่ารายชื่อไฟล์และไดเรกทอรีใน path ที่กำหนด
4. os.mkdir(path) - สร้างไดเรกทอรีใหม่ตาม path ที่กำหนด
5. os.remove(path) - ลบไฟล์ที่ระบุโดย path
6. os.rename(src, dst) - เปลี่ยนชื่อไฟล์หรือย้ายไฟล์จาก src ไปยัง dst
7. os.path.join(path1, path2, ...) - รวม path ย่อยหลายๆ ส่วนให้เป็น path เดียว
8. os.path.exists(path) - ตรวจสอบว่ามี path นั้นอยู่จริงหรือไม่

ตัวอย่างการใช้งาน os:

```python
import os

# ไดเรกทอรีปัจจุบัน
current_dir = os.getcwd()
print("Current directory:", current_dir)

# รายชื่อไฟล์และไดเรกทอรีใน current_dir
print("Files and directories:", os.listdir(current_dir))

# สร้างไดเรกทอรีใหม่
new_dir = "test_dir"
os.mkdir(new_dir)
print(f"Created new directory: {new_dir}")

# สร้างและเขียนไฟล์
file_path = os.path.join(new_dir, "test.txt")
with open(file_path, "w") as file:
    file.write("Hello, World!")
print(f"Created file: {file_path}")

# เปลี่ยนชื่อไฟล์
new_file_path = os.path.join(new_dir, "new_test.txt")
os.rename(file_path, new_file_path)
print(f"Renamed file: {file_path} -> {new_file_path}")

# ลบไฟล์
os.remove(new_file_path)
print(f"Removed file: {new_file_path}")
```

นอกจากนี้ os ยังมีฟังก์ชันอื่นๆ อีกมากมายในการจัดการและทำงานกับระบบไฟล์ รวมถึงการดึงข้อมูลเกี่ยวกับสภาพแวดล้อมของระบบ การใช้งาน os จะช่วยให้สามารถสร้างสคริปต์ที่ทำงานกับไฟล์และไดเรกทอรีได้อย่างมีประสิทธิภาพ และยังสามารถปรับแต่งให้ทำงานข้ามระบบปฏิบัติการได้อีกด้วย

### 5. sys

ต่อไปเป็นเรื่องของ package sys ซึ่งใช้ในการเข้าถึงและควบคุมการทำงานของ Python interpreter นอกจากนี้ sys ยังมีฟังก์ชันที่เกี่ยวข้องกับระบบ เช่น การอ่านหรือเขียนข้อมูลกับ standard input/output/error และการจัดการกับ command line arguments

ตัวอย่างฟังก์ชันและแอตทริบิวต์ที่น่าสนใจใน sys:

1. sys.argv - ลิสต์ของ command line arguments ที่ส่งให้กับสคริปต์ (รวม ชื่อสคริปต์เป็นอาร์กิวเมนต์ตัวแรก)
2. sys.stdin - อ็อบเจ็กต์สำหรับอ่านข้อมูลจาก standard input
3. sys.stdout - อ็อบเจ็กต์สำหรับเขียนข้อมูลไปยัง standard output
4. sys.stderr - อ็อบเจ็กต์สำหรับเขียนข้อความแสดงข้อผิดพลาดไปยัง standard error
5. sys.exit([arg]) - ออกจากสคริปต์ทันที โดยส่งค่า arg เป็น exit status (ถ้าไม่กำหนด arg จะใช้ค่า 0)
6. sys.path - ลิสต์ของไดเรกทอรีที่ Python จะค้นหาโมดูลเพื่อ import
7. sys.version - ข้อมูลเวอร์ชันของ Python ที่กำลังรัน

ตัวอย่างการใช้งาน sys:

```python
import sys

# รับ command line arguments
print("Command line arguments:", sys.argv)

# อ่านข้อมูลจาก standard input
print("Enter your name:")
name = sys.stdin.readline().strip()
print(f"Hello, {name}!")

# เขียนข้อมูลไปยัง standard output และ standard error
sys.stdout.write("This is a normal message.\n")
sys.stderr.write("This is an error message.\n")

# ตรวจสอบเวอร์ชันของ Python
print("Python version:", sys.version)

# เพิ่ม current directory เข้าไปใน sys.path เพื่อให้สามารถ import โมดูลในไดเรกทอรีปัจจุบันได้
sys.path.append(".")
print("Module search path:", sys.path)

# ออกจากสคริปต์พร้อมกับส่ง exit status
sys.exit(0)
```

ในตัวอย่างนี้ เราใช้ sys.argv เพื่อเข้าถึง command line arguments, ใช้ sys.stdin.readline() เพื่ออ่านข้อมูลจาก standard input, เขียนข้อความปกติไปยัง sys.stdout และข้อความแสดงข้อผิดพลาดไปยัง sys.stderr, แสดงเวอร์ชันของ Python ผ่าน sys.version, เพิ่มไดเรกทอรีปัจจุบันเข้าไปใน sys.path และสุดท้ายออกจากสคริปต์ด้วย sys.exit(0)

sys เป็น package ที่มีประโยชน์ในการควบคุมและปรับแต่งการทำงานของ Python interpreter รวมถึงการส่งข้อมูลเข้าออกกับระบบ ซึ่งจะช่วยให้สามารถสร้างสคริปต์ที่มีปฏิสัมพันธ์กับผู้ใช้และระบบได้ดียิ่งขึ้น

# 6. Json

ต่อไปเป็นเรื่องของ package json ซึ่งใช้ในการจัดการกับข้อมูลในรูปแบบ JSON (JavaScript Object Notation) JSON เป็นรูปแบบข้อมูลที่นิยมใช้ในการแลกเปลี่ยนข้อมูลระหว่างเว็บแอปพลิเคชันและเซิร์ฟเวอร์ เนื่องจากมีโครงสร้างที่เรียบง่ายและอ่านเข้าใจได้ง่าย

ฟังก์ชันหลักๆ ใน package json ได้แก่:

1. json.dumps(obj) - แปลงออบเจ็กต์ Python เป็นสตริง JSON
2. json.loads(json_string) - แปลงสตริง JSON เป็นออบเจ็กต์ Python
3. json.dump(obj, file) - เขียนออบเจ็กต์ Python เป็น JSON ลงในไฟล์
4. json.load(file) - อ่านไฟล์ JSON และแปลงเป็นออบเจ็กต์ Python

ตัวอย่างการใช้งาน json:

```python
import json

# สร้างออบเจ็กต์ Python
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "music"],
    "married": False
}

# แปลงออบเจ็กต์ Python เป็นสตริง JSON
json_string = json.dumps(data)
print("JSON string:", json_string)

# แปลงสตริง JSON เป็นออบเจ็กต์ Python
parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)

# เขียนออบเจ็กต์ Python เป็น JSON ลงในไฟล์
with open("data.json", "w") as file:
    json.dump(data, file)

# อ่านไฟล์ JSON และแปลงเป็นออบเจ็กต์ Python
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("Loaded data:", loaded_data)
```

ในตัวอย่างนี้ เราสร้างออบเจ็กต์ Python ที่มีข้อมูลต่างๆ จากนั้นใช้ json.dumps() เพื่อแปลงออบเจ็กต์ให้เป็นสตริง JSON ใช้ json.loads() เพื่อแปลงสตริง JSON กลับเป็นออบเจ็กต์ Python เขียนออบเจ็กต์ Python ลงในไฟล์ JSON ด้วย json.dump() และอ่านไฟล์ JSON แล้วแปลงเป็นออบเจ็กต์ Python ด้วย json.load()

json เป็น package ที่มีประโยชน์อย่างมากในการทำงานกับข้อมูล JSON ไม่ว่าจะเป็นการแลกเปลี่ยนข้อมูลผ่านเว็บ API หรือการจัดเก็บข้อมูลการกำหนดค่า (configuration) ของแอปพลิเคชัน ด้วย json จะช่วยให้จัดการกับข้อมูล JSON ได้อย่างสะดวกและมีประสิทธิภาพมากขึ้น

### 7. CSV

package csv ใน Python ใช้สำหรับอ่านและเขียนไฟล์ CSV (Comma-Separated Values) ซึ่งเป็นรูปแบบไฟล์ที่นิยมใช้ในการจัดเก็บและแลกเปลี่ยนข้อมูลตารางอย่างง่าย โดยแต่ละแถวในไฟล์ CSV จะแทนข้อมูลหนึ่งระเบียน และแต่ละคอลัมน์จะถูกคั่นด้วยเครื่องหมายจุลภาค (comma)

ฟังก์ชันหลักใน package csv ได้แก่:

1. csv.reader(csvfile) - อ่านข้อมูลจากไฟล์ CSV และคืนค่าเป็นออบเจ็กต์ที่ใช้สำหรับ iterate ข้อมูลแต่ละแถว
2. csv.writer(csvfile) - เขียนข้อมูลลงในไฟล์ CSV โดยรับข้อมูลเป็นลิสต์หรือทูเพิล
3. csv.DictReader(csvfile) - อ่านข้อมูลจากไฟล์ CSV และคืนค่าเป็นออบเจ็กต์ที่ใช้สำหรับ iterate ข้อมูลแต่ละแถวในรูปแบบของ dict โดยใช้ header row เป็นคีย์
4. csv.DictWriter(csvfile, fieldnames) - เขียนข้อมูลลงในไฟล์ CSV จาก dict โดยใช้ fieldnames เป็นรายชื่อคอลัมน์

ตัวอย่างการใช้งาน csv:

```python
import csv

# เขียนข้อมูลลงในไฟล์ CSV
with open('employees.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Name', 'Department'])
    writer.writerow(['1', 'John Doe', 'Sales'])
    writer.writerow(['2', 'Jane Smith', 'Marketing'])
    writer.writerow(['3', 'Bob Johnson', 'Engineering'])

# อ่านข้อมูลจากไฟล์ CSV
with open('employees.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# เขียนข้อมูลลงในไฟล์ CSV ในรูปแบบ dict
with open('employees_dict.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Name', 'Department']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'ID': '1', 'Name': 'John Doe', 'Department': 'Sales'})
    writer.writerow({'ID': '2', 'Name': 'Jane Smith', 'Department': 'Marketing'})
    writer.writerow({'ID': '3', 'Name': 'Bob Johnson', 'Department': 'Engineering'})

# อ่านข้อมูลจากไฟล์ CSV ในรูปแบบ dict
with open('employees_dict.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(dict(row))
```

ในตัวอย่างนี้ เราใช้ csv.writer เพื่อเขียนข้อมูลลงในไฟล์ CSV ทั้งในรูปแบบของลิสต์และ dict และใช้ csv.reader และ csv.DictReader เพื่ออ่านข้อมูลจากไฟล์ CSV โดยเมื่ออ่านข้อมูลด้วย csv.DictReader จะได้ข้อมูลในรูปแบบของ dict ที่สามารถเข้าถึงข้อมูลในแต่ละคอลัมน์ด้วยชื่อคอลัมน์แทนการใช้ index

package csv เป็นเครื่องมือที่มีประโยชน์อย่างมากในการทำงานกับไฟล์ CSV ในภาษา Python โดยช่วยให้สามารถอ่านและเขียนข้อมูล CSV ได้อย่างสะดวกและรวดเร็ว ซึ่งเหมาะสำหรับงานที่ต้องจัดการกับข้อมูลตารางขนาดใหญ่ เช่น การวิเคราะห์ข้อมูล หรือการนำเข้าและส่งออกข้อมูลระหว่างแอปพลิเคชัน

## แบบฝึกหัด

ได้เลยครับ นี่คือแบบฝึกหัด 10 ข้อที่ผสมผสานการใช้งาน package ต่างๆ ของ Python ที่ได้เรียนไปแล้ว ในระดับความยากปานกลาง (Medium Level):

1.  เขียนโปรแกรมที่รับวันที่จากผู้ใช้ในรูปแบบ "YYYY-MM-DD" และแสดงผลลัพธ์เป็นชื่อวันในสัปดาห์ เช่น "Monday", "Tuesday", ฯลฯ (ใช้ datetime)

2.  สร้างฟังก์ชันที่รับพารามิเตอร์เป็นลิสต์ของตัวเลข และคืนค่าเป็นลิสต์ใหม่ที่มีเฉพาะตัวเลขที่เป็นจำนวนเฉพาะ (prime numbers) (ใช้ math และ list comprehension)

    **สำหรับวิธีตรวจสอบความเป็นจำนวนเฉพาะ สามารถทำได้ ดังนี้**

    สมมติเขาถามว่า 331 เป็นจำนวนเฉพาะหรือเปล่า ทุกคนก็คงจะเริ่มด้วยการประมาณค่ารากที่สองของ 331 ซึ่งได้ประมาณเกือบ ๆ 18 จากนั้นก็เริ่มเอาจำนวนเฉพาะไปหาร 331 ดู โดยเริ่มจาก 2, 3, 5, 7 ไปเรื่อย ๆ แต่พอเราลองไปจนถึง 17 แล้วยังไม่มีจำนวนเฉพาะสักตัวหาร 331 ลงตัว เราก็หยุดและสรุปว่า 331 เป็นจำนวนเฉพาะ โดยไม่ต้องลองเอาจำนวนเฉพาะอื่นๆ ไปหาร 331 อีกต่อไป

    มีวิธีคิดดังนี้คือ

    - ให้ `n` เป็นจำนวนนับใด ๆ (`n` เป็นจำนวนเฉพาะหรือไม่ก็เป็นจำนวนประกอบเพียงอย่างใดอย่างหนึ่ง)
    - สมมติว่า `n` เป็นจำนวนประกอบ
    - จำนวนประกอบคือจำนวนที่มีจำนวนอื่นนอกจาก 1 และตัวมันเองที่หารมันลงตัว
    - ดังนั้นมีจำนวนนับ `a` โดย `a` หาร `n` ลงตัว และ 1 < `a` < `n`
    - นั่นคือจะมีจำนวนนับ `b` ที่ 1 < `b` < `n` และ `n` = `a` \* `b`
    - โดยไม่เสียนัยสำคัญกำหนดให้ `a` <= `b` (ถ้า `a` > `b` ก็ให้สลับค่า `a` กับ `b`)
    - สังเกตว่า `a` = √(`a`^2) <= √(`a` \* `b`) = √`n`

3.  เขียนโปรแกรมที่สุ่มตัวเลขระหว่าง 1 ถึง 100 จำนวน 20 ตัว และแสดงผลลัพธ์เป็นลิสต์ที่เรียงลำดับจากน้อยไปมาก (ใช้ random และ sorted)

    ตัวอย่างการใช้ sorted

    ```python
    sorted_list = sorted([4,7,6,9,2,5,3,1,8])
    ```

4.  สร้างฟังก์ชันที่รับพารามิเตอร์เป็นเส้นทางไดเรกทอรี และคืนค่าเป็นลิสต์ของชื่อไฟล์ทั้งหมดในไดเรกทอรีนั้น (ใช้ os และ os.path) โดยใช้ `os.listdir` และ `os.path.join`

5.  เขียนโปรแกรมที่อ่านไฟล์ CSV ที่มีข้อมูลนักเรียน (ชื่อ, อายุ, เกรด) และสร้างไฟล์ CSV ใหม่ที่มีเฉพาะนักเรียนที่มีเกรดมากกว่าหรือเท่ากับ 3.5 (ใช้ csv)

    ```csv
    Alice,18,4.0
    Bob,19,3.2
    Charlie,17,3.8
    David,18,2.9
    Eve,20,3.5
    ```

6.  เขียนโปรแกรมที่อ่านข้อมูลจาก JSON ไฟล์ที่มีข้อมูลหนังสือ (ชื่อหนังสือ, ผู้แต่ง, ปีที่พิมพ์) และแสดงผลลัพธ์เป็นชื่อหนังสือที่พิมพ์หลังปี ค.ศ. 2000 (ใช้ json)
    ```json
    [
      {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
      },
      {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
      },
      {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
      },
      {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813
      },
      {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951
      }
    ]
    ```
