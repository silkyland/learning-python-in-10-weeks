# Object-Oriented Programming (OOP)

## 1. หลักการพื้นฐานของ OOP:

1. Class และ Object

   - Class คือพิมพ์เขียวหรือแม่แบบที่กำหนดคุณสมบัติและพฤติกรรมของวัตถุ
   - Object คือตัวแทนของ Class ที่ถูกสร้างขึ้นมาเพื่อใช้งานจริง โดยมีสถานะ (state) และพฤติกรรม (behavior) ตามที่กำหนดไว้ใน Class

2. การห่อหุ้ม (Encapsulation)

   - Encapsulation คือการซ่อนรายละเอียดการทำงานภายใน Class และให้เข้าถึงผ่าน public interface เท่านั้น
   - ช่วยป้องกันการเข้าถึงและแก้ไขข้อมูลใน Object โดยไม่ได้ตั้งใจ ทำให้โปรแกรมมีความน่าเชื่อถือมากขึ้น

3. การสืบทอด (Inheritance)

   - Inheritance ช่วยให้ Class ลูก (subclass) สามารถสืบทอดและนำ attributes กับ methods มาจาก Class แม่ (superclass) ได้
   - ช่วยลดการเขียนโค้ดซ้ำซ้อน เพิ่มการใช้ code ร่วมกัน (code reusability)

4. การพ้องรูป (Polymorphism)
   - Polymorphism ทำให้ object ต่างชนิดกันสามารถใช้ method ชื่อเดียวกันได้ (method overriding) ช่วยให้เขียนโค้ดให้สั้น กระชับขึ้น
   - รองรับการส่ง object ที่แตกต่างเข้าไปให้ method เดียวกันได้ (duck typing) เพิ่มความยืดหยุ่นของโปรแกรม

ประโยชน์ของการเขียนโปรแกรมแบบ OOP:

1. โค้ดมีความชัดเจน เป็นระเบียบ และอ่านง่ายขึ้น เพราะจัดกลุ่มข้อมูลและฟังก์ชันที่เกี่ยวข้องเข้าด้วยกันเป็น Class

2. ลดการพึ่งพากันระหว่างส่วนต่างๆ (low coupling) เพราะ object สื่อสารกันผ่าน interface ที่กำหนดไว้ชัดเจน ทำให้ปรับเปลี่ยนหรือแก้ไขโค้ดง่าย

3. สามารถนำ Class ที่สร้างไว้แล้วกลับมาใช้ใหม่ได้ (reusability) ไม่ต้องเขียนโค้ดซ้ำๆ ช่วยลดเวลาและทรัพยากรในการพัฒนา

4. รองรับการขยายตัวของโปรแกรมในอนาคต เพราะสามารถสร้าง Class ใหม่ๆได้ตลอด และแก้ไข Class ที่มีอยู่ได้โดยไม่ส่งผลกระทบมากนัก

OOP ใน Python:

- Python เป็นภาษาที่สนับสนุน OOP อย่างเต็มที่ โดยทุกอย่างใน Python ถือเป็น object ทั้งหมด
- สามารถสร้าง Class ได้โดยใช้ keyword "class" และสร้าง object instance ด้วยการเรียกใช้ Class เหมือนฟังก์ชัน
- รองรับ Inheritance ทั้งแบบ single, multiple และ multi-level inheritance
- รองรับ Polymorphism, Duck Typing และ Operator Overloading
- มี magic methods มากมาย เช่น **init** สำหรับกำหนด constructor, **str** และ **repr** สำหรับแปลง object เป็น string, **eq** สำหรับเปรียบเทียบ object เป็นต้น
- สนับสนุนการเขียนโปรแกรมเชิง functional ร่วมกับ OOP ได้ เช่น เก็บ function ใน attribute ของ class หรือส่งต่อ function เป็น argument ได้

## 2.สร้าง Class และ Object

1. กำหนด Class ด้วย class keyword

   - ใช้ keyword "class" เพื่อประกาศสร้าง class ใหม่
   - ตั้งชื่อ class เป็นคำนามและขึ้นต้นด้วยอักษรตัวใหญ่เสมอ (ตามแนวทาง PEP8)
   - ภายใน class ประกอบด้วย attributes (ตัวแปร) และ methods (ฟังก์ชัน)
   - ตัวอย่างการสร้าง class เปล่าๆ:
     ```python
     class Person:
         pass
     ```

2. สร้าง Object จาก Class

   - Object คือ instance ของ class ที่ถูกสร้างขึ้นมาเพื่อใช้งานจริง
   - สร้าง object โดยเรียกใช้ class เหมือนเรียกใช้ฟังก์ชัน เช่น `person = Person()`
   - Object ที่ถูกสร้างขึ้นจะมี attribute และ method ตามที่กำหนดใน class
   - สามารถสร้าง object ได้หลายตัวจาก class เดียว โดย object แต่ละตัวจะมีค่า attribute เป็นของตัวเอง

3. ใช้ Constructor Method (**init**)

   - Constructor คือ special method ที่ถูกเรียกใช้โดยอัตโนมัติเมื่อมีการสร้าง object
   - ใน Python จะใช้ `__init__` เป็นชื่อของ constructor method เสมอ
   - `__init__` ใช้สำหรับกำหนดค่าเริ่มต้นให้กับ attribute ต่างๆของ object
   - ตัวอย่างการใช้ `__init__`:
     ```python
     class Person:
         def __init__(self, name, age):
             self.name = name
             self.age = age
     ```

4. กำหนด Attributes ของ Class

   - Attribute คือตัวแปรที่เก็บข้อมูลสถานะของ object
   - Attribute มี 2 ประเภท คือ instance attribute ที่เป็นของ object แต่ละตัว กับ class attribute ที่ใช้ร่วมกันทั้ง class
   - กำหนด instance attribute ได้ใน `__init__` ด้วยการใช้ `self` นำหน้า เช่น `self.name`, `self.age`
   - กำหนด class attribute นอก method ได้เลย และจะมีค่าเหมือนกันในทุก object เช่น

     ```python
     class Person:
         species = "Human"

         def __init__(self, name, age):
             self.name = name
             self.age = age
     ```

ตัวอย่างการสร้าง object และเข้าถึง attribute:

```python
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)  # "Alice"
print(person2.age)   # 30
print(person1.species)  # "Human"
```

## 3. Methods ใน Class

1. สร้าง Instance Method และเรียกใช้งาน

   - Instance method คือ method ที่ถูกเรียกใช้กับ object เฉพาะตัว และสามารถเข้าถึง instance attribute ได้
   - กำหนด instance method เหมือนกำหนดฟังก์ชันปกติ แต่ต้องมี parameter แรกเป็น `self` เสมอ
   - เรียกใช้ instance method ผ่าน object เช่น `obj.method()`
   - ตัวอย่าง:

     ```python
     class Person:
         def __init__(self, name, age):
             self.name = name
             self.age = age

         def introduce(self):
             print(f"Hi, my name is {self.name} and I'm {self.age} years old.")

     person = Person("Alice", 25)
     person.introduce()  # Output: Hi, my name is Alice and I'm 25 years old.
     ```

2. สร้าง Class Method และ Static Method

   - Class method คือ method ที่ถูกเรียกใช้กับ class โดยตรง ไม่ผูกกับ object ใดๆ
   - ใช้ decorator `@classmethod` กำหนด class method และต้องมี parameter แรกเป็น `cls` แทน `self`
   - Class method สามารถเข้าถึง class attribute ได้ แต่ไม่สามารถเข้าถึง instance attribute ได้
   - Static method คือ method ที่ไม่ต้องมี parameter พิเศษ และไม่สามารถเข้าถึง instance และ class attribute ได้เลย
   - ใช้ decorator `@staticmethod` กำหนด static method
   - ตัวอย่าง:

     ```python
     class Calculator:
         @classmethod
         def add(cls, a, b):
             return a + b

         @staticmethod
         def multiply(a, b):
             return a * b

     print(Calculator.add(3, 5))  # Output: 8
     print(Calculator.multiply(3, 5))  # Output: 15
     ```

3. ความแตกต่างระหว่าง Instance, Class และ Static Method

   - Instance method ถูกเรียกใช้กับ object, สามารถเข้าถึง instance และ class attribute ได้
   - Class method ถูกเรียกใช้กับ class, สามารถเข้าถึง class attribute ได้ แต่ไม่สามารถเข้าถึง instance attribute ได้
   - Static method ไม่สามารถเข้าถึง instance และ class attribute ได้เลย เหมาะสำหรับเป็น utility function
   - ตัวอย่าง:

     ```python
     class MyClass:
         class_attr = 'I am a class attribute'

         def __init__(self, instance_attr):
             self.instance_attr = instance_attr

         def instance_method(self):
             print(f"Accessing instance attribute: {self.instance_attr}")
             print(f"Accessing class attribute: {MyClass.class_attr}")

         @classmethod
         def class_method(cls):
             print(f"Accessing class attribute: {cls.class_attr}")

         @staticmethod
         def static_method():
             print("I cannot access any attribute")

     obj = MyClass("I am an instance attribute")

     obj.instance_method()
     # Output:
     # Accessing instance attribute: I am an instance attribute
     # Accessing class attribute: I am a class attribute

     MyClass.class_method()
     # Output: Accessing class attribute: I am a class attribute

     MyClass.static_method()
     # Output: I cannot access any attribute
     ```

4. ส่งผ่านและรับค่า Argument ใน Method

   - ส่งผ่านและรับค่า argument ใน method เหมือนกับในฟังก์ชันทั่วไป
   - สามารถกำหนด default value ให้ parameter ได้
   - สามารถรับ arbitrary arguments ได้ด้วย `*args` และ `**kwargs`
   - สามารถ return ค่าออกมาจาก method ได้
   - ตัวอย่าง:

     ```python
     class Calculator:
         def add(self, a, b):
             return a + b

         def multiply(self, a, b=1):
             return a * b

         def sum(self, *args):
             return sum(args)

         def calculate(self, **kwargs):
             if 'add' in kwargs:
                 return self.add(kwargs['a'], kwargs['b'])
             elif 'multiply' in kwargs:
                 return self.multiply(kwargs['a'], kwargs.get('b', 1))

     calc = Calculator()
     print(calc.add(3, 5))  # Output: 8
     print(calc.multiply(3))  # Output: 3
     print(calc.multiply(3, 5))  # Output: 15
     print(calc.sum(1, 2, 3, 4, 5))  # Output: 15
     print(calc.calculate(add=True, a=3, b=5))  # Output: 8
     print(calc.calculate(multiply=True, a=3))  # Output: 3
     ```

การใช้ method ใน class ช่วยให้เราสามารถจัดการ behavior ของ object ได้อย่างมีประสิทธิภาพ วิธีการเลือกใช้ instance, class หรือ static method ขึ้นอยู่กับความต้องการในการเข้าถึง attribute และการออกแบบ class นั้นๆ

## 4. Inheritance (การสืบทอด)

### หลักการของ Inheritance:

- Inheritance (การสืบทอด) คือการสร้าง class ใหม่ (subclass หรือ derived class) จาก class ที่มีอยู่แล้ว (superclass หรือ base class)
- Subclass จะสืบทอด attribute และ method ทั้งหมดมาจาก superclass และสามารถเพิ่ม attribute กับ method ใหม่ หรือ override ที่มีอยู่แล้วได้
- Inheritance ช่วยลดการเขียนโค้ดซ้ำซ้อน (code duplication) และส่งเสริมการใช้โค้ดร่วมกัน (code reuse)
- Python รองรับทั้ง single inheritance (สืบทอดจาก 1 superclass) และ multiple inheritance (สืบทอดมาจากหลาย superclass)

### สร้าง Subclass ด้วย Inheritance:

- สร้าง subclass โดยกำหนดชื่อ superclass ไว้ในวงเล็บตามหลังชื่อ subclass
- ตัวอย่างการสร้าง subclass `Dog` ที่สืบทอดมาจาก superclass `Animal`:

  ```python
  class Animal:
      def __init__(self, name):
          self.name = name

      def speak(self):
          pass

  class Dog(Animal):
      def speak(self):
          return "Woof!"

  dog = Dog("Buddy")
  print(dog.name)  # Output: Buddy
  print(dog.speak())  # Output: Woof!
  ```

### ประกาศ Constructor ใน Subclass (**init**):

- Subclass สามารถประกาศ constructor (**init**) ของตัวเองได้
- ใน constructor ของ subclass ต้องเรียก constructor ของ superclass ด้วย เพื่อให้มีการกำหนดค่า attribute ใน superclass ด้วย
- ตัวอย่างการประกาศ constructor ใน subclass:

  ```python
  class Dog(Animal):
      def __init__(self, name, breed):
          super().__init__(name)
          self.breed = breed

      def speak(self):
          return "Woof!"

  dog = Dog("Buddy", "Labrador")
  print(dog.name)  # Output: Buddy
  print(dog.breed)  # Output: Labrador
  ```

### Override Method ใน Subclass:

- Subclass สามารถ override method ที่สืบทอดมาจาก superclass ได้ เพื่อให้มีการทำงานแตกต่างออกไป
- ในตัวอย่างข้างต้น subclass `Dog` ได้ override method `speak()` ที่สืบทอดมาจาก `Animal` เพื่อให้ return ค่าเป็น "Woof!"

### ใช้ super() เพื่อเรียก Method ใน Superclass:

- ใน subclass เราสามารถเรียกใช้ method ของ superclass ได้โดยใช้ฟังก์ชัน `super()`
- `super()` จะ return object ของ superclass และเราสามารถเรียก method ของ superclass ผ่าน object นั้นได้
- การใช้ `super()` มีประโยชน์เมื่อเราต้องการ override method ใน subclass แต่ยังต้องการใช้งานโค้ดบางส่วนใน method ของ superclass ด้วย
- ตัวอย่างการใช้ `super()` เพื่อเรียก method ของ superclass:

  ```python
  class Dog(Animal):
      def __init__(self, name, breed):
          super().__init__(name)
          self.breed = breed

      def speak(self):
          super_speak = super().speak()
          return f"{super_speak} I am a {self.breed}."

  dog = Dog("Buddy", "Labrador")
  print(dog.speak())  # Output: I am a Labrador.
  ```

Inheritance เป็นหนึ่งในหลักการสำคัญของ OOP ที่ช่วยให้เราสามารถออกแบบและพัฒนาโปรแกรมได้อย่างมีประสิทธิภาพ โดยอาศัยการสืบทอด attribute และ method จาก superclass มายัง subclass การใช้ inheritance อย่างเหมาะสมจะทำให้โค้ดมีความยืดหยุ่น ง่ายต่อการปรับเปลี่ยนและนำกลับมาใช้ใหม่ได้

## 5. Encapsulation (การห่อหุ้ม) และ Access Modifiers

หลักการของ Encapsulation:

- Encapsulation (การห่อหุ้ม) คือการซ่อน implementaion details ภายใน class และอนุญาตให้เข้าถึงหรือแก้ไขได้ผ่าน public interface (method) ที่กำหนดไว้เท่านั้น
- Encapsulation ช่วยลดความซับซ้อน ป้องกันการเข้าถึงหรือแก้ไขข้อมูลโดยไม่ได้ตั้งใจ และทำให้ class ง่ายต่อการบำรุงรักษา (maintainance)
- Encapsulation เป็นส่วนสำคัญในการรักษา invariants ของ object (สถานะที่ต้องเป็นจริงเสมอ) เนื่องจากการแก้ไขข้อมูลจะผ่านการตรวจสอบของ method

ใช้ Access Modifiers (public, protected, private):

- Access modifier คือการกำหนดสิทธิ์การเข้าถึง attribute และ method ภายใน class
- Python ไม่ได้มี access modifier อย่างเป็นทางการเหมือนภาษาอื่นๆ แต่มีข้อตกลงในการตั้งชื่อที่เป็นที่นิยม ดังนี้
  - ชื่อที่ขึ้นต้นด้วย `_` (single underscore) ถือเป็น protected attribute/method เข้าถึงได้จากภายใน class และ subclass เท่านั้น
  - ชื่อที่ขึ้นต้นด้วย `__` (double underscore) ถือเป็น private attribute/method เข้าถึงได้จากภายใน class เท่านั้น (เรียกว่า name mangling)
- ตัวอย่างการใช้ access modifier:

  ```python
  class BankAccount:
      def __init__(self, account_number, balance):
          self._account_number = account_number  # protected attribute
          self.__balance = balance  # private attribute

      def get_balance(self):
          return self.__balance

      def deposit(self, amount):
          if amount > 0:
              self.__balance += amount

      def withdraw(self, amount):
          if amount > 0 and amount <= self.__balance:
              self.__balance -= amount

  account = BankAccount("1234567890", 1000)
  print(account.get_balance())  # Output: 1000
  account.deposit(500)
  print(account.get_balance())  # Output: 1500
  account.withdraw(2000)  # ไม่สามารถถอนได้เพราะยอดเงินไม่พอ
  print(account.get_balance())  # Output: 1500
  ```

กำหนด Private Attribute และ Method:

- Private attribute คือ attribute ที่เข้าถึงได้จากภายใน class เท่านั้น
- Private method คือ method ที่เข้าถึงได้จากภายใน class เท่านั้น
- ในตัวอย่างข้างต้น `__balance` เป็น private attribute และมี method อย่าง `deposit()` และ `withdraw()` ที่ใช้ในการแก้ไขค่า `__balance` ภายใน class เท่านั้น

สร้าง Getter และ Setter Method:

- Getter method คือ method ที่ใช้ในการอ่านค่า attribute ของ object
- Setter method คือ method ที่ใช้ในการแก้ไขค่า attribute ของ object
- Getter และ setter ช่วยให้เราสามารถตรวจสอบและควบคุมการเข้าถึง attribute ได้ โดยไม่จำเป็นต้องเข้าถึง attribute โดยตรง
- ในตัวอย่างข้างต้น `get_balance()` คือ getter method ที่ใช้อ่านค่า `__balance`
- เราสามารถสร้าง setter method เพื่อแก้ไขค่า `__balance` ได้ เช่น:
  ```python
  def set_balance(self, balance):
      if balance >= 0:
          self.__balance = balance
  ```

Encapsulation เป็นหลักการสำคัญที่ช่วยให้เราสามารถควบคุมการเข้าถึงและแก้ไข attribute ของ object ได้อย่างปลอดภัย โดยใช้ access modifier และสร้าง public interface ผ่าน getter/setter method การออกแบบ class ที่ดีควรคำนึงถึงหลัก encapsulation เพื่อให้ object มีสถานะที่ถูกต้องและลดความเสี่ยงจากการแก้ไขข้อมูลโดยไม่ได้ตั้งใจ

## 6. Polymorphism (การพ้องรูป)

หลักการของ Polymorphism:

- Polymorphism (การพ้องรูป) คือความสามารถของ object ที่มาจากคนละ class ในการตอบสนองต่อ method ที่มีชื่อเดียวกันในแบบที่แตกต่างกัน
- Polymorphism อนุญาตให้เราเขียนโค้ดที่สามารถทำงานกับ object จากหลาย class ที่มี interface เดียวกันได้ โดยไม่ต้องสนใจชนิดของ object
- Polymorphism ช่วยให้โค้ดมีความยืดหยุ่น ง่ายต่อการขยายและบำรุงรักษา เนื่องจากเราสามารถเพิ่ม class ใหม่ที่รองรับ interface เดียวกันโดยไม่ต้องแก้ไขโค้ดเดิม

ตัวอย่างการใช้ Polymorphism ใน Python:

- ใน Python เราสามารถใช้ polymorphism ผ่านการสืบทอด (inheritance) โดยให้ subclass ต่างๆ implement method ชื่อเดียวกันแต่มีการทำงานแตกต่างกันไป
- ตัวอย่างการใช้ polymorphism ผ่าน inheritance:

  ```python
  class Shape:
      def area(self):
          pass

  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def area(self):
          return self.width * self.height

  class Circle(Shape):
      def __init__(self, radius):
          self.radius = radius

      def area(self):
          return 3.14 * self.radius ** 2

  shapes = [Rectangle(3, 4), Circle(5), Rectangle(2, 6)]

  for shape in shapes:
      print(f"Area: {shape.area()}")

  # Output:
  # Area: 12
  # Area: 78.5
  # Area: 12
  ```

ใช้ isinstance() และ issubclass():

- ฟังก์ชัน `isinstance()` ใช้ตรวจสอบว่า object เป็น instance ของ class ที่กำหนดหรือไม่
- ฟังก์ชัน `issubclass()` ใช้ตรวจสอบว่า class หนึ่งเป็น subclass ของอีก class หนึ่งหรือไม่
- เราสามารถใช้ `isinstance()` และ `issubclass()` เพื่อตรวจสอบประเภทของ object และปรับเปลี่ยนการทำงานของโปรแกรมตามผลการตรวจสอบได้
- ตัวอย่างการใช้ `isinstance()` และ `issubclass()`:

  ```python
  print(isinstance(shapes[0], Rectangle))  # Output: True
  print(isinstance(shapes[1], Rectangle))  # Output: False
  print(issubclass(Rectangle, Shape))  # Output: True
  print(issubclass(Circle, Rectangle))  # Output: False

  for shape in shapes:
      if isinstance(shape, Rectangle):
          print("This is a rectangle.")
      elif isinstance(shape, Circle):
          print("This is a circle.")

  # Output:
  # This is a rectangle.
  # This is a circle.
  # This is a rectangle.
  ```

กำหนด Abstract Base Class (ABC):

- Abstract base class (ABC) คือ class ที่ไม่สามารถสร้าง instance ได้โดยตรง แต่ใช้เป็นแม่แบบสำหรับ subclass อื่นๆ
- ใน Python เราสามารถกำหนด ABC โดยใช้โมดูล `abc` และ decorator `@abstractmethod`
- ตัวอย่างการกำหนด ABC:

  ```python
  from abc import ABC, abstractmethod

  class Shape(ABC):
      @abstractmethod
      def area(self):
          pass

  # s = Shape()  # ไม่สามารถสร้าง instance จาก ABC ได้

  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def area(self):
          return self.width * self.height
  ```

Polymorphism เป็นแนวคิดสำคัญใน OOP ที่ช่วยให้เราสามารถออกแบบและเขียนโค้ดที่ยืดหยุ่นและง่ายต่อการขยาย โดยใช้ประโยชน์จากการสืบทอดและ override method ใน subclass ต่างๆ การใช้ polymorphism อย่างเหมาะสมจะทำให้โค้ดของเรามีความสามารถในการปรับตัวและรองรับความเปลี่ยนแปลงได้ดียิ่งขึ้น

## 7. Special Methods

รู้จัก Dunder/Magic Methods:

- Dunder methods หรือ magic methods คือ special methods ที่มีชื่อขึ้นต้นและลงท้ายด้วย double underscore `__`
- Dunder methods ถูกใช้เพื่อกำหนดพฤติกรรมพิเศษให้กับ object เช่น การเปรียบเทียบ การทำงานร่วมกับ built-in functions และ operator ต่างๆ
- Python interpreter จะเรียกใช้ dunder methods โดยอัตโนมัติในสถานการณ์ที่เกี่ยวข้อง เช่น เมื่อมีการใช้ operator หรือ built-in function กับ object

ใช้ **str** และ **repr** เพื่อ represent object เป็น string:

- `__str__` และ `__repr__` เป็น dunder methods ที่ใช้แปลง object เป็น string representation
- `__str__` ควรคืนค่าเป็น string ที่อ่านเข้าใจง่ายสำหรับมนุษย์ ใช้เมื่อเรียก `str()` หรือ `print()` กับ object
- `__repr__` ควรคืนค่าเป็น string ที่ใช้ construct object ได้ใหม่ ใช้เมื่อเรียก `repr()` กับ object หรือเวลาแสดง object ใน interactive shell
- ตัวอย่างการใช้ `__str__` และ `__repr__`:

  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def __str__(self):
          return f"{self.name} ({self.age} years old)"

      def __repr__(self):
          return f"Person('{self.name}', {self.age})"

  p = Person("Alice", 25)
  print(p)  # Output: Alice (25 years old)
  print(repr(p))  # Output: Person('Alice', 25)
  ```

ใช้ **len**, **getitem**, **setitem** สำหรับ Container Object:

- Container object คือ object ที่เก็บ object อื่นๆไว้ภายใน เช่น list, dict, tuple
- `__len__` ใช้กำหนดความยาวหรือขนาดของ container เมื่อเรียก `len()` กับ object
- `__getitem__` ใช้กำหนดวิธีการเข้าถึง item ภายใน container ด้วย square bracket `[]`
- `__setitem__` ใช้กำหนดวิธีการกำหนดค่า item ภายใน container ด้วย square bracket `[]`
- ตัวอย่างการใช้ `__len__`, `__getitem__`, `__setitem__`:

  ```python
  class MyList:
      def __init__(self, items):
          self.items = items

      def __len__(self):
          return len(self.items)

      def __getitem__(self, index):
          return self.items[index]

      def __setitem__(self, index, value):
          self.items[index] = value

  lst = MyList([1, 2, 3, 4, 5])
  print(len(lst))  # Output: 5
  print(lst[2])  # Output: 3
  lst[2] = 10
  print(lst[2])  # Output: 10
  ```

Operator Overloading ด้วย Special Methods:

- Operator overloading คือการกำหนดพฤติกรรมของ operator เมื่อใช้กับ user-defined object
- Python มี special methods จำนวนมากสำหรับ overload operator ต่างๆ เช่น:
  - `__add__` สำหรับ `+`
  - `__sub__` สำหรับ `-`
  - `__mul__` สำหรับ `*`
  - `__eq__` สำหรับ `==`
  - `__lt__`, `__gt__` สำหรับ `<`, `>`
- ตัวอย่างการใช้ special methods สำหรับ operator overloading:

  ```python
  class Point:
      def __init__(self, x, y):
          self.x = x
          self.y = y

      def __add__(self, other):
          return Point(self.x + other.x, self.y + other.y)

      def __str__(self):
          return f"({self.x}, {self.y})"

  p1 = Point(1, 2)
  p2 = Point(3, 4)
  print(p1 + p2)  # Output: (4, 6)
  ```

Special methods หรือ dunder methods มีบทบาทสำคัญในการกำหนดพฤติกรรมพิเศษให้กับ object ใน Python เราสามารถใช้ special methods เพื่อปรับแต่งวิธีการทำงานของ object เมื่อมีการใช้ operator หรือ built-in function ต่างๆ รวมถึงกำหนดวิธีการแสดงผล object เป็น string การใช้ special methods อย่างเหมาะสมจะช่วยให้ object ของเรามีพฤติกรรมที่สอดคล้องกับความคาดหวังและเป็นธรรมชาติมากขึ้น

## 8. Class และ Inheritance ขั้นสูง

Multiple Inheritance และลำดับการสืบทอด (MRO):

- Multiple inheritance คือการที่ class หนึ่งสืบทอดมาจากมากกว่าหนึ่ง superclass
- เมื่อมี multiple inheritance จะต้องคำนึงถึงลำดับการสืบทอด (Method Resolution Order, MRO) ซึ่งเป็นลำดับที่ Python ใช้ในการค้นหา attribute และ method ใน class hierarchy
- MRO ใน Python ใช้อัลกอริทึม C3 ซึ่งพยายามจัดลำดับ superclass ให้สอดคล้องกับลำดับที่ปรากฏในคำสั่ง class และหลีกเลี่ยงปัญหา diamond inheritance
- ตัวอย่าง multiple inheritance และการใช้ MRO:

  ```python
  class A:
      def method(self):
          print("A")

  class B:
      def method(self):
          print("B")

  class C(A, B):
      pass

  obj = C()
  obj.method()  # Output: A
  print(C.mro())  # Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
  ```

Mixin Class:

- Mixin คือ class ที่ไม่ได้มีจุดประสงค์เพื่อสร้าง instance โดยตรง แต่ใช้เป็น building block เพื่อเสริม functionality ให้กับ class อื่น
- Mixin class มักจะมีขนาดเล็ก มุ่งเน้นที่ functionality เฉพาะด้าน และไม่พึ่งพา state ของ class ที่นำไปผสม
- Mixin ช่วยส่งเสริมการนำ code กลับมาใช้ซ้ำ (code reuse) และลดการเขียน code ที่ซ้ำซ้อน
- ตัวอย่างการใช้ mixin class:

  ```python
  class Flyable:
      def fly(self):
          print("I can fly!")

  class Walkable:
      def walk(self):
          print("I can walk!")

  class Bird(Flyable, Walkable):
      pass

  class Human(Walkable):
      pass

  bird = Bird()
  bird.fly()   # Output: I can fly!
  bird.walk()  # Output: I can walk!

  human = Human()
  human.walk()  # Output: I can walk!
  # human.fly()   # Error: 'Human' object has no attribute 'fly'
  ```

Metaclass และการปรับแต่ง Class Creation:

- Metaclass คือ class ของ class หรือ class ที่ใช้ในการสร้าง class อื่นๆ
- ใน Python ทุก class ถูกสร้างจาก metaclass อย่าง `type()` โดยอัตโนมัติ แต่เราสามารถสร้าง custom metaclass เพื่อปรับแต่งกระบวนการสร้าง class ได้
- Metaclass ช่วยให้เราสามารถ intercept และ modify กระบวนการสร้าง class เช่น แก้ไข class attributes, ตรวจสอบ class definition, inject code หรือ register class กับระบบอื่น
- ตัวอย่างการสร้าง custom metaclass:

  ```python
  class MyMeta(type):
      def __new__(cls, name, bases, attrs):
          attrs['hello'] = lambda self: print(f"Hello from {name}")
          return type.__new__(cls, name, bases, attrs)

  class MyClass(metaclass=MyMeta):
      pass

  obj = MyClass()
  obj.hello()  # Output: Hello from MyClass
  ```

ใช้ Singleton Pattern และ Dependency Injection:

- Singleton คือ design pattern ที่ทำให้มี instance ของ class ได้แค่ตัวเดียว ถ้าพยายามสร้าง instance ใหม่จะได้ reference ไปยัง instance เดิมแทน
- การใช้ metaclass เป็นวิธีหนึ่งในการสร้าง singleton ใน Python โดยจะ override method `__call__` ของ metaclass เพื่อตรวจสอบและคืน instance เดิม
- Dependency Injection (DI) คือเทคนิคในการจัดการ dependency ระหว่าง object โดย object ไม่ต้องสร้าง dependency เอง แต่จะรับ dependency ผ่านทาง constructor หรือ setter method แทน
- DI ช่วยให้ object มีความเป็นอิสระ (loosely coupled) สามารถเปลี่ยนแปลง dependency ได้ง่าย และทดสอบได้สะดวกขึ้น
- ตัวอย่างการใช้ metaclass เพื่อสร้าง singleton และการทำ DI:

  ```python
  class Singleton(type):
      _instances = {}

      def __call__(cls, *args, **kwargs):
          if cls not in cls._instances:
              cls._instances[cls] = super().__call__(*args, **kwargs)
          return cls._instances[cls]

  class MyClass(metaclass=Singleton):
      def __init__(self, dependency):
          self.dependency = dependency

  obj1 = MyClass("Dependency 1")
  obj2 = MyClass("Dependency 2")
  print(obj1 is obj2)  # Output: True
  print(obj1.dependency)  # Output: Dependency 1
  ```

การใช้ความสามารถขั้นสูงของ class และ inheritance เช่น multiple inheritance, mixin class และ metaclass ช่วยให้เราสามารถออกแบบโครงสร้าง class ที่ยืดหยุ่นและปรับแต่งได้มากขึ้น อย่างไรก็ตามต้องใช้ด้วยความระมัดระวังและคำนึงถึงความซับซ้อนที่อาจเกิดขึ้น รวมถึงยึดหลัก best practices ในการออกแบบด้วย เพื่อให้โค้ดมีคุณภาพและง่ายต่อการบำรุงรักษาในระยะยาว

## 9. Best Practices และการออกแบบ

หลักการออกแบบ Class ที่ดี (SOLID Principles):

- SOLID คือชุดหลักการในการออกแบบ class และ object ที่มุ่งเน้นให้โค้ดมีคุณภาพ ยืดหยุ่น และง่ายต่อการบำรุงรักษา
- SOLID ประกอบด้วย 5 หลักการย่อย ได้แก่
  - Single Responsibility Principle (SRP): class ควรมีหน้าที่รับผิดชอบเพียงอย่างเดียว
  - Open-Closed Principle (OCP): class ควรเปิดให้ขยายได้ (open for extension) แต่ปิดสำหรับการแก้ไข (closed for modification)
  - Liskov Substitution Principle (LSP): object ของ subclass ควรสามารถใช้แทน object ของ superclass ได้โดยไม่ทำให้โปรแกรมผิดพลาด
  - Interface Segregation Principle (ISP): ควรแยก interface ให้มีขนาดเล็กและเฉพาะเจาะจงกับความต้องการของ client
  - Dependency Inversion Principle (DIP): ควรพึ่งพา abstraction (interface หรือ abstract class) แทนที่จะพึ่งพา concrete class โดยตรง

ลดการใช้ Inheritance ที่ไม่จำเป็น:

- Inheritance เป็นเครื่องมือที่ทรงพลัง แต่หากใช้มากเกินไปอาจทำให้โค้ดมีความซับซ้อนและยากต่อการทำความเข้าใจ
- ก่อนจะใช้ inheritance ให้พิจารณาว่าเป็นความสัมพันธ์แบบ "is-a" จริงๆหรือไม่ เช่น Dog is an Animal ถ้าไม่ใช่อาจต้องใช้วิธีอื่นแทน
- หลีกเลี่ยงการสร้าง deep hierarchy หรือ inheritance หลายชั้นเกินความจำเป็น เพราะจะทำให้โค้ดอ่านเข้าใจยากและเปลี่ยนแปลงลำบาก

ใช้ Composition แทน Inheritance เมื่อเป็นไปได้:

- Composition คือการที่ object หนึ่งมี (has-a) object อื่นเป็นส่วนประกอบ แทนที่จะเป็น (is-a) object อื่น
- Composition มีความยืดหยุ่นกว่า inheritance เพราะเราสามารถเปลี่ยนส่วนประกอบของ object ได้ at runtime
- การใช้ composition และ dependency injection จะทำให้โค้ดมีความเป็นอิสระมากขึ้น ง่ายต่อการทดสอบและปรับเปลี่ยน
- ตัวอย่างการใช้ composition แทน inheritance:

  ```python
  class Engine:
      def start(self):
          print("Engine started.")

  class Car:
      def __init__(self, engine):
          self.engine = engine

      def start(self):
          self.engine.start()

  engine = Engine()
  car = Car(engine)
  car.start()  # Output: Engine started.
  ```

ทดสอบ Class ด้วย Unit Testing:

- Unit testing คือการเขียน test case เพื่อทดสอบการทำงานของแต่ละหน่วย (unit) ของโปรแกรม ซึ่งส่วนใหญ่มักเป็นระดับ method หรือ function
- การเขียน unit test ช่วยให้มั่นใจได้ว่า class และ method ทำงานได้อย่างถูกต้องตามที่ออกแบบไว้
- ใน Python เราสามารถใช้ module มาตรฐานอย่าง `unittest` หรือ third-party library อย่าง `pytest` ในการเขียน unit test
- ควรเขียน unit test ควบคู่ไปกับการพัฒนา class เลย (test-driven development) และรันเทสอย่างสม่ำเสมอ
- ตัวอย่างการเขียน unit test ด้วย `unittest`:

  ```python
  import unittest

  class MyClass:
      def add(self, a, b):
          return a + b

  class MyClassTest(unittest.TestCase):
      def test_add(self):
          obj = MyClass()
          self.assertEqual(obj.add(2, 3), 5)
          self.assertEqual(obj.add(-1, 1), 0)

  if __name__ == '__main__':
      unittest.main()
  ```

ตัวอย่างการประยุกต์ใช้ Class ในโปรเจคจริง:

- การเขียนโปรแกรมเชิงวัตถุเป็นวิธีการพื้นฐานในการพัฒนาโปรแกรมขนาดใหญ่ในปัจจุบัน
- ตัวอย่างการประยุกต์ใช้ class เช่น:
  - การสร้างเกม (game development) โดยใช้ class แทน game objects, characters, items, levels เป็นต้น
  - การพัฒนาเว็บแอปพลิเคชัน (web development) โดยใช้ class แทน models, views, controllers, forms, templates เป็นต้น
  - การเขียนโปรแกรมสำหรับงานวิทยาศาสตร์ข้อมูล (data science) โดยใช้ class แทน datasets, models, algorithms, visualizations เป็นต้น
  - การสร้างระบบหลังบ้าน (backend systems) โดยใช้ class แทน services, repositories, entities, DTOs เป็นต้น
- การนำแนวคิดและหลักการต่างๆของ OOP ไปปรับใช้ให้เหมาะสมกับบริบทของโปรเจค จะช่วยให้การพัฒนาโปรแกรมเป็นไปอย่างมีประสิทธิภาพและประสบความสำเร็จมากขึ้น

สรุปแล้ว การออกแบบและพัฒนาโปรแกรมเชิงวัตถุที่ดีนั้นต้องอาศัยทั้งความรู้ ประสบการณ์ และความใส่ใจในรายละเอียด ไม่ว่าจะเป็นการนำหลักการ SOLID มาปรับใช้ การเลือกใช้ inheritance และ composition อย่างเหมาะสม การเขียน unit test เพื่อทดสอบความถูกต้อง รวมถึงการศึกษา design patterns และ best practices จากโปรเจคและไลบรารีชั้นนำต่างๆ

สิ่งสำคัญคือต้องฝึกฝนและพัฒนาทักษะการออกแบบและเขียนโปรแกรมเชิงวัตถุอย่างต่อเนื่อง รวมถึงเปิดใจเรียนรู้สิ่งใหม่ๆอยู่เสมอ เพื่อให้สามารถสร้างซอฟต์แวร์ที่มีคุณภาพ ตอบโจทย์ความต้องการ และง่ายต่อการบำรุงรักษาในระยะยาวได้อย่างแท้จริง

## แบบฝึกหัด

ได้เลยครับ ผมมีแบบฝึกหัดพร้อมเฉลย 2 ข้อดังนี้

แบบฝึกหัดที่ 1: การสร้าง Class และ Inheritance

จงสร้าง class สำหรับจำลองการทำงานของรูปทรงเรขาคณิต ดังนี้

- สร้าง class ชื่อ `Shape` ซึ่งมี attribute ชื่อ `color` และมี method ชื่อ `area()` ซึ่ง return ค่าพื้นที่ของรูปทรง (ให้ return 0 ในคลาส `Shape`)
- สร้าง subclass ชื่อ `Rectangle` ที่สืบทอดจาก `Shape` และมี attribute ชื่อ `width` และ `height` พร้อมทั้ง implement method `area()` ให้ return ค่าพื้นที่ของสี่เหลี่ยมผืนผ้า
- สร้าง subclass ชื่อ `Circle` ที่สืบทอดจาก `Shape` และมี attribute ชื่อ `radius` พร้อมทั้ง implement method `area()` ให้ return ค่าพื้นที่ของวงกลม

เฉลย:

```python
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

rect = Rectangle("Red", 3, 4)
print(rect.color)  # Output: Red
print(rect.area())  # Output: 12

circ = Circle("Blue", 5)
print(circ.color)  # Output: Blue
print(circ.area())  # Output: 78.5
```

แบบฝึกหัดที่ 2: Polymorphism และ Encapsulation

จงสร้าง class สำหรับจำลองการทำงานของ bank account ดังนี้

- สร้าง class ชื่อ `BankAccount` ซึ่งมี attribute ชื่อ `balance` (ให้เป็น private attribute) และมี method `deposit()` และ `withdraw()` สำหรับฝากและถอนเงิน
- สร้าง subclass ชื่อ `SavingsAccount` ที่สืบทอดจาก `BankAccount` และมี method ชื่อ `add_interest()` ซึ่งจะเพิ่มดอกเบี้ยเข้าไปใน balance (ให้คิดดอกเบี้ย 1% ต่อครั้ง)
- สร้าง subclass ชื่อ `CurrentAccount` ที่สืบทอดจาก `BankAccount` และมี attribute ชื่อ `overdraft_limit` ซึ่งจะอนุญาตให้ถอนเงินเกินจาก balance ได้ไม่เกินกำหนด

เฉลย:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self._balance * 0.01
        self.deposit(interest)

class CurrentAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
        else:
            print("Exceeds overdraft limit")

savings = SavingsAccount(1000)
savings.add_interest()
print(savings.get_balance())  # Output: 1010.0

current = CurrentAccount(1000, 500)
current.withdraw(1200)
print(current.get_balance())  # Output: -200
current.withdraw(800)  # Output: Exceeds overdraft limit
```
