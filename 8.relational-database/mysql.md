# RDBMS (Relational Database Management System)

### RDBMS (Relational Database Management System) คืออะไร?

**RDBMS (Relational Database Management System)** หรือ **ระบบจัดการฐานข้อมูลเชิงสัมพันธ์** เป็นระบบซอฟต์แวร์ที่ช่วยจัดการฐานข้อมูลที่มีการเชื่อมโยงกันระหว่างตารางต่างๆ โดยมีการจัดเก็บข้อมูลในรูปแบบตาราง (table) ซึ่งแต่ละตารางจะประกอบด้วยแถว (row) และคอลัมน์ (column)

#### คุณสมบัติหลักของ RDBMS:

1. **โครงสร้างฐานข้อมูลเชิงสัมพันธ์**:

   - ข้อมูลถูกจัดเก็บในตารางที่มีการกำหนดโครงสร้างชัดเจน โดยแต่ละตารางจะมีแถวที่แทนข้อมูลหนึ่งชุด และคอลัมน์ที่แทนประเภทของข้อมูล

2. **ความสมบูรณ์ของข้อมูล**:

   - RDBMS ใช้การกำหนดคีย์หลัก (primary key) เพื่อระบุเอกลักษณ์ของแถวในตาราง และคีย์ต่างประเทศ (foreign key) เพื่อเชื่อมโยงข้อมูลระหว่างตาราง

3. **การจัดการข้อมูลอย่างมีประสิทธิภาพ**:

   - มีการใช้ดัชนี (index) เพื่อเพิ่มประสิทธิภาพในการค้นหาข้อมูล
   - สามารถทำการปรับปรุง แทรก ลบ และค้นหาข้อมูลได้อย่างรวดเร็ว

4. **การใช้ภาษา SQL (Structured Query Language)**:

   - RDBMS ใช้ SQL ในการจัดการฐานข้อมูล เช่น การสร้างตาราง การเพิ่มข้อมูล การอัปเดตข้อมูล และการลบข้อมูล

5. **การควบคุมความปลอดภัยและสิทธิ์การเข้าถึง**:

   - มีระบบการควบคุมสิทธิ์การเข้าถึงข้อมูล เพื่อให้แน่ใจว่าผู้ใช้ที่มีสิทธิ์เท่านั้นสามารถเข้าถึงหรือแก้ไขข้อมูลได้

6. **การบำรุงรักษาความสมบูรณ์ของข้อมูล (Data Integrity)**:

   - ใช้ข้อจำกัด (constraints) และกฎเกณฑ์ (rules) ต่างๆ เพื่อรักษาความถูกต้องและความสอดคล้องของข้อมูล

7. **ความสามารถในการกู้คืนข้อมูล (Data Recovery)**:
   - มีระบบการสำรองข้อมูล (backup) และการกู้คืนข้อมูล (recovery) เพื่อป้องกันการสูญหายของข้อมูล

#### ตัวอย่างของ RDBMS ที่เป็นที่นิยม:

- **MySQL**: ใช้กันอย่างแพร่หลายทั้งในเว็บไซต์ขนาดเล็กและใหญ่
- **PostgreSQL**: เป็นระบบที่มีความสามารถสูงและสนับสนุนมาตรฐาน SQL อย่างเต็มรูปแบบ
- **SQLite**: เป็นฐานข้อมูลขนาดเล็กที่เหมาะสำหรับการใช้งานในแอปพลิเคชันที่ไม่ต้องการการจัดการฐานข้อมูลที่ซับซ้อน
- **Microsoft SQL Server**: เป็นฐานข้อมูลที่นิยมใช้ในองค์กรที่ใช้ผลิตภัณฑ์ของ Microsoft
- **Oracle Database**: เป็นฐานข้อมูลที่มีความสามารถสูงและนิยมใช้ในองค์กรขนาดใหญ่

การใช้งาน RDBMS ทำให้การจัดการข้อมูลมีประสิทธิภาพและเป็นระเบียบ สามารถรองรับการทำงานของระบบที่ซับซ้อนได้อย่างดี

### โครงสร้างของ RDBMS

**RDBMS (Relational Database Management System)** มีโครงสร้างที่ชัดเจนและสามารถเข้าใจได้ง่าย โดยประกอบด้วยส่วนประกอบหลักๆ ดังนี้:

1. **ตาราง (Table)**:

   - ตารางคือโครงสร้างหลักใน RDBMS ที่ใช้ในการเก็บข้อมูล
   - แต่ละตารางประกอบด้วยแถว (row) และคอลัมน์ (column)
   - แถว (row) แทนแต่ละระเบียน (record) ของข้อมูล
   - คอลัมน์ (column) แทนประเภทของข้อมูลหรือฟิลด์ (field)

2. **แถว (Row)**:

   - แถวเป็นระเบียนของข้อมูลหนึ่งชุดในตาราง
   - แต่ละแถวมีคีย์หลัก (primary key) ซึ่งเป็นค่าที่ไม่ซ้ำกันและใช้ระบุแถวได้เฉพาะเจาะจง

3. **คอลัมน์ (Column)**:

   - คอลัมน์เป็นฟิลด์ที่เก็บข้อมูลชนิดเดียวกันในทุกแถวของตาราง
   - แต่ละคอลัมน์มีชื่อและชนิดข้อมูล (data type) ที่กำหนดไว้

4. **คีย์หลัก (Primary Key)**:

   - คีย์หลักคือฟิลด์หรือชุดของฟิลด์ที่ระบุเอกลักษณ์ของแต่ละแถวในตาราง
   - ไม่มีค่าซ้ำกันและไม่สามารถเป็นค่าว่างได้

5. **คีย์ต่างประเทศ (Foreign Key)**:

   - คีย์ต่างประเทศคือฟิลด์ที่ใช้เชื่อมโยงข้อมูลระหว่างตารางสองตาราง
   - ใช้เพื่อรักษาความสัมพันธ์ระหว่างตาราง โดยคีย์ต่างประเทศในตารางหนึ่งจะอ้างอิงถึงคีย์หลักในอีกตารางหนึ่ง

6. **ดัชนี (Index)**:

   - ดัชนีใช้เพื่อเพิ่มประสิทธิภาพในการค้นหาข้อมูล
   - ดัชนีสร้างขึ้นบนฟิลด์หนึ่งหรือหลายฟิลด์ในตาราง

7. **มุมมอง (View)**:

   - มุมมองคือการนำเสนอข้อมูลจากหลายตารางในรูปแบบตารางเสมือน
   - ใช้เพื่อทำให้ง่ายต่อการเข้าถึงและการจัดการข้อมูลที่ซับซ้อน

8. **ข้อจำกัด (Constraints)**:
   - ข้อจำกัดใช้เพื่อกำหนดกฎเกณฑ์และความสมบูรณ์ของข้อมูลในตาราง
   - เช่น ข้อจำกัดของคีย์หลัก (Primary Key Constraint), ข้อจำกัดของคีย์ต่างประเทศ (Foreign Key Constraint), ข้อจำกัดไม่เป็นค่าว่าง (NOT NULL Constraint), และข้อจำกัดค่าที่ไม่ซ้ำกัน (UNIQUE Constraint)

#### การใช้งาน SQL ใน RDBMS:

- **คำสั่ง DDL (Data Definition Language)**:

  - ใช้ในการกำหนดโครงสร้างของฐานข้อมูล เช่น `CREATE`, `ALTER`, `DROP`

- **คำสั่ง DML (Data Manipulation Language)**:

  - ใช้ในการจัดการข้อมูลในฐานข้อมูล เช่น `SELECT`, `INSERT`, `UPDATE`, `DELETE`

- **คำสั่ง DCL (Data Control Language)**:

  - ใช้ในการควบคุมสิทธิ์การเข้าถึงข้อมูล เช่น `GRANT`, `REVOKE`

- **คำสั่ง TCL (Transaction Control Language)**:
  - ใช้ในการควบคุมธุรกรรม เช่น `COMMIT`, `ROLLBACK`, `SAVEPOINT`

การเข้าใจโครงสร้างและองค์ประกอบของ RDBMS จะช่วยให้สามารถออกแบบและจัดการฐานข้อมูลได้อย่างมีประสิทธิภาพและปลอดภัย

### MySQL คืออะไร?

**MySQL** เป็นหนึ่งในระบบจัดการฐานข้อมูลเชิงสัมพันธ์ (RDBMS) ที่ได้รับความนิยมมากที่สุดในโลก ได้รับการพัฒนาและดูแลโดยบริษัท Oracle Corporation MySQL ถูกใช้อย่างแพร่หลายในหลากหลายแอปพลิเคชัน ตั้งแต่เว็บแอปพลิเคชันขนาดเล็กไปจนถึงระบบขนาดใหญ่ที่ต้องการประสิทธิภาพและความน่าเชื่อถือสูง

#### คุณสมบัติหลักของ MySQL:

1. **โอเพนซอร์ส (Open Source)**:

   - MySQL เป็นซอฟต์แวร์โอเพนซอร์สที่สามารถดาวน์โหลดและใช้งานได้ฟรี
   - มีการพัฒนาอย่างต่อเนื่องโดยชุมชนผู้ใช้งานและผู้พัฒนา

2. **ประสิทธิภาพสูง (High Performance)**:

   - MySQL ถูกออกแบบมาให้มีประสิทธิภาพสูงในการจัดการข้อมูล
   - สามารถรองรับการทำงานกับฐานข้อมูลขนาดใหญ่ได้อย่างมีประสิทธิภาพ

3. **ความสามารถในการทำซ้ำข้อมูล (Replication)**:

   - MySQL รองรับการทำซ้ำข้อมูลแบบ Master-Slave และ Master-Master
   - ช่วยให้สามารถทำการสำรองข้อมูลและปรับปรุงประสิทธิภาพการอ่านข้อมูล

4. **ความปลอดภัย (Security)**:

   - MySQL มีระบบการควบคุมสิทธิ์การเข้าถึงข้อมูลที่เข้มงวด
   - รองรับการเชื่อมต่อแบบ SSL เพื่อเพิ่มความปลอดภัยในการสื่อสาร

5. **ความสามารถในการปรับขนาด (Scalability)**:

   - MySQL สามารถปรับขนาดได้ตามความต้องการของระบบ
   - รองรับการขยายระบบทั้งในแนวนอน (horizontal scaling) และแนวตั้ง (vertical scaling)

6. **สนับสนุนหลายแพลตฟอร์ม (Cross-Platform Support)**:

   - MySQL สามารถทำงานได้บนหลายแพลตฟอร์ม เช่น Windows, Linux, macOS, และอื่นๆ

7. **รองรับการทำธุรกรรม (ACID Compliance)**:

   - MySQL รองรับคุณสมบัติของ ACID (Atomicity, Consistency, Isolation, Durability) ซึ่งช่วยให้การทำธุรกรรมมีความเชื่อถือได้และปลอดภัย

8. **การสำรองข้อมูลและกู้คืน (Backup and Recovery)**:
   - MySQL มีเครื่องมือสำหรับการสำรองข้อมูลและการกู้คืนข้อมูล เพื่อป้องกันการสูญหายของข้อมูล

#### การใช้งาน MySQL:

1. **การติดตั้ง MySQL**:

   - สามารถติดตั้ง MySQL จากแพ็คเกจที่มีให้ดาวน์โหลดจากเว็บไซต์ MySQL หรือผ่านเครื่องมือจัดการแพ็คเกจของระบบปฏิบัติการต่างๆ

2. **การเชื่อมต่อกับ MySQL**:

   - สามารถใช้โปรแกรมจัดการฐานข้อมูลเช่น MySQL Workbench หรือใช้เครื่องมือบรรทัดคำสั่ง (command line) เพื่อเชื่อมต่อและจัดการฐานข้อมูล

3. **การสร้างฐานข้อมูลและตาราง**:

   - ใช้คำสั่ง SQL เช่น `CREATE DATABASE` และ `CREATE TABLE` เพื่อสร้างฐานข้อมูลและตารางใน MySQL

4. **การเพิ่ม, แก้ไข, และลบข้อมูล**:

   - ใช้คำสั่ง SQL เช่น `INSERT`, `UPDATE`, และ `DELETE` เพื่อจัดการข้อมูลในตาราง

5. **การค้นหาข้อมูล**:

   - ใช้คำสั่ง `SELECT` เพื่อค้นหาข้อมูลจากตาราง
   - สามารถใช้เงื่อนไข (conditions) และการจัดกลุ่ม (grouping) เพื่อค้นหาข้อมูลที่ต้องการ

6. **การสำรองข้อมูล**:

   - ใช้เครื่องมือเช่น `mysqldump` เพื่อสำรองข้อมูลจากฐานข้อมูล

7. **การตั้งค่าและปรับแต่ง**:
   - MySQL มีไฟล์คอนฟิกูเรชันที่สามารถปรับแต่งค่าต่างๆ เพื่อเพิ่มประสิทธิภาพและความปลอดภัยของระบบ

การใช้ MySQL ในการจัดการฐานข้อมูลทำให้สามารถพัฒนาแอปพลิเคชันที่มีประสิทธิภาพสูงและมีความปลอดภัย อีกทั้งยังสามารถขยายระบบได้ตามความต้องการของผู้ใช้งาน

### การติดตั้ง MySQL

การติดตั้ง MySQL สามารถทำได้บนหลายแพลตฟอร์ม เช่น Windows, macOS และ Linux ด้านล่างนี้จะอธิบายขั้นตอนการติดตั้ง MySQL บนแต่ละแพลตฟอร์มอย่างละเอียด

#### 1. การติดตั้ง MySQL บน Windows

1. **ดาวน์โหลด MySQL Installer**:

   - ไปที่เว็บไซต์ [MySQL Downloads](https://dev.mysql.com/downloads/installer/) และดาวน์โหลด MySQL Installer สำหรับ Windows

2. **รัน MySQL Installer**:

   - เปิดไฟล์ติดตั้ง MySQL Installer ที่ดาวน์โหลดมา แล้วทำตามขั้นตอนที่ปรากฏบนหน้าจอ
   - เลือกการติดตั้งแบบ "Developer Default" หรือ "Custom" ตามความต้องการ

3. **กำหนดค่าการติดตั้ง**:

   - เลือกฟีเจอร์ต่างๆ ที่ต้องการติดตั้ง เช่น MySQL Server, MySQL Workbench, MySQL Shell
   - กำหนดค่าการเชื่อมต่อฐานข้อมูล เช่น รหัสผ่าน root และพอร์ตที่ต้องการใช้งาน

4. **ดำเนินการติดตั้ง**:

   - คลิก "Execute" เพื่อเริ่มการติดตั้ง เมื่อเสร็จสิ้นคลิก "Next" เพื่อดำเนินการต่อ
   - กำหนดค่าคอนฟิกูเรชันเพิ่มเติม เช่น การตั้งค่า Windows Service และการตั้งค่า Authentication Method

5. **ตรวจสอบการติดตั้ง**:
   - เมื่อการติดตั้งเสร็จสิ้น ให้เปิด MySQL Workbench หรือใช้ MySQL Command Line Client เพื่อตรวจสอบการเชื่อมต่อและการทำงานของ MySQL

#### 2. การติดตั้ง MySQL บน macOS

1. **ดาวน์โหลด MySQL DMG**:

   - ไปที่เว็บไซต์ [MySQL Downloads](https://dev.mysql.com/downloads/mysql/) และดาวน์โหลดไฟล์ DMG สำหรับ macOS

2. **ติดตั้ง MySQL**:

   - เปิดไฟล์ DMG ที่ดาวน์โหลดมา และลาก MySQL ไปยังโฟลเดอร์ Applications

3. **รัน MySQL Server**:

   - เปิด System Preferences และคลิกที่ MySQL
   - คลิก "Start MySQL Server" เพื่อเริ่มการทำงานของ MySQL

4. **ตั้งค่าเริ่มต้น**:
   - กำหนดรหัสผ่าน root เมื่อเปิด MySQL ครั้งแรก
   - ใช้ Terminal เพื่อตรวจสอบการเชื่อมต่อด้วยคำสั่ง `mysql -u root -p`

#### 3. การติดตั้ง MySQL บน Linux (Ubuntu)

1. **อัปเดตแพ็คเกจ**:

   - เปิด Terminal และรันคำสั่งเพื่ออัปเดตแพ็คเกจในระบบ
     ```bash
     sudo apt update
     sudo apt upgrade
     ```

2. **ติดตั้ง MySQL Server**:

   - รันคำสั่งเพื่อติดตั้ง MySQL Server
     ```bash
     sudo apt install mysql-server
     ```

3. **ตั้งค่าการรักษาความปลอดภัย**:

   - รันคำสั่งเพื่อเริ่มการตั้งค่าการรักษาความปลอดภัย
     ```bash
     sudo mysql_secure_installation
     ```
   - ทำตามคำแนะนำบนหน้าจอเพื่อตั้งค่ารหัสผ่าน root และตั้งค่าความปลอดภัยอื่นๆ

4. **ตรวจสอบสถานะของ MySQL**:

   - รันคำสั่งเพื่อตรวจสอบสถานะของ MySQL
     ```bash
     sudo systemctl status mysql
     ```

5. **การเชื่อมต่อกับ MySQL**:
   - ใช้คำสั่ง `mysql -u root -p` เพื่อเชื่อมต่อกับ MySQL
   - ใส่รหัสผ่านที่ตั้งค่าไว้เพื่อเข้าสู่ MySQL Command Line

#### การติดตั้ง MySQL Workbench

MySQL Workbench เป็นเครื่องมือที่ใช้สำหรับการจัดการและออกแบบฐานข้อมูล MySQL สามารถติดตั้งได้ดังนี้:

1. **ดาวน์โหลด MySQL Workbench**:

   - ไปที่เว็บไซต์ [MySQL Workbench Downloads](https://dev.mysql.com/downloads/workbench/) และดาวน์โหลด MySQL Workbench สำหรับระบบปฏิบัติการของคุณ

2. **ติดตั้ง MySQL Workbench**:

   - ทำตามขั้นตอนการติดตั้งที่ปรากฏบนหน้าจอ

3. **เปิด MySQL Workbench**:
   - ใช้ MySQL Workbench เพื่อตั้งค่าและจัดการฐานข้อมูล MySQL ของคุณ

การติดตั้ง MySQL และ MySQL Workbench ทำให้คุณสามารถเริ่มต้นการพัฒนาและจัดการฐานข้อมูลได้อย่างรวดเร็วและมีประสิทธิภาพ

### ชนิดของข้อมูลใน MySQL

ใน MySQL มีชนิดของข้อมูลหลากหลายชนิดที่สามารถใช้ในการกำหนดรูปแบบของข้อมูลในตาราง เพื่อให้สามารถจัดเก็บข้อมูลได้อย่างมีประสิทธิภาพและตรงตามความต้องการ ด้านล่างนี้จะเป็นรายละเอียดเกี่ยวกับชนิดของข้อมูลที่สำคัญใน MySQL:

#### ชนิดของข้อมูล (Data Types)

1. **Numeric Types (ชนิดตัวเลข)**

   - **TINYINT**: ตัวเลขขนาดเล็ก (-128 ถึง 127)
   - **SMALLINT**: ตัวเลขขนาดเล็ก (-32,768 ถึง 32,767)
   - **MEDIUMINT**: ตัวเลขขนาดกลาง (-8,388,608 ถึง 8,388,607)
   - **INT**: ตัวเลขขนาดใหญ่ (-2,147,483,648 ถึง 2,147,483,647)
   - **BIGINT**: ตัวเลขขนาดใหญ่พิเศษ (-9,223,372,036,854,775,808 ถึง 9,223,372,036,854,775,807)
   - **FLOAT**: ตัวเลขทศนิยมแบบจุดลอย
   - **DOUBLE**: ตัวเลขทศนิยมแบบจุดลอยความแม่นยำสูง
   - **DECIMAL**: ตัวเลขทศนิยมแบบจุดคงที่

2. **String Types (ชนิดข้อความ)**

   - **CHAR**: ข้อความขนาดคงที่ (0-255 ตัวอักษร)
   - **VARCHAR**: ข้อความขนาดเปลี่ยนแปลงได้ (0-65,535 ตัวอักษร)
   - **TEXT**: ข้อความขนาดใหญ่ (0-65,535 ตัวอักษร)
   - **TINYTEXT**: ข้อความขนาดเล็ก (0-255 ตัวอักษร)
   - **MEDIUMTEXT**: ข้อความขนาดกลาง (0-16,777,215 ตัวอักษร)
   - **LONGTEXT**: ข้อความขนาดใหญ่มาก (0-4,294,967,295 ตัวอักษร)

3. **Date and Time Types (ชนิดวันที่และเวลา)**

   - **DATE**: วันที่ (รูปแบบ: YYYY-MM-DD)
   - **TIME**: เวลา (รูปแบบ: HH:MM:SS)
   - **DATETIME**: วันที่และเวลา (รูปแบบ: YYYY-MM-DD HH:MM:SS)
   - **TIMESTAMP**: วันที่และเวลาพร้อมโซนเวลา (รูปแบบ: YYYY-MM-DD HH:MM:SS)
   - **YEAR**: ปี (รูปแบบ: YYYY)

4. **Binary Types (ชนิดไบนารี)**

   - **BLOB**: ข้อมูลไบนารีขนาดใหญ่ (0-65,535 ไบต์)
   - **TINYBLOB**: ข้อมูลไบนารีขนาดเล็ก (0-255 ไบต์)
   - **MEDIUMBLOB**: ข้อมูลไบนารีขนาดกลาง (0-16,777,215 ไบต์)
   - **LONGBLOB**: ข้อมูลไบนารีขนาดใหญ่มาก (0-4,294,967,295 ไบต์)

5. **Other Types (ชนิดอื่นๆ)**
   - **ENUM**: ชุดค่าที่กำหนด (เช่น ENUM('value1', 'value2', ...))
   - **SET**: ชุดของค่า (สามารถเก็บค่าหลายค่าในหนึ่งฟิลด์)

#### ความกว้างของข้อมูล (Data Width)

- **CHAR vs VARCHAR**:

  - **CHAR**: ความยาวคงที่ เหมาะสำหรับข้อมูลที่มีความยาวเท่ากันเสมอ เช่น รหัสประเทศ
  - **VARCHAR**: ความยาวแปรเปลี่ยน เหมาะสำหรับข้อมูลที่มีความยาวไม่แน่นอน เช่น ชื่อผู้ใช้

- **TEXT Types**:

  - **TINYTEXT**: ข้อความขนาดเล็ก
  - **TEXT**: ข้อความขนาดทั่วไป
  - **MEDIUMTEXT**: ข้อความขนาดใหญ่
  - **LONGTEXT**: ข้อความขนาดใหญ่มาก

- **BLOB Types**:
  - **TINYBLOB**: ข้อมูลไบนารีขนาดเล็ก
  - **BLOB**: ข้อมูลไบนารีขนาดทั่วไป
  - **MEDIUMBLOB**: ข้อมูลไบนารีขนาดใหญ่
  - **LONGBLOB**: ข้อมูลไบนารีขนาดใหญ่มาก

การเลือกใช้ชนิดของข้อมูลที่เหมาะสมจะช่วยให้การจัดเก็บข้อมูลมีประสิทธิภาพมากขึ้น ทั้งในแง่ของการใช้พื้นที่เก็บข้อมูลและประสิทธิภาพในการประมวลผล ควรพิจารณาความต้องการของข้อมูลและเลือกใช้ชนิดที่เหมาะสมกับแต่ละฟิลด์ในตาราง

### ตัวอย่างการใช้ชนิดของข้อมูลใน MySQL

#### ตัวอย่างที่ 1: ข้อมูลนักเรียน (Students)

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- รหัสนักเรียน
    first_name VARCHAR(50) NOT NULL,           -- ชื่อจริง
    last_name VARCHAR(50) NOT NULL,            -- นามสกุล
    birth_date DATE NOT NULL,                  -- วันเกิด
    email VARCHAR(100) NOT NULL,               -- อีเมล
    grade_level TINYINT NOT NULL,              -- ระดับชั้นเรียน
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP -- วันที่ลงทะเบียน
);
```

- **INT**: ใช้สำหรับรหัสนักเรียน (id) เนื่องจากต้องการค่าที่ไม่ซ้ำกันและสามารถเพิ่มขึ้นอัตโนมัติ
- **VARCHAR**: ใช้สำหรับชื่อจริง (first_name), นามสกุล (last_name), และอีเมล (email) เนื่องจากเป็นข้อความที่มีความยาวไม่แน่นอน
- **DATE**: ใช้สำหรับวันเกิด (birth_date) เนื่องจากต้องการเก็บวันที่
- **TINYINT**: ใช้สำหรับระดับชั้นเรียน (grade_level) เนื่องจากเป็นตัวเลขขนาดเล็ก
- **DATETIME**: ใช้สำหรับวันที่ลงทะเบียน (enrollment_date) เพื่อเก็บวันที่และเวลา

#### ตัวอย่างที่ 2: ข้อมูลสินค้า (Products)

```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- รหัสสินค้า
    product_name VARCHAR(100) NOT NULL,        -- ชื่อสินค้า
    description TEXT,                          -- คำอธิบายสินค้า
    price DECIMAL(10, 2) NOT NULL,             -- ราคาสินค้า
    stock_quantity INT NOT NULL,               -- จำนวนสินค้าในสต็อก
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- วันที่สร้างข้อมูล
);
```

- **INT**: ใช้สำหรับรหัสสินค้า (product_id) และจำนวนสินค้าในสต็อก (stock_quantity) เนื่องจากต้องการค่าที่ไม่ซ้ำกันและสามารถเพิ่มขึ้นอัตโนมัติ
- **VARCHAR**: ใช้สำหรับชื่อสินค้า (product_name) เนื่องจากเป็นข้อความที่มีความยาวไม่แน่นอน
- **TEXT**: ใช้สำหรับคำอธิบายสินค้า (description) เนื่องจากอาจมีความยาวมาก
- **DECIMAL**: ใช้สำหรับราคาสินค้า (price) เนื่องจากต้องการความแม่นยำในการเก็บข้อมูลทางการเงิน
- **TIMESTAMP**: ใช้สำหรับวันที่สร้างข้อมูล (created_at) เพื่อเก็บวันที่และเวลา

#### ตัวอย่างที่ 3: ข้อมูลการจองห้องพัก (Room Bookings)

```sql
CREATE TABLE room_bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,   -- รหัสการจอง
    customer_name VARCHAR(100) NOT NULL,         -- ชื่อลูกค้า
    room_number INT NOT NULL,                    -- หมายเลขห้อง
    check_in_date DATE NOT NULL,                 -- วันที่เช็คอิน
    check_out_date DATE NOT NULL,                -- วันที่เช็คเอาท์
    total_amount DECIMAL(10, 2) NOT NULL,        -- ยอดรวมการจอง
    booking_status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending' -- สถานะการจอง
);
```

- **INT**: ใช้สำหรับรหัสการจอง (booking_id) และหมายเลขห้อง (room_number) เนื่องจากต้องการค่าที่ไม่ซ้ำกันและสามารถเพิ่มขึ้นอัตโนมัติ
- **VARCHAR**: ใช้สำหรับชื่อลูกค้า (customer_name) เนื่องจากเป็นข้อความที่มีความยาวไม่แน่นอน
- **DATE**: ใช้สำหรับวันที่เช็คอิน (check_in_date) และวันที่เช็คเอาท์ (check_out_date) เนื่องจากต้องการเก็บวันที่
- **DECIMAL**: ใช้สำหรับยอดรวมการจอง (total_amount) เนื่องจากต้องการความแม่นยำในการเก็บข้อมูลทางการเงิน
- **ENUM**: ใช้สำหรับสถานะการจอง (booking_status) เนื่องจากมีค่าเฉพาะที่กำหนดไว้

การเลือกชนิดของข้อมูลที่เหมาะสมในแต่ละตัวอย่างจะช่วยให้สามารถจัดเก็บและจัดการข้อมูลได้อย่างมีประสิทธิภาพและตรงตามความต้องการ

### ตัวอย่างข้อมูลในรูปแบบตารางพร้อมข้อมูลตัวอย่าง (Fake Data)

#### ตารางนักเรียน (Students)

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    email VARCHAR(100) NOT NULL,
    grade_level TINYINT NOT NULL,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ข้อมูลตัวอย่าง
INSERT INTO students (first_name, last_name, birth_date, email, grade_level) VALUES
('John', 'Doe', '2005-06-15', 'john.doe@example.com', 10),
('Jane', 'Smith', '2006-07-20', 'jane.smith@example.com', 9),
('Emily', 'Johnson', '2004-03-12', 'emily.johnson@example.com', 11);
```

| id  | first_name | last_name | birth_date | email                     | grade_level | enrollment_date     |
| --- | ---------- | --------- | ---------- | ------------------------- | ----------- | ------------------- |
| 1   | John       | Doe       | 2005-06-15 | john.doe@example.com      | 10          | 2023-06-15 12:00:00 |
| 2   | Jane       | Smith     | 2006-07-20 | jane.smith@example.com    | 9           | 2023-06-15 12:00:00 |
| 3   | Emily      | Johnson   | 2004-03-12 | emily.johnson@example.com | 11          | 2023-06-15 12:00:00 |

#### ตารางสินค้า (Products)

```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ข้อมูลตัวอย่าง
INSERT INTO products (product_name, description, price, stock_quantity) VALUES
('Laptop', 'High performance laptop', 999.99, 50),
('Smartphone', 'Latest model smartphone', 699.99, 200),
('Headphones', 'Noise-cancelling headphones', 199.99, 150);
```

| product_id | product_name | description                 | price  | stock_quantity | created_at          |
| ---------- | ------------ | --------------------------- | ------ | -------------- | ------------------- |
| 1          | Laptop       | High performance laptop     | 999.99 | 50             | 2023-06-15 12:00:00 |
| 2          | Smartphone   | Latest model smartphone     | 699.99 | 200            | 2023-06-15 12:00:00 |
| 3          | Headphones   | Noise-cancelling headphones | 199.99 | 150            | 2023-06-15 12:00:00 |

#### ตารางการจองห้องพัก (Room Bookings)

```sql
CREATE TABLE room_bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    room_number INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    booking_status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending'
);

-- ข้อมูลตัวอย่าง
INSERT INTO room_bookings (customer_name, room_number, check_in_date, check_out_date, total_amount, booking_status) VALUES
('Alice Johnson', 101, '2023-07-01', '2023-07-05', 500.00, 'Confirmed'),
('Bob Brown', 102, '2023-07-10', '2023-07-15', 750.00, 'Pending'),
('Charlie Davis', 103, '2023-08-01', '2023-08-03', 300.00, 'Cancelled');
```

| booking_id | customer_name | room_number | check_in_date | check_out_date | total_amount | booking_status |
| ---------- | ------------- | ----------- | ------------- | -------------- | ------------ | -------------- |
| 1          | Alice Johnson | 101         | 2023-07-01    | 2023-07-05     | 500.00       | Confirmed      |
| 2          | Bob Brown     | 102         | 2023-07-10    | 2023-07-15     | 750.00       | Pending        |
| 3          | Charlie Davis | 103         | 2023-08-01    | 2023-08-03     | 300.00       | Cancelled      |

ตารางและข้อมูลตัวอย่างเหล่านี้จะแสดงให้เห็นถึงการใช้ชนิดของข้อมูลและความกว้างของข้อมูลใน MySQL เพื่อจัดเก็บข้อมูลที่มีความหลากหลายตามความต้องการของแต่ละกรณี

### การใช้งาน MySQL เบื้องต้น

การใช้งาน MySQL เบื้องต้นจะครอบคลุมการสร้างฐานข้อมูล, ตาราง, การเพิ่มและจัดการข้อมูล รวมถึงการค้นหาข้อมูล ด้านล่างนี้เป็นคำสั่ง SQL ที่จำเป็นสำหรับการเริ่มต้นใช้งาน MySQL:

#### 1. การสร้างฐานข้อมูล (Creating a Database)

```sql
CREATE DATABASE database_name;
```

ตัวอย่าง:

```sql
CREATE DATABASE mydatabase;
```

#### 2. การเลือกใช้งานฐานข้อมูล (Selecting a Database)

```sql
USE database_name;
```

ตัวอย่าง:

```sql
USE mydatabase;
```

#### 3. การสร้างตาราง (Creating a Table)

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);
```

ตัวอย่าง:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 4. การเพิ่มข้อมูลลงในตาราง (Inserting Data into a Table)

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

ตัวอย่าง:

```sql
INSERT INTO users (username, email)
VALUES ('john_doe', 'john@example.com');
```

#### 5. การดึงข้อมูลจากตาราง (Querying Data from a Table)

```sql
SELECT column1, column2, ...
FROM table_name;
```

ตัวอย่าง:

```sql
SELECT * FROM users;
```

#### 6. การอัปเดตข้อมูลในตาราง (Updating Data in a Table)

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

ตัวอย่าง:

```sql
UPDATE users
SET email = 'john_doe@example.com'
WHERE username = 'john_doe';
```

#### 7. การลบข้อมูลจากตาราง (Deleting Data from a Table)

```sql
DELETE FROM table_name
WHERE condition;
```

ตัวอย่าง:

```sql
DELETE FROM users
WHERE username = 'john_doe';
```

#### 8. การใช้งานเงื่อนไข (Using Conditions)

ในการดึงข้อมูล, อัปเดต, หรือลบข้อมูล สามารถใช้เงื่อนไขเพื่อระบุข้อมูลที่ต้องการทำงานด้วย เช่น:

- **WHERE Clause**: ใช้เพื่อระบุเงื่อนไขในการเลือกข้อมูล
- **AND, OR, NOT**: ใช้เพื่อเชื่อมโยงเงื่อนไขหลายเงื่อนไข
- **LIKE**: ใช้เพื่อค้นหาข้อมูลที่ตรงกับรูปแบบที่กำหนด
- **IN**: ใช้เพื่อระบุค่าหลายค่าในเงื่อนไข

ตัวอย่าง:

```sql
SELECT * FROM users
WHERE email LIKE '%@example.com'
AND created_at > '2023-01-01';
```

#### 9. การจัดเรียงข้อมูล (Sorting Data)

สามารถจัดเรียงข้อมูลที่ดึงมาได้ด้วยคำสั่ง `ORDER BY`:

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 ASC|DESC, column2 ASC|DESC;
```

ตัวอย่าง:

```sql
SELECT * FROM users
ORDER BY created_at DESC;
```

#### 10. การจัดกลุ่มข้อมูล (Grouping Data)

สามารถจัดกลุ่มข้อมูลและคำนวณค่าทางสถิติต่างๆ ด้วยคำสั่ง `GROUP BY`:

```sql
SELECT column1, COUNT(column2)
FROM table_name
GROUP BY column1;
```

ตัวอย่าง:

```sql
SELECT username, COUNT(*)
FROM users
GROUP BY username;
```

#### 11. การรวมข้อมูลจากหลายตาราง (Joining Tables)

MySQL รองรับการรวมข้อมูลจากหลายตารางด้วยคำสั่ง JOIN:

```sql
SELECT table1.column1, table2.column2, ...
FROM table1
JOIN table2
ON table1.common_column = table2.common_column;
```

ตัวอย่าง:

```sql
SELECT users.username, orders.order_date
FROM users
JOIN orders
ON users.id = orders.user_id;
```

การใช้งาน MySQL เบื้องต้นเหล่านี้จะช่วยให้คุณสามารถจัดการและดึงข้อมูลจากฐานข้อมูลได้อย่างมีประสิทธิภาพ ในขั้นตอนต่อไปจะเป็นการเรียนรู้เพิ่มเติมเกี่ยวกับคำสั่ง SQL ขั้นสูง และการปรับแต่ง MySQL เพื่อเพิ่มประสิทธิภาพในการทำงาน

### แบบฝึกหัดสำหรับการใช้งาน MySQL เบื้องต้น

แบบฝึกหัดด้านล่างนี้จะช่วยให้คุณฝึกฝนการใช้งานคำสั่ง SQL เบื้องต้นใน MySQL:

#### แบบฝึกหัดที่ 1: การสร้างฐานข้อมูลและตาราง

1. สร้างฐานข้อมูลชื่อ `company`
2. สร้างตารางชื่อ `employees` ในฐานข้อมูล `company` โดยมีโครงสร้างดังนี้:
   - `id` (INT, Primary Key, Auto Increment)
   - `first_name` (VARCHAR(50))
   - `last_name` (VARCHAR(50))
   - `email` (VARCHAR(100))
   - `hire_date` (DATE)

#### แบบฝึกหัดที่ 2: การเพิ่มข้อมูลลงในตาราง

3. เพิ่มข้อมูลพนักงานลงในตาราง `employees` ดังนี้:
   - พนักงานคนที่ 1: John Doe, john.doe@example.com, วันที่จ้างงาน 2023-01-15
   - พนักงานคนที่ 2: Jane Smith, jane.smith@example.com, วันที่จ้างงาน 2023-02-20

#### แบบฝึกหัดที่ 3: การดึงข้อมูลจากตาราง

4. ดึงข้อมูลทั้งหมดจากตาราง `employees` และแสดงผลทุกคอลัมน์

#### แบบฝึกหัดที่ 4: การอัปเดตข้อมูลในตาราง

5. อัปเดตที่อยู่อีเมลของพนักงานที่มีชื่อว่า "John Doe" เป็น `john.doe@company.com`

#### แบบฝึกหัดที่ 5: การลบข้อมูลจากตาราง

6. ลบข้อมูลพนักงานที่มีชื่อว่า "Jane Smith" ออกจากตาราง `employees`

#### การตรวจสอบและการทำงานเพิ่มเติม:

หลังจากทำแบบฝึกหัดทั้ง 5 ข้อแล้ว ลองใช้คำสั่ง `SELECT` เพื่อดึงข้อมูลจากตาราง `employees` เพื่อตรวจสอบผลลัพธ์การทำงานของคุณ

#### ตัวอย่างการทำแบบฝึกหัด:

**แบบฝึกหัดที่ 1: การสร้างฐานข้อมูลและตาราง**

```sql
-- สร้างฐานข้อมูล
CREATE DATABASE company;

-- เลือกใช้งานฐานข้อมูล
USE company;

-- สร้างตาราง employees
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE
);
```

**แบบฝึกหัดที่ 2: การเพิ่มข้อมูลลงในตาราง**

```sql
-- เพิ่มข้อมูลพนักงานคนที่ 1
INSERT INTO employees (first_name, last_name, email, hire_date)
VALUES ('John', 'Doe', 'john.doe@example.com', '2023-01-15');

-- เพิ่มข้อมูลพนักงานคนที่ 2
INSERT INTO employees (first_name, last_name, email, hire_date)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', '2023-02-20');
```

**แบบฝึกหัดที่ 3: การดึงข้อมูลจากตาราง**

```sql
-- ดึงข้อมูลทั้งหมดจากตาราง employees
SELECT * FROM employees;
```

**แบบฝึกหัดที่ 4: การอัปเดตข้อมูลในตาราง**

```sql
-- อัปเดตอีเมลของ John Doe
UPDATE employees
SET email = 'john.doe@company.com'
WHERE first_name = 'John' AND last_name = 'Doe';
```

**แบบฝึกหัดที่ 5: การลบข้อมูลจากตาราง**

```sql
-- ลบข้อมูลพนักงานที่ชื่อ Jane Smith
DELETE FROM employees
WHERE first_name = 'Jane' AND last_name = 'Smith';
```

ลองทำแบบฝึกหัดเหล่านี้และตรวจสอบผลลัพธ์ของคุณเพื่อให้แน่ใจว่าคุณเข้าใจการใช้งานคำสั่ง SQL เบื้องต้นใน MySQL

### การใช้คำสั่ง SQL JOIN ใน MySQL

การใช้คำสั่ง JOIN ใน MySQL ช่วยให้สามารถดึงข้อมูลจากหลายตารางที่มีความสัมพันธ์กันได้อย่างมีประสิทธิภาพ มีชนิดของ JOIN หลายแบบที่สามารถใช้ได้ ได้แก่ INNER JOIN, LEFT JOIN, RIGHT JOIN และ FULL JOIN

#### 1. INNER JOIN

INNER JOIN จะดึงข้อมูลเฉพาะแถวที่มีความสัมพันธ์กันในทั้งสองตาราง

**โครงสร้าง**:

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.common_column = table2.common_column;
```

**ตัวอย่าง**:

สมมุติว่าเรามีสองตารางคือ `students` และ `courses`

```sql
-- ตาราง students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- ตาราง courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100)
);

-- ตาราง enrollments (เพื่อแสดงการลงทะเบียนเรียน)
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- ข้อมูลตัวอย่าง
INSERT INTO students (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Emily', 'Johnson');

INSERT INTO courses (course_name) VALUES
('Mathematics'),
('Science'),
('History');

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 3);
```

**การใช้ INNER JOIN**:

```sql
SELECT students.first_name, students.last_name, courses.course_name
FROM enrollments
INNER JOIN students ON enrollments.student_id = students.student_id
INNER JOIN courses ON enrollments.course_id = courses.course_id;
```

**ผลลัพธ์**:

| first_name | last_name | course_name |
| ---------- | --------- | ----------- |
| John       | Doe       | Mathematics |
| John       | Doe       | Science     |
| Jane       | Smith     | Mathematics |
| Emily      | Johnson   | History     |

#### 2. LEFT JOIN (หรือ LEFT OUTER JOIN)

LEFT JOIN จะดึงข้อมูลจากตารางแรกทั้งหมด และข้อมูลจากตารางที่สองที่มีความสัมพันธ์กัน ถ้าไม่มีความสัมพันธ์กัน จะให้ค่า NULL

**โครงสร้าง**:

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.common_column = table2.common_column;
```

**ตัวอย่าง**:

```sql
SELECT students.first_name, students.last_name, courses.course_name
FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.student_id
LEFT JOIN courses ON enrollments.course_id = courses.course_id;
```

**ผลลัพธ์**:

| first_name | last_name | course_name |
| ---------- | --------- | ----------- |
| John       | Doe       | Mathematics |
| John       | Doe       | Science     |
| Jane       | Smith     | Mathematics |
| Emily      | Johnson   | History     |
| Jane       | Smith     | NULL        |
| Emily      | Johnson   | NULL        |

#### 3. RIGHT JOIN (หรือ RIGHT OUTER JOIN)

RIGHT JOIN จะดึงข้อมูลจากตารางที่สองทั้งหมด และข้อมูลจากตารางแรกที่มีความสัมพันธ์กัน ถ้าไม่มีความสัมพันธ์กัน จะให้ค่า NULL

**โครงสร้าง**:

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.common_column = table2.common_column;
```

**ตัวอย่าง**:

```sql
SELECT students.first_name, students.last_name, courses.course_name
FROM courses
RIGHT JOIN enrollments ON courses.course_id = enrollments.course_id
RIGHT JOIN students ON enrollments.student_id = students.student_id;
```

**ผลลัพธ์**:

| first_name | last_name | course_name |
| ---------- | --------- | ----------- |
| John       | Doe       | Mathematics |
| John       | Doe       | Science     |
| Jane       | Smith     | Mathematics |
| Emily      | Johnson   | History     |

#### 4. FULL JOIN (หรือ FULL OUTER JOIN)

MySQL ไม่รองรับ FULL JOIN โดยตรง แต่สามารถใช้ UNION เพื่อจำลองการทำงานของ FULL JOIN ได้

**โครงสร้าง**:

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.common_column = table2.common_column
UNION
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.common_column = table2.common_column;
```

**ตัวอย่าง**:

```sql
SELECT students.first_name, students.last_name, courses.course_name
FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.student_id
LEFT JOIN courses ON enrollments.course_id = courses.course_id
UNION
SELECT students.first_name, students.last_name, courses.course_name
FROM courses
RIGHT JOIN enrollments ON courses.course_id = enrollments.course_id
RIGHT JOIN students ON enrollments.student_id = students.student_id;
```

**ผลลัพธ์**:

| first_name | last_name | course_name |
| ---------- | --------- | ----------- |
| John       | Doe       | Mathematics |
| John       | Doe       | Science     |
| Jane       | Smith     | Mathematics |
| Emily      | Johnson   | History     |
| Jane       | Smith     | NULL        |
| Emily      | Johnson   | NULL        |

ตัวอย่างเหล่านี้แสดงให้เห็นการใช้งานคำสั่ง JOIN ใน MySQL เพื่อดึงข้อมูลจากหลายตารางที่มีความสัมพันธ์กันตามเงื่อนไขที่กำหนด

### แบบฝึกหัดสำหรับการใช้ JOIN และ Aggregate Functions ใน MySQL

#### แบบฝึกหัดที่ 1: การใช้ INNER JOIN

1. **โจทย์**: ใช้ INNER JOIN เพื่อดึงข้อมูลนักเรียนและคอร์สที่นักเรียนแต่ละคนลงทะเบียน

   - **ตารางที่ใช้**: `students`, `courses`, `enrollments`
   - **ฟิลด์ที่ต้องการ**: `first_name`, `last_name`, `course_name`

   **คำสั่ง SQL**:

   ```sql
   SELECT students.first_name, students.last_name, courses.course_name
   FROM enrollments
   INNER JOIN students ON enrollments.student_id = students.student_id
   INNER JOIN courses ON enrollments.course_id = courses.course_id;
   ```

#### แบบฝึกหัดที่ 2: การใช้ LEFT JOIN

2. **โจทย์**: ใช้ LEFT JOIN เพื่อดึงข้อมูลนักเรียนทั้งหมด รวมถึงนักเรียนที่ยังไม่ได้ลงทะเบียนคอร์สใดๆ

   - **ตารางที่ใช้**: `students`, `enrollments`, `courses`
   - **ฟิลด์ที่ต้องการ**: `first_name`, `last_name`, `course_name`

   **คำสั่ง SQL**:

   ```sql
   SELECT students.first_name, students.last_name, courses.course_name
   FROM students
   LEFT JOIN enrollments ON students.student_id = enrollments.student_id
   LEFT JOIN courses ON enrollments.course_id = courses.course_id;
   ```

#### แบบฝึกหัดที่ 3: การใช้ COUNT() และ GROUP BY

3. **โจทย์**: นับจำนวนการลงทะเบียนของแต่ละคอร์ส

   - **ตารางที่ใช้**: `enrollments`, `courses`
   - **ฟิลด์ที่ต้องการ**: `course_name`, `number_of_enrollments`

   **คำสั่ง SQL**:

   ```sql
   SELECT courses.course_name, COUNT(enrollments.enrollment_id) AS number_of_enrollments
   FROM enrollments
   INNER JOIN courses ON enrollments.course_id = courses.course_id
   GROUP BY courses.course_name;
   ```

#### แบบฝึกหัดที่ 4: การใช้ SUM() และ GROUP BY

4. **โจทย์**: หายอดรวมการจองของแต่ละสถานะการจอง

   - **ตารางที่ใช้**: `room_bookings`
   - **ฟิลด์ที่ต้องการ**: `booking_status`, `total_revenue`

   **คำสั่ง SQL**:

   ```sql
   SELECT booking_status, SUM(total_amount) AS total_revenue
   FROM room_bookings
   GROUP BY booking_status;
   ```

#### แบบฝึกหัดที่ 5: การใช้ AVG() และ GROUP BY

5. **โจทย์**: หาค่าเฉลี่ยของราคาสินค้าในแต่ละหมวดหมู่ (สมมุติว่ามีคอลัมน์ `category` ในตาราง `products`)

   - **ตารางที่ใช้**: `products`
   - **ฟิลด์ที่ต้องการ**: `category`, `average_price`

   **คำสั่ง SQL**:

   ```sql
   SELECT category, AVG(price) AS average_price
   FROM products
   GROUP BY category;
   ```

ลองทำแบบฝึกหัดเหล่านี้เพื่อฝึกฝนการใช้ JOIN และ Aggregate Functions ใน MySQL และตรวจสอบผลลัพธ์ที่ได้เพื่อให้แน่ใจว่าคุณเข้าใจการใช้งานคำสั่ง SQL เหล่านี้

### การใช้งาน Subqueries ใน MySQL

Subqueries หรือ Queries ย่อยคือการใช้คำสั่ง SELECT ภายในคำสั่ง SQL อื่นๆ ซึ่งสามารถใช้ในการดึงข้อมูลที่ซับซ้อนมากขึ้น Subqueries สามารถใช้ในหลายบริบท เช่น ในคำสั่ง SELECT, INSERT, UPDATE และ DELETE

#### ประเภทของ Subqueries

1. **Subquery ในคำสั่ง SELECT**
2. **Subquery ในคำสั่ง INSERT**
3. **Subquery ในคำสั่ง UPDATE**
4. **Subquery ในคำสั่ง DELETE**

#### ตัวอย่างการใช้งาน Subqueries

##### 1. Subquery ในคำสั่ง SELECT

```sql
SELECT first_name, last_name
FROM students
WHERE student_id IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = 1
);
```

คำสั่งนี้ดึงชื่อนักเรียนที่ลงทะเบียนในคอร์สที่มี `course_id = 1`

##### 2. Subquery ในคำสั่ง INSERT

```sql
INSERT INTO students (first_name, last_name)
SELECT first_name, last_name
FROM old_students
WHERE graduation_year = 2023;
```

คำสั่งนี้เพิ่มข้อมูลนักเรียนที่สำเร็จการศึกษาในปี 2023 จากตาราง `old_students` ไปยังตาราง `students`

##### 3. Subquery ในคำสั่ง UPDATE

```sql
UPDATE products
SET price = price * 1.1
WHERE product_id IN (
    SELECT product_id
    FROM sales
    WHERE sale_date > '2023-01-01'
);
```

คำสั่งนี้เพิ่มราคาสินค้า 10% สำหรับสินค้าที่ขายหลังวันที่ 1 มกราคม 2023

##### 4. Subquery ในคำสั่ง DELETE

```sql
DELETE FROM students
WHERE student_id NOT IN (
    SELECT student_id
    FROM enrollments
);
```

คำสั่งนี้ลบนักเรียนที่ไม่ได้ลงทะเบียนในคอร์สใดๆ

#### Fake Data สำหรับแบบฝึกหัด

```sql
-- ตาราง students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- ตาราง old_students
CREATE TABLE old_students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    graduation_year INT
);

-- ตาราง courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100)
);

-- ตาราง enrollments
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- ตาราง products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- ตาราง sales
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ข้อมูลตัวอย่าง
INSERT INTO students (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Emily', 'Johnson');

INSERT INTO old_students (first_name, last_name, graduation_year) VALUES
('Alice', 'Brown', 2023),
('Bob', 'Davis', 2022);

INSERT INTO courses (course_name) VALUES
('Mathematics'),
('Science'),
('History');

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1),
(2, 1),
(3, 2);

INSERT INTO products (product_name, price) VALUES
('Laptop', 999.99),
('Smartphone', 699.99),
('Headphones', 199.99);

INSERT INTO sales (product_id, sale_date) VALUES
(1, '2023-05-01'),
(2, '2022-11-15'),
(3, '2023-06-10');
```

### แบบฝึกหัดสำหรับ Subqueries

#### แบบฝึกหัดที่ 1: Subquery ในคำสั่ง SELECT

1. **โจทย์**: ดึงชื่อและนามสกุลของนักเรียนที่ลงทะเบียนในคอร์ส `Mathematics`

   - **ตารางที่ใช้**: `students`, `courses`, `enrollments`

   **คำสั่ง SQL**:

   ```sql
   SELECT first_name, last_name
   FROM students
   WHERE student_id IN (
       SELECT student_id
       FROM enrollments
       WHERE course_id = (
           SELECT course_id
           FROM courses
           WHERE course_name = 'Mathematics'
       )
   );
   ```

#### แบบฝึกหัดที่ 2: Subquery ในคำสั่ง INSERT

2. **โจทย์**: เพิ่มนักเรียนที่สำเร็จการศึกษาในปี 2023 จากตาราง `old_students` ไปยังตาราง `students`

   - **ตารางที่ใช้**: `old_students`, `students`

   **คำสั่ง SQL**:

   ```sql
   INSERT INTO students (first_name, last_name)
   SELECT first_name, last_name
   FROM old_students
   WHERE graduation_year = 2023;
   ```

#### แบบฝึกหัดที่ 3: Subquery ในคำสั่ง UPDATE

3. **โจทย์**: เพิ่มราคาสินค้า 10% สำหรับสินค้าที่ขายหลังวันที่ 1 มกราคม 2023

   - **ตารางที่ใช้**: `products`, `sales`

   **คำสั่ง SQL**:

   ```sql
   UPDATE products
   SET price = price * 1.1
   WHERE product_id IN (
       SELECT product_id
       FROM sales
       WHERE sale_date > '2023-01-01'
   );
   ```

#### แบบฝึกหัดที่ 4: Subquery ในคำสั่ง DELETE

4. **โจทย์**: ลบนักเรียนที่ไม่ได้ลงทะเบียนในคอร์สใดๆ

   - **ตารางที่ใช้**: `students`, `enrollments`

   **คำสั่ง SQL**:

   ```sql
   DELETE FROM students
   WHERE student_id NOT IN (
       SELECT student_id
       FROM enrollments
   );
   ```

#### แบบฝึกหัดที่ 5: Subquery ที่ซับซ้อนในคำสั่ง SELECT

5. **โจทย์**: ดึงชื่อสินค้าและราคาของสินค้าที่ขายในปี 2023 และราคาสูงกว่า 500

   - **ตารางที่ใช้**: `products`, `sales`

   **คำสั่ง SQL**:

   ```sql
   SELECT product_name, price
   FROM products
   WHERE product_id IN (
       SELECT product_id
       FROM sales
       WHERE YEAR(sale_date) = 2023
   ) AND price > 500;
   ```

ลองทำแบบฝึกหัดเหล่านี้เพื่อฝึกฝนการใช้ Subqueries ใน MySQL และตรวจสอบผลลัพธ์ที่ได้เพื่อให้แน่ใจว่าคุณเข้าใจการใช้งานคำสั่ง SQL เหล่านี้

### ตัวอย่างการสร้างฐานข้อมูลและข้อมูลตัวอย่างสำหรับ Company

#### การสร้างฐานข้อมูลและตาราง

```sql
-- สร้างฐานข้อมูล
CREATE DATABASE company;

-- เลือกใช้งานฐานข้อมูล
USE company;

-- สร้างตาราง employees
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2),
    department_id INT
);

-- สร้างตาราง departments
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100)
);

-- สร้างตาราง projects
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100),
    start_date DATE,
    end_date DATE
);

-- สร้างตาราง employee_projects
CREATE TABLE employee_projects (
    employee_project_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    project_id INT,
    role VARCHAR(50),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
```

#### ข้อมูลตัวอย่าง (Fake Data)

```sql
-- ข้อมูลตัวอย่างสำหรับตาราง departments
INSERT INTO departments (department_name) VALUES
('Human Resources'),
('Finance'),
('Engineering'),
('Marketing');

-- ข้อมูลตัวอย่างสำหรับตาราง employees
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id) VALUES
('John', 'Doe', 'john.doe@example.com', '2020-01-15', 60000.00, 3),
('Jane', 'Smith', 'jane.smith@example.com', '2019-03-10', 65000.00, 2),
('Alice', 'Johnson', 'alice.johnson@example.com', '2018-06-23', 70000.00, 1),
('Bob', 'Brown', 'bob.brown@example.com', '2021-07-30', 55000.00, 3);

-- ข้อมูลตัวอย่างสำหรับตาราง projects
INSERT INTO projects (project_name, start_date, end_date) VALUES
('Project Alpha', '2021-01-01', '2021-12-31'),
('Project Beta', '2022-01-01', '2022-06-30'),
('Project Gamma', '2023-01-01', '2023-12-31');

-- ข้อมูลตัวอย่างสำหรับตาราง employee_projects
INSERT INTO employee_projects (employee_id, project_id, role) VALUES
(1, 1, 'Developer'),
(1, 2, 'Lead Developer'),
(2, 2, 'Accountant'),
(3, 3, 'HR Manager'),
(4, 1, 'Developer'),
(4, 3, 'Project Manager');
```

### แบบฝึกหัดสำหรับ Company Database

#### แบบฝึกหัดที่ 1: การใช้ INNER JOIN

1. **โจทย์**: ใช้ INNER JOIN เพื่อดึงข้อมูลพนักงานและโปรเจคที่พนักงานแต่ละคนทำงาน

   - **ตารางที่ใช้**: `employees`, `projects`, `employee_projects`
   - **ฟิลด์ที่ต้องการ**: `first_name`, `last_name`, `project_name`, `role`

   **คำสั่ง SQL**:

   ```sql
   SELECT employees.first_name, employees.last_name, projects.project_name, employee_projects.role
   FROM employee_projects
   INNER JOIN employees ON employee_projects.employee_id = employees.employee_id
   INNER JOIN projects ON employee_projects.project_id = projects.project_id;
   ```

#### แบบฝึกหัดที่ 2: การใช้ LEFT JOIN

2. **โจทย์**: ใช้ LEFT JOIN เพื่อดึงข้อมูลพนักงานทั้งหมด รวมถึงพนักงานที่ยังไม่ได้ทำงานในโปรเจคใดๆ

   - **ตารางที่ใช้**: `employees`, `employee_projects`, `projects`
   - **ฟิลด์ที่ต้องการ**: `first_name`, `last_name`, `project_name`

   **คำสั่ง SQL**:

   ```sql
   SELECT employees.first_name, employees.last_name, projects.project_name
   FROM employees
   LEFT JOIN employee_projects ON employees.employee_id = employee_projects.employee_id
   LEFT JOIN projects ON employee_projects.project_id = projects.project_id;
   ```

#### แบบฝึกหัดที่ 3: การใช้ COUNT() และ GROUP BY

3. **โจทย์**: นับจำนวนพนักงานในแต่ละแผนก

   - **ตารางที่ใช้**: `employees`, `departments`
   - **ฟิลด์ที่ต้องการ**: `department_name`, `number_of_employees`

   **คำสั่ง SQL**:

   ```sql
   SELECT departments.department_name, COUNT(employees.employee_id) AS number_of_employees
   FROM employees
   INNER JOIN departments ON employees.department_id = departments.department_id
   GROUP BY departments.department_name;
   ```

#### แบบฝึกหัดที่ 4: การใช้ SUM() และ GROUP BY

4. **โจทย์**: หายอดรวมเงินเดือนของพนักงานในแต่ละแผนก

   - **ตารางที่ใช้**: `employees`, `departments`
   - **ฟิลด์ที่ต้องการ**: `department_name`, `total_salary`

   **คำสั่ง SQL**:

   ```sql
   SELECT departments.department_name, SUM(employees.salary) AS total_salary
   FROM employees
   INNER JOIN departments ON employees.department_id = departments.department_id
   GROUP BY departments.department_name;
   ```

#### แบบฝึกหัดที่ 5: การใช้ AVG() และ GROUP BY

5. **โจทย์**: หาค่าเฉลี่ยของเงินเดือนพนักงานในแต่ละแผนก

   - **ตารางที่ใช้**: `employees`, `departments`
   - **ฟิลด์ที่ต้องการ**: `department_name`, `average_salary`

   **คำสั่ง SQL**:

   ```sql
   SELECT departments.department_name, AVG(employees.salary) AS average_salary
   FROM employees
   INNER JOIN departments ON employees.department_id = departments.department_id
   GROUP BY departments.department_name;
   ```

ลองทำแบบฝึกหัดเหล่านี้เพื่อฝึกฝนการใช้คำสั่ง SQL ในบริบทของฐานข้อมูลบริษัทและตรวจสอบผลลัพธ์ที่ได้เพื่อให้แน่ใจว่าคุณเข้าใจการใช้งานคำสั่ง SQL เหล่านี้
