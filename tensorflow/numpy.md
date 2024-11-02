```python
import numpy as np

# 1. การสร้าง Array พื้นฐาน
print("1. การสร้าง Array พื้นฐาน")
print("-" * 50)

# สร้าง array 1 มิติ
array_1d = np.array([1, 2, 3, 4, 5])
print("Array 1 มิติ:", array_1d)

# สร้าง array 2 มิติ
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
print("\nArray 2 มิติ:\n", array_2d)

# สร้าง array พิเศษ
zeros = np.zeros((2, 3))  # array ที่มีแต่เลข 0
ones = np.ones((2, 3))    # array ที่มีแต่เลข 1
random_array = np.random.rand(2, 3)  # array สุ่ม

print("\nArray ที่มีแต่เลข 0:\n", zeros)
print("\nArray ที่มีแต่เลข 1:\n", ones)
print("\nArray สุ่ม:\n", random_array)

# 2. การดูข้อมูลของ Array
print("\n2. การดูข้อมูลของ Array")
print("-" * 50)

print("รูปร่างของ array:", array_2d.shape)
print("จำนวนมิติ:", array_2d.ndim)
print("ประเภทข้อมูล:", array_2d.dtype)
print("จำนวนข้อมูลทั้งหมด:", array_2d.size)

# 3. การเข้าถึงข้อมูล (Indexing และ Slicing)
print("\n3. การเข้าถึงข้อมูล")
print("-" * 50)

# สร้าง array ตัวอย่าง
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Array ต้นฉบับ:\n", arr)
print("\nข้อมูลแถวที่ 1:", arr[1])
print("ข้อมูลที่ตำแหน่ง [1,2]:", arr[1,2])
print("ข้อมูลแถวที่ 0-1:\n", arr[0:2])
print("ข้อมูลคอลัมน์ที่ 1:\n", arr[:,1])

# 4. การคำนวณพื้นฐาน
print("\n4. การคำนวณพื้นฐาน")
print("-" * 50)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)
print("\nการบวก:", a + b)
print("การคูณ:", a * b)
print("ยกกำลัง:", a ** 2)
print("ค่าเฉลี่ย:", a.mean())
print("ผลรวม:", a.sum())
print("ค่าต่ำสุด:", a.min())
print("ค่าสูงสุด:", a.max())

# 5. การคำนวณทางสถิติ
print("\n5. การคำนวณทางสถิติ")
print("-" * 50)

data = np.array([15, 23, 45, 67, 12, 89, 34, 56])
print("ข้อมูล:", data)
print("ค่าเฉลี่ย:", np.mean(data))
print("ส่วนเบี่ยงเบนมาตรฐาน:", np.std(data))
print("มัธยฐาน:", np.median(data))
print("เปอร์เซ็นไทล์ที่ 75:", np.percentile(data, 75))

# 6. การแปลงรูปร่าง Array (Reshaping)
print("\n6. การแปลงรูปร่าง Array")
print("-" * 50)

arr = np.array([1, 2, 3, 4, 5, 6])
print("Array เดิม:", arr)
print("Reshape เป็น 2x3:\n", arr.reshape(2, 3))
print("Reshape เป็น 3x2:\n", arr.reshape(3, 2))

# 7. ตัวอย่างการใช้งานจริง
print("\n7. ตัวอย่างการใช้งานจริง")
print("-" * 50)

# สร้างข้อมูลคะแนนสอบ
scores = np.array([[85, 90, 75],   # นักเรียนคนที่ 1
                   [77, 88, 92],   # นักเรียนคนที่ 2
                   [95, 85, 85]])  # นักเรียนคนที่ 3

weights = np.array([0.3, 0.3, 0.4])  # น้ำหนักคะแนนแต่ละวิชา

print("คะแนนสอบ:\n", scores)
print("\nน้ำหนักคะแนน:", weights)

# คำนวณคะแนนเฉลี่ยถ่วงน้ำหนัก
weighted_scores = np.dot(scores, weights)
print("\nคะแนนเฉลี่ยถ่วงน้ำหนักของแต่ละคน:", weighted_scores)

# หาคนที่ได้คะแนนสูงสุด
top_student = np.argmax(weighted_scores)
print("นักเรียนที่ได้คะแนนสูงสุดคือคนที่:", top_student + 1)

```


```python
import numpy as np

# 1. การสร้าง Array พื้นฐาน
print("1. การสร้าง Array พื้นฐาน")
print("-" * 50)

# สร้าง array 1 มิติ
array_1d = np.array([1, 2, 3, 4, 5])
print("Array 1 มิติ:", array_1d)

# สร้าง array 2 มิติ
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
print("\nArray 2 มิติ:\n", array_2d)

# สร้าง array พิเศษ
zeros = np.zeros((2, 3))  # array ที่มีแต่เลข 0
ones = np.ones((2, 3))    # array ที่มีแต่เลข 1
random_array = np.random.rand(2, 3)  # array สุ่ม

print("\nArray ที่มีแต่เลข 0:\n", zeros)
print("\nArray ที่มีแต่เลข 1:\n", ones)
print("\nArray สุ่ม:\n", random_array)

# 2. การดูข้อมูลของ Array
print("\n2. การดูข้อมูลของ Array")
print("-" * 50)

print("รูปร่างของ array:", array_2d.shape)
print("จำนวนมิติ:", array_2d.ndim)
print("ประเภทข้อมูล:", array_2d.dtype)
print("จำนวนข้อมูลทั้งหมด:", array_2d.size)

# 3. การเข้าถึงข้อมูล (Indexing และ Slicing)
print("\n3. การเข้าถึงข้อมูล")
print("-" * 50)

# สร้าง array ตัวอย่าง
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Array ต้นฉบับ:\n", arr)
print("\nข้อมูลแถวที่ 1:", arr[1])
print("ข้อมูลที่ตำแหน่ง [1,2]:", arr[1,2])
print("ข้อมูลแถวที่ 0-1:\n", arr[0:2])
print("ข้อมูลคอลัมน์ที่ 1:\n", arr[:,1])

# 4. การคำนวณพื้นฐาน
print("\n4. การคำนวณพื้นฐาน")
print("-" * 50)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)
print("\nการบวก:", a + b)
print("การคูณ:", a * b)
print("ยกกำลัง:", a ** 2)
print("ค่าเฉลี่ย:", a.mean())
print("ผลรวม:", a.sum())
print("ค่าต่ำสุด:", a.min())
print("ค่าสูงสุด:", a.max())

# 5. การคำนวณทางสถิติ
print("\n5. การคำนวณทางสถิติ")
print("-" * 50)

data = np.array([15, 23, 45, 67, 12, 89, 34, 56])
print("ข้อมูล:", data)
print("ค่าเฉลี่ย:", np.mean(data))
print("ส่วนเบี่ยงเบนมาตรฐาน:", np.std(data))
print("มัธยฐาน:", np.median(data))
print("เปอร์เซ็นไทล์ที่ 75:", np.percentile(data, 75))

# 6. การแปลงรูปร่าง Array (Reshaping)
print("\n6. การแปลงรูปร่าง Array")
print("-" * 50)

arr = np.array([1, 2, 3, 4, 5, 6])
print("Array เดิม:", arr)
print("Reshape เป็น 2x3:\n", arr.reshape(2, 3))
print("Reshape เป็น 3x2:\n", arr.reshape(3, 2))

# 7. ตัวอย่างการใช้งานจริง
print("\n7. ตัวอย่างการใช้งานจริง")
print("-" * 50)

# สร้างข้อมูลคะแนนสอบ
scores = np.array([[85, 90, 75],   # นักเรียนคนที่ 1
                   [77, 88, 92],   # นักเรียนคนที่ 2
                   [95, 85, 85]])  # นักเรียนคนที่ 3

weights = np.array([0.3, 0.3, 0.4])  # น้ำหนักคะแนนแต่ละวิชา

print("คะแนนสอบ:\n", scores)
print("\nน้ำหนักคะแนน:", weights)

# คำนวณคะแนนเฉลี่ยถ่วงน้ำหนัก
weighted_scores = np.dot(scores, weights)
print("\nคะแนนเฉลี่ยถ่วงน้ำหนักของแต่ละคน:", weighted_scores)

# หาคนที่ได้คะแนนสูงสุด
top_student = np.argmax(weighted_scores)
print("นักเรียนที่ได้คะแนนสูงสุดคือคนที่:", top_student + 1)

```


1. ประโยชน์ของ NumPy
   - ทำงานกับข้อมูลจำนวนมากได้เร็วกว่า Python ปกติ
   - มีฟังก์ชันคณิตศาสตร์และสถิติพร้อมใช้
   - เป็นพื้นฐานสำหรับ Machine Learning

2. แนวทางการสอน
   - เริ่มจากการสร้าง array พื้นฐาน
   - สอนการเข้าถึงข้อมูลแบบต่างๆ
   - แสดงการคำนวณพื้นฐาน
   - ยกตัวอย่างการใช้งานจริง

3. โจทย์แนะนำสำหรับฝึก:

```python
# โจทย์ 1: จัดการข้อมูลนักเรียน
# สร้าง array คะแนนสอบ 3 วิชาของนักเรียน 4 คน
scores = np.array([
    [80, 85, 90],
    [70, 75, 85],
    [90, 95, 85],
    [85, 80, 80]
])

# คำถาม:
# 1. หาคะแนนเฉลี่ยของแต่ละวิชา
# 2. หานักเรียนที่ได้คะแนนรวมสูงสุด
# 3. หาจำนวนนักเรียนที่ได้คะแนนมากกว่า 85 ในแต่ละวิชา

# โจทย์ 2: วิเคราะห์ข้อมูลร้านค้า
# สร้าง array ยอดขาย 3 สาขา 4 วัน
sales = np.array([
    [1000, 1200, 800],
    [1100, 1300, 900],
    [950, 1100, 850],
    [1300, 1400, 1000]
])

# คำถาม:
# 1. หายอดขายรวมของแต่ละวัน
# 2. หาสาขาที่มียอดขายเฉลี่ยสูงสุด
# 3. หาวันที่ยอดขายรวมทุกสาขาสูงที่สุด
```

4. ข้อควรระวัง:
   - การ broadcast ใน NumPy
   - ความแตกต่างระหว่าง copy และ view
   - การจัดการกับ missing values

