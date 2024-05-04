# List

### 1. ความรู้เบื้องต้นเกี่ยวกับ List

**1.1 List คืออะไร**

- List เป็นโครงสร้างข้อมูลแบบลำดับ (Sequence Data Type) ใน Python ที่ใช้จัดเก็บข้อมูลหลายค่าไว้ในตัวแปรเดียว
- List สามารถเก็บข้อมูลได้หลากหลายประเภท เช่น ตัวเลข, สตริง, หรือแม้แต่ List อื่นๆ
- List เป็นโครงสร้างข้อมูลที่มีลำดับ (Ordered) และสามารถแก้ไขข้อมูลได้ (Mutable)

**1.2 ประโยชน์และการใช้งานของ List**

- ใช้เก็บกลุ่มของข้อมูลที่มีความสัมพันธ์กัน เช่น รายชื่อนักเรียน, คะแนนสอบ, หรือรายการสินค้า
- ช่วยให้การจัดการและเข้าถึงข้อมูลทำได้ง่ายและมีประสิทธิภาพมากขึ้น
- สามารถนำไปประยุกต์ใช้ในการแก้ปัญหาและพัฒนาโปรแกรมต่างๆ ได้

**1.3 การสร้าง List**

- List สร้างได้โดยใช้เครื่องหมาย [] (Square Brackets) และคั่นแต่ละข้อมูลด้วยเครื่องหมาย , (Comma)
- ตัวอย่างการสร้าง List เก็บตัวเลข:

```python
numbers = [1, 2, 3, 4, 5]
```

- ตัวอย่างการสร้าง List เก็บสตริง:

```python
fruits = ['apple', 'banana', 'orange']
```

**1.4 การเข้าถึงและแก้ไขข้อมูลใน List**

- ในการเข้าถึงข้อมูลใน List สามารถใช้ Index (ตำแหน่ง) ของข้อมูลนั้นๆ ได้
- Index ใน List เริ่มต้นที่ 0 สำหรับข้อมูลตัวแรก และเพิ่มขึ้นทีละ 1 สำหรับข้อมูลถัดไป
- ตัวอย่างการเข้าถึงข้อมูลใน List:

```python
fruits = ['apple', 'banana', 'orange']
print(fruits[0])  # Output: 'apple'
print(fruits[1])  # Output: 'banana'
```

- สามารถใช้ Index ในการแก้ไขข้อมูลได้ด้วย:

```python
fruits = ['apple', 'banana', 'orange']
fruits[1] = 'grape'
print(fruits)  # Output: ['apple', 'grape', 'orange']
```

**1.5 การใช้ Negative Index**

- นอกจาก Index ปกติแล้ว สามารถใช้ Negative Index ในการเข้าถึงข้อมูลจากท้าย List ได้ด้วย
- Negative Index เริ่มต้นที่ -1 สำหรับข้อมูลตัวสุดท้าย และลดลงทีละ 1 สำหรับข้อมูลก่อนหน้า
- ตัวอย่างการใช้ Negative Index:

```python
fruits = ['apple', 'banana', 'orange']
print(fruits[-1])  # Output: 'orange'
print(fruits[-2])  # Output: 'banana'
```

### 2. การจัดการและปรับเปลี่ยน List

**2.1 การเพิ่มและลบข้อมูลใน List**

- append(element): ใช้เพิ่มข้อมูล element ไปท้าย List

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]
```

- extend(iterable): ใช้เพิ่มข้อมูลจาก iterable (เช่น List อื่น) ไปท้าย List

```python
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)  # Output: [1, 2, 3, 4, 5]
```

- insert(index, element): ใช้แทรกข้อมูล element ลงใน List ที่ตำแหน่ง index

```python
numbers = [1, 2, 3]
numbers.insert(1, 1.5)
print(numbers)  # Output: [1, 1.5, 2, 3]
```

- remove(element): ใช้ลบข้อมูล element ตัวแรกที่พบใน List

```python
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'banana']
```

- pop(index): ใช้ลบข้อมูลที่ตำแหน่ง index ออกจาก List และคืนค่าข้อมูลนั้น (ถ้าไม่ระบุ index จะลบข้อมูลตัวสุดท้าย)

```python
numbers = [1, 2, 3]
removed_number = numbers.pop(1)
print(numbers)  # Output: [1, 3]
print(removed_number)  # Output: 2
```

- clear(): ใช้ลบข้อมูลทั้งหมดออกจาก List

```python
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # Output: []
```

**2.2 การค้นหาข้อมูลใน List**

- index(element): ใช้หา Index ของข้อมูล element ใน List (ถ้าไม่พบจะเกิด ValueError)

```python
fruits = ['apple', 'banana', 'orange']
index = fruits.index('banana')
print(index)  # Output: 1
```

- count(element): ใช้นับจำนวนข้อมูล element ที่ปรากฏใน List

```python
fruits = ['apple', 'banana', 'orange', 'banana']
count = fruits.count('banana')
print(count)  # Output: 2
```

**2.3 การเรียงลำดับข้อมูลใน List**

- sort(): ใช้เรียงลำดับข้อมูลใน List จากน้อยไปมาก (สามารถกำหนด Key Function และ Reverse ได้)

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

- reverse(): ใช้กลับลำดับข้อมูลใน List

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]
```

**2.4 การคัดลอก List**

- copy(): ใช้สร้าง Shallow Copy ของ List

```python
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3]
```

- list(iterable): ใช้สร้าง List ใหม่จาก Iterable

```python
original_list = [1, 2, 3]
new_list = list(original_list)
print(new_list)  # Output: [1, 2, 3]
```

### 3. การใช้ List Comprehension

**3.1 รูปแบบและไวยากรณ์ของ List Comprehension**

- List Comprehension เป็นวิธีการสร้าง List ใหม่จากการประมวลผล Iterable อื่น เช่น List, Tuple, หรือ Dictionary
- รูปแบบทั่วไปของ List Comprehension:

```
new_list = [expression for item in iterable if condition]
```

- `expression`: นิพจน์ที่ใช้กำหนดค่าสำหรับแต่ละรายการใน List ใหม่
- `item`: ตัวแปรที่ใช้อ้างอิงถึงแต่ละรายการใน Iterable
- `iterable`: Iterable ที่ต้องการประมวลผล เช่น List, Tuple, หรือ Dictionary
- `condition` (ไม่จำเป็น): เงื่อนไขที่ใช้กรองรายการจาก Iterable

**3.2 การสร้าง List ด้วย List Comprehension**

- ตัวอย่างการสร้าง List ใหม่ที่เก็บค่ากำลังสองของตัวเลขใน List เดิม:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

- ตัวอย่างการสร้าง List ใหม่ที่เก็บความยาวของสตริงใน List เดิม:

```python
fruits = ['apple', 'banana', 'orange']
lengths = [len(fruit) for fruit in fruits]
print(lengths)  # Output: [5, 6, 6]
```

**3.3 การใช้เงื่อนไขใน List Comprehension**

- สามารถใช้เงื่อนไข `if` ใน List Comprehension เพื่อกรองรายการที่ต้องการได้
- ตัวอย่างการสร้าง List ใหม่ที่เก็บเฉพาะตัวเลขคู่จาก List เดิม:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]
```

- สามารถใช้เงื่อนไข `if-else` ใน List Comprehension เพื่อกำหนดค่าตามเงื่อนไขได้
- ตัวอย่างการสร้าง List ใหม่ที่เก็บ 'even' หรือ 'odd' ตามเงื่อนไขของตัวเลขใน List เดิม:

```python
numbers = [1, 2, 3, 4, 5]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd']
```

List Comprehension เป็นเครื่องมือที่ทรงพลังและช่วยให้สามารถสร้าง List ใหม่ได้อย่างกระชับและมีประสิทธิภาพ โดยสามารถใช้นิพจน์และเงื่อนไขต่างๆ ในการกำหนดค่าและกรองรายการตามต้องการ

### การใช้ List กับ Loop และ Conditional Statement

**4.1 การวนลูปข้อมูลใน List ด้วย for loop**

- ใช้ for loop เพื่อวนลูปและเข้าถึงข้อมูลในแต่ละรายการของ List
- รูปแบบการใช้ for loop กับ List:

```python
for item in list:
    # คำสั่งที่ต้องการทำกับแต่ละรายการ
```

- ตัวอย่างการใช้ for loop เพื่อแสดงข้อมูลใน List:

```python
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# orange
```

- ตัวอย่างการใช้ for loop เพื่อหาผลรวมของตัวเลขใน List:

```python
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)  # Output: 15
```

**4.2 การใช้ List กับ if-else statement**

- สามารถใช้ if-else statement ร่วมกับ List เพื่อตรวจสอบเงื่อนไขและดำเนินการตามต้องการ
- ตัวอย่างการใช้ if-else statement เพื่อตรวจสอบว่ามีรายการที่ต้องการอยู่ใน List หรือไม่:

```python
fruits = ['apple', 'banana', 'orange']
if 'banana' in fruits:
    print('Banana is in the list')
else:
    print('Banana is not in the list')
# Output: Banana is in the list
```

- ตัวอย่างการใช้ if-else statement เพื่อตรวจสอบเงื่อนไขของแต่ละรายการใน List:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')
# Output:
# 1 is odd
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd
```

การใช้ List กับ Loop และ Conditional Statement เป็นเทคนิคที่มีประโยชน์มากในการประมวลผลและตรวจสอบข้อมูลใน List โดยสามารถใช้ for loop ในการวนลูปและเข้าถึงข้อมูลในแต่ละรายการ และใช้ if-else statement ในการตรวจสอบเงื่อนไขและดำเนินการตามต้องการ

### การประยุกต์ใช้ List ในการแก้ปัญหา

**5.1 ตัวอย่างการใช้ List ในการแก้ปัญหาต่างๆ**

- List เป็นโครงสร้างข้อมูลที่มีประโยชน์และสามารถนำไปประยุกต์ใช้ในการแก้ปัญหาหลากหลายประเภท
- ตัวอย่างการใช้ List เพื่อเก็บข้อมูลและคำนวณค่าเฉลี่ย:

```python
scores = [85, 92, 78, 90, 88]
sum_scores = sum(scores)
average = sum_scores / len(scores)
print('Average score:', average)  # Output: Average score: 86.6
```

- ตัวอย่างการใช้ List เพื่อเก็บข้อมูลและหาค่ามากที่สุด (Maximum):

```python
numbers = [12, 45, 23, 56, 78, 34, 90]
max_number = max(numbers)
print('Maximum number:', max_number)  # Output: Maximum number: 90
```

- ตัวอย่างการใช้ List เพื่อเก็บข้อมูลและกรองเฉพาะข้อมูลที่ต้องการ:

```python
ages = [25, 18, 32, 16, 40, 28, 19]
adults = [age for age in ages if age >= 18]
print('Ages of adults:', adults)  # Output: Ages of adults: [25, 18, 32, 40, 28, 19]
```

- ตัวอย่างการใช้ List เพื่อเก็บข้อมูลและหาความถี่ (Frequency) ของข้อมูล:

```python
fruits = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
freq_apple = fruits.count('apple')
freq_banana = fruits.count('banana')
freq_orange = fruits.count('orange')
print('Frequency of apple:', freq_apple)  # Output: Frequency of apple: 3
print('Frequency of banana:', freq_banana)  # Output: Frequency of banana: 2
print('Frequency of orange:', freq_orange)  # Output: Frequency of orange: 1
```

นี่เป็นเพียงตัวอย่างบางส่วนของการประยุกต์ใช้ List ในการแก้ปัญหาต่างๆ ซึ่งแสดงให้เห็นถึงความยืดหยุ่นและประโยชน์ของ List ในการจัดเก็บและจัดการข้อมูล List สามารถนำไปใช้ในสถานการณ์ที่หลากหลาย เช่น การจัดเก็บข้อมูล การค้นหา การกรอง การคำนวณ และอื่นๆ อีกมากมาย

---

### แบบฝึกหัด

1. ให้สร้าง List ชื่อ `names` ที่เก็บชื่อ 5 คน และแสดงชื่อคนที่อยู่ตำแหน่งที่ 2 และ 4

2. ให้เพิ่มชื่อ 2 คนลงใน List `names` โดยให้คนแรกอยู่ท้าย List และคนที่สองอยู่ต้น List จากนั้นแสดง List ที่ได้

3. ให้ใช้ List Comprehension สร้าง List ใหม่ชื่อ `even_numbers` ที่เก็บเลขคู่ตั้งแต่ 1 ถึง 10

4. ให้เขียนโปรแกรมรับตัวเลขจากผู้ใช้ 5 ตัว เก็บใน List ชื่อ `user_numbers` จากนั้นหาผลรวมของตัวเลขทั้งหมดใน List และแสดงผลลัพธ์

5. ให้เขียนโปรแกรมรับชื่อผลไม้จากผู้ใช้ไปเรื่อยๆ จนกว่าผู้ใช้จะพิมพ์ 'q' เพื่อหยุด จากนั้นแสดงชื่อผลไม้ทั้งหมดที่ผู้ใช้ป้อนเข้ามา

หวังว่าเนื้อหา ตัวอย่าง และแบบฝึกหัดเหล่านี้จะเป็นประโยชน์สำหรับการสอนของคุณนะครับ ถ้ามีอะไรเพิ่มเติม สามารถถามได้เลย ผมยินดีช่วยเหลือครับ!
