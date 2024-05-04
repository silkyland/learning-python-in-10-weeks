# Dictionary

### 1. ความรู้เบื้องต้นเกี่ยวกับ Dictionary

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

---

### 2. การจัดการและปรับเปลี่ยน Dictionary

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
