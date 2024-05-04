# Dictionary

## 1. ความรู้เบื้องต้นเกี่ยวกับ Dictionary

### 1.1. Dictionary คืออะไร:

Dictionary เป็นโครงสร้างข้อมูลใน Python ที่ใช้ในการจัดเก็บข้อมูลในรูปแบบคู่ Key-Value ซึ่ง Key จะเป็นตัวระบุเฉพาะสำหรับข้อมูลแต่ละชุด และ Value คือค่าของข้อมูลที่สอดคล้องกับ Key นั้น ๆ Dictionary เป็นโครงสร้างข้อมูลที่ไม่เรียงลำดับ (Unordered) และสามารถเปลี่ยนแปลงได้ (Mutable)

### 1.2. โครงสร้างและส่วนประกอบของ Dictionary:

Dictionary ประกอบด้วยคู่ Key-Value ที่ถูกล้อมรอบด้วยวงเล็บปีกกา `{}` แต่ละคู่ Key-Value คั่นด้วยเครื่องหมายจุลภาค (Comma) โดย Key และ Value คั่นด้วยเครื่องหมายทวิภาค (Colon) Key ใน Dictionary ต้องเป็นข้อมูลที่ไม่สามารถเปลี่ยนแปลงได้ (Immutable) เช่น String, Number หรือ Tuple ส่วน Value สามารถเป็นข้อมูลชนิดใดก็ได้ รวมถึง Dictionary อื่น ๆ

### ตัวอย่าง:

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
```

### 1.3. การสร้าง Dictionary:

สามารถสร้าง Dictionary ได้หลายวิธี เช่น:

1. ใช้วงเล็บปีกกา `{}` และระบุคู่ Key-Value ข้างใน

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```

2. ใช้ Constructor `dict()` และส่งคู่ Key-Value เป็น Keyword Arguments

```python
my_dict = dict(key1='value1', key2='value2')
```

1.3. ใช้ Constructor `dict()` และส่ง Iterable ของคู่ (Tuple) ของ Key และ Value

```python
my_dict = dict([('key1', 'value1'), ('key2', 'value2')])
```

### 1.4. การเข้าถึงและแก้ไขข้อมูลใน Dictionary:

สามารถเข้าถึงและแก้ไขข้อมูลใน Dictionary ได้โดยใช้ Key ในวงเล็บเหลี่ยม `[]`

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])  # Output: 'John'
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31}
```

หากพยายามเข้าถึง Key ที่ไม่มีอยู่ใน Dictionary จะเกิด `KeyError` ขึ้น สามารถใช้เมธอด `get()` เพื่อหลีกเลี่ยง `KeyError` โดยระบุค่าเริ่มต้นที่จะส่งกลับหาก Key ไม่พบ

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.get('city', 'Unknown'))  # Output: 'Unknown'
```

## 2. การจัดการและปรับเปลี่ยน Dictionary

### 2.1. การเพิ่มและลบ Key-Value Pairs ใน Dictionary:

สามารถเพิ่ม Key-Value Pair ใหม่เข้าไปใน Dictionary ได้โดยใช้วงเล็บเหลี่ยม `[]` และกำหนด Key ที่ต้องการเพิ่ม ตามด้วย Value ที่ต้องการ

```python
my_dict = {'name': 'John', 'age': 30}
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

สามารถลบ Key-Value Pair ออกจาก Dictionary ได้โดยใช้คำสั่ง `del` ตามด้วย Dictionary และ Key ที่ต้องการลบ

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 30}
```

### 2.2. การใช้เมธอด keys(), values(), items():

1. `keys()` ใช้สำหรับดึง Keys ทั้งหมดใน Dictionary ออกมาเป็น Dictionary View Object
2. `values()` ใช้สำหรับดึง Values ทั้งหมดใน Dictionary ออกมาเป็น Dictionary View Object
3. `items()` ใช้สำหรับดึงคู่ Key-Value ทั้งหมดใน Dictionary ออกมาเป็น Dictionary View Object ซึ่งแต่ละคู่จะอยู่ในรูปแบบ Tuple

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
print(keys)    # Output: dict_keys(['name', 'age', 'city'])
print(values)  # Output: dict_values(['John', 30, 'New York'])
print(items)   # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
```

### 2.3. การตรวจสอบการมีอยู่ของ Key ใน Dictionary:

สามารถตรวจสอบว่า Key มีอยู่ใน Dictionary หรือไม่โดยใช้คำสั่ง `in`

```python
my_dict = {'name': 'John', 'age': 30}
print('name' in my_dict)  # Output: True
print('city' in my_dict)  # Output: False
```

### 2.4. การใช้ get() และ setdefault():

1. `get(key[, default])` ใช้สำหรับดึงค่า Value ของ Key ที่ระบุ หากไม่พบ Key จะส่งคืนค่า default (ค่าเริ่มต้นเป็น None)

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.get('name'))     # Output: 'John'
print(my_dict.get('city'))     # Output: None
print(my_dict.get('city', 'Unknown'))  # Output: 'Unknown'
```

2. `setdefault(key[, default])` ใช้สำหรับดึงค่า Value ของ Key ที่ระบุ หากไม่พบ Key จะเพิ่ม Key นั้นเข้าไปใน Dictionary พร้อมกับ Value เป็นค่า default (ค่าเริ่มต้นเป็น None)

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.setdefault('name'))  # Output: 'John'
print(my_dict.setdefault('city'))  # Output: None
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': None}
```

### 2.5 การใช้ update() เพื่ออัปเดต Dictionary:

`update([other])` ใช้สำหรับอัปเดต Dictionary ด้วยคู่ Key-Value จาก Dictionary อื่น หรือจาก Iterable ของคู่ Key-Value

```python
my_dict = {'name': 'John', 'age': 30}
my_dict.update({'age': 31, 'city': 'New York'})
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

my_dict.update([('country', 'USA'), ('phone', '1234567890')])
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA', 'phone': '1234567890'}
```

## 3. การวนลูปและการใช้ Dictionary กับ Loop

### 3.1. การวนลูปผ่าน Keys ของ Dictionary:

สามารถวนลูปผ่าน Keys ของ Dictionary ได้โดยใช้คำสั่ง `for` ร่วมกับเมธอด `keys()` หรือวนลูปผ่าน Dictionary โดยตรง (ซึ่งจะวนลูปผ่าน Keys เช่นกัน)

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for key in my_dict.keys():
    print(key)
# Output:
# name
# age
# city

for key in my_dict:
    print(key)
# Output:
# name
# age
# city
```

## 3.2. การวนลูปผ่าน Values ของ Dictionary:

สามารถวนลูปผ่าน Values ของ Dictionary ได้โดยใช้คำสั่ง `for` ร่วมกับเมธอด `values()`

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for value in my_dict.values():
    print(value)
# Output:
# John
# 30
# New York
```

## 3.3. การวนลูปผ่าน Key-Value Pairs ของ Dictionary:

สามารถวนลูปผ่านคู่ Key-Value ของ Dictionary ได้โดยใช้คำสั่ง `for` ร่วมกับเมธอด `items()` ซึ่งจะให้ผลลัพธ์เป็น Tuple ของคู่ Key-Value ในแต่ละรอบของลูป

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in my_dict.items():
    print(key + ':', value)
# Output:
# name: John
# age: 30
# city: New York
```

### 3.4. การใช้ Dictionary Comprehension:

Dictionary Comprehension เป็นวิธีการสร้าง Dictionary ใหม่จาก Iterable อื่น เช่น List หรือ Tuple โดยใช้รูปแบบที่กระชับ
รูปแบบทั่วไป: `{key_expression: value_expression for item in iterable if condition}`

```python
# สร้าง Dictionary ที่มี Key เป็นตัวเลข และ Value เป็นกำลังสองของตัวเลขนั้น
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# สร้าง Dictionary จาก List ของคู่ Key-Value โดยมีเงื่อนไข
my_list = [('a', 1), ('b', 2), ('c', 3), ('a', 4)]
my_dict = {key: value for key, value in my_list if value % 2 == 0}
print(my_dict)  # Output: {'b': 2, 'a': 4}
```

Dictionary Comprehension เป็นวิธีที่มีประสิทธิภาพและเขียนโค้ดได้กระชับในการสร้าง Dictionary ใหม่ โดยเฉพาะเมื่อต้องการสร้าง Dictionary จาก Iterable อื่น หรือต้องการกำหนดเงื่อนไขในการสร้าง Dictionary

## 4. การประยุกต์ใช้ Dictionary

### 4.1. การใช้ Dictionary ในการนับจำนวนและความถี่:

Dictionary สามารถใช้ในการนับจำนวนหรือความถี่ของข้อมูลได้อย่างมีประสิทธิภาพ โดยใช้ข้อมูลเป็น Key และจำนวนหรือความถี่เป็น Value

```python
# นับจำนวนตัวอักษรในสตริง
string = "hello world"
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# นับจำนวนคำในประโยค
sentence = "the quick brown fox jumps over the lazy dog"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

### 4.2. การใช้ Dictionary ในการจับคู่และแมป (Mapping) ข้อมูล:

Dictionary สามารถใช้ในการจับคู่ข้อมูลจากชุดหนึ่งไปยังอีกชุดหนึ่งได้ โดยใช้ข้อมูลจากชุดแรกเป็น Key และข้อมูลจากชุดที่สองเป็น Value

```python
# แมปชื่อประเทศเป็นรหัสประเทศ
country_code = {'USA': 1, 'BRA': 55, 'CHN': 86, 'THA': 66}
country_name = 'THA'
print(country_code[country_name])  # Output: 66

# แมปรหัสนักศึกษากับชื่อนักศึกษา
student_id = {'001': 'John', '002': 'Jane', '003': 'Bob'}
student_info = [('001', 'Male', '01/01/2000'), ('002', 'Female', '02/02/2000'), ('003', 'Male', '03/03/2000')]
for id, gender, dob in student_info:
    name = student_id[id]
    print(name, gender, dob)
# Output:
# John Male 01/01/2000
# Jane Female 02/02/2000
# Bob Male 03/03/2000
```

### 4.3. การใช้ Dictionary ในการกรองและจัดกลุ่มข้อมูล:

Dictionary สามารถใช้ในการกรองและจัดกลุ่มข้อมูลได้ โดยใช้ Key เป็นเงื่อนไขในการกรองหรือจัดกลุ่ม

```python
# กรองข้อมูลตามเงื่อนไข
scores = {'John': 85, 'Jane': 92, 'Bob': 78, 'Alice': 90}
passed_students = {name: score for name, score in scores.items() if score >= 80}
print(passed_students)  # Output: {'John': 85, 'Jane': 92, 'Alice': 90}

# จัดกลุ่มข้อมูลตามเงื่อนไข
students = {'John': 'A', 'Jane': 'B', 'Bob': 'C', 'Alice': 'A', 'Mike': 'B'}
grade_groups = {}
for name, grade in students.items():
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append(name)
print(grade_groups)  # Output: {'A': ['John', 'Alice'], 'B': ['Jane', 'Mike'], 'C': ['Bob']}
```

Dictionary เป็นโครงสร้างข้อมูลที่มีประสิทธิภาพและยืดหยุ่นสูง สามารถนำไปประยุกต์ใช้ในการแก้ปัญหาและจัดการข้อมูลได้หลากหลาย ไม่ว่าจะเป็นการนับจำนวน การจับคู่ข้อมูล หรือการกรองและจัดกลุ่มข้อมูล

## 5. ข้อควรรู้เพิ่มเติมเกี่ยวกับ Dictionary

### 5.1. การเปรียบเทียบ Dictionary:

ในการเปรียบเทียบ Dictionary สองตัว จะเปรียบเทียบโดยดูที่ความเท่ากันของคู่ Key-Value โดยไม่สนใจลำดับของคู่ Key-Value

```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'a': 1, 'b': 2}
dict3 = {'a': 1, 'b': 2}
print(dict1 == dict2)  # Output: True
print(dict1 == dict3)  # Output: False
```

### 5.2. การคัดลอก Dictionary:

ในการคัดลอก Dictionary สามารถใช้เมธอด `copy()` หรือฟังก์ชัน `dict()` เพื่อสร้าง Shallow Copy ของ Dictionary ได้ (Shallow Copy คือการคัดลอกโดยที่ Object ที่อยู่ภายใน Dictionary จะถูกอ้างอิงแบบเดียวกันกับ Dictionary ต้นฉบับ)

```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = dict1.copy()
dict3 = dict(dict1)
print(dict2)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(dict3)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

### 5.3. การรวม Dictionary:

ในการรวม Dictionary สองตัวเข้าด้วยกัน สามารถใช้เมธอด `update()` หรือ Unpacking Operator (`**`) ในรูปแบบ Dictionary Comprehension ได้

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict3 = {**dict1, **dict2}
print(dict3)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### 5.4. การใช้ Dictionary กับฟังก์ชัน:

Dictionary สามารถใช้เป็น Keyword Arguments ในการเรียกใช้ฟังก์ชันได้ โดยใช้ Unpacking Operator (`**`)

```python
def my_func(a, b, c):
    print(a, b, c)

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_func(**my_dict)  # Output: 1 2 3
```

นอกจากนี้ ยังสามารถใช้ Dictionary ในการรับ Keyword Arguments ที่ไม่ได้ระบุชื่อไว้ล่วงหน้าในฟังก์ชันได้ด้วย โดยใช้ `**kwargs` ในพารามิเตอร์ของฟังก์ชัน

```python
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_func(a=1, b=2, c=3)
# Output:
# a 1
# b 2
# c 3
```

Dictionary เป็นโครงสร้างข้อมูลที่มีความสามารถและความยืดหยุ่นสูง สามารถนำไปใช้ในสถานการณ์ต่าง ๆ ได้อย่างมีประสิทธิภาพ ไม่ว่าจะเป็นการจัดเก็บและจัดการข้อมูล การประมวลผลข้อมูล หรือการใช้งานร่วมกับฟังก์ชันต่าง ๆ ความเข้าใจที่ดีเกี่ยวกับคุณสมบัติและวิธีการใช้งาน Dictionary จะช่วยให้สามารถเขียนโปรแกรมได้อย่างมีประสิทธิภาพและตรงตามวัตถุประสงค์มากยิ่งขึ้น

## แบบฝึกหัด

1. จงเขียนโปรแกรมที่รับชื่อและคะแนนของนักเรียน 5 คน จากนั้นเก็บข้อมูลลงใน Dictionary และแสดงชื่อและคะแนนของนักเรียนที่ได้คะแนนสูงสุด

2. จงเขียนโปรแกรมที่รับข้อความ (string) จากผู้ใช้ จากนั้นนับจำนวนตัวอักษรแต่ละตัวที่ปรากฏในข้อความและเก็บลงใน Dictionary แล้วแสดงผลลัพธ์

3. จงเขียนโปรแกรมที่สร้าง Dictionary ซึ่งเก็บข้อมูลของพนักงาน 3 คน โดยมี key เป็นชื่อพนักงาน และ value เป็น tuple ของอายุและเงินเดือน จากนั้นให้คำนวณและแสดงผลรวมของอายุและเงินเดือนของพนักงานทั้งหมด

4. จงเขียนโปรแกรมที่รับ Dictionary สองตัว จากนั้นให้รวม Dictionary ทั้งสองเข้าด้วยกัน โดยกรณีที่มี key ซ้ำกัน ให้ใช้ value ของ Dictionary ตัวที่สอง

5. จงเขียนโปรแกรมที่รับ List ของตัวเลข จากนั้นสร้าง Dictionary ที่มี key เป็นตัวเลขใน List และ value เป็นกำลังสองของตัวเลขนั้น โดยใช้ Dictionary Comprehension
