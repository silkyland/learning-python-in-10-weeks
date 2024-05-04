# Set

## 1. ความรู้เบื้องต้นเกี่ยวกับ Set

### 1.1. Set คืออะไร?

Set เป็นโครงสร้างข้อมูลในภาษา Python ที่ใช้เก็บข้อมูลที่ไม่ซ้ำกัน (unique) และไม่มีลำดับ (unordered) Set ถูกล้อมรอบด้วยเครื่องหมายวงเล็บปีกกา `{}` หรือสร้างจากฟังก์ชัน `set()` โดยข้อมูลภายใน Set คั่นด้วยเครื่องหมายจุลภาค (comma)

### 1.2. ลักษณะสำคัญของ Set

1. Set เก็บข้อมูลที่ไม่ซ้ำกัน (unique) หากมีการเพิ่มข้อมูลที่ซ้ำกันเข้าไปใน Set ข้อมูลจะถูกเพิ่มเข้าไปเพียงครั้งเดียว
2. Set ไม่มีลำดับ (unordered) ดังนั้นจึงไม่สามารถเข้าถึงข้อมูลด้วยการระบุตำแหน่งหรือ index ได้
3. Set เป็น mutable คือสามารถเปลี่ยนแปลงข้อมูลภายใน Set ได้ เช่น เพิ่ม ลบ หรืออัปเดตข้อมูล
4. ข้อมูลใน Set ต้องเป็น immutable เช่น ตัวเลข (number), สตริง (string) หรือ tuple ไม่สามารถใช้ข้อมูลประเภท list หรือ dictionary เป็นสมาชิกของ Set ได้

### 1.3. การสร้าง Set

Set สามารถสร้างได้หลายวิธี เช่น:

1. ใช้เครื่องหมายวงเล็บปีกกา `{}` และระบุข้อมูลภายใน Set คั่นด้วยเครื่องหมายจุลภาค

```python
my_set = {1, 2, 3, 4, 5}
```

2. ใช้ฟังก์ชัน `set()` โดยส่งข้อมูลที่ต้องการเป็น Set เข้าไปเป็นอาร์กิวเมนต์

```python
my_set = set([1, 2, 3, 4, 5])
```

3. สร้าง Empty Set ด้วยฟังก์ชัน `set()`

```python
my_set = set()
```

### 1.4. การเข้าถึงข้อมูลใน Set

เนื่องจาก Set ไม่มีลำดับ จึงไม่สามารถเข้าถึงข้อมูลด้วยการระบุตำแหน่งหรือ index ได้ แต่สามารถตรวจสอบว่าข้อมูลมีอยู่ใน Set หรือไม่ได้ด้วยคำสั่ง `in`

```python
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False
```

นอกจากนี้ ยังสามารถใช้ loop `for` เพื่อวนลูปและเข้าถึงข้อมูลใน Set ได้

```python
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
```

Set เป็นโครงสร้างข้อมูลที่มีประสิทธิภาพในการตรวจสอบการมีอยู่ของข้อมูล และการกรองข้อมูลที่ซ้ำกัน การทำความเข้าใจถึงลักษณะสำคัญและวิธีการสร้าง Set จะช่วยให้สามารถใช้ Set ได้อย่างมีประสิทธิภาพในการแก้ปัญหาต่าง ๆ

## 2. การเพิ่ม ลบ และอัปเดตข้อมูลใน Set

### 2.1. การเพิ่มข้อมูลด้วย add() และ update():

1. `add(element)` ใช้เพื่อเพิ่มข้อมูลเข้าไปใน Set

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

2. `update(iterable)` ใช้เพื่อเพิ่มข้อมูลจาก iterable เข้าไปใน Set

```python
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
```

### 2.2. การลบข้อมูลด้วย remove(), discard() และ pop():

1. `remove(element)` ใช้เพื่อลบข้อมูลออกจาก Set หากข้อมูลที่ต้องการลบไม่มีอยู่ใน Set จะเกิด KeyError

```python
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}
```

2. `discard(element)` ใช้เพื่อลบข้อมูลออกจาก Set เหมือนกับ remove() แต่ถ้าข้อมูลที่ต้องการลบไม่มีอยู่ใน Set จะไม่เกิด Error

```python
my_set = {1, 2, 3, 4, 5}
my_set.discard(6)
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

3. `pop()` ใช้เพื่อลบและคืนค่าข้อมูลแบบสุ่มออกจาก Set (เนื่องจาก Set ไม่มีลำดับ)

```python
my_set = {1, 2, 3, 4, 5}
item = my_set.pop()
print(item)  # Output: ข้อมูลสุ่มที่ถูกลบออกจาก Set
print(my_set)  # Output: Set ที่เหลือหลังจากลบข้อมูลออกไป
```

### 2.3. การล้าง Set ด้วย clear():

`clear()` ใช้เพื่อลบข้อมูลทั้งหมดออกจาก Set

```python
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)  # Output: set()
```

การเพิ่ม ลบ และอัปเดตข้อมูลใน Set เป็นเรื่องสำคัญในการจัดการกับข้อมูลใน Set การเลือกใช้เมธอดที่เหมาะสมขึ้นอยู่กับความต้องการและสถานการณ์ เช่น หากต้องการเพิ่มข้อมูลทีละชิ้น ใช้ `add()` แต่ถ้าต้องการเพิ่มข้อมูลหลายชิ้นพร้อมกัน ใช้ `update()` ในทำนองเดียวกัน หากต้องการลบข้อมูลและต้องการจัดการกับกรณีที่ข้อมูลอาจไม่มีอยู่ใน Set ให้ใช้ `discard()` แทน `remove()` เป็นต้น

## 3. การตรวจสอบสมาชิกใน Set

### 3.1. การใช้ in และ not in:

สามารถตรวจสอบว่าข้อมูลเป็นสมาชิกของ Set หรือไม่ได้โดยใช้คำสั่ง `in` และ `not in`

```python
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True
print(6 not in my_set)  # Output: True
```

- การนับจำนวนสมาชิกด้วย len():
  ใช้ฟังก์ชัน `len()` เพื่อนับจำนวนสมาชิกใน Set

```python
my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5
```

## 4. การดำเนินการเชิงตรรกะกับ Set

### 4.1. การรวม Set ด้วย union() และ |:

1. `union(set1, set2, ...)` ใช้เพื่อรวม Set ตั้งแต่ 2 Set ขึ้นไป และคืนค่าเป็น Set ใหม่

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
union_set = set1.union(set2, set3)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
```

2. `|` (Vertical bar) ใช้เพื่อรวม Set โดยใช้ Operator แทนการเรียกใช้เมธอด `union()`

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

### 4.2. การหาส่วนตัดของ Set ด้วย intersection() และ &:

1. `intersection(set1, set2, ...)` ใช้เพื่อหาส่วนตัดของ Set ตั้งแต่ 2 Set ขึ้นไป และคืนค่าเป็น Set ใหม่

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
intersection_set = set1.intersection(set2, set3)
print(intersection_set)  # Output: {3}
```

2. `&` (Ampersand) ใช้เพื่อหาส่วนตัดของ Set โดยใช้ Operator แทนการเรียกใช้เมธอด `intersection()`

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1 & set2
print(intersection_set)  # Output: {2, 3}
```

### 4.3. การหาผลต่างของ Set ด้วย difference() และ -:

1. `difference(set)` ใช้เพื่อหาผลต่างของ Set ที่เรียกใช้เมธอดกับ Set ที่ส่งเป็นอาร์กิวเมนต์ และคืนค่าเป็น Set ใหม่

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2, 3}
```

2. `-` (Minus) ใช้เพื่อหาผลต่างของ Set โดยใช้ Operator แทนการเรียกใช้เมธอด `difference()`

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2, 3}
```

### 4.4. การหา Symmetric Difference ด้วย symmetric_difference() และ ^:

1. `symmetric_difference(set)` ใช้เพื่อหาความแตกต่างสมมาตร (Symmetric Difference) ระหว่าง Set ที่เรียกใช้เมธอดกับ Set ที่ส่งเป็นอาร์กิวเมนต์ และคืนค่าเป็น Set ใหม่ (เก็บสมาชิกที่อยู่ใน Set ใดSet หนึ่ง แต่ไม่อยู่ใน Set ที่เหลือ)

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 4}
```

2. `^` (Caret) ใช้เพื่อหาความแตกต่างสมมาตรของ Set โดยใช้ Operator แทนการเรียกใช้เมธอด `symmetric_difference()`

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
sym_diff_set = set1 ^ set2
print(sym_diff_set)  # Output: {1, 4}
```

การดำเนินการเชิงตรรกะกับ Set ช่วยให้สามารถจัดการและวิเคราะห์ข้อมูลได้อย่างมีประสิทธิภาพ เช่น การหาข้อมูลที่ซ้ำกันระหว่าง Set การหาข้อมูลที่แตกต่างกันระหว่าง Set หรือการรวมข้อมูลจากหลาย Set เข้าด้วยกัน ซึ่งมีประโยชน์อย่างมากในการประมวลผลและวิเคราะห์ข้อมูล

## 5. การเปรียบเทียบ Set

### 5.1. ความเท่ากันของ Set:

สามารถเปรียบเทียบความเท่ากันของ Set โดยใช้เครื่องหมาย `==` และ `!=`

```python
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {1, 2, 3, 4}
print(set1 == set2)  # Output: True
print(set1 == set3)  # Output: False
print(set1 != set3)  # Output: True
```

### 5.2. ความสัมพันธ์แบบ Subset และ Superset:

1. Subset: Set A เป็น Subset ของ Set B เมื่อสมาชิกทุกตัวใน Set A เป็นสมาชิกของ Set B ด้วย สามารถตรวจสอบได้โดยใช้เมธอด `issubset()` หรือ Operator `<=`

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True
print(set1 <= set2)  # Output: True
```

2. Proper Subset: Set A เป็น Proper Subset ของ Set B เมื่อ Set A เป็น Subset ของ Set B และ Set A ไม่เท่ากับ Set B สามารถตรวจสอบได้โดยใช้ Operator `<`

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1 < set2)  # Output: True
```

3. Superset: Set A เป็น Superset ของ Set B เมื่อสมาชิกทุกตัวใน Set B เป็นสมาชิกของ Set A ด้วย สามารถตรวจสอบได้โดยใช้เมธอด `issuperset()` หรือ Operator `>=`

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set1.issuperset(set2))  # Output: True
print(set1 >= set2)  # Output: True
```

4. Proper Superset: Set A เป็น Proper Superset ของ Set B เมื่อ Set A เป็น Superset ของ Set B และ Set A ไม่เท่ากับ Set B สามารถตรวจสอบได้โดยใช้ Operator `>`

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set1 > set2)  # Output: True
```

การเปรียบเทียบ Set มีประโยชน์ในการตรวจสอบความสัมพันธ์ระหว่าง Set เช่น ตรวจสอบว่า Set หนึ่งเป็นส่วนหนึ่งของอีก Set หนึ่งหรือไม่ หรือตรวจสอบความเท่ากันของ Set ซึ่งสามารถนำไปประยุกต์ใช้ในการวิเคราะห์และจัดการข้อมูลได้

## 6. การวนลูปกับ Set

### 6.1. การใช้ for loop กับ Set:

สามารถใช้ for loop เพื่อวนลูปและเข้าถึงสมาชิกใน Set ได้

```python
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
```

### 6.2. การใช้ Set Comprehension:

Set Comprehension เป็นวิธีการสร้าง Set ใหม่จาก Iterable อื่น เช่น List, Tuple, หรือ Set โดยใช้รูปแบบที่กระชับ
รูปแบบทั่วไป: `{expression for item in iterable if condition}`

```python
# สร้าง Set ของตัวเลขยกกำลังสองจาก List ของตัวเลข
numbers = [1, 2, 3, 4, 5]
squared_set = {x**2 for x in numbers}
print(squared_set)  # Output: {1, 4, 9, 16, 25}

# สร้าง Set ของตัวอักษรพิมพ์ใหญ่จาก Set ของตัวอักษรพิมพ์เล็ก
lowercase_set = {'a', 'b', 'c', 'd'}
uppercase_set = {char.upper() for char in lowercase_set}
print(uppercase_set)  # Output: {'A', 'B', 'C', 'D'}
```

Set Comprehension ช่วยให้สามารถสร้าง Set ใหม่ได้อย่างกระชับและมีประสิทธิภาพ โดยเฉพาะเมื่อต้องการสร้าง Set จาก Iterable อื่น หรือต้องการกำหนดเงื่อนไขในการสร้าง Set

## 7. การประยุกต์ใช้ Set

### 7.1. การกรองข้อมูลที่ซ้ำกันด้วย Set:

เนื่องจาก Set เก็บข้อมูลที่ไม่ซ้ำกัน ดังนั้นสามารถใช้ Set ในการกรองข้อมูลที่ซ้ำกันออกจาก Iterable อื่นได้

```python
# กรองข้อมูลที่ซ้ำกันใน List
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
unique_set = set(my_list)
print(unique_set)  # Output: {1, 2, 3, 4, 5}

# กรองข้อมูลที่ซ้ำกันใน String
my_string = "Hello World"
unique_chars = set(my_string)
print(unique_chars)  # Output: {'H', 'e', 'l', 'o', ' ', 'W', 'r', 'd'}
```

### 7.2. การหาความแตกต่างระหว่างข้อมูล:

สามารถใช้ Set ในการหาความแตกต่างระหว่างข้อมูล 2 ชุดได้ โดยใช้เมธอด `difference()` หรือ Operator `-`

```python
# หาความแตกต่างระหว่าง Set ของเลขคู่และเลขคี่
even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}
difference_set = even_numbers - odd_numbers
print(difference_set)  # Output: {2, 4, 6, 8, 10}
```

### 7.3. การตรวจสอบการเป็นสมาชิกของข้อมูล:

Set มีประสิทธิภาพในการตรวจสอบการเป็นสมาชิกของข้อมูล เนื่องจากใช้ Hashing ในการจัดเก็บข้อมูล ทำให้มีความเร็วในการค้นหาสูง

```python
# ตรวจสอบว่าตัวอักษรเป็นสมาชิกของ Set หรือไม่
vowels = {'a', 'e', 'i', 'o', 'u'}
print('a' in vowels)  # Output: True
print('b' in vowels)  # Output: False
```

นอกจากนี้ ยังสามารถใช้ Set ในการแก้ปัญหาอื่น ๆ เช่น:

- หาจำนวนข้อมูลที่ไม่ซ้ำกันใน Iterable
- ตรวจสอบว่า Iterable มีข้อมูลที่ซ้ำกันหรือไม่
- หาข้อมูลที่ปรากฏในทุก Set (Intersection)
- หาข้อมูลที่ปรากฏในอย่างน้อยหนึ่ง Set (Union)

Set เป็นโครงสร้างข้อมูลที่มีประสิทธิภาพและเหมาะสำหรับการจัดการข้อมูลที่ไม่ซ้ำกัน การประยุกต์ใช้ Set อย่างเหมาะสมสามารถช่วยให้การจัดการและวิเคราะห์ข้อมูลเป็นไปอย่างมีประสิทธิภาพ
