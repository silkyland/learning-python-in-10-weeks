# บทนำสู่ CSS (Cascading Style Sheets)

CSS เป็นภาษาที่ใช้ในการจัดรูปแบบและการนำเสนอของเอกสาร HTML ช่วยให้เราสามารถควบคุมลักษณะและการจัดวางของเว็บเพจได้

## 1. วิธีการใช้ CSS

มี 3 วิธีในการใช้ CSS กับ HTML:

1. **Inline CSS**: ใช้ attribute `style` ใน HTML element
   ```html
   <p style="color: blue; font-size: 16px;">ข้อความนี้เป็นสีน้ำเงิน</p>
   ```

2. **Internal CSS**: ใช้ tag `<style>` ในส่วน `<head>` ของ HTML
   ```html
   <head>
     <style>
       p {
         color: blue;
         font-size: 16px;
       }
     </style>
   </head>
   ```

3. **External CSS**: ใช้ไฟล์ CSS แยกต่างหากและเชื่อมโยงกับ HTML
   ```html
   <head>
     <link rel="stylesheet" href="styles.css">
   </head>
   ```

## 2. Selectors

Selectors ใช้เพื่อเลือก HTML elements ที่ต้องการจัดรูปแบบ:

- **Element Selector**: `p { color: blue; }`
- **Class Selector**: `.highlight { background-color: yellow; }`
- **ID Selector**: `#header { font-size: 24px; }`
- **Attribute Selector**: `[type="text"] { border: 1px solid gray; }`

## 3. Properties และ Values

CSS ประกอบด้วย properties และ values:

```css
selector {
  property: value;
}
```

ตัวอย่าง:
```css
p {
  color: blue;
  font-size: 16px;
  margin: 10px 0;
}
```

## 4. Box Model

CSS Box Model อธิบายพื้นที่รอบๆ ของแต่ละ element:

- **Content**: เนื้อหาของ element
- **Padding**: พื้นที่รอบเนื้อหา
- **Border**: เส้นขอบรอบ padding
- **Margin**: พื้นที่ภายนอกสุดรอบ border

```css
div {
  width: 300px;
  padding: 10px;
  border: 5px solid black;
  margin: 20px;
}
```

## 5. Layout

CSS มีหลายวิธีในการจัดวาง elements:

- **Display**: `block`, `inline`, `inline-block`, `flex`, `grid`
- **Position**: `static`, `relative`, `absolute`, `fixed`
- **Float**: `left`, `right`, `none`

ตัวอย่าง Flexbox:
```css
.container {
  display: flex;
  justify-content: space-between;
}
```

## 6. Responsive Design

ใช้ Media Queries เพื่อสร้าง responsive design:

```css
@media screen and (max-width: 600px) {
  body {
    font-size: 14px;
  }
}
```

## 7. การฝึกปฏิบัติ: สไตล์หน้าเว็บอย่างง่าย

ตัวอย่าง HTML และ CSS:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>หน้าเว็บตัวอย่าง CSS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .nav {
            background-color: #333;
            color: white;
            padding: 10px;
            margin-bottom: 20px;
        }
        .nav ul {
            list-style-type: none;
            padding: 0;
            display: flex;
            justify-content: center;
        }
        .nav ul li {
            margin: 0 10px;
        }
        .nav ul li a {
            color: white;
            text-decoration: none;
        }
        .content {
            display: flex;
            flex-wrap: wrap;
        }
        .content-item {
            flex: 1 1 200px;
            margin: 10px;
            padding: 10px;
            background-color: #e9e9e9;
            border-radius: 5px;
        }
        @media screen and (max-width: 600px) {
            .content-item {
                flex: 1 1 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ยินดีต้อนรับสู่เว็บไซต์ของเรา</h1>
        <nav class="nav">
            <ul>
                <li><a href="#">หน้าแรก</a></li>
                <li><a href="#">เกี่ยวกับเรา</a></li>
                <li><a href="#">บริการ</a></li>
                <li><a href="#">ติดต่อ</a></li>
            </ul>
        </nav>
        <div class="content">
            <div class="content-item">
                <h2>หัวข้อที่ 1</h2>
                <p>เนื้อหาสำหรับหัวข้อที่ 1</p>
            </div>
            <div class="content-item">
                <h2>หัวข้อที่ 2</h2>
                <p>เนื้อหาสำหรับหัวข้อที่ 2</p>
            </div>
            <div class="content-item">
                <h2>หัวข้อที่ 3</h2>
                <p>เนื้อหาสำหรับหัวข้อที่ 3</p>
            </div>
        </div>
    </div>
</body>
</html>
```

ตัวอย่างนี้แสดงการใช้ CSS เพื่อจัดรูปแบบหน้าเว็บอย่างง่าย รวมถึงการใช้ flexbox สำหรับ layout และ media query สำหรับ responsive design