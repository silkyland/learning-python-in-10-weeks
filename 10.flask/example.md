## บริษัท
ตัวอย่างฐานข้อมูลของบริษัทหนึ่งที่มีตารางสำหรับ `employees`, `departments`, และ `projects` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง:
```
+-------------------+        +-------------------+
|    departments    |        |     employees     |
+-------------------+        +-------------------+
| department_id (PK)|<-------|  employee_id (PK) |
| department_name   |        |  first_name       |
+-------------------+        |  last_name        |
                             |  email            |
                             |  hire_date        |
                             |  department_id(FK)|
                             +-------------------+
                                       |
                                       |
                                       |
                             +-------------------+
                             | employees_projects|
                             +-------------------+
                             |  employee_id (PK) |
                             |  project_id (PK)  |
                             +-------------------+
                                       |
                                       |
                                       |
                             +-------------------+
                             |     projects      |
                             +-------------------+
                             |  project_id (PK)  |
                             |  project_name     |
                             |  start_date       |
                             |  end_date         |
                             |  budget           |
                             +-------------------+
```
### สร้างฐานข้อมูลและตาราง
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE company_db;
USE company_db;

-- สร้างตาราง departments
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL
);

-- สร้างตาราง employees
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- สร้างตาราง projects
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(10, 2)
);

-- สร้างตาราง employees_projects
CREATE TABLE employees_projects (
    employee_id INT,
    project_id INT,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน departments
INSERT INTO departments (department_name) VALUES
('Human Resources'),
('Finance'),
('Engineering'),
('Sales'),
('Marketing');

-- แทรกข้อมูลตัวอย่างใน employees
INSERT INTO employees (first_name, last_name, email, hire_date, department_id) VALUES
('John', 'Doe', 'john.doe@example.com', '2022-01-15', 3),
('Jane', 'Smith', 'jane.smith@example.com', '2021-06-25', 1),
('Emily', 'Johnson', 'emily.johnson@example.com', '2020-09-10', 2),
('Michael', 'Brown', 'michael.brown@example.com', '2019-11-05', 4),
('Jessica', 'Davis', 'jessica.davis@example.com', '2018-03-18', 5);

-- แทรกข้อมูลตัวอย่างใน projects
INSERT INTO projects (project_name, start_date, end_date, budget) VALUES
('Project Apollo', '2023-01-01', '2023-12-31', 100000.00),
('Project Mercury', '2022-03-15', '2023-03-14', 150000.00),
('Project Gemini', '2021-07-01', '2022-06-30', 200000.00);

-- แทรกข้อมูลตัวอย่างใน employees_projects
INSERT INTO employees_projects (employee_id, project_id) VALUES
(1, 1),
(2, 2),
(3, 1),
(3, 3),
(4, 2),
(5, 3);
```

ด้วยคำสั่งเหล่านี้ คุณจะได้ฐานข้อมูล `company_db` ที่มีตาราง `departments`, `employees`, `projects`, และ `employees_projects` พร้อมด้วยข้อมูลตัวอย่างในการจัดการและแสดงข้อมูลของพนักงานและโครงการในบริษัทได้


--- 

## สำหรับระบบยืมคืนหนังสือ

ตัวอย่างฐานข้อมูลสำหรับระบบยืมคืนหนังสือห้องสมุดของโรงเรียนที่มีตารางสำหรับ `students`, `books`, `borrow_records`, และ `fines` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง:

```
+-------------------+        +-------------------+
|     students      |        |  borrow_records   |
+-------------------+        +-------------------+
| student_id (PK)   |<-------| record_id (PK)    |
| first_name        |        | student_id (FK)   |
| last_name         |        | book_id (FK)      |
| email             |        | borrow_date       |
| enrollment_date   |        | return_date       |
+-------------------+        +-------------------+
                                    |
                                    |
          +-------------------+     |
          |      books        |     |
          +-------------------+     |
          | book_id (PK)      |<----+
          | title             |
          | author            |
          | published_year    |
          | isbn              |
          | available         |
          +-------------------+
                   |
                   |
                   |
          +-------------------+
          |      fines        |
          +-------------------+
          | fine_id (PK)      |
          | record_id (FK)    |
          | fine_amount       |
          | paid              |
          +-------------------+
```

### สร้างฐานข้อมูลและตาราง
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE library_system;
USE library_system;

-- สร้างตาราง students
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL
);

-- สร้างตาราง books
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    published_year YEAR NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    available BOOLEAN NOT NULL DEFAULT TRUE
);

-- สร้างตาราง borrow_records
CREATE TABLE borrow_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- สร้างตาราง fines
CREATE TABLE fines (
    fine_id INT PRIMARY KEY AUTO_INCREMENT,
    record_id INT,
    fine_amount DECIMAL(5, 2) NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (record_id) REFERENCES borrow_records(record_id)
);
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน students
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('Alice', 'Wong', 'alice.wong@example.com', '2022-09-01'),
('Bob', 'Johnson', 'bob.johnson@example.com', '2021-09-01'),
('Charlie', 'Smith', 'charlie.smith@example.com', '2020-09-01'),
('David', 'Brown', 'david.brown@example.com', '2019-09-01'),
('Eva', 'Davis', 'eva.davis@example.com', '2018-09-01');

-- แทรกข้อมูลตัวอย่างใน books
INSERT INTO books (title, author, published_year, isbn) VALUES
('Introduction to Algorithms', 'Thomas H. Cormen', 2009, '9780262033848'),
('Clean Code', 'Robert C. Martin', 2008, '9780132350884'),
('The Pragmatic Programmer', 'Andrew Hunt', 1999, '9780201616224'),
('Design Patterns', 'Erich Gamma', 1994, '9780201633610'),
('Code Complete', 'Steve McConnell', 2004, '9780735619678');

-- แทรกข้อมูลตัวอย่างใน borrow_records
INSERT INTO borrow_records (student_id, book_id, borrow_date, return_date) VALUES
(1, 1, '2023-01-10', '2023-02-10'),
(2, 2, '2023-01-15', '2023-02-15'),
(3, 3, '2023-02-01', '2023-03-01'),
(4, 4, '2023-03-01', NULL), -- ยังไม่ได้คืน
(5, 5, '2023-03-10', '2023-04-10');

-- แทรกข้อมูลตัวอย่างใน fines
INSERT INTO fines (record_id, fine_amount, paid) VALUES
(1, 5.00, TRUE),
(2, 10.00, FALSE),
(3, 0.00, TRUE),
(4, 15.00, FALSE), -- ค่าปรับสำหรับการคืนหนังสือล่าช้า
(5, 0.00, TRUE);
```

คำสั่งเหล่านี้จะสร้างฐานข้อมูล `library_system` ที่มีตาราง `students`, `books`, `borrow_records`, และ `fines` พร้อมกับข้อมูลตัวอย่างในการจัดการการยืมคืนหนังสือและการคิดค่าปรับสำหรับการคืนหนังสือช้าของนักเรียนในโรงเรียน

---
## ระบบ stock สินค้า
ตัวอย่างฐานข้อมูลสำหรับระบบสต็อกสินค้าที่มีตารางสำหรับ `products`, `suppliers`, `stock_movements`, และ `orders` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง:
```
+-------------------+        +-------------------+
|     suppliers     |        |     products      |
+-------------------+        +-------------------+
| supplier_id (PK)  |<-------| product_id (PK)   |
| supplier_name     |        | product_name      |
| contact_name      |        | supplier_id (FK)  |
| contact_email     |        | price             |
+-------------------+        | quantity_in_stock |
                             +-------------------+
                                       |
                                       |
                                       |
                    +-------------------+
                    |  stock_movements  |
                    +-------------------+
                    | movement_id (PK)  |
                    | product_id (FK)   |
                    | movement_date     |
                    | movement_type     |
                    | quantity          |
                    +-------------------+
                             |
                             |
                             |
                    +-------------------+
                    |      orders       |
                    +-------------------+
                    | order_id (PK)     |
                    | product_id (FK)   |
                    | order_date        |
                    | quantity          |
                    | total_price       |
                    +-------------------+
```
### สร้างฐานข้อมูลและตาราง
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE stock_system;
USE stock_system;

-- สร้างตาราง suppliers
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(50),
    contact_email VARCHAR(100) UNIQUE
);

-- สร้างตาราง products
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    supplier_id INT,
    price DECIMAL(10, 2) NOT NULL,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- สร้างตาราง stock_movements
CREATE TABLE stock_movements (
    movement_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    movement_date DATE NOT NULL,
    movement_type ENUM('IN', 'OUT') NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- สร้างตาราง orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    order_date DATE NOT NULL,
    quantity INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน suppliers
INSERT INTO suppliers (supplier_name, contact_name, contact_email) VALUES
('ABC Supplies', 'John Doe', 'john.doe@abcsupplies.com'),
('XYZ Distributors', 'Jane Smith', 'jane.smith@xyzdistributors.com'),
('Global Goods', 'Emily Johnson', 'emily.johnson@globalgoods.com');

-- แทรกข้อมูลตัวอย่างใน products
INSERT INTO products (product_name, supplier_id, price, quantity_in_stock) VALUES
('Product A', 1, 50.00, 100),
('Product B', 2, 30.00, 200),
('Product C', 3, 20.00, 150),
('Product D', 1, 40.00, 50),
('Product E', 2, 60.00, 300);

-- แทรกข้อมูลตัวอย่างใน stock_movements
INSERT INTO stock_movements (product_id, movement_date, movement_type, quantity) VALUES
(1, '2024-01-01', 'IN', 100),
(2, '2024-01-05', 'IN', 200),
(3, '2024-01-10', 'IN', 150),
(4, '2024-01-15', 'IN', 50),
(5, '2024-01-20', 'IN', 300),
(1, '2024-02-01', 'OUT', 10),
(2, '2024-02-05', 'OUT', 20),
(3, '2024-02-10', 'OUT', 15),
(4, '2024-02-15', 'OUT', 5),
(5, '2024-02-20', 'OUT', 30);

-- แทรกข้อมูลตัวอย่างใน orders
INSERT INTO orders (product_id, order_date, quantity, total_price) VALUES
(1, '2024-02-01', 10, 500.00),
(2, '2024-02-05', 20, 600.00),
(3, '2024-02-10', 15, 300.00),
(4, '2024-02-15', 5, 200.00),
(5, '2024-02-20', 30, 1800.00);
```

คำสั่งเหล่านี้จะสร้างฐานข้อมูล `stock_system` ที่มีตาราง `suppliers`, `products`, `stock_movements`, และ `orders` พร้อมกับข้อมูลตัวอย่างในการจัดการการสต็อกสินค้า การเคลื่อนไหวของสต็อก และการสั่งซื้อสินค้าจากซัพพลายเออร์


## ระบบลงทะเบียนเรียน
ตัวอย่างฐานข้อมูลสำหรับระบบลงทะเบียนเรียนที่มีตารางสำหรับ `students`, `courses`, `enrollments`, และ `instructors` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง:
```
+-------------------+        +-------------------+
|    instructors    |        |     courses       |
+-------------------+        +-------------------+
| instructor_id (PK)|<-------| course_id (PK)    |
| first_name        |        | course_name       |
| last_name         |        | course_description|
| email             |        | instructor_id (FK)|
+-------------------+        | credits           |
                             +-------------------+
                                       |
                                       |
                                       |
+-------------------+        +-------------------+
|     students      |        |    enrollments    |
+-------------------+        +-------------------+
| student_id (PK)   |<-------| enrollment_id (PK)|
| first_name        |        | student_id (FK)   |
| last_name         |        | course_id (FK)    |
| email             |        | enrollment_date   |
| enrollment_date   |        | grade             |
+-------------------+        +-------------------+
                                       |
                                       |
                                       |
                             +-------------------+
                             |     courses       |
                             +-------------------+
                             | course_id (PK)    |
                             | course_name       |
                             | course_description|
                             | instructor_id (FK)|
                             | credits           |
                             +-------------------+
```

### สร้างฐานข้อมูลและตาราง
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE enrollment_system;
USE enrollment_system;

-- สร้างตาราง instructors
CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- สร้างตาราง courses
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT,
    instructor_id INT,
    credits INT NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- สร้างตาราง students
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL
);

-- สร้างตาราง enrollments
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE NOT NULL,
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน instructors
INSERT INTO instructors (first_name, last_name, email) VALUES
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com'),
('Emily', 'Johnson', 'emily.johnson@example.com');

-- แทรกข้อมูลตัวอย่างใน courses
INSERT INTO courses (course_name, course_description, instructor_id, credits) VALUES
('Introduction to Computer Science', 'Basic concepts of computer science.', 1, 3),
('Data Structures and Algorithms', 'In-depth study of data structures and algorithms.', 2, 4),
('Database Systems', 'Introduction to database design and SQL.', 3, 3);

-- แทรกข้อมูลตัวอย่างใน students
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('Alice', 'Wong', 'alice.wong@example.com', '2022-09-01'),
('Bob', 'Johnson', 'bob.johnson@example.com', '2021-09-01'),
('Charlie', 'Smith', 'charlie.smith@example.com', '2020-09-01'),
('David', 'Brown', 'david.brown@example.com', '2019-09-01'),
('Eva', 'Davis', 'eva.davis@example.com', '2018-09-01');

-- แทรกข้อมูลตัวอย่างใน enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2022-09-01', 'A'),
(1, 2, '2022-09-01', 'B'),
(2, 1, '2021-09-01', 'A'),
(2, 3, '2021-09-01', 'B'),
(3, 2, '2020-09-01', 'C'),
(4, 1, '2019-09-01', 'B'),
(5, 3, '2018-09-01', 'A');
```

คำสั่งเหล่านี้จะสร้างฐานข้อมูล `enrollment_system` ที่มีตาราง `instructors`, `courses`, `students`, และ `enrollments` พร้อมกับข้อมูลตัวอย่างในการจัดการการลงทะเบียนเรียนของนักเรียน, ข้อมูลของหลักสูตร, และการลงทะเบียนเรียนของนักเรียน

## ระบบตั๋วคอนเสิร์ต
ตัวอย่างฐานข้อมูลสำหรับระบบตั๋วคอนเสิร์ตที่มีตารางสำหรับ `customers`, `events`, `tickets`, และ `venues` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง:
```
+-------------------+        +-------------------+
|      venues       |        |      events       |
+-------------------+        +-------------------+
| venue_id (PK)     |<-------| event_id (PK)     |
| venue_name        |        | event_name        |
| location          |        | event_date        |
| capacity          |        | venue_id (FK)     |
+-------------------+        +-------------------+
                                       |
                                       |
                                       |
+-------------------+        +-------------------+
|     customers     |        |      tickets      |
+-------------------+        +-------------------+
| customer_id (PK)  |<-------| ticket_id (PK)    |
| first_name        |        | event_id (FK)     |
| last_name         |        | customer_id (FK)  |
| email             |        | purchase_date     |
+-------------------+        | seat_number       |
                             | price             |
                             +-------------------+
```

### สร้างฐานข้อมูลและตาราง
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE concert_ticket_system;
USE concert_ticket_system;

-- สร้างตาราง venues
CREATE TABLE venues (
    venue_id INT PRIMARY KEY AUTO_INCREMENT,
    venue_name VARCHAR(100) NOT NULL,
    location VARCHAR(200) NOT NULL,
    capacity INT NOT NULL
);

-- สร้างตาราง events
CREATE TABLE events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(100) NOT NULL,
    event_date DATE NOT NULL,
    venue_id INT,
    FOREIGN KEY (venue_id) REFERENCES venues(venue_id)
);

-- สร้างตาราง customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- สร้างตาราง tickets
CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    customer_id INT,
    purchase_date DATE NOT NULL,
    seat_number VARCHAR(10),
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน venues
INSERT INTO venues (venue_name, location, capacity) VALUES
('Central Park Arena', '123 Main St, New York, NY', 5000),
('Downtown Concert Hall', '456 Elm St, Los Angeles, CA', 3000),
('Riverside Theater', '789 River Rd, Chicago, IL', 2000);

-- แทรกข้อมูลตัวอย่างใน events
INSERT INTO events (event_name, event_date, venue_id) VALUES
('Rock Fest 2024', '2024-07-01', 1),
('Jazz Night', '2024-08-15', 2),
('Classical Evening', '2024-09-10', 3);

-- แทรกข้อมูลตัวอย่างใน customers
INSERT INTO customers (first_name, last_name, email) VALUES
('Alice', 'Wong', 'alice.wong@example.com'),
('Bob', 'Johnson', 'bob.johnson@example.com'),
('Charlie', 'Smith', 'charlie.smith@example.com'),
('David', 'Brown', 'david.brown@example.com'),
('Eva', 'Davis', 'eva.davis@example.com');

-- แทรกข้อมูลตัวอย่างใน tickets
INSERT INTO tickets (event_id, customer_id, purchase_date, seat_number, price) VALUES
(1, 1, '2024-06-01', 'A1', 100.00),
(1, 2, '2024-06-01', 'A2', 100.00),
(2, 3, '2024-07-15', 'B1', 75.00),
(2, 4, '2024-07-16', 'B2', 75.00),
(3, 5, '2024-08-01', 'C1', 50.00);
```

คำสั่งเหล่านี้จะสร้างฐานข้อมูล `concert_ticket_system` ที่มีตาราง `venues`, `events`, `customers`, และ `tickets` พร้อมกับข้อมูลตัวอย่างในการจัดการการขายตั๋วคอนเสิร์ต การจัดการข้อมูลลูกค้า สถานที่จัดงาน และข้อมูลเกี่ยวกับคอนเสิร์ตต่างๆ

## ระบบข้อมูลผู้ป่วยนอก
ตัวอย่างฐานข้อมูลสำหรับระบบข้อมูลผู้ป่วยนอกที่มีตารางสำหรับ `patients`, `doctors`, `appointments`, และ `prescriptions` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง:
```
+-------------------+        +-------------------+
|     patients      |        |     doctors       |
+-------------------+        +-------------------+
| patient_id (PK)   |        | doctor_id (PK)    |
| first_name        |        | first_name        |
| last_name         |        | last_name         |
| date_of_birth     |        | specialty         |
| gender            |        | contact_number    |
| contact_number    |        | email             |
| email             |        |                   |
+-------------------+        +-------------------+
         |                            |
         |                            |
         |                            |
         |    +-------------------+   |
         |    |   appointments    |   |
         |    +-------------------+   |
         +--->| appointment_id(PK)|<--+
              | patient_id (FK)   |
              | doctor_id (FK)    |
              | appointment_date  |
              | appointment_time  |
              | status            |
              +-------------------+
                        |
                        |
                        |
              +--------------------+
              |   prescriptions    |
              +--------------------+
              | prescription_id(PK)|
              | appointment_id(FK) |
              | medication_name    |
              | dosage             |
              | frequency          |
              +--------------------+
```   

### สร้างฐานข้อมูลและตาราง
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE outpatient_system;
USE outpatient_system;

-- สร้างตาราง patients
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- สร้างตาราง doctors
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- สร้างตาราง appointments
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- สร้างตาราง prescriptions
CREATE TABLE prescriptions (
    prescription_id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_id INT,
    medication_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(50) NOT NULL,
    frequency VARCHAR(50) NOT NULL,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน patients
INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_number, email) VALUES
('Alice', 'Wong', '1980-01-15', 'Female', '555-1234', 'alice.wong@example.com'),
('Bob', 'Johnson', '1975-05-20', 'Male', '555-5678', 'bob.johnson@example.com'),
('Charlie', 'Smith', '1990-09-30', 'Male', '555-8765', 'charlie.smith@example.com'),
('David', 'Brown', '1985-12-10', 'Male', '555-4321', 'david.brown@example.com'),
('Eva', 'Davis', '1978-03-25', 'Female', '555-6789', 'eva.davis@example.com');

-- แทรกข้อมูลตัวอย่างใน doctors
INSERT INTO doctors (first_name, last_name, specialty, contact_number, email) VALUES
('John', 'Doe', 'Cardiology', '555-1111', 'john.doe@hospital.com'),
('Jane', 'Smith', 'Dermatology', '555-2222', 'jane.smith@hospital.com'),
('Emily', 'Johnson', 'Neurology', '555-3333', 'emily.johnson@hospital.com'),
('Michael', 'Brown', 'Pediatrics', '555-4444', 'michael.brown@hospital.com'),
('Jessica', 'Davis', 'Orthopedics', '555-5555', 'jessica.davis@hospital.com');

-- แทรกข้อมูลตัวอย่างใน appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status) VALUES
(1, 1, '2024-06-01', '09:00:00', 'Scheduled'),
(2, 2, '2024-06-01', '10:00:00', 'Completed'),
(3, 3, '2024-06-02', '11:00:00', 'Scheduled'),
(4, 4, '2024-06-03', '13:00:00', 'Cancelled'),
(5, 5, '2024-06-04', '14:00:00', 'Completed');

-- แทรกข้อมูลตัวอย่างใน prescriptions
INSERT INTO prescriptions (appointment_id, medication_name, dosage, frequency) VALUES
(2, 'Aspirin', '500mg', 'Twice a day'),
(2, 'Metformin', '500mg', 'Once a day'),
(5, 'Lisinopril', '10mg', 'Once a day'),
(5, 'Atorvastatin', '20mg', 'Once a day');
```

คำสั่งเหล่านี้จะสร้างฐานข้อมูล `outpatient_system` ที่มีตาราง `patients`, `doctors`, `appointments`, และ `prescriptions` พร้อมกับข้อมูลตัวอย่างในการจัดการข้อมูลผู้ป่วย ข้อมูลแพทย์ การนัดหมาย และใบสั่งยาในระบบผู้ป่วยนอก

## ระบบซ่อมบำรุง
ได้เลยครับ นี่คือตัวอย่างฐานข้อมูลสำหรับระบบซ่อมบำรุงที่มีตารางสำหรับ `customers`, `technicians`, `service_requests`, และ `service_logs` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง พร้อมกับใส่คอมเมนต์เพื่ออธิบายแต่ละตาราง:
```
+-------------------+        +-------------------+
|     customers     |        |    technicians    |
+-------------------+        +-------------------+
| customer_id (PK)  |        | technician_id (PK)|
| first_name        |        | first_name        |
| last_name         |        | last_name         |
| contact_number    |        | specialty         |
| email             |        | contact_number    |
+-------------------+        +-------------------+
         |                            |
         |                            |
         |                            |
         |    +-------------------+   |
         |    | service_requests  |   |
         |    +-------------------+   |
         +--->| request_id (PK)   |<--+
              | customer_id (FK)  |
              | technician_id (FK)|
              | request_date      |
              | status            |
              | description       |
              +-------------------+
                        |
                        |
                        |
              +-------------------+
              |   service_logs    |
              +-------------------+
              | log_id (PK)       |
              | request_id (FK)   |
              | log_date          |
              | notes             |
              +-------------------+
```

### สร้างฐานข้อมูลและตารางพร้อมคอมเมนต์
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE maintenance_system;
USE maintenance_system;

-- สร้างตาราง customers (ข้อมูลลูกค้า)
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสลูกค้า
    first_name VARCHAR(50) NOT NULL, -- ชื่อลูกค้า
    last_name VARCHAR(50) NOT NULL, -- นามสกุลลูกค้า
    contact_number VARCHAR(15) NOT NULL, -- เบอร์โทรศัพท์ลูกค้า
    email VARCHAR(100) UNIQUE NOT NULL -- อีเมลลูกค้า
) COMMENT 'ตารางสำหรับเก็บข้อมูลลูกค้า';

-- สร้างตาราง technicians (ข้อมูลช่างซ่อมบำรุง)
CREATE TABLE technicians (
    technician_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสช่าง
    first_name VARCHAR(50) NOT NULL, -- ชื่อช่าง
    last_name VARCHAR(50) NOT NULL, -- นามสกุลช่าง
    specialty VARCHAR(100) NOT NULL, -- ความเชี่ยวชาญของช่าง
    contact_number VARCHAR(15) NOT NULL -- เบอร์โทรศัพท์ช่าง
) COMMENT 'ตารางสำหรับเก็บข้อมูลช่างซ่อมบำรุง';

-- สร้างตาราง service_requests (ข้อมูลการร้องขอบริการซ่อมบำรุง)
CREATE TABLE service_requests (
    request_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสคำร้องขอ
    customer_id INT, -- รหัสลูกค้าที่ร้องขอ
    technician_id INT, -- รหัสช่างที่ได้รับมอบหมาย
    request_date DATE NOT NULL, -- วันที่ร้องขอบริการ
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL, -- สถานะของคำร้องขอ
    description TEXT NOT NULL, -- รายละเอียดของปัญหา
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id), -- การอ้างอิงไปยังรหัสลูกค้า
    FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) -- การอ้างอิงไปยังรหัสช่าง
) COMMENT 'ตารางสำหรับเก็บข้อมูลการร้องขอบริการซ่อมบำรุง';

-- สร้างตาราง service_logs (ข้อมูลบันทึกการซ่อมบำรุง)
CREATE TABLE service_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสบันทึก
    request_id INT, -- รหัสคำร้องขอที่เกี่ยวข้อง
    log_date DATE NOT NULL, -- วันที่บันทึก
    notes TEXT NOT NULL, -- บันทึกการดำเนินงาน
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) -- การอ้างอิงไปยังรหัสคำร้องขอ
) COMMENT 'ตารางสำหรับเก็บข้อมูลบันทึกการซ่อมบำรุง';
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน customers (ข้อมูลลูกค้า)
INSERT INTO customers (first_name, last_name, contact_number, email) VALUES
('Alice', 'Wong', '555-1234', 'alice.wong@example.com'),
('Bob', 'Johnson', '555-5678', 'bob.johnson@example.com'),
('Charlie', 'Smith', '555-8765', 'charlie.smith@example.com'),
('David', 'Brown', '555-4321', 'david.brown@example.com'),
('Eva', 'Davis', '555-6789', 'eva.davis@example.com');

-- แทรกข้อมูลตัวอย่างใน technicians (ข้อมูลช่างซ่อมบำรุง)
INSERT INTO technicians (first_name, last_name, specialty, contact_number) VALUES
('John', 'Doe', 'Electrical', '555-1111'),
('Jane', 'Smith', 'Plumbing', '555-2222'),
('Emily', 'Johnson', 'HVAC', '555-3333'),
('Michael', 'Brown', 'Carpentry', '555-4444'),
('Jessica', 'Davis', 'General Maintenance', '555-5555');

-- แทรกข้อมูลตัวอย่างใน service_requests (ข้อมูลการร้องขอบริการซ่อมบำรุง)
INSERT INTO service_requests (customer_id, technician_id, request_date, status, description) VALUES
(1, 1, '2024-06-01', 'Pending', 'Fix electrical outlet in living room'),
(2, 2, '2024-06-01', 'In Progress', 'Repair leaking sink in kitchen'),
(3, 3, '2024-06-02', 'Completed', 'Service HVAC system'),
(4, 4, '2024-06-03', 'Pending', 'Repair broken door in bedroom'),
(5, 5, '2024-06-04', 'Completed', 'General maintenance and inspection');

-- แทรกข้อมูลตัวอย่างใน service_logs (ข้อมูลบันทึกการซ่อมบำรุง)
INSERT INTO service_logs (request_id, log_date, notes) VALUES
(2, '2024-06-01', 'Started working on the sink repair'),
(2, '2024-06-02', 'Replaced the faulty pipe and tested for leaks'),
(3, '2024-06-02', 'Completed HVAC service and replaced filters'),
(5, '2024-06-04', 'Completed general maintenance and inspection, no issues found');
```

คำสั่งเหล่านี้จะสร้างฐานข้อมูล `maintenance_system` ที่มีตาราง `customers`, `technicians`, `service_requests`, และ `service_logs` พร้อมกับข้อมูลตัวอย่างในการจัดการการซ่อมบำรุง ข้อมูลลูกค้า ข้อมูลช่างซ่อมบำรุง การร้องขอบริการ และบันทึกการซ่อมบำรุง


## ระบบบันทึกรายรับ-รายจ่าย
ตัวอย่างฐานข้อมูลสำหรับระบบบันทึกรายรับรายจ่ายที่มีตารางสำหรับ `users`, `categories`, `transactions`, และ `budgets` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง พร้อมกับใส่คอมเมนต์เพื่ออธิบายแต่ละตาราง:
```
+-------------------+
|       users       |
+-------------------+
| user_id (PK)      |
| username          |
| password          |
| email             |
| created_at        |
+-------------------+
         |
         |
    +----+---------------------------+
    |                                |
    |                                |
+-------------------+        +-------------------+
|   transactions    |        |     budgets       |
+-------------------+        +-------------------+
| transaction_id(PK)|        | budget_id (PK)    |
| user_id (FK)      |        | user_id (FK)      |
| category_id (FK)  |        | category_id (FK)  |
| transaction_date  |        | budget_amount     |
| amount            |        | start_date        |
| description       |        | end_date          |
+-------------------+        +-------------------+
         |                            |
         |                            |
         |                            |
         |    +-------------------+   |
         |    |    categories     |   |
         |    +-------------------+   |
         +--->| category_id (PK)  |<--+
              | category_name     |
              | type              |
              +-------------------+
```

### สร้างฐานข้อมูลและตารางพร้อมคอมเมนต์
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE expense_tracking_system;
USE expense_tracking_system;

-- สร้างตาราง users (ข้อมูลผู้ใช้)
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสผู้ใช้
    username VARCHAR(50) NOT NULL UNIQUE, -- ชื่อผู้ใช้
    password VARCHAR(100) NOT NULL, -- รหัสผ่านผู้ใช้
    email VARCHAR(100) UNIQUE NOT NULL, -- อีเมลผู้ใช้
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- วันที่สร้างบัญชี
) COMMENT 'ตารางสำหรับเก็บข้อมูลผู้ใช้';

-- สร้างตาราง categories (ประเภทของรายรับรายจ่าย)
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสประเภท
    category_name VARCHAR(50) NOT NULL, -- ชื่อประเภท
    type ENUM('Income', 'Expense') NOT NULL -- ประเภท (รายรับ หรือ รายจ่าย)
) COMMENT 'ตารางสำหรับเก็บประเภทของรายรับรายจ่าย';

-- สร้างตาราง transactions (ข้อมูลการทำธุรกรรม)
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสธุรกรรม
    user_id INT, -- รหัสผู้ใช้ที่ทำธุรกรรม
    category_id INT, -- รหัสประเภทของธุรกรรม
    transaction_date DATE NOT NULL, -- วันที่ทำธุรกรรม
    amount DECIMAL(10, 2) NOT NULL, -- จำนวนเงิน
    description TEXT, -- คำอธิบาย
    FOREIGN KEY (user_id) REFERENCES users(user_id), -- การอ้างอิงไปยังรหัสผู้ใช้
    FOREIGN KEY (category_id) REFERENCES categories(category_id) -- การอ้างอิงไปยังรหัสประเภท
) COMMENT 'ตารางสำหรับเก็บข้อมูลการทำธุรกรรม';

-- สร้างตาราง budgets (ข้อมูลงบประมาณ)
CREATE TABLE budgets (
    budget_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสงบประมาณ
    user_id INT, -- รหัสผู้ใช้ที่ตั้งงบประมาณ
    category_id INT, -- รหัสประเภทของงบประมาณ
    budget_amount DECIMAL(10, 2) NOT NULL, -- จำนวนงบประมาณ
    start_date DATE NOT NULL, -- วันที่เริ่มต้นงบประมาณ
    end_date DATE NOT NULL, -- วันที่สิ้นสุดงบประมาณ
    FOREIGN KEY (user_id) REFERENCES users(user_id), -- การอ้างอิงไปยังรหัสผู้ใช้
    FOREIGN KEY (category_id) REFERENCES categories(category_id) -- การอ้างอิงไปยังรหัสประเภท
) COMMENT 'ตารางสำหรับเก็บข้อมูลงบประมาณ';
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน users (ข้อมูลผู้ใช้)
INSERT INTO users (username, password, email) VALUES
('alice', 'password1', 'alice@example.com'),
('bob', 'password2', 'bob@example.com'),
('charlie', 'password3', 'charlie@example.com');

-- แทรกข้อมูลตัวอย่างใน categories (ประเภทของรายรับรายจ่าย)
INSERT INTO categories (category_name, type) VALUES
('Salary', 'Income'),
('Freelance', 'Income'),
('Groceries', 'Expense'),
('Rent', 'Expense'),
('Utilities', 'Expense');

-- แทรกข้อมูลตัวอย่างใน transactions (ข้อมูลการทำธุรกรรม)
INSERT INTO transactions (user_id, category_id, transaction_date, amount, description) VALUES
(1, 1, '2024-06-01', 3000.00, 'Monthly salary'),
(1, 3, '2024-06-02', 150.00, 'Grocery shopping'),
(2, 2, '2024-06-03', 500.00, 'Freelance project'),
(2, 4, '2024-06-04', 1200.00, 'Monthly rent'),
(3, 5, '2024-06-05', 100.00, 'Utility bill');

-- แทรกข้อมูลตัวอย่างใน budgets (ข้อมูลงบประมาณ)
INSERT INTO budgets (user_id, category_id, budget_amount, start_date, end_date) VALUES
(1, 3, 500.00, '2024-06-01', '2024-06-30'),
(2, 4, 1200.00, '2024-06-01', '2024-06-30'),
(3, 5, 150.00, '2024-06-01', '2024-06-30');
```

คำสั่งเหล่านี้จะสร้างฐานข้อมูล `expense_tracking_system` ที่มีตาราง `users`, `categories`, `transactions`, และ `budgets` พร้อมกับข้อมูลตัวอย่างในการจัดการบันทึกรายรับรายจ่าย ข้อมูลผู้ใช้ ประเภทของธุรกรรม และการตั้งงบประมาณ

## ระบบโรงเรียน
ได้เลยครับ นี่คือตัวอย่างฐานข้อมูลสำหรับระบบจัดการโรงเรียนที่มีความซับซ้อน โดยมีตารางสำหรับ `students`, `teachers`, `courses`, `enrollments`, `classes`, `grades`, `departments`, `assignments`, และ `class_assignments` พร้อมกับการสร้างและแทรกข้อมูลตัวอย่าง พร้อมกับใส่คอมเมนต์เพื่ออธิบายแต่ละตารางและความสัมพันธ์:
```
+-------------+     +-------------+     +-------------+
|  students   |     |  teachers   |     | departments |
+-------------+     +-------------+     +-------------+
|student_id PK|     |teacher_id PK|     |department_id|
|first_name   |     |first_name   |     |    PK       |
|last_name    |     |last_name    |     |department_  |
|date_of_birth|     |hire_date    |     |   name      |
|gender       |     |department_id|     +-------------+
|contact_     |     |   FK        |           |
|  number     |     |contact_     |           |
|email        |     |  number     |           |
|enrollment_  |     |email        |           |
|  date       |     +-------------+           |
+-------------+           |                   |
      |                   |                   |
      |                   |                   |
      |               +---+-------------------+
      |               |
      |         +-----+-----+
      |         |  courses  |
      |         +-----------+
      |         |course_id  |
      |         |   PK      |
      |         |course_name|
      |         |course_    |
      |         | description|
      |         |credits    |
      |         |department_|
      |         |  id FK    |
      |         +-----------+
      |               |
      |               |
+-----+-----+   +-----+-----+
|enrollments|   |  classes  |
+-----------+   +-----------+
|enrollment_|   |class_id PK|
| id PK     |   |course_id  |
|student_id |   |  FK       |
|  FK       |   |teacher_id |
|class_id FK|   |  FK       |
|enrollment_|   |semester   |
|  date     |   |year       |
+-----------+   +-----------+
      |               |
      |         +-----+-----+
      |         |   class_  |
      |         |assignments|
      |         +-----------+
      |         |class_     |
      |         | assignment_|
      |         |  id PK    |
      |         |class_id FK|
      |         |assignment_|
      |         |  id FK    |
      |         |assigned_  |
      |         |  date     |
      |         +-----------+
      |               |
+-----+-----+   +-----+-----+
|  grades   |   |assignments|
+-----------+   +-----------+
|grade_id PK|   |assignment_|
|enrollment_|   |  id PK    |
| id FK     |   |assignment_|
|assignment_|   |  title    |
| id FK     |   |assignment_|
|grade      |   | description|
|grade_date |   |due_date   |
+-----------+   +-----------+
```

### สร้างฐานข้อมูลและตารางพร้อมคอมเมนต์
```sql
-- สร้างฐานข้อมูล
CREATE DATABASE school_management_system;
USE school_management_system;

-- สร้างตาราง students (ข้อมูลนักเรียน)
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสนักเรียน
    first_name VARCHAR(50) NOT NULL, -- ชื่อนักเรียน
    last_name VARCHAR(50) NOT NULL, -- นามสกุลนักเรียน
    date_of_birth DATE NOT NULL, -- วันเกิดนักเรียน
    gender ENUM('Male', 'Female') NOT NULL, -- เพศนักเรียน
    contact_number VARCHAR(15), -- เบอร์โทรศัพท์นักเรียน
    email VARCHAR(100) UNIQUE, -- อีเมลนักเรียน
    enrollment_date DATE NOT NULL -- วันที่ลงทะเบียน
) COMMENT 'ตารางสำหรับเก็บข้อมูลนักเรียน';

-- สร้างตาราง teachers (ข้อมูลครู)
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสครู
    first_name VARCHAR(50) NOT NULL, -- ชื่อครู
    last_name VARCHAR(50) NOT NULL, -- นามสกุลครู
    hire_date DATE NOT NULL, -- วันที่เข้าทำงาน
    department_id INT, -- รหัสแผนก
    contact_number VARCHAR(15), -- เบอร์โทรศัพท์ครู
    email VARCHAR(100) UNIQUE -- อีเมลครู
) COMMENT 'ตารางสำหรับเก็บข้อมูลครู';

-- สร้างตาราง departments (ข้อมูลแผนก)
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสแผนก
    department_name VARCHAR(100) NOT NULL -- ชื่อแผนก
) COMMENT 'ตารางสำหรับเก็บข้อมูลแผนก';

-- สร้างตาราง courses (ข้อมูลรายวิชา)
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสรายวิชา
    course_name VARCHAR(100) NOT NULL, -- ชื่อรายวิชา
    course_description TEXT, -- รายละเอียดรายวิชา
    credits INT NOT NULL, -- จำนวนหน่วยกิต
    department_id INT, -- รหัสแผนก
    FOREIGN KEY (department_id) REFERENCES departments(department_id) -- การอ้างอิงไปยังรหัสแผนก
) COMMENT 'ตารางสำหรับเก็บข้อมูลรายวิชา';

-- สร้างตาราง classes (ข้อมูลชั้นเรียน)
CREATE TABLE classes (
    class_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสชั้นเรียน
    course_id INT, -- รหัสรายวิชา
    teacher_id INT, -- รหัสครู
    semester VARCHAR(10) NOT NULL, -- ภาคการศึกษา
    year INT NOT NULL, -- ปีการศึกษา
    FOREIGN KEY (course_id) REFERENCES courses(course_id), -- การอ้างอิงไปยังรหัสรายวิชา
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) -- การอ้างอิงไปยังรหัสครู
) COMMENT 'ตารางสำหรับเก็บข้อมูลชั้นเรียน';

-- สร้างตาราง enrollments (ข้อมูลการลงทะเบียนเรียน)
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสการลงทะเบียน
    student_id INT, -- รหัสนักเรียน
    class_id INT, -- รหัสชั้นเรียน
    enrollment_date DATE NOT NULL, -- วันที่ลงทะเบียน
    FOREIGN KEY (student_id) REFERENCES students(student_id), -- การอ้างอิงไปยังรหัสนักเรียน
    FOREIGN KEY (class_id) REFERENCES classes(class_id) -- การอ้างอิงไปยังรหัสชั้นเรียน
) COMMENT 'ตารางสำหรับเก็บข้อมูลการลงทะเบียนเรียน';

-- สร้างตาราง assignments (ข้อมูลการบ้าน/งานที่มอบหมาย)
CREATE TABLE assignments (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสการบ้าน
    assignment_title VARCHAR(100) NOT NULL, -- ชื่อการบ้าน
    assignment_description TEXT, -- รายละเอียดการบ้าน
    due_date DATE NOT NULL -- วันที่ครบกำหนดส่ง
) COMMENT 'ตารางสำหรับเก็บข้อมูลการบ้าน/งานที่มอบหมาย';

-- สร้างตาราง class_assignments (ข้อมูลการบ้านที่มอบหมายในแต่ละชั้นเรียน)
CREATE TABLE class_assignments (
    class_assignment_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสการบ้านในชั้นเรียน
    class_id INT, -- รหัสชั้นเรียน
    assignment_id INT, -- รหัสการบ้าน
    assigned_date DATE NOT NULL, -- วันที่มอบหมาย
    FOREIGN KEY (class_id) REFERENCES classes(class_id), -- การอ้างอิงไปยังรหัสชั้นเรียน
    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id) -- การอ้างอิงไปยังรหัสการบ้าน
) COMMENT 'ตารางสำหรับเก็บข้อมูลการบ้านที่มอบหมายในแต่ละชั้นเรียน';

-- สร้างตาราง grades (ข้อมูลเกรด)
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT, -- รหัสเกรด
    enrollment_id INT, -- รหัสการลงทะเบียน
    assignment_id INT, -- รหัสการบ้าน
    grade VARCHAR(2), -- เกรด
    grade_date DATE NOT NULL, -- วันที่ให้เกรด
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id), -- การอ้างอิงไปยังรหัสการลงทะเบียน
    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id) -- การอ้างอิงไปยังรหัสการบ้าน
) COMMENT 'ตารางสำหรับเก็บข้อมูลเกรด';
```

### แทรกข้อมูลตัวอย่าง

```sql
-- แทรกข้อมูลตัวอย่างใน students (ข้อมูลนักเรียน)
INSERT INTO students (first_name, last_name, date_of_birth, gender, contact_number, email, enrollment_date) VALUES
('Alice', 'Wong', '2005-01-15', 'Female', '555-1234', 'alice.wong@example.com', '2020-09-01'),
('Bob', 'Johnson', '2004-05-20', 'Male', '555-5678', 'bob.johnson@example.com', '2019-09-01'),
('Charlie', 'Smith', '2006-09-30', 'Male', '555-8765', 'charlie.smith@example.com', '2021-09-01');

-- แทรกข้อมูลตัวอย่างใน departments (ข้อมูลแผนก)
INSERT INTO departments (department_name) VALUES
('Computer Science'),
('Mathematics'),
('Physics');

-- แทรกข้อมูลตัวอย่างใน teachers (ข้อมูลครู)
INSERT INTO teachers (first_name, last_name, hire_date, department_id, contact_number, email) VALUES
('John', 'Doe', '2010-01-10', 1, '555-1111', 'john.doe@school.com'),
('Jane', 'Smith', '2012-02-20', 2, '555-2222', 'jane.smith@school.com'),
('Emily', 'Johnson', '2015-03-30', 3, '555-3333', 'emily.johnson@school.com');

-- แทรกข้อมูลตัวอย่างใน courses (ข้อมูลรายวิชา)
INSERT INTO courses (course_name, course_description, credits, department_id) VALUES
('Introduction to Computer Science', 'Basic concepts of computer science.', 3, 1),
('Calculus I', 'Introduction to calculus.', 4, 2),
('Physics I', 'Introduction to physics.', 3, 3);

-- แทรกข้อมูลตัวอย่างใน classes (ข้อมูลชั้นเรียน)
INSERT INTO classes (course_id, teacher_id, semester, year) VALUES
(1, 1, 'Fall', 2023),
(2, 2, 'Fall', 2023),
(3, 3, 'Fall', 2023);

-- แทรกข้อมูลตัวอย่างใน enrollments (ข้อมูลการลงทะเบียนเรียน)
INSERT INTO enrollments (student_id, class_id, enrollment_date) VALUES
(1, 1, '2023-09-01'),
(2, 2, '2023-09-01'),
(3, 3, '2023-09-01');

-- แทรกข้อมูลตัวอย่างใน assignments (ข้อมูลการบ้าน/งานที่มอบหมาย)
INSERT INTO assignments (assignment_title, assignment_description, due_date) VALUES
('Homework 1', 'Solve problems 1-10.', '2023-09-15'),
('Project 1', 'Complete the project proposal.', '2023-10-01');

-- แทรกข้อมูลตัวอย่างใน class_assignments (ข้อมูลการบ้านที่มอบหมายในแต่ละชั้นเรียน)
INSERT INTO class_assignments (class_id, assignment_id, assigned_date) VALUES
(1, 1, '2023-09-01'),
(2, 2, '2023-09-01');

-- แทรกข้อมูลตัวอย่างใน grades (ข้อมูลเกรด)
INSERT INTO grades (enrollment_id, assignment_id, grade, grade