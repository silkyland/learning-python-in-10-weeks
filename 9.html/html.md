# การแนะนำ HTML

## ความหมายและประวัติของ HTML

HTML ย่อมาจาก Hypertext Markup Language เป็นภาษามาร์กอัพมาตรฐานที่ใช้ในการสร้างหน้าเว็บ HTML ถูกพัฒนาขึ้นโดย Tim Berners-Lee ในปี 1989 เพื่อเป็นวิธีในการแบ่งปันเอกสารระหว่างนักวิทยาศาสตร์ที่ CERN

ประวัติโดยสังเขป:
- 1989: Tim Berners-Lee เสนอแนวคิด World Wide Web
- 1991: เวอร์ชันแรกของ HTML ถูกเผยแพร่
- 1995: HTML 2.0 เป็นมาตรฐานแรกอย่างเป็นทางการ
- 1997: HTML 3.2 ถูกเผยแพร่
- 1999: HTML 4.01 ออกมาพร้อมกับการปรับปรุงหลายอย่าง
- 2014: HTML5 กลายเป็นมาตรฐานที่แนะนำโดย W3C

## โครงสร้างพื้นฐานของเว็บเพจ HTML

โครงสร้างพื้นฐานของหน้าเว็บ HTML ประกอบด้วยส่วนสำคัญดังนี้:

1. Document Type Declaration (DOCTYPE)
2. HTML element
3. Head element
4. Body element

ตัวอย่างโครงสร้างพื้นฐาน:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ชื่อหน้าเว็บ</title>
</head>
<body>
    <h1>สวัสดีชาวโลก</h1>
    <p>นี่คือย่อหน้าแรกของฉัน</p>
</body>
</html>
```

## การใช้งาน Tags, Attributes และ Elements

1. **Tags**: เป็นเครื่องหมายที่ใช้กำหนดโครงสร้างและความหมายของเนื้อหา เช่น `<p>`, `<h1>`, `<div>`
   - Tags ส่วนใหญ่มีทั้งแท็กเปิดและแท็กปิด เช่น `<p>` และ `</p>`
   - บางแท็กเป็นแท็กเดี่ยว เช่น `<img>`, `<br>`

2. **Attributes**: ให้ข้อมูลเพิ่มเติมเกี่ยวกับ elements เช่น `id`, `class`, `src`, `href`
   - ตัวอย่าง: `<img src="รูปภาพ.jpg" alt="คำอธิบายรูปภาพ">`

3. **Elements**: ประกอบด้วย opening tag, เนื้อหา, และ closing tag
   - ตัวอย่าง: `<p>นี่คือย่อหน้า</p>`

## การตั้งค่าเอกสาร HTML

1. `<!DOCTYPE html>`: บอกเบราว์เซอร์ว่านี่เป็นเอกสาร HTML5
2. `<html>`: เป็น root element ของหน้า HTML
3. `<head>`: ประกอบด้วยข้อมูล meta และการเชื่อมโยงไปยังไฟล์ภายนอก
4. `<body>`: ประกอบด้วยเนื้อหาที่แสดงบนหน้าเว็บ

## การฝึกปฏิบัติ: สร้างหน้าเว็บเรียบง่าย

ลองสร้างหน้าเว็บอย่างง่ายดังนี้:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>หน้าแรกของฉัน</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #f4f4f4;
            padding: 1rem;
            text-align: center;
        }
        main {
            padding: 1rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>ยินดีต้อนรับสู่เว็บไซต์ของฉัน</h1>
    </header>
    <main>
        <h2>เกี่ยวกับฉัน</h2>
        <p>สวัสดีครับ! ฉันกำลังเรียนรู้การสร้างเว็บไซต์ด้วย HTML</p>
        <h2>งานอดิเรก</h2>
        <ul>
            <li>อ่านหนังสือ</li>
            <li>ฟังเพลง</li>
            <li>เล่นกีฬา</li>
        </ul>
    </main>
</body>
</html>
```

หน้าเว็บนี้ประกอบด้วยส่วนหัว รายการ และข้อความพื้นฐาน ซึ่งแสดงให้เห็นถึงการใช้ HTML tags ต่างๆ รวมถึงการจัดรูปแบบอย่างง่ายด้วย CSS ภายใน `<style>` tag

เมื่อคุณเขียนโค้ดนี้และบันทึกเป็นไฟล์ .html แล้วเปิดในเบราว์เซอร์ คุณจะเห็นหน้าเว็บที่สร้างขึ้น ซึ่งเป็นจุดเริ่มต้นที่ดีในการเรียนรู้และพัฒนาทักษะ HTML ต่อไป


# การจัดการข้อความและลิงก์ใน HTML

## การจัดรูปแบบข้อความด้วย Tags

HTML มี tags หลายตัวที่ใช้ในการจัดรูปแบบข้อความ ซึ่งช่วยให้เราสามารถกำหนดโครงสร้างและความสำคัญของเนื้อหาได้:

1. **`<h1>` ถึง `<h6>`**: ใช้สำหรับหัวข้อ โดย `<h1>` มีความสำคัญสูงสุด และ `<h6>` มีความสำคัญน้อยที่สุด
   ```html
   <h1>หัวข้อหลัก</h1>
   <h2>หัวข้อรอง</h2>
   <h3>หัวข้อย่อย</h3>
   ```

2. **`<p>`**: ใช้สำหรับย่อหน้า
   ```html
   <p>นี่คือตัวอย่างย่อหน้า ซึ่งใช้สำหรับเนื้อหาทั่วไป</p>
   ```

3. **`<strong>`**: ใช้เน้นข้อความให้มีความสำคัญมาก (แสดงเป็นตัวหนา)
   ```html
   <p>ข้อความนี้มี<strong>ส่วนที่สำคัญมาก</strong>อยู่ด้วย</p>
   ```

4. **`<em>`**: ใช้เน้นข้อความ (แสดงเป็นตัวเอียง)
   ```html
   <p>นี่คือ<em>ข้อความที่ต้องการเน้น</em>ในประโยค</p>
   ```

## การสร้างลิงก์ภายในและภายนอกด้วย `<a>`

Tag `<a>` (anchor) ใช้สำหรับสร้างลิงก์ไปยังหน้าเว็บอื่นหรือส่วนต่างๆ ภายในหน้าเดียวกัน:

1. **ลิงก์ภายนอก**:
   ```html
   <a href="https://www.example.com">เว็บไซต์ตัวอย่าง</a>
   ```

2. **ลิงก์ภายใน** (ไปยังส่วนอื่นในหน้าเดียวกัน):
   ```html
   <a href="#section1">ไปยังส่วนที่ 1</a>
   
   <!-- ในส่วนอื่นของหน้าเว็บ -->
   <h2 id="section1">ส่วนที่ 1</h2>
   ```

3. **ลิงก์ที่เปิดในแท็บใหม่**:
   ```html
   <a href="https://www.example.com" target="_blank">เปิดในแท็บใหม่</a>
   ```

## การใช้งานรายการด้วย `<ul>`, `<ol>`, `<li>`

HTML มี tags สำหรับสร้างรายการแบบมีลำดับและไม่มีลำดับ:

1. **`<ul>` (Unordered List)**: สร้างรายการแบบไม่มีลำดับ
2. **`<ol>` (Ordered List)**: สร้างรายการแบบมีลำดับ
3. **`<li>` (List Item)**: ใช้สำหรับแต่ละรายการใน `<ul>` หรือ `<ol>`

ตัวอย่าง:

```html
<h3>รายการผลไม้ (ไม่มีลำดับ)</h3>
<ul>
    <li>แอปเปิ้ล</li>
    <li>กล้วย</li>
    <li>ส้ม</li>
</ul>

<h3>ขั้นตอนการทำอาหาร (มีลำดับ)</h3>
<ol>
    <li>เตรียมวัตถุดิบ</li>
    <li>หั่นผัก</li>
    <li>ปรุงรส</li>
    <li>ปรุงสุก</li>
</ol>
```

## การฝึกปฏิบัติ: สร้างเมนูนำทางและรายการต่างๆ

ลองสร้างหน้าเว็บที่มีเมนูนำทางและรายการต่างๆ ดังนี้:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เว็บไซต์ของฉัน</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
        nav { background-color: #f4f4f4; padding: 10px; }
        nav ul { list-style-type: none; padding: 0; }
        nav ul li { display: inline; margin-right: 10px; }
        nav ul li a { text-decoration: none; color: #333; }
    </style>
</head>
<body>
    <header>
        <h1>ยินดีต้อนรับสู่เว็บไซต์ของฉัน</h1>
    </header>
    
    <nav>
        <ul>
            <li><a href="#home">หน้าแรก</a></li>
            <li><a href="#about">เกี่ยวกับเรา</a></li>
            <li><a href="#services">บริการ</a></li>
            <li><a href="#contact">ติดต่อ</a></li>
        </ul>
    </nav>
    
    <main>
        <section id="home">
            <h2>หน้าแรก</h2>
            <p>ยินดีต้อนรับสู่เว็บไซต์ของเรา ที่นี่คุณจะพบข้อมูลที่น่าสนใจมากมาย</p>
        </section>
        
        <section id="about">
            <h2>เกี่ยวกับเรา</h2>
            <p>เราคือบริษัทที่มุ่งมั่นในการให้บริการที่ดีที่สุดแก่ลูกค้า</p>
        </section>
        
        <section id="services">
            <h2>บริการของเรา</h2>
            <ul>
                <li>การออกแบบเว็บไซต์</li>
                <li>การพัฒนาแอปพลิเคชัน</li>
                <li>การให้คำปรึกษาด้านไอที</li>
            </ul>
        </section>
        
        <section id="contact">
            <h2>ติดต่อเรา</h2>
            <p>คุณสามารถติดต่อเราได้ที่:</p>
            <ul>
                <li>อีเมล: info@example.com</li>
                <li>โทรศัพท์: 02-123-4567</li>
                <li>ที่อยู่: 123 ถนนตัวอย่าง กรุงเทพฯ 10100</li>
            </ul>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 เว็บไซต์ของฉัน. สงวนลิขสิทธิ์.</p>
    </footer>
</body>
</html>
```

ตัวอย่างนี้แสดงการใช้งาน tags ต่างๆ ที่เราได้เรียนรู้ รวมถึงการสร้างเมนูนำทางด้วย `<nav>` และการใช้ `<ul>` และ `<li>` ในการสร้างรายการต่างๆ นอกจากนี้ยังมีการใช้ CSS อย่างง่ายเพื่อจัดรูปแบบเมนูให้ดูสวยงามขึ้น

# การใช้งานภาพและตารางใน HTML

## การแทรกภาพในเว็บเพจด้วย `<img>`

การแทรกภาพใน HTML ทำได้โดยใช้ tag `<img>` ซึ่งเป็น self-closing tag (ไม่ต้องมี closing tag)

ตัวอย่างการใช้งาน:
```html
<img src="path/to/image.jpg" alt="คำอธิบายภาพ">
```

- `src`: ระบุที่อยู่ของไฟล์ภาพ (URL หรือ path)
- `alt`: ข้อความที่จะแสดงเมื่อไม่สามารถโหลดภาพได้ หรือสำหรับ screen readers

## การปรับขนาดและจัดตำแหน่งภาพ

1. **การปรับขนาด**:
   ใช้ attributes `width` และ `height` (หน่วยเป็นพิกเซล)
   ```html
   <img src="image.jpg" alt="ภาพตัวอย่าง" width="300" height="200">
   ```

2. **การจัดตำแหน่ง**:
   ใช้ CSS เพื่อจัดตำแหน่งภาพ
   ```html
   <img src="image.jpg" alt="ภาพตัวอย่าง" style="float: left; margin-right: 10px;">
   ```

## การสร้างและจัดรูปแบบตารางด้วย `<table>`, `<tr>`, `<td>`, `<th>`

- `<table>`: กำหนดตาราง
- `<tr>`: Table Row (แถว)
- `<td>`: Table Data (ข้อมูลในเซลล์)
- `<th>`: Table Header (หัวข้อตาราง)

ตัวอย่างการสร้างตาราง:
```html
<table border="1">
  <tr>
    <th>หัวข้อที่ 1</th>
    <th>หัวข้อที่ 2</th>
  </tr>
  <tr>
    <td>ข้อมูล 1</td>
    <td>ข้อมูล 2</td>
  </tr>
  <tr>
    <td>ข้อมูล 3</td>
    <td>ข้อมูล 4</td>
  </tr>
</table>
```

## การฝึกปฏิบัติ: สร้างแกลเลอรีภาพและตารางข้อมูล

ตัวอย่างการสร้างแกลเลอรีภาพและตารางข้อมูล:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>แกลเลอรีภาพและตารางข้อมูล</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
        .gallery { display: flex; flex-wrap: wrap; justify-content: space-around; }
        .gallery img { width: 200px; height: 150px; object-fit: cover; margin: 10px; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>แกลเลอรีภาพและตารางข้อมูล</h1>

    <h2>แกลเลอรีภาพ</h2>
    <div class="gallery">
        <img src="/api/placeholder/200/150" alt="ภาพที่ 1">
        <img src="/api/placeholder/200/150" alt="ภาพที่ 2">
        <img src="/api/placeholder/200/150" alt="ภาพที่ 3">
        <img src="/api/placeholder/200/150" alt="ภาพที่ 4">
    </div>

    <h2>ตารางข้อมูล</h2>
    <table>
        <tr>
            <th>ชื่อ</th>
            <th>อายุ</th>
            <th>อาชีพ</th>
        </tr>
        <tr>
            <td>สมชาย ใจดี</td>
            <td>30</td>
            <td>วิศวกร</td>
        </tr>
        <tr>
            <td>สมหญิง รักเรียน</td>
            <td>28</td>
            <td>ครู</td>
        </tr>
        <tr>
            <td>สมศักดิ์ มุ่งมั่น</td>
            <td>35</td>
            <td>นักธุรกิจ</td>
        </tr>
    </table>

</body>
</html>
```

ในตัวอย่างนี้:
- เราสร้างแกลเลอรีภาพโดยใช้ `<div>` ที่มี class "gallery" และใช้ CSS Flexbox เพื่อจัดวางภาพ
- เราสร้างตารางข้อมูลโดยใช้ `<table>`, `<tr>`, `<th>`, และ `<td>`
- เราใช้ CSS เพื่อจัดรูปแบบของแกลเลอรีและตารางให้ดูสวยงามและเป็นระเบียบ

หมายเหตุ: ใน HTML จริง คุณควรแทนที่ "/api/placeholder/200/150" ด้วย URL หรือ path ของภาพจริงที่คุณต้องการแสดง

# แบบฟอร์มและอินพุตใน HTML

## การสร้างแบบฟอร์มด้วย `<form>`

แบบฟอร์มใน HTML สร้างด้วย tag `<form>` ซึ่งใช้เพื่อรวบรวมและส่งข้อมูลจากผู้ใช้

ตัวอย่างโครงสร้างพื้นฐานของแบบฟอร์ม:
```html
<form action="/submit-form" method="post">
  <!-- ส่วนประกอบของฟอร์มจะอยู่ที่นี่ -->
</form>
```

- `action`: ระบุ URL ที่จะส่งข้อมูลฟอร์มไป
- `method`: ระบุวิธีการส่งข้อมูล (เช่น "get" หรือ "post")

## การใช้งานตัวเลือกอินพุตต่างๆ

1. **`<input>`**: ใช้สำหรับสร้างช่องกรอกข้อมูลหลายประเภท
   ```html
   <input type="text" name="username" placeholder="ชื่อผู้ใช้">
   <input type="password" name="password" placeholder="รหัสผ่าน">
   <input type="email" name="email" placeholder="อีเมล">
   <input type="checkbox" name="subscribe" id="subscribe">
   <label for="subscribe">สมัครรับจดหมายข่าว</label>
   <input type="radio" name="gender" value="male" id="male">
   <label for="male">ชาย</label>
   <input type="radio" name="gender" value="female" id="female">
   <label for="female">หญิง</label>
   ```

2. **`<textarea>`**: ใช้สำหรับข้อความหลายบรรทัด
   ```html
   <textarea name="message" rows="4" cols="50" placeholder="ข้อความของคุณ"></textarea>
   ```

3. **`<select>` และ `<option>`**: ใช้สำหรับสร้างรายการแบบเลือก
   ```html
   <select name="country">
     <option value="th">ไทย</option>
     <option value="us">สหรัฐอเมริกา</option>
     <option value="jp">ญี่ปุ่น</option>
   </select>
   ```

4. **`<button>`**: ใช้สำหรับสร้างปุ่มในฟอร์ม
   ```html
   <button type="submit">ส่งข้อมูล</button>
   <button type="reset">รีเซ็ต</button>
   ```

## การจัดการข้อมูลอินพุตและการส่งข้อมูล

1. **การตรวจสอบความถูกต้อง (Validation)**:
   ใช้ attributes เช่น `required`, `pattern`, `min`, `max` เพื่อตรวจสอบข้อมูลเบื้องต้น
   ```html
   <input type="text" name="username" required minlength="3" maxlength="20">
   <input type="email" name="email" required>
   ```

2. **การส่งข้อมูล**:
   เมื่อกดปุ่ม submit ข้อมูลจะถูกส่งไปยัง URL ที่ระบุใน `action` attribute ของ `<form>`

3. **การจัดการด้วย JavaScript**:
   ใช้ JavaScript เพื่อจัดการการส่งข้อมูลแบบ AJAX หรือตรวจสอบความถูกต้องเพิ่มเติม

## การฝึกปฏิบัติ: สร้างแบบฟอร์มติดต่อและการลงทะเบียน

ตัวอย่างแบบฟอร์มติดต่อและการลงทะเบียน:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>แบบฟอร์มติดต่อและลงทะเบียน</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
        form { max-width: 500px; margin: 20px auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="email"], input[type="password"], textarea, select {
            width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 4px;
        }
        button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <h1>แบบฟอร์มติดต่อและลงทะเบียน</h1>

    <form action="/submit-contact" method="post">
        <h2>แบบฟอร์มติดต่อ</h2>
        <label for="name">ชื่อ:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">อีเมล:</label>
        <input type="email" id="email" name="email" required>

        <label for="subject">หัวข้อ:</label>
        <input type="text" id="subject" name="subject" required>

        <label for="message">ข้อความ:</label>
        <textarea id="message" name="message" rows="4" required></textarea>

        <button type="submit">ส่งข้อความ</button>
    </form>

    <form action="/submit-registration" method="post">
        <h2>แบบฟอร์มลงทะเบียน</h2>
        <label for="username">ชื่อผู้ใช้:</label>
        <input type="text" id="username" name="username" required minlength="3" maxlength="20">

        <label for="password">รหัสผ่าน:</label>
        <input type="password" id="password" name="password" required minlength="8">

        <label for="confirm-password">ยืนยันรหัสผ่าน:</label>
        <input type="password" id="confirm-password" name="confirm-password" required minlength="8">

        <label for="user-email">อีเมล:</label>
        <input type="email" id="user-email" name="user-email" required>

        <label for="gender">เพศ:</label>
        <select id="gender" name="gender">
            <option value="">เลือกเพศ</option>
            <option value="male">ชาย</option>
            <option value="female">หญิง</option>
            <option value="other">อื่นๆ</option>
        </select>

        <label>
            <input type="checkbox" name="agree-terms" required>
            ฉันยอมรับข้อตกลงและเงื่อนไข
        </label>

        <button type="submit">ลงทะเบียน</button>
    </form>
</body>
</html>
```

ในตัวอย่างนี้:
- เราสร้างสองแบบฟอร์ม: แบบฟอร์มติดต่อและแบบฟอร์มลงทะเบียน
- ใช้ HTML5 input types และ attributes เพื่อช่วยในการตรวจสอบความถูกต้องของข้อมูล
- ใช้ CSS เพื่อจัดรูปแบบให้แบบฟอร์มดูสวยงามและใช้งานง่าย
- แสดงการใช้งาน input types ต่างๆ เช่น text, email, password, checkbox, และ select