ได้เลย นี่คือเนื้อหาทั้งหมดพร้อมการปรับปรุงและเพิ่มเติมตัวอย่างให้มากขึ้น:

# ไวยากรณ์และโครงสร้างพื้นฐานของ Python

## 1. ชนิดของข้อมูล (Data Types)

Python มีชนิดข้อมูลพื้นฐานหลายประเภท:

### 1.1 Numbers
- int: จำนวนเต็ม เช่น 5, -3, 1000
- float: จำนวนทศนิยม เช่น 3.14, -0.5, 2.0
- ตัวอย่างการใช้งาน:
  ```python
  x = 10
  y = 3.14
  ```

### 1.2 Strings
- ข้อความที่อยู่ในเครื่องหมายคำพูดเดี่ยว (' ') หรือคู่ (" ")
- ตัวอย่าง: 'Hello', "Python"
- ตัวอย่างการใช้งาน:
  ```python
  greeting = "Hello, World!"
  name = 'Alice'
  ```

### 1.3 Lists
- ลำดับของข้อมูลที่สามารถเปลี่ยนแปลงได้ ใช้วงเล็บเหลี่ยม [ ]
- ตัวอย่าง: [1, 2, 3], ['a', 'b', 'c']
- ตัวอย่างการใช้งาน:
  ```python
  numbers = [1, 2, 3, 4, 5]
  fruits = ['apple', 'banana', 'cherry']
  ```

### 1.4 Tuples
- ลำดับของข้อมูลที่ไม่สามารถเปลี่ยนแปลงได้ ใช้วงเล็บกลม ( )
- ตัวอย่าง: (1, 2, 3), ('x', 'y', 'z')
- ตัวอย่างการใช้งาน:
  ```python
  coordinates = (10.0, 20.0)
  colors = ('red', 'green', 'blue')
  ```

### 1.5 Dictionaries
- คู่ของ key-value ใช้วงเล็บปีกกา { }
- ตัวอย่าง: {'name': 'John', 'age': 30}
- ตัวอย่างการใช้งาน:
  ```python
  person = {'name': 'John', 'age': 30, 'city': 'New York'}
  ```

### 1.6 Booleans
- ชนิดข้อมูลที่แทนค่าความจริง เช่น True หรือ False
- ตัวอย่างการใช้งาน:
  ```python
  is_active = True
  has_permission = False
  ```

### 1.7 NoneType
- ชนิดข้อมูลที่แทนค่าว่างหรือไม่มีค่า
- ตัวอย่างการใช้งาน:
  ```python
  result = None
  ```

## 2. ตัวแปร (Variables) และการกำหนดค่า

- ใช้เครื่องหมาย = ในการกำหนดค่า
- ชื่อตัวแปรควรเริ่มต้นด้วยตัวอักษรหรือ underscore
- ตัวอย่างการใช้งาน:
  ```python
  x = 5
  name = "Alice"
  my_list = [1, 2, 3]
  ```

- ตัวอย่างการใช้งานตัวแปรเพื่อเก็บผลลัพธ์จากฟังก์ชัน:
  ```python
  sum_result = sum([1, 2, 3])
  print("ผลรวม:", sum_result)  # Output: ผลรวม: 6
  ```

## 3. โครงสร้างควบคุม (Control Structures)

### 3.1 if-else
- การใช้งาน if-else เบื้องต้น:
  ```python
  if condition:
      # code to execute if condition is True
  elif another_condition:
      # code to execute if another_condition is True
  else:
      # code to execute if all conditions are False
  ```

- ตัวอย่าง:
  ```python
  age = 20
  if age >= 18:
      print("ผู้ใหญ่")
  else:
      print("เด็ก")
  ```

### 3.2 Loops

#### for loop
- การใช้งาน for loop เพื่อวนซ้ำข้อมูลในลิสต์:
  ```python
  for item in iterable:
      # code to execute for each item
  ```

- ตัวอย่าง:
  ```python
  fruits = ['apple', 'banana', 'cherry']
  for fruit in fruits:
      print(fruit)
  ```

#### while loop
- การใช้งาน while loop เพื่อวนซ้ำตามเงื่อนไข:
  ```python
  while condition:
      # code to execute while condition is True
  ```

- ตัวอย่าง:
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```

#### Nested if-else
- การใช้ if-else ซ้อนกันเพื่อตรวจสอบเงื่อนไขหลายชั้น:
  ```python
  age = 20
  if age >= 18:
      if age <= 30:
          print("วัยรุ่น")
      else:
          print("ผู้ใหญ่")
  else:
      print("เด็ก")
  ```

## 4. ฟังก์ชัน (Functions)

- ใช้คำสั่ง def ในการสร้างฟังก์ชัน
- ตัวอย่าง:
  ```python
  def greet(name):
      return f"Hello, {name}!"

  # การเรียกใช้ฟังก์ชัน
  message = greet("Alice")
  print(message)  # Output: Hello, Alice!
  ```

- ฟังก์ชันที่คำนวณพื้นที่สามเหลี่ยม:
  ```python
  def triangle_area(base, height):
      return 0.5 * base * height

  area = triangle_area(10, 5)
  print("พื้นที่สามเหลี่ยม:", area)  # Output: พื้นที่สามเหลี่ยม: 25.0
  ```

## 5. คลาสและออบเจ็กต์ (Classes & Objects) เบื้องต้น

- ใช้คำสั่ง class ในการสร้างคลาส
- ตัวอย่าง:
  ```python
  class Dog:
      def __init__(self, name):
          self.name = name
      
      def bark(self):
          return f"{self.name} says Woof!"

  # การสร้างออบเจ็กต์
  my_dog = Dog("Buddy")
  print(my_dog.bark())  # Output: Buddy says Woof!
  ```

นี่คือพื้นฐานเบื้องต้นของ Python ที่จะช่วยให้คุณเริ่มต้นเขียนโปรแกรมได้ การฝึกฝนและทำความเข้าใจกับแนวคิดเหล่านี้จะช่วยให้คุณพัฒนาทักษะการเขียนโปรแกรม Python ได้อย่างมีประสิทธิภาพ

# การติดตั้งและเตรียมสภาพแวดล้อมสำหรับ Flask

การพัฒนาเว็บแอปพลิเคชันด้วย Flask จำเป็นต้องมีการเตรียมสภาพแวดล้อมการพัฒนาอย่างถูกต้อง นี่คือขั้นตอนที่คุณต้องทำ:

## 1. การติดตั้ง Python

ก่อนอื่นคุณต้องติดตั้ง Python ลงในระบบของคุณ:
- สำหรับ Windows:
  1. ดาวน์โหลด Python ได้จาก [เว็บไซต์ Python](https://www.python.org/downloads/)
  2. เมื่อดาวน์โหลดเสร็จสิ้น ให้เปิดไฟล์ติดตั้งและตรวจสอบให้แน่ใจว่าได้เลือกตัวเลือก "Add Python to PATH"
  3. คลิกที่ "Install Now"

- สำหรับ macOS:
  1. เปิด Terminal
  2. ใช้คำสั่ง Homebrew ในการติดตั้ง Python (ถ้ายังไม่มี Homebrew สามารถติดตั้งได้จาก [brew.sh](https://brew.sh/)):
     ```bash
     brew install python
     ```

- สำหรับ Linux:
  1. เปิด Terminal
  2. ใช้คำสั่ง apt ในการติดตั้ง Python:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

## 2. การสร้าง Virtual Environment

Virtual Environment ช่วยให้เราสามารถจัดการแพ็กเกจและไลบรารีต่าง ๆ ที่ใช้ในโปรเจ็กต์ของเราแยกออกจากระบบหลักได้:
1. เปิด Terminal หรือ Command Prompt
2. ใช้คำสั่งต่อไปนี้เพื่อสร้าง Virtual Environment:
   ```bash
   python3 -m venv myenv
   ```
   (ใน Windows ให้ใช้ `python` แทน `python3`)

3. เปิดใช้งาน Virtual Environment:
   - บน Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - บน macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

## 3. การติดตั้ง Flask ผ่าน pip

เมื่อเปิดใช้งาน Virtual Environment แล้ว สามารถติดตั้ง Flask ได้โดยใช้ pip:
```bash
pip install Flask
```

## 4. การเตรียมโครงสร้างโปรเจ็กต์เริ่มต้น

การจัดการโครงสร้างโปรเจ็กต์เป็นสิ่งสำคัญเพื่อให้โปรเจ็กต์ของคุณมีความเป็นระเบียบ นี่คือโครงสร้างโปรเจ็กต์เริ่มต้นที่แนะนำสำหรับ Flask:
```
my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
│       └── index.html
│
├── venv/
│   └── ... (ไฟล์และโฟลเดอร์ของ Virtual Environment)
│
├── .gitignore
├── config.py
└── run.py
```

### รายละเอียดไฟล์และโฟลเดอร์

- `app/`: โฟลเดอร์หลักที่เก็บไฟล์ของแอปพลิเคชัน
  - `__init__.py`: ไฟล์สำหรับสร้างแอปพลิเคชันและกำหนดค่าต่าง ๆ
  - `routes.py`: ไฟล์สำหรับกำหนดเส้นทางต่าง ๆ ของแอปพลิเคชัน
  - `models.py`: ไฟล์สำหรับกำหนดโมเดลของฐานข้อมูล (ถ้ามี)
  - `templates/`: โฟลเดอร์สำหรับเก็บเทมเพลต HTML

- `venv/`: โฟลเดอร์ของ Virtual Environment

- `.gitignore`: ไฟล์สำหรับบอก Git ว่าไม่ต้องติดตามไฟล์หรือโฟลเดอร์ใดบ้าง

- `config.py`: ไฟล์สำหรับกำหนดค่าต่าง ๆ ของแอปพลิเคชัน

- `run.py`: ไฟล์สำหรับรันแอปพลิเคชัน

### ตัวอย่างการตั้งค่าไฟล์

**app/__init__.py**:
```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Import parts of our application
        from . import routes
        
        return app
```

**app/routes.py**:
```python
from flask import render_template
from app import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('index.html')
```

**app/templates/index.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to Flask!</h1>
</body>
</html>
```

**run.py**:
```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

เมื่อทำตามขั้นตอนทั้งหมดนี้ คุณจะมีสภาพแวดล้อมที่พร้อมสำหรับการพัฒนาเว็บแอปพลิเคชันด้วย Flask พร้อมทั้งโครงสร้างโปรเจ็กต์ที่มีความเป็นระเบียบและพร้อมใช้งาน


# แอปพลิเคชัน Flask เบื้องต้นและการกำหนดเส้นทาง (Routing)

การสร้างแอปพลิเคชัน Flask เบื้องต้นและการกำหนดเส้นทางเป็นขั้นตอนสำคัญในการพัฒนาเว็บแอปพลิเคชัน นี่คือวิธีการเริ่มต้น:

## 1. สร้างแอปพลิเคชัน Flask

ก่อนอื่นให้สร้างไฟล์ `app.py` ซึ่งจะเป็นไฟล์หลักของแอปพลิเคชัน:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

รันแอปพลิเคชัน:
```bash
python app.py
```

เปิดเว็บเบราว์เซอร์และไปที่ `http://127.0.0.1:5000/` คุณจะเห็นข้อความ "Hello, Flask!"

## 2. กำหนดเส้นทางด้วย route decorator

คุณสามารถกำหนดเส้นทางหลาย ๆ เส้นทางได้โดยใช้ `@app.route` decorator:
```python
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is the about page."
```

## 3. ส่งผ่านข้อมูลจากเส้นทางไปยังฟังก์ชันด้วย URL parameters

การส่งผ่านข้อมูลใน URL สามารถทำได้โดยการใช้ `<parameter>` ในเส้นทาง:
```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'
```

คุณสามารถกำหนดชนิดของ parameter ได้ เช่น `<int:post_id>`:
```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'
```

## 4. render templates ด้วย render_template()

การใช้เทมเพลต HTML เพื่อแสดงผลหน้าเว็บสามารถทำได้ด้วย `render_template`:
```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('profile.html', username=username)
```

สร้างโฟลเดอร์ `templates` และไฟล์ `index.html` กับ `profile.html` ภายในโฟลเดอร์:
**templates/index.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Flask!</h1>
</body>
</html>
```

**templates/profile.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
</head>
<body>
    <h1>Profile of {{ username }}</h1>
</body>
</html>
```

## 5. ทำงานกับ HTTP methods เช่น GET และ POST

คุณสามารถระบุ HTTP methods ที่ต้องการให้เส้นทางรองรับได้โดยใช้ `methods` parameter:
```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Logged in as {username}'
    else:
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        '''
```

การทำงานของโค้ด:
- ถ้าการร้องขอเป็นแบบ GET จะแสดงฟอร์มให้กรอกข้อมูล
- ถ้าการร้องขอเป็นแบบ POST จะดึงข้อมูลจากฟอร์มและแสดงผลลัพธ์

นี่คือวิธีการสร้างแอปพลิเคชัน Flask เบื้องต้น พร้อมการกำหนดเส้นทาง การส่งผ่านข้อมูล และการทำงานกับเทมเพลตและ HTTP methods เพื่อให้คุณเริ่มต้นพัฒนาเว็บแอปพลิเคชันได้อย่างมั่นใจ

# Templates และ Static Files ใน Flask

การใช้เทมเพลตและจัดการไฟล์สถิตใน Flask ช่วยให้การพัฒนาเว็บแอปพลิเคชันมีความเป็นระเบียบและง่ายต่อการดูแลรักษา นี่คือวิธีการใช้ Jinja2 template engine, ส่งข้อมูลไปยัง template, การใช้ template inheritance และการจัดการ static files

## 1. การใช้ Jinja2 template engine

Jinja2 เป็น template engine ที่ใช้ใน Flask ช่วยให้เราสามารถสร้าง HTML templates ที่ยืดหยุ่นและมีการใช้ตัวแปรได้:

**ตัวอย่างไฟล์เทมเพลต Jinja2 (`index.html`)**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ message }}</p>
</body>
</html>
```

## 2. ส่งข้อมูลไปยัง template ด้วย render_template()

การส่งข้อมูลไปยังเทมเพลตสามารถทำได้โดยการใช้ `render_template`:

**app.py**:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page', heading='Welcome to Flask', message='This is a basic Flask application.')
```

## 3. การใช้ template inheritance เพื่อสร้าง base layout

Template inheritance ช่วยให้เราสามารถสร้าง layout พื้นฐานที่ใช้ร่วมกันในหลาย ๆ เทมเพลต:

**base.html** (base layout):
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Flask App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>My Flask App</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>Footer content here.</p>
    </footer>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

**index.html** (extends base layout):
```html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <h2>{{ heading }}</h2>
    <p>{{ message }}</p>
{% endblock %}
```

## 4. จัดการ static files เช่น CSS, JavaScript และรูปภาพ

สร้างโฟลเดอร์ `static` สำหรับเก็บไฟล์ CSS, JavaScript และรูปภาพ

**โครงสร้างโปรเจ็กต์**:
```
my_flask_app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
└── static/
    ├── style.css
    └── script.js
```

**ตัวอย่างไฟล์ CSS (`style.css`)**:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
}

header {
    background-color: #333;
    color: white;
    padding: 1rem;
    text-align: center;
}

footer {
    background-color: #333;
    color: white;
    padding: 1rem;
    text-align: center;
    position: fixed;
    width: 100%;
    bottom: 0;
}
```

**ตัวอย่างไฟล์ JavaScript (`script.js`)**:
```javascript
document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is loaded and ready.');
});
```

## สรุป

การใช้ Jinja2 template engine ช่วยให้การสร้างเทมเพลต HTML มีความยืดหยุ่นและสามารถส่งข้อมูลไปยังเทมเพลตได้ง่าย การใช้ template inheritance ช่วยให้เราสามารถสร้าง layout พื้นฐานที่ใช้ร่วมกันในหลาย ๆ หน้า และการจัดการ static files ทำให้การจัดการไฟล์ CSS, JavaScript และรูปภาพเป็นระบบมากขึ้น

เมื่อคุณสร้างและกำหนดค่าเส้นทางใน Flask พร้อมกับการใช้เทมเพลตและไฟล์สถิตอย่างมีประสิทธิภาพ คุณจะสามารถพัฒนาเว็บแอปพลิเคชันที่มีความสวยงามและใช้งานได้อย่างเต็มประสิทธิภาพ


# Forms และ User Input ใน Flask

การสร้างฟอร์มและการรับข้อมูลจากผู้ใช้เป็นสิ่งสำคัญในการพัฒนาเว็บแอปพลิเคชัน นี่คือวิธีการสร้างฟอร์มด้วย HTML การรับและตรวจสอบข้อมูลใน Flask รวมถึงการสร้างฟอร์มด้วย Flask-WTF extension

## 1. การสร้างฟอร์มด้วย HTML และกำหนด action กับ method

สร้างฟอร์มด้วย HTML โดยกำหนด `action` และ `method`:

**templates/form.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h1>Input Form</h1>
    <form action="/submit" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

## 2. รับข้อมูลที่ส่งมาจากฟอร์มใน Flask ด้วย request object

ใน `app.py` ให้ใช้ request object เพื่อรับข้อมูลที่ส่งมาจากฟอร์ม:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # ตรวจสอบข้อมูลและประมวลผล
        return f'Received: Username={username}, Password={password}'
    return 'Invalid request method.'

if __name__ == '__main__':
    app.run(debug=True)
```

## 3. ตรวจสอบ HTTP method ของ request (GET หรือ POST)

คุณสามารถตรวจสอบ HTTP method ของ request ได้โดยใช้ `request.method`:

```python
if request.method == 'POST':
    # handle POST request
else:
    # handle GET request
```

## 4. ดึงข้อมูลจาก form fields ด้วย request.form

การดึงข้อมูลจาก form fields ใช้ `request.form`:

```python
username = request.form['username']
password = request.form['password']
```

## 5. ตรวจสอบและ validate ข้อมูลด้วยเงื่อนไขต่างๆ

คุณสามารถตรวจสอบและ validate ข้อมูลที่ได้รับจากฟอร์มด้วยเงื่อนไขต่างๆ:

```python
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            error = "Both fields are required."
            return render_template('form.html', error=error)
        # ประมวลผลข้อมูล
        return f'Received: Username={username}, Password={password}'
    return 'Invalid request method.'
```

**templates/form.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h1>Input Form</h1>
    <form action="/submit" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if error %}
    <p style="color:red;">{{ error }}</p>
    {% endif %}
</body>
</html>
```

## 6. สร้างฟอร์มด้วย Flask-WTF extension

Flask-WTF ช่วยให้การสร้างฟอร์มและการตรวจสอบข้อมูลเป็นเรื่องง่ายขึ้น:

1. ติดตั้ง Flask-WTF:
   ```bash
   pip install Flask-WTF
   ```

2. สร้างฟอร์มโดยใช้ Flask-WTF:

**forms.py**:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

3. อัปเดต `app.py` เพื่อใช้งานฟอร์ม:

**app.py**:
```python
from flask import Flask, render_template, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f'Received: Username={username}, Password={password}'
    return render_template('form_wtf.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

4. สร้างเทมเพลตสำหรับฟอร์ม:

**templates/form_wtf.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h1>Input Form</h1>
    <form method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}<br>
            {% for error in form.username.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}<br>
            {% for error in form.password.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

การใช้ Flask-WTF จะช่วยให้การสร้างฟอร์มและการตรวจสอบข้อมูลเป็นเรื่องง่ายขึ้นและมีประสิทธิภาพมากขึ้น

# การใช้งานฐานข้อมูลกับ Flask

การเชื่อมต่อ Flask กับฐานข้อมูล เช่น SQLite, MySQL, หรือ PostgreSQL เป็นสิ่งสำคัญในการพัฒนาเว็บแอปพลิเคชันที่ต้องจัดการข้อมูล นี่คือวิธีการใช้งานฐานข้อมูลแบบ raw query และการใช้ ORM กับ Flask-SQLAlchemy extension

## การใช้งานฐานข้อมูลด้วย raw query

### 1. สร้างการเชื่อมต่อกับฐานข้อมูล

ตัวอย่างการเชื่อมต่อกับ SQLite:

**app.py**:
```python
import sqlite3
from flask import Flask, g

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
```

### 2. สร้างตารางและกำหนด schema ของฐานข้อมูล

ใช้ raw query เพื่อสร้างตาราง:

**app.py**:
```python
@app.before_first_request
def create_tables():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    db.commit()
```

### 3. Insert records ลงในตารางด้วย SQL INSERT statements

**app.py**:
```python
@app.route('/add_user', methods=['POST'])
def add_user():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO users (username, email) VALUES (?, ?)
    ''', ('john_doe', 'john@example.com'))
    db.commit()
    return 'User added!'
```

### 4. Query ข้อมูลจากตารางด้วย SQL SELECT statements

**app.py**:
```python
@app.route('/users')
def get_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return str(users)
```

### 5. Update records ด้วย SQL UPDATE statements

**app.py**:
```python
@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        UPDATE users SET username = ? WHERE id = ?
    ''', ('new_username', id))
    db.commit()
    return 'User updated!'
```

### 6. Delete records ด้วย SQL DELETE statements

**app.py**:
```python
@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    db.commit()
    return 'User deleted!'
```

## การใช้งานฐานข้อมูลด้วย Flask-SQLAlchemy (ORM)

### 1. ติดตั้งและกำหนดค่า Flask-SQLAlchemy extension

ติดตั้ง Flask-SQLAlchemy:
```bash
pip install Flask-SQLAlchemy
```

ตั้งค่าใน **app.py**:
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```

### 2. ออกแบบและสร้างโมเดลฐานข้อมูล

**models.py**:
```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

สร้างตารางในฐานข้อมูล:
```python
from app import db
from models import User

db.create_all()
```

### 3. ทำ CRUD operations (Create, Read, Update, Delete)

**app.py**:
```python
from flask import request
from models import User

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return 'User added!'

@app.route('/users')
def get_users():
    users = User.query.all()
    return str(users)

@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    user = User.query.get(id)
    if user:
        user.username = request.form['username']
        db.session.commit()
        return 'User updated!'
    return 'User not found!'

@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User deleted!'
    return 'User not found!'
```

### 4. ทำ database queries และ filtering

**app.py**:
```python
@app.route('/user/<int:id>')
def get_user(id):
    user = User.query.get(id)
    return str(user)

@app.route('/search_user')
def search_user():
    username = request.args.get('username')
    users = User.query.filter_by(username=username).all()
    return str(users)
```

การใช้งานฐานข้อมูลกับ Flask สามารถทำได้ทั้งแบบ raw query และการใช้ ORM ผ่าน Flask-SQLAlchemy ซึ่งช่วยให้การจัดการฐานข้อมูลเป็นเรื่องง่ายและสะดวกยิ่งขึ้น


# การพัฒนา Todos APP

ในตัวอย่างนี้เราจะสร้างแอปพลิเคชันจัดการงาน (Todos) โดยใช้ Flask และการสืบค้น SQL แบบ raw โดยใช้ SQLite เป็นฐานข้อมูล

## 1. การเตรียมสภาพแวดล้อม

ติดตั้ง Flask และสร้างโครงสร้างโปรเจ็กต์:
```bash
pip install Flask
mkdir todos_app
cd todos_app
```

สร้างไฟล์และโฟลเดอร์ต่อไปนี้:
```
todos_app/
├── app.py
├── templates/
│   ├── index.html
│   ├── add_todo.html
│   └── edit_todo.html
└── database.db
```

## 2. สร้างการเชื่อมต่อกับฐานข้อมูลและการตั้งค่า Flask

**app.py**:
```python
import sqlite3
from flask import Flask, request, redirect, url_for, render_template, g

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.before_first_request
def create_tables():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1))
        )
    ''')
    db.commit()
```

## 3. การแสดงผลรายการ Todos

**app.py** (ต่อ):
```python
@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    return render_template('index.html', todos=todos)
```

**templates/index.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todos</title>
</head>
<body>
    <h1>Todos</h1>
    <a href="{{ url_for('add_todo') }}">Add Todo</a>
    <ul>
        {% for todo in todos %}
        <li>
            <strong>{{ todo[1] }}</strong><br>
            {{ todo[2] }}<br>
            <a href="{{ url_for('edit_todo', todo_id=todo[0]) }}">Edit</a>
            <form action="{{ url_for('delete_todo', todo_id=todo[0]) }}" method="post" style="display:inline;">
                <input type="submit" value="Delete">
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

## 4. การเพิ่มรายการ Todos

**app.py** (ต่อ):
```python
@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO todos (title, description, done) VALUES (?, ?, ?)
        ''', (title, description, 0))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_todo.html')
```

**templates/add_todo.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Todo</title>
</head>
<body>
    <h1>Add Todo</h1>
    <form action="{{ url_for('add_todo') }}" method="post">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description"></textarea><br>
        <input type="submit" value="Add">
    </form>
</body>
</html>
```

## 5. การแก้ไขรายการ Todos

**app.py** (ต่อ):
```python
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    db = get_db()
    cursor = db.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        done = int('done' in request.form)
        cursor.execute('''
            UPDATE todos SET title = ?, description = ?, done = ? WHERE id = ?
        ''', (title, description, done, todo_id))
        db.commit()
        return redirect(url_for('index'))
    else:
        cursor.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
        todo = cursor.fetchone()
        return render_template('edit_todo.html', todo=todo)
```

**templates/edit_todo.html**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Todo</title>
</head>
<body>
    <h1>Edit Todo</h1>
    <form action="{{ url_for('edit_todo', todo_id=todo[0]) }}" method="post">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" value="{{ todo[1] }}" required><br>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description">{{ todo[2] }}</textarea><br>
        <label for="done">Done:</label>
        <input type="checkbox" id="done" name="done" {% if todo[3] %}checked{% endif %}><br>
        <input type="submit" value="Update">
    </form>
</body>
</html>
```

## 6. การลบรายการ Todos

**app.py** (ต่อ):
```python
@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    db.commit()
    return redirect(url_for('index'))
```

## แบบฝึกหัด
เราจะสร้างแอปสมุดบันทึกส่วนตัวที่ผู้ใช้สามารถเพิ่ม อ่าน อัปเดต และลบบันทึกได้

ขั้นตอนที่ 1: ติดตั้ง Flask และเตรียมโปรเจ็กต์
1. สร้าง virtual environment และ activate
2. ติดตั้ง Flask ด้วยคำสั่ง `pip install flask`
3. สร้างไฟล์ `app.py` สำหรับเขียนโค้ด Flask
4. สร้างโฟลเดอร์ `templates` สำหรับเก็บไฟล์ HTML

ขั้นตอนที่ 2: สร้างฐานข้อมูล SQLite
1. สร้างไฟล์ฐานข้อมูล `database.db` 
2. สร้างตารางชื่อ `notes` ด้วย SQL command นี้:
   ```sql
   CREATE TABLE notes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       title TEXT NOT NULL,
       content TEXT NOT NULL
   );
   ```

ขั้นตอนที่ 3: เขียนโค้ด Flask ใน `app.py`:
```python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:note_id>', methods=('GET', 'POST'))
def update(note_id):
    conn = get_db_connection()
    note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, note_id))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('update.html', note=note)

@app.route('/delete/<int:note_id>', methods=('POST',))
def delete(note_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
```

ขั้นตอนที่ 4: สร้างไฟล์ HTML templates ใน `templates` folder:
1. `index.html` แสดงบันทึกทั้งหมดและลิงก์เพื่อเพิ่ม อัปเดต หรือลบบันทึก
2. `create.html` มีฟอร์มสำหรับเพิ่มบันทึกใหม่
3. `update.html` มีฟอร์มสำหรับอัปเดตบันทึกที่มีอยู่

เมื่อเสร็จแล้ว คุณสามารถรันแอปด้วยคำสั่ง `flask run` และเข้าถึงแอปได้ที่ `http://localhost:5000`
