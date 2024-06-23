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


## 1. บทนำสู่ MySQL

**1.1 นิยามและความสำคัญของ MySQL**

MySQL เป็นระบบจัดการฐานข้อมูลเชิงสัมพันธ์ (Relational Database Management System: RDBMS) ที่ได้รับความนิยมสูงในการพัฒนาแอปพลิเคชัน โดยเฉพาะอย่างยิ่งในบริบทของเว็บแอปพลิเคชัน MySQL ถูกพัฒนาโดย MySQL AB และปัจจุบันเป็นของ Oracle Corporation

ความสำคัญของ MySQL:

1. **ประสิทธิภาพสูง**: MySQL มีความเร็วในการประมวลผลและจัดการข้อมูลขนาดใหญ่
2. **ความน่าเชื่อถือ**: มีความเสถียรสูง เหมาะสำหรับการใช้งานในระดับองค์กร
3. **ความยืดหยุ่น**: รองรับหลากหลายแพลตฟอร์มและภาษาโปรแกรมมิ่ง
4. **การรักษาความปลอดภัย**: มีระบบรักษาความปลอดภัยที่แข็งแกร่ง
5. **ชุมชนขนาดใหญ่**: มีฐานผู้ใช้และนักพัฒนาจำนวนมาก ทำให้มีแหล่งข้อมูลและการสนับสนุนที่กว้างขวาง

**1.2 ประวัติและพัฒนาการของ MySQL**

- 1995: เริ่มพัฒนาโดย Michael Widenius และ David Axmark
- 2000: เปิดตัวภายใต้สัญญาอนุญาต GPL
- 2008: Sun Microsystems ซื้อกิจการ MySQL AB
- 2010: Oracle Corporation เข้าซื้อ Sun Microsystems

**1.3 คุณสมบัติหลักของ MySQL**

1. **การทำงานแบบหลายผู้ใช้**: รองรับการเข้าถึงพร้อมกันจากผู้ใช้หลายคน
2. **การสนับสนุน SQL**: ใช้ภาษา SQL มาตรฐานในการจัดการข้อมูล
3. **Cross-platform**: ทำงานได้บนระบบปฏิบัติการหลากหลาย
4. **Stored procedures**: สนับสนุนการเขียนโปรแกรมฝั่งเซิร์ฟเวอร์
5. **Triggers**: กลไกการทำงานอัตโนมัติเมื่อเกิดเหตุการณ์กับข้อมูล
6. **Replication**: ความสามารถในการทำสำเนาฐานข้อมูล
7. **Indexing**: เพิ่มประสิทธิภาพการค้นหาข้อมูล

**1.4 การประยุกต์ใช้ MySQL ในอุตสาหกรรม**

1. **E-commerce**: 
   - การจัดการสินค้าคงคลัง
   - ระบบการสั่งซื้อและการชำระเงิน
   - ข้อมูลลูกค้าและพฤติกรรมการซื้อ

2. **สื่อสังคมออนไลน์**:
   - การเก็บข้อมูลโพสต์และความคิดเห็น
   - ระบบการแจ้งเตือน
   - การวิเคราะห์เครือข่ายสังคม

3. **ระบบการจัดการเนื้อหา (CMS)**:
   - การจัดเก็บบทความและสื่อมัลติมีเดีย
   - ระบบจัดการผู้ใช้และสิทธิ์การเข้าถึง
   - การจัดการเวอร์ชันของเนื้อหา

4. **ระบบการเงินและการธนาคาร**:
   - การบันทึกธุรกรรมทางการเงิน
   - ระบบการยืนยันตัวตนและการรักษาความปลอดภัย
   - การวิเคราะห์ความเสี่ยงและการตรวจจับการฉ้อโกง

5. **การศึกษาออนไลน์**:
   - การจัดการหลักสูตรและเนื้อหาบทเรียน
   - ระบบติดตามความก้าวหน้าของผู้เรียน
   - การวิเคราะห์ผลการเรียนรู้

**แบบฝึกหัดท้ายบท**

1. จงอธิบายความแตกต่างระหว่าง MySQL กับระบบจัดการฐานข้อมูลอื่นๆ เช่น PostgreSQL หรือ Oracle Database พร้อมยกตัวอย่างสถานการณ์ที่เหมาะสมในการเลือกใช้แต่ละระบบ

2. ให้ออกแบบโครงสร้างฐานข้อมูลอย่างง่ายสำหรับระบบจองตั๋วภาพยนตร์ออนไลน์ โดยระบุตารางที่จำเป็น ฟิลด์สำคัญในแต่ละตาราง และความสัมพันธ์ระหว่างตาราง พร้อมอธิบายเหตุผลในการออกแบบ

3. จงอภิปรายถึงความสำคัญของ MySQL ในบริบทของการพัฒนาเว็บแอปพลิเคชันด้วย Python และ Flask โดยเน้นถึงข้อดีและข้อควรระวังในการใช้งาน

## 2. การติดตั้งและการตั้งค่า MySQL

**2.1 ข้อกำหนดระบบ**

ก่อนการติดตั้ง MySQL ควรตรวจสอบข้อกำหนดระบบดังนี้:

1. **ระบบปฏิบัติการ**: 
   - Windows 7/8/10/11, Server 2012 R2 หรือใหม่กว่า
   - macOS 10.14 หรือใหม่กว่า
   - Linux distributions: Ubuntu, CentOS, Fedora, Debian

2. **ฮาร์ดแวร์**:
   - CPU: 1 GHz หรือเร็วกว่า
   - RAM: อย่างน้อย 1 GB (แนะนำ 4 GB ขึ้นไป)
   - พื้นที่ดิสก์: อย่างน้อย 5 GB

3. **ซอฟต์แวร์เพิ่มเติม**:
   - .NET Framework 4.5.2 หรือใหม่กว่า (สำหรับ Windows)
   - OpenSSL (สำหรับการเชื่อมต่อแบบเข้ารหัส)

**2.2 ขั้นตอนการติดตั้ง MySQL**

**Windows:**
1. ดาวน์โหลด MySQL Installer จากเว็บไซต์ทางการ
2. เปิดไฟล์ติดตั้งและเลือก "Full" installation
3. ทำตามขั้นตอนในตัวช่วยติดตั้ง
4. ตั้งค่ารหัสผ่านสำหรับ root user
5. เลือกการกำหนดค่าเซิร์ฟเวอร์ (Developer Default แนะนำสำหรับการพัฒนา)

**macOS:**
1. ดาวน์โหลด MySQL Community Server DMG file
2. เปิดไฟล์ DMG และติดตั้ง MySQL package
3. เปิด System Preferences และคลิกที่ MySQL
4. คลิก "Start MySQL Server"
5. ใช้ Terminal เพื่อตั้งค่ารหัสผ่าน root

**Linux (Ubuntu):**
1. เปิด Terminal
2. อัพเดทแพ็คเกจ: `sudo apt update`
3. ติดตั้ง MySQL: `sudo apt install mysql-server`
4. ตั้งค่าความปลอดภัย: `sudo mysql_secure_installation`
5. ทำตามคำแนะนำเพื่อตั้งค่ารหัสผ่านและการรักษาความปลอดภัยอื่นๆ

**2.3 การตั้งค่าพื้นฐาน MySQL**

1. **การเปิด/ปิดบริการ MySQL**:
   - Windows: ใช้ Services manager
   - macOS: ใช้ System Preferences
   - Linux: `sudo systemctl start mysql` / `sudo systemctl stop mysql`

2. **การเข้าถึง MySQL shell**:
   - ใช้คำสั่ง `mysql -u root -p` แล้วป้อนรหัสผ่าน

3. **การสร้างฐานข้อมูลใหม่**:
   ```sql
   CREATE DATABASE mydatabase;
   ```

4. **การสร้างผู้ใช้และให้สิทธิ์**:
   ```sql
   CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON mydatabase.* TO 'newuser'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. **การตั้งค่าไฟล์ my.cnf (Linux/macOS) หรือ my.ini (Windows)**:
   - ปรับแต่งค่า max_connections, buffer_pool_size, ฯลฯ ตามความเหมาะสม

**2.4 การตรวจสอบการติดตั้ง**

1. ตรวจสอบเวอร์ชัน MySQL:
   ```sql
   SELECT VERSION();
   ```

2. ตรวจสอบสถานะเซิร์ฟเวอร์:
   ```sql
   SHOW STATUS;
   ```

3. ตรวจสอบฐานข้อมูลที่มีอยู่:
   ```sql
   SHOW DATABASES;
   ```

**2.5 การติดตั้งเครื่องมือเสริม**

1. **MySQL Workbench**: GUI tool สำหรับจัดการฐานข้อมูล
2. **phpMyAdmin**: เครื่องมือจัดการฐานข้อมูลผ่านเว็บ
3. **HeidiSQL**: เครื่องมือจัดการฐานข้อมูลสำหรับ Windows

**แบบฝึกหัดท้ายบท**

1. ให้ติดตั้ง MySQL บนเครื่องคอมพิวเตอร์ของคุณ และสร้างฐานข้อมูลชื่อ "university" พร้อมทั้งสร้างผู้ใช้ชื่อ "student" ที่มีสิทธิ์เข้าถึงฐานข้อมูลนี้

2. อธิบายความแตกต่างระหว่างการติดตั้ง MySQL บน Windows, macOS, และ Linux พร้อมระบุข้อดีและข้อเสียของแต่ละระบบปฏิบัติการ

3. ศึกษาและอธิบายความสำคัญของพารามิเตอร์ต่อไปนี้ในไฟล์ตั้งค่า MySQL: innodb_buffer_pool_size, max_connections, และ query_cache_size พร้อมแนะนำค่าที่เหมาะสมสำหรับเซิร์ฟเวอร์ขนาดเล็กที่มี RAM 8 GB

## ชนิดของข้อมูลใน MySQL

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

### ตัวอย่างข้อมูลในรูปแบบตารางพร้อมข้อมูลตัวอย่าง

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


## 3. พื้นฐานการใช้งาน MySQL

**3.1 การเชื่อมต่อกับ MySQL Server**

1. **การเชื่อมต่อผ่าน Command Line**:
   ```
   mysql -u username -p
   ```
   ป้อนรหัสผ่านเมื่อได้รับแจ้ง ตัวอย่างการใช้งาน:
   ```shell
   mysql -u root -p
   ```

2. **การเชื่อมต่อผ่าน GUI Tools**:
   - **MySQL Workbench**: 
     1. เปิด MySQL Workbench
     2. คลิกที่ไอคอน "Local instance MySQL"
     3. ป้อนรหัสผ่านของ root หรือผู้ใช้ที่ต้องการ
   - **phpMyAdmin**:
     1. เปิดเว็บเบราว์เซอร์และเข้าไปที่ URL ของ phpMyAdmin
     2. ป้อนชื่อผู้ใช้และรหัสผ่าน
   - **HeidiSQL**:
     1. เปิด HeidiSQL
     2. คลิก "New" เพื่อสร้างการเชื่อมต่อใหม่
     3. ป้อนข้อมูลเซิร์ฟเวอร์, ชื่อผู้ใช้ และรหัสผ่าน

**3.2 โครงสร้างพื้นฐานของฐานข้อมูล**

1. **Database**: ฐานข้อมูลคือกลุ่มของตารางที่เกี่ยวข้องกัน ฐานข้อมูลหนึ่งสามารถประกอบไปด้วยหลายตาราง โดยแต่ละตารางจะเก็บข้อมูลเกี่ยวกับสิ่งเฉพาะเจาะจง ตัวอย่างเช่น:
   - ฐานข้อมูลของมหาวิทยาลัยอาจประกอบด้วยตารางเช่น `students` (นักเรียน), `courses` (หลักสูตร), `enrollments` (การลงทะเบียน)

   ```sql
   CREATE DATABASE university_db;
   ```

2. **Table**: ตารางคือโครงสร้างที่ใช้เก็บข้อมูลในรูปแบบแถวและคอลัมน์ ตารางหนึ่งจะมีหลายคอลัมน์ที่กำหนดชนิดของข้อมูลที่เก็บ และมีหลายแถวที่เก็บข้อมูลจริง ตัวอย่างเช่น:
   - ตาราง `students` ที่เก็บข้อมูลนักเรียนแต่ละคน

   ```sql
   CREATE TABLE students (
       student_id INT PRIMARY KEY AUTO_INCREMENT,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       date_of_birth DATE,
       email VARCHAR(100) UNIQUE
   );
   ```

3. **Column (Field)**: คอลัมน์คือส่วนประกอบของตารางที่กำหนดชนิดข้อมูล แต่ละคอลัมน์มีชื่อและชนิดข้อมูลที่เฉพาะเจาะจง ตัวอย่างเช่น:
   - คอลัมน์ `first_name` ในตาราง `students` เก็บชื่อแรกของนักเรียน และมีชนิดข้อมูลเป็น `VARCHAR(50)`

   ```sql
   CREATE TABLE example_table (
       id INT PRIMARY KEY AUTO_INCREMENT,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL
   );
   ```

4. **Row (Record)**: แถวคือข้อมูลแต่ละรายการในตาราง แต่ละแถวประกอบด้วยค่าของคอลัมน์ต่างๆ ในตาราง ตัวอย่างเช่น:
   - แถวในตาราง `students` ที่เก็บข้อมูลนักเรียนชื่อ "John Doe"

   ```sql
   INSERT INTO students (first_name, last_name, date_of_birth, email)
   VALUES ('John', 'Doe', '2000-01-01', 'john.doe@example.com');
   ```

5. **Primary Key**: Primary Key คือฟิลด์ที่ใช้ระบุแถวข้อมูลแต่ละแถวอย่างเป็นเอกลักษณ์ Primary Key ต้องมีค่าที่ไม่ซ้ำกันและไม่เป็นค่าว่าง ตัวอย่างเช่น:
   - คอลัมน์ `student_id` ในตาราง `students` ถูกกำหนดเป็น Primary Key

   ```sql
   CREATE TABLE courses (
       course_id INT PRIMARY KEY AUTO_INCREMENT,
       course_name VARCHAR(100) NOT NULL,
       credits INT
   );
   ```

6. **Foreign Key**: Foreign Key คือฟิลด์ที่ใช้อ้างอิงถึง Primary Key ในตารางอื่น ช่วยรักษาความสัมพันธ์ระหว่างตาราง ตัวอย่างเช่น:
   - คอลัมน์ `student_id` ในตาราง `enrollments` อ้างอิงถึง `student_id` ในตาราง `students`

   ```sql
   CREATE TABLE enrollments (
       enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
       student_id INT,
       course_id INT,
       enrollment_date DATE,
       FOREIGN KEY (student_id) REFERENCES students(student_id),
       FOREIGN KEY (course_id) REFERENCES courses(course_id)
   );
   ```

   **ตัวอย่างการใช้งานรวม:**

   ```sql
   -- สร้างฐานข้อมูล
   CREATE DATABASE university_db;

   -- ใช้ฐานข้อมูล
   USE university_db;

   -- สร้างตาราง students
   CREATE TABLE students (
      student_id INT PRIMARY KEY AUTO_INCREMENT,
      first_name VARCHAR(50) NOT NULL,
      last_name VARCHAR(50) NOT NULL,
      date_of_birth DATE,
      email VARCHAR(100) UNIQUE
   );

   -- สร้างตาราง courses
   CREATE TABLE courses (
      course_id INT PRIMARY KEY AUTO_INCREMENT,
      course_name VARCHAR(100) NOT NULL,
      credits INT
   );

   -- สร้างตาราง enrollments และกำหนด Foreign Key
   CREATE TABLE enrollments (
      enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
      student_id INT,
      course_id INT,
      enrollment_date DATE,
      FOREIGN KEY (student_id) REFERENCES students(student_id),
      FOREIGN KEY (course_id) REFERENCES courses(course_id)
   );

   -- เพิ่มข้อมูลในตาราง students
   INSERT INTO students (first_name, last_name, date_of_birth, email)
   VALUES 
   ('John', 'Doe', '2000-01-01', 'john.doe@example.com'),
   ('Jane', 'Smith', '1999-05-15', 'jane.smith@example.com');

   -- เพิ่มข้อมูลในตาราง courses
   INSERT INTO courses (course_name, credits)
   VALUES 
   ('Database Systems', 3),
   ('Operating Systems', 4);

   -- เพิ่มข้อมูลในตาราง enrollments
   INSERT INTO enrollments (student_id, course_id, enrollment_date)
   VALUES 
   (1, 1, '2024-06-15'),
   (2, 2, '2024-06-16');
   ```

   การใช้งานนี้ทำให้เห็นภาพรวมของการออกแบบและจัดการฐานข้อมูลอย่างเป็นระบบ โดยแสดงความสัมพันธ์ระหว่างตารางต่างๆ ในฐานข้อมูลเดียวกัน

**3.3 ชนิดข้อมูลพื้นฐานใน MySQL**

1. **ตัวเลข**:
   - INT: เลขจำนวนเต็ม
   - FLOAT, DOUBLE: เลขทศนิยม
   - DECIMAL: เลขทศนิยมที่มีความแม่นยำสูง

   ตัวอย่าง:
   ```sql
   CREATE TABLE example_numbers (
       id INT PRIMARY KEY,
       quantity INT,
       price FLOAT,
       exact_price DECIMAL(10, 2)
   );
   ```

2. **ข้อความ**:
   - CHAR: ข้อความความยาวคงที่
   - VARCHAR: ข้อความความยาวไม่เกินที่กำหนด
   - TEXT: ข้อความขนาดใหญ่

   ตัวอย่าง:
   ```sql
   CREATE TABLE example_texts (
       id INT PRIMARY KEY,
       fixed_length CHAR(10),
       variable_length VARCHAR(255),
       large_text TEXT
   );
   ```

3. **วันที่และเวลา**:
   - DATE: วันที่ (YYYY-MM-DD)
   - TIME: เวลา (HH:MM:SS)
   - DATETIME: วันที่และเวลา

   ตัวอย่าง:
   ```sql
   CREATE TABLE example_dates (
       id INT PRIMARY KEY,
       event_date DATE,
       event_time TIME,
       event_datetime DATETIME
   );
   ```

4. **อื่นๆ**:
   - BOOLEAN: ค่าจริง/เท็จ
   - ENUM: ค่าที่เลือกได้จากรายการที่กำหนด
   - BLOB: ข้อมูลไบนารีขนาดใหญ่

   ตัวอย่าง:
   ```sql
   CREATE TABLE example_others (
       id INT PRIMARY KEY,
       is_active BOOLEAN,
       status ENUM('active', 'inactive', 'pending'),
       binary_data BLOB
   );
   ```

**3.4 คำสั่ง SQL พื้นฐาน**

1. **การจัดการฐานข้อมูล**:
   ```sql
   CREATE DATABASE database_name;
   USE database_name;
   DROP DATABASE database_name;
   ```

   ตัวอย่าง:
   ```sql
   CREATE DATABASE library_db;
   USE library_db;
   DROP DATABASE test_db;
   ```

2. **การจัดการตาราง**:
   ```sql
   CREATE TABLE table_name (
       column1 datatype,
       column2 datatype,
       ...
   );
   
   ALTER TABLE table_name ADD column_name datatype;
   
   DROP TABLE table_name;
   ```

   ตัวอย่าง:
   ```sql
   CREATE TABLE books (
       id INT PRIMARY KEY AUTO_INCREMENT,
       title VARCHAR(255),
       author VARCHAR(255),
       publication_year INT,
       ISBN VARCHAR(13)
   );
   
   ALTER TABLE books ADD publisher VARCHAR(255);
   
   DROP TABLE old_books;
   ```

3. **การจัดการข้อมูล**:
   ```sql
   INSERT INTO table_name (column1, column2, ...)
   VALUES (value1, value2, ...);
   
   UPDATE table_name
   SET column1 = value1, column2 = value2, ...
   WHERE condition;
   
   DELETE FROM table_name WHERE condition;
   ```

   ตัวอย่าง:
   ```sql
   INSERT INTO books (title, author, publication_year, ISBN)
   VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, '9780743273565');
   
   UPDATE books
   SET author = 'George Orwell'
   WHERE title = '1984';
   
   DELETE FROM books WHERE publication_year < 2000;
   ```

4. **การสืบค้นข้อมูล**:
   ```sql
   SELECT column1, column2, ...
   FROM table_name
   WHERE condition;
   ```

   ตัวอย่าง:
   ```sql
   SELECT title, author
   FROM books
   WHERE publication_year > 2000;
   ```

**3.5 การใช้ Indexes**

Indexes ช่วยเพิ่มประสิทธิภาพในการค้นหาข้อมูล:

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

ตัวอย่าง:
```sql
CREATE INDEX idx_author
ON books (author);
```

**3.6 การสำรองและกู้คืนข้อมูล**

1. **การสำรองข้อมูล**:
   ```
   mysqldump -u username -p database_name > backup.sql
   ```

   ตัวอย่าง:
   ```shell
   mysqldump -u root -p library_db > library_backup.sql
   ```

2. **การกู้คืนข้อมูล**:
   ```
   mysql -u username -p database_name < backup.sql
   ```

   ตัวอย่าง:
   ```shell
   mysql -u root -p library_db < library_backup.sql
   ```

**แบบฝึกหัดท้ายบท**

1. สร้างฐานข้อมูลชื่อ "library" และสร้างตาราง "books" ที่มีคอลัมน์ดังนี้: id (INT, PRIMARY KEY), title (VARCHAR), author (VARCHAR), publication_year (INT), ISBN (VARCHAR)

   ```sql
   CREATE DATABASE library;
   USE library;

   CREATE TABLE books (
       id INT PRIMARY KEY AUTO_INCREMENT,
       title VARCHAR(255),
       author VARCHAR(255),
       publication_year INT,
       ISBN VARCHAR(13)
   );
   ```

2. เพิ่มข้อมูลหนังสืออย่างน้อย 5 รายการลงในตาราง "books"

   ```sql
   INSERT INTO books (title, author, publication_year, ISBN)
   VALUES
   ('To Kill a Mockingbird', 'Harper Lee', 1960, '9780061120084'),
   ('1984', 'George Orwell', 1949, '9780451524935'),
   ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, '9780743273565'),
   ('Pride and Prejudice', 'Jane Austen', 1813, '9781503290563'),
   ('The Catcher in the Rye', 'J.D. Salinger', 1951, '9780316769488');
   ```

3. เขียนคำสั่ง SQL เพื่อ:
   a) แสดงรายชื่อหนังสือทั้งหมดเรียงตามปีที่พิมพ์
   ```sql
   SELECT title, author, publication_year
   FROM books
   ORDER BY publication_year;
   ```

   b) อัพเดตชื่อผู้แต่งของหนังสือที่มี ISBN เป็น "978-0-13-468599-1"
   ```sql
   UPDATE books
   SET author = 'Updated Author'
   WHERE ISBN = '978-0-13-468599-1';
   ```

   c) ลบหนังสือที่พิมพ์ก่อนปี 2000
   ```sql
   DELETE FROM books
   WHERE publication_year < 2000;
   ```

4. สร้าง index บนคอลัมน์ "author" และอธิบายว่าทำไมการสร้าง index นี้อาจช่วยเพิ่มประสิทธิภาพการค้นหา
   ```sql
   CREATE INDEX idx_author ON books (author);
   ```
   **คำอธิบาย**: การสร้าง index บนคอลัมน์ "author" จะช่วยเพิ่มประสิทธิภาพในการสืบค้นข้อมูลเมื่อทำการค้นหาหรือกรองข้อมูลโดยใช้ชื่อผู้แต่ง เช่น การใช้คำสั่ง `SELECT * FROM books WHERE author = 'George Orwell'` จะทำให้ MySQL สามารถค้นหาข้อมูลได้รวดเร็วขึ้นเนื่องจากมี index บนคอลัมน์นี้

5. ทำการสำรองข้อมูลของฐานข้อมูล "library" และอธิบายขั้นตอนที่จะใช้ในการกู้คืนข้อมูลนี้ไปยังเซิร์ฟเวอร์ใหม่
   **สำรองข้อมูล**:
   ```shell
   mysqldump -u root -p library > library_backup.sql
   ```

## 4. การออกแบบและสร้างฐานข้อมูล

**4.1 หลักการออกแบบฐานข้อมูล**

1. **กฎการทำให้เป็นบรรทัดฐาน (Normalization Rules)**:
   - First Normal Form (1NF): ข้อมูลต้องอยู่ในรูปแบบอะตอมมิก หมายความว่าแต่ละคอลัมน์ต้องเก็บค่าเดี่ยวเท่านั้น ตัวอย่างเช่น:
     ```sql
     CREATE TABLE employees (
         employee_id INT PRIMARY KEY,
         employee_name VARCHAR(100) NOT NULL,
         phone_numbers VARCHAR(50)
     );
     -- ผิด: phone_numbers สามารถมีหลายเบอร์โทรในคอลัมน์เดียว
     ```
     แก้ไขให้ถูกต้อง:
     ```sql
     CREATE TABLE employees (
         employee_id INT PRIMARY KEY,
         employee_name VARCHAR(100) NOT NULL
     );

     CREATE TABLE employee_phone_numbers (
         employee_id INT,
         phone_number VARCHAR(15),
         PRIMARY KEY (employee_id, phone_number),
         FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
     );
     ```

   - Second Normal Form (2NF): ต้องอยู่ใน 1NF และไม่มี partial dependency หมายความว่า ทุก attribute ที่ไม่ใช่ primary key ต้องขึ้นอยู่กับ primary key ทั้งหมด ตัวอย่าง:
     ```sql
     CREATE TABLE order_details (
         order_id INT,
         product_id INT,
         product_name VARCHAR(100),
         quantity INT,
         PRIMARY KEY (order_id, product_id)
     );
     -- ผิด: product_name ขึ้นอยู่กับ product_id เท่านั้น ไม่ได้ขึ้นอยู่กับ order_id
     ```
     แก้ไขให้ถูกต้อง:
     ```sql
     CREATE TABLE orders (
         order_id INT PRIMARY KEY,
         order_date DATE
     );

     CREATE TABLE products (
         product_id INT PRIMARY KEY,
         product_name VARCHAR(100)
     );

     CREATE TABLE order_details (
         order_id INT,
         product_id INT,
         quantity INT,
         PRIMARY KEY (order_id, product_id),
         FOREIGN KEY (order_id) REFERENCES orders(order_id),
         FOREIGN KEY (product_id) REFERENCES products(product_id)
     );
     ```

   - Third Normal Form (3NF): ต้องอยู่ใน 2NF และไม่มี transitive dependency หมายความว่า ไม่มี attribute ใดขึ้นอยู่กับ attribute อื่นที่ไม่ใช่ primary key ตัวอย่าง:
     ```sql
     CREATE TABLE students (
         student_id INT PRIMARY KEY,
         student_name VARCHAR(100),
         advisor_id INT,
         advisor_name VARCHAR(100)
     );
     -- ผิด: advisor_name ขึ้นอยู่กับ advisor_id ซึ่งไม่ใช่ primary key
     ```
     แก้ไขให้ถูกต้อง:
     ```sql
     CREATE TABLE advisors (
         advisor_id INT PRIMARY KEY,
         advisor_name VARCHAR(100)
     );

     CREATE TABLE students (
         student_id INT PRIMARY KEY,
         student_name VARCHAR(100),
         advisor_id INT,
         FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id)
     );
     ```

**2. Entity-Relationship Diagram (ERD)**

ERD เป็นแผนภาพที่ใช้ในการออกแบบฐานข้อมูลเชิงสัมพันธ์ โดยแสดงความสัมพันธ์ระหว่างentities ต่างๆ ในระบบ

2.1 **Entity**:
   - คือสิ่งที่เราต้องการเก็บข้อมูล สามารถเป็นสิ่งที่จับต้องได้หรือเป็นแนวคิดก็ได้
   - แทนด้วยสี่เหลี่ยมในแผนภาพ ERD
   - ตัวอย่าง: Student, Course, Instructor, Department

   ```
   ┌─────────────┐
   │   Student   │
   └─────────────┘
   ```

2.2 **Attribute**:
   - คือคุณสมบัติหรือลักษณะของ Entity
   - แทนด้วยวงรีที่เชื่อมต่อกับ Entity ในแผนภาพ ERD
   - ตัวอย่าง:
     - Student: student_id, first_name, last_name, date_of_birth, email
     - Course: course_id, course_name, credits, department_id

   ```
       ┌─────────────┐
       │   Student   │
       └─────────────┘
            │
     ┌──────┴──────┐
     │             │
  ┌──────┐     ┌──────┐
  │ Name │     │  ID  │
  └──────┘     └──────┘
   ```

2.3 **Relationship**:
   - แสดงความสัมพันธ์ระหว่าง Entities
   - แทนด้วยเส้นที่เชื่อมระหว่าง Entities ในแผนภาพ ERD
   - ตัวอย่าง: 
     - Student "enrolls in" Course
     - Instructor "teaches" Course
     - Department "offers" Course

   ```
   ┌─────────────┐     enrolls in   ┌─────────────┐
   │   Student   │─────────────────▶│   Course    │
   └─────────────┘                  └─────────────┘
   ```

2.4 **Cardinality**:
   - แสดงจำนวนของ instances ที่สามารถมีความสัมพันธ์กันได้
   - ตัวอย่าง:
     - One-to-One (1:1): หนึ่ง Student มีหนึ่ง Student ID Card
     - One-to-Many (1:N): หนึ่ง Department มีหลาย Courses
     - Many-to-Many (M:N): หลาย Students ลงทะเบียนเรียนหลาย Courses

   ```
   ┌─────────────┐ 1     N ┌─────────────┐
   │ Department  │─────────│   Course    │
   └─────────────┘         └─────────────┘
   ```

2.5 **แอตทริบิวต์พิเศษ**:
   - Primary Key: แอตทริบิวต์ที่ใช้ระบุ Entity อย่างเป็นเอกลักษณ์ (ขีดเส้นใต้ในแผนภาพ ERD)
   - Composite Attribute: แอตทริบิวต์ที่ประกอบด้วยแอตทริบิวต์ย่อยหลายตัว
   - Derived Attribute: แอตทริบิวต์ที่คำนวณได้จากแอตทริบิวต์อื่น (แทนด้วยวงรีเส้นประ)
   - Multi-valued Attribute: แอตทริบิวต์ที่มีได้หลายค่า (แทนด้วยวงรีซ้อน)

   ```
       ┌─────────────┐
       │   Student   │
       └─────────────┘
            │
     ┌──────┴──────┐
     │             │
  ┌──────┐     ┌──────┐
  │ Name │     │  ID  │
  └──────┘     └──────┘
     │
   ┌───┴───┐
┌─────┐ ┌─────┐
│First│ │Last │
└─────┘ └─────┘
   ```

2.6 **ตัวอย่าง ERD ที่สมบูรณ์**:

```
┌─────────────┐ 1     N ┌─────────────┐ N     1 ┌─────────────┐
│ Department  │─────────│   Course    │─────────│ Instructor  │
└─────────────┘         └─────────────┘         └─────────────┘
      │                       │ N                     │
      │                       │                       │
      │                       │ M                     │
      │                 ┌─────────────┐               │
      └─────────────────│   Student   │───────────────┘
                        └─────────────┘
```

ในตัวอย่างนี้:
- หนึ่ง Department มีหลาย Courses (1:N)
- หนึ่ง Instructor สอนหลาย Courses (1:N)
- หลาย Students ลงทะเบียนเรียนหลาย Courses (M:N)
- หนึ่ง Department มีหลาย Students (1:N)
- หนึ่ง Instructor ดูแลหลาย Students (1:N)

การใช้ ERD ช่วยให้เราสามารถมองเห็นภาพรวมของระบบฐานข้อมูลได้อย่างชัดเจน ทำให้ง่ายต่อการออกแบบและพัฒนาฐานข้อมูลที่มีประสิทธิภาพ

3. **ชนิดของความสัมพันธ์**:
   **1. One-to-One (1:1) - บุคคลกับบัตรประชาชน**

   ```
   ┌─────────────────┐      ┌─────────────────┐
   │    Citizens     │      │    ID Cards     │
   ├─────────────────┤      ├─────────────────┤
   │ citizen_id      │──┐   │ id_card_id      │
   │ name            │  └──>│ citizen_id      │
   └─────────────────┘      └─────────────────┘
   ```

   SQL:
   ```sql
   CREATE TABLE citizens (
      citizen_id INT PRIMARY KEY,
      name VARCHAR(100)
   );

   CREATE TABLE id_cards (
      id_card_id INT PRIMARY KEY,
      citizen_id INT UNIQUE,
      FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
   );
   ```

   **2. One-to-Many (1:N) - อาจารย์กับนักเรียน**

   ```
   ┌─────────────────┐      ┌─────────────────┐
   │    Teachers     │      │    Students     │
   ├─────────────────┤      ├─────────────────┤
   │ teacher_id      │──┐   │ student_id      │
   │ name            │  │   │ name            │
   └─────────────────┘  └──>│ teacher_id      │
                           └─────────────────┘
   ```

   SQL:
   ```sql
   CREATE TABLE teachers (
      teacher_id INT PRIMARY KEY,
      name VARCHAR(100)
   );

   CREATE TABLE students (
      student_id INT PRIMARY KEY,
      name VARCHAR(100),
      teacher_id INT,
      FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
   );
   ```

   **3. Many-to-Many (M:N) - นักเรียนกับวิชาเรียน**

   ```
   ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
   │    Students     │     │   Enrollments   │     │    Courses      │
   ├─────────────────┤     ├─────────────────┤     ├─────────────────┤
   │ student_id      │──┐  │ student_id      │  ┌──│ course_id       │
   │ name            │  └─>│ course_id       │<─┘  │ course_name     │
   └─────────────────┘     │ enrollment_date │     └─────────────────┘
                           └─────────────────┘
   ```

   SQL:
   ```sql
   CREATE TABLE students (
      student_id INT PRIMARY KEY,
      name VARCHAR(100)
   );

   CREATE TABLE courses (
      course_id INT PRIMARY KEY,
      course_name VARCHAR(100)
   );

   CREATE TABLE enrollments (
      student_id INT,
      course_id INT,
      enrollment_date DATE,
      PRIMARY KEY (student_id, course_id),
      FOREIGN KEY (student_id) REFERENCES students(student_id),
      FOREIGN KEY (course_id) REFERENCES courses(course_id)
   );
   ```

   ในแต่ละกรณี:

   1. **1:1**: ใช้ `UNIQUE` constraint บน `citizen_id` ใน `id_cards` table เพื่อรับประกันว่าแต่ละบุคคลมีเพียงหนึ่งบัตรประชาชน

   2. **1:N**: ใช้ `FOREIGN KEY` ใน `students` table ที่อ้างอิงถึง `teachers` table เพื่อแสดงว่านักเรียนหลายคนสามารถมีอาจารย์คนเดียวกันได้

   3. **M:N**: สร้างตาราง junction (`enrollments`) ที่มี foreign keys อ้างอิงทั้ง `students` และ `courses` tables โดยใช้ composite primary key เพื่อแสดงความสัมพันธ์ระหว่างนักเรียนและวิชาเรียน

**4.2 การสร้างฐานข้อมูลและตาราง**

```sql
CREATE DATABASE university_db;
USE university_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    credits INT,
    department VARCHAR(50)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

**4.3 การกำหนด Constraints**

1. **Primary Key**:
   ```sql
   PRIMARY KEY (column_name)
   ```

2. **Foreign Key**:
   ```sql
   FOREIGN KEY (column_name) REFERENCES other_table(other_column)
   ```

3. **Unique**:
   ```sql
   UNIQUE (column_name)
   ```

4. **Not Null**:
   ```sql
   column_name datatype NOT NULL
   ```

5. **Check**:
   ```sql
   CHECK (condition)
   ```

**ตัวอย่างการกำหนด Constraints เพิ่มเติม:**

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0)
);
```

**4.4 การใช้ AUTO_INCREMENT**

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100)
);
```

**4.5 การสร้าง Views**

Views เป็นตารางเสมือนที่สร้างจากผลลัพธ์ของ query:

```sql
CREATE VIEW student_course_view AS
SELECT s.student_id, s.first_name, s.last_name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;
```

**ตัวอย่างการใช้ Views เพิ่มเติม:**

```sql
CREATE VIEW department_credits_view AS
SELECT department, SUM(credits) AS total_credits
FROM courses
GROUP BY department;
```

**4.6 การใช้ Stored Procedures**

Stored Procedures เป็นชุดคำสั่ง SQL ที่สามารถเรียกใช้ซ้ำได้:

```sql
DELIMITER //
CREATE PROCEDURE GetCourseEnrollments(IN course_name VARCHAR(100))
BEGIN
    SELECT s.first_name, s.last_name
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    WHERE c.course_name = course_name;
END //
DELIMITER ;

-- เรียกใช้ Stored Procedure
CALL GetCourseEnrollments('Database Systems');
```

**ตัวอย่างการใช้ Stored Procedures เพิ่มเติม:**

```sql
DELIMITER //
CREATE PROCEDURE GetStudentDetails(IN student_id INT)
BEGIN
    SELECT s.first_name, s.last_name, c.course_name
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
    WHERE s.student_id = student_id;
END //
DELIMITER ;

-- เรียกใช้ Stored Procedure
CALL GetStudentDetails(1);
```

**4.7 การสร้าง Triggers**

Triggers เป็นการกำหนดการทำงานอัตโนมัติเมื่อมีการเปลี่ยนแปลงข้อมูล:

```sql
DELIMITER //
CREATE TRIGGER after_enrollment_insert
AFTER INSERT ON enrollments
FOR EACH ROW
BEGIN
    UPDATE courses
    SET enrolled_students = enrolled_students + 1
    WHERE course_id = NEW.course_id;
END //
DELIMITER ;
```

**ตัวอย่างการใช้ Triggers เพิ่มเติม:**

```sql
DELIMITER //
CREATE TRIGGER before_student_delete
BEFORE DELETE ON students
FOR EACH ROW
BEGIN
    DELETE FROM enrollments WHERE student_id = OLD.student_id;
END //
DELIMITER ;
```

**แบบฝึกหัดท้ายบท**

1. ออกแบบ ERD สำหรับระบบห้องสมุดที่มี entities ดังนี้: Books, Authors, Members, และ Loans

2. สร้างฐานข้อมูลและตารางตาม ERD ที่ออกแบบในข้อ 1 พร้อมทั้งกำหนด constraints ที่เหมาะสม

3. สร้าง View ที่แสดงรายชื่อหนังสือที่ถูกยืมมากที่สุด 10 อันดับแรก

4. เขียน Stored Procedure ที่รับ input เป็นรหัสสมาชิก และคืนค่าเป็นรายการหนังสือที่สมาชิกนั้นยืมอยู่ในปัจจุบัน

5. สร้าง Trigger ที่จะอัพเดตจำนวนหนังสือที่มีอยู่ (available_copies) ในตาราง Books เมื่อมีการยืมหรือคืนหนังสือ

ต่อไปนี้เป็นเนื้อหาสำหรับหัวข้อถัดไป ซึ่งเกี่ยวกับการจัดการข้อมูลด้วย SQL:

## 5. การจัดการข้อมูลด้วย SQL

**5.1 การเพิ่มข้อมูล (INSERT)**

การเพิ่มข้อมูลใหม่ลงในตารางใช้คำสั่ง INSERT

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

ตัวอย่าง:
```sql
INSERT INTO students (first_name, last_name, email)
VALUES ('John', 'Doe', 'john.doe@example.com');
```

สามารถเพิ่มข้อมูลหลายแถวได้ในครั้งเดียว:
```sql
INSERT INTO students (first_name, last_name, email)
VALUES 
('Jane', 'Smith', 'jane.smith@example.com'),
('Robert', 'Brown', 'robert.brown@example.com');
```

**5.2 การอ่านข้อมูล (SELECT)**

การดึงข้อมูลจากตารางใช้คำสั่ง SELECT

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

ตัวอย่าง:
```sql
SELECT first_name, last_name
FROM students
WHERE age > 20;
```

สามารถใช้ฟังก์ชันในการดึงข้อมูล เช่น `COUNT`, `SUM`, `AVG`, `MAX`, และ `MIN`:
```sql
SELECT COUNT(*) FROM students;
SELECT AVG(age) FROM students;
SELECT MAX(salary) FROM employees;
```

**5.3 การอัปเดตข้อมูล (UPDATE)**

การแก้ไขข้อมูลที่มีอยู่ในตารางใช้คำสั่ง UPDATE

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

ตัวอย่าง:
```sql
UPDATE students
SET email = 'new.email@example.com'
WHERE student_id = 1;
```

ควรระมัดระวังในการอัปเดตข้อมูลที่ไม่มีเงื่อนไข เพราะอาจทำให้ข้อมูลทั้งหมดในตารางถูกอัปเดต:
```sql
UPDATE students
SET email = 'new.email@example.com';
```

**5.4 การลบข้อมูล (DELETE)**

การลบข้อมูลจากตารางใช้คำสั่ง DELETE

```sql
DELETE FROM table_name
WHERE condition;
```

ตัวอย่าง:
```sql
DELETE FROM students
WHERE student_id = 1;
```

การลบข้อมูลที่ไม่มีเงื่อนไขสามารถทำให้ข้อมูลทั้งหมดในตารางถูกลบได้:
```sql
DELETE FROM students;
```

**5.5 การใช้ WHERE clause**

WHERE clause ใช้เพื่อกำหนดเงื่อนไขในการดึง อัปเดต หรือลบข้อมูล

ตัวอย่างการใช้ operator ต่างๆ:
```sql
SELECT * FROM students WHERE age >= 18;
SELECT * FROM students WHERE last_name LIKE 'S%';
SELECT * FROM students WHERE age BETWEEN 20 AND 25;
SELECT * FROM students WHERE city IN ('New York', 'Los Angeles', 'Chicago');
```

สามารถใช้ร่วมกับหลายเงื่อนไขโดยใช้ AND, OR:
```sql
SELECT * FROM students WHERE age >= 18 AND city = 'New York';
SELECT * FROM students WHERE last_name LIKE 'S%' OR age < 18;
```

**5.6 การใช้ ORDER BY**

ORDER BY ใช้เพื่อเรียงลำดับผลลัพธ์

```sql
SELECT * FROM students
ORDER BY last_name ASC, first_name DESC;
```

สามารถใช้ร่วมกับฟังก์ชัน เช่น `LIMIT` เพื่อกำหนดจำนวนผลลัพธ์:
```sql
SELECT * FROM students
ORDER BY last_name ASC
LIMIT 10;
```

**5.7 การใช้ GROUP BY และ HAVING**

GROUP BY ใช้เพื่อจัดกลุ่มข้อมูล และ HAVING ใช้เพื่อกำหนดเงื่อนไขสำหรับกลุ่ม

```sql
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

สามารถใช้ฟังก์ชัน aggregate ในการจัดกลุ่มข้อมูล:
```sql
SELECT department, COUNT(*) as num_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

**5.8 การใช้ JOIN**

JOIN ใช้เพื่อรวมข้อมูลจากหลายตาราง โดยมีประเภทหลักๆ ดังนี้:

1. **INNER JOIN**: รวมข้อมูลเฉพาะแถวที่มีค่าตรงกันในทั้งสองตาราง

    ```sql
    SELECT s.student_name, c.class_name
    FROM students s
    INNER JOIN classes c ON s.class_id = c.class_id;
    ```

2. **LEFT JOIN**: รวมทุกแถวจากตารางซ้าย และแถวที่ตรงกันจากตารางขวา ถ้าไม่มีค่าตรงกัน จะคืนค่า NULL

    ```sql
    SELECT s.student_name, c.class_name
    FROM students s
    LEFT JOIN classes c ON s.class_id = c.class_id;
    ```

3. **RIGHT JOIN**: รวมทุกแถวจากตารางขวา และแถวที่ตรงกันจากตารางซ้าย ถ้าไม่มีค่าตรงกัน จะคืนค่า NULL

    ```sql
    SELECT e.emp_name, d.dept_name
    FROM employees e
    RIGHT JOIN departments d ON e.dept_id = d.dept_id;
    ```

4. **FULL OUTER JOIN**: รวมทุกแถวจากทั้งสองตาราง ถ้าไม่มีค่าตรงกัน จะคืนค่า NULL

    ```sql
    SELECT s.student_name, c.class_name
    FROM students s
    FULL OUTER JOIN classes c ON s.class_id = c.class_id;
    ```

### ตัวอย่างในบริบทต่างๆ

#### **ตัวอย่างในบริบทโรงเรียน**

สมมติว่าเรามีตาราง `students` และ `classes`

```
┌────────────┐        ┌────────────┐
│  Students  │        │  Classes   │
├────────────┤        ├────────────┤
│ student_id │        │ class_id   │
│ student_name│       │ class_name │
│ class_id   │        │            │
└────────────┘        └────────────┘
      │ N                 │ 1
      │                   │
      └───────────────────┘
         belongs to
```

ในแผนภาพนี้:

1. สี่เหลี่ยมแทน Entity (ในที่นี้คือตาราง students และ classes)
2. ข้อความในสี่เหลี่ยมแสดงถึง Attributes ของแต่ละ Entity
3. เส้นที่เชื่อมระหว่างสองตารางแสดงถึงความสัมพันธ์ระหว่าง Entity
4. "N" และ "1" แสดงถึง Cardinality ของความสัมพันธ์
5. "belongs to" อธิบายลักษณะความสัมพันธ์

ความสัมพันธ์นี้อ่านได้ว่า:
- หนึ่งนักเรียน (Student) belongs to หนึ่งชั้นเรียน (Class)
- หนึ่งชั้นเรียน (Class) สามารถมีได้หลายนักเรียน (Students)

นี่เป็นความสัมพันธ์แบบ "One-to-Many" (1:N) ระหว่าง Classes และ Students โดยที่ class_id ในตาราง Students เป็น Foreign Key ที่อ้างอิงถึง class_id ในตาราง Classes

```sql
-- สร้างตาราง
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    class_id INT
);

CREATE TABLE classes (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(50)
);

-- เพิ่มข้อมูลตัวอย่าง
INSERT INTO students VALUES (1, 'Alice', 101), (2, 'Bob', 102), (3, 'Charlie', 101), (4, 'David', NULL);
INSERT INTO classes VALUES (101, 'Math'), (102, 'Science'), (103, 'History');

-- INNER JOIN
SELECT s.student_name, c.class_name
FROM students s
INNER JOIN classes c ON s.class_id = c.class_id;

-- LEFT JOIN
SELECT s.student_name, c.class_name
FROM students s
LEFT JOIN classes c ON s.class_id = c.class_id;
```

#### **ตัวอย่างในบริบทบริษัท**

สมมติว่าเรามีตาราง `employees` และ `departments`

```
┌────────────┐        ┌────────────┐
│ Employees  │        │Departments │
├────────────┤        ├────────────┤
│ emp_id     │        │ dept_id    │
│ emp_name   │        │ dept_name  │
│ dept_id    │        │            │
└────────────┘        └────────────┘
      │ N                 │ 1
      │                   │
      └───────────────────┘
         works in
```

ในแผนภาพนี้:

1. สี่เหลี่ยมแทน Entity (ในที่นี้คือตาราง employees และ departments)
2. ข้อความในสี่เหลี่ยมแสดงถึง Attributes ของแต่ละ Entity
3. เส้นที่เชื่อมระหว่างสองตารางแสดงถึงความสัมพันธ์ระหว่าง Entity
4. "N" และ "1" แสดงถึง Cardinality ของความสัมพันธ์
5. "works in" อธิบายลักษณะความสัมพันธ์

ความสัมพันธ์นี้อ่านได้ว่า:
- หนึ่งพนักงาน (Employee) works in หนึ่งแผนก (Department)
- หนึ่งแผนก (Department) สามารถมีได้หลายพนักงาน (Employees)

นี่เป็นความสัมพันธ์แบบ "One-to-Many" (1:N) ระหว่าง Departments และ Employees โดยที่ dept_id ในตาราง Employees เป็น Foreign Key ที่อ้างอิงถึง dept_id ในตาราง Departments

```

sql
-- สร้างตาราง
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT
);

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- เพิ่มข้อมูลตัวอย่าง
INSERT INTO employees VALUES (1, 'John', 10), (2, 'Jane', 20), (3, 'Bob', 10), (4, 'Alice', NULL);
INSERT INTO departments VALUES (10, 'IT'), (20, 'HR'), (30, 'Finance');

-- INNER JOIN
SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- RIGHT JOIN
SELECT e.emp_name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;
```

#### **ตัวอย่างในบริบทระบบยืมคืน**

สมมติว่าเรามีตาราง `books`, `members`, และ `loans` ที่เก็บข้อมูลของระบบยืมคืนหนังสือ

```
┌────────────┐        ┌────────────┐
│   Books    │        │   Loans    │        ┌────────────┐
├────────────┤        ├────────────┤        │  Members   │
│ book_id    │        │ loan_id    │        ├────────────┤
│ title      │        │ book_id    │        │ member_id  │
│            │        │ member_id  │        │ member_name│
│            │        │ loan_date  │        │            │
│            │        │ return_date│        │            │
└────────────┘        └────────────┘        └────────────┘
      │ 1                 │ N         N      │ 1
      │                   │                  │
      └───────────────────┘                  │
             is loaned                       │
                       └──────────────────────┘
                              borrows
```

ในแผนภาพนี้:

1. สี่เหลี่ยมแทน Entity (ตาราง books, loans, และ members)
2. ข้อความในสี่เหลี่ยมแสดงถึง Attributes ของแต่ละ Entity
3. เส้นที่เชื่อมระหว่างตารางแสดงถึงความสัมพันธ์ระหว่าง Entity
4. "1" และ "N" แสดงถึง Cardinality ของความสัมพันธ์
5. "is loaned" และ "borrows" อธิบายลักษณะความสัมพันธ์

ความสัมพันธ์นี้อ่านได้ว่า:
- หนึ่งหนังสือ (Book) สามารถถูกยืม (is loaned) ได้หลายครั้ง (ผ่านตาราง Loans)
- หนึ่งสมาชิก (Member) สามารถยืม (borrows) หนังสือได้หลายเล่ม (ผ่านตาราง Loans)
- หนึ่งการยืม (Loan) เกี่ยวข้องกับหนึ่งหนังสือ (Book) และหนึ่งสมาชิก (Member)

นี่เป็นความสัมพันธ์แบบ "Many-to-Many" ระหว่าง Books และ Members ผ่านตาราง Loans ซึ่งทำหน้าที่เป็น junction table

```sql
-- สร้างตาราง
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200)
);

CREATE TABLE members (
    member_id INT PRIMARY KEY,
    member_name VARCHAR(100)
);

CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE,
    return_date DATE
);

-- เพิ่มข้อมูลตัวอย่าง
INSERT INTO books VALUES (1, 'The Great Gatsby'), (2, 'To Kill a Mockingbird'), (3, '1984');
INSERT INTO members VALUES (101, 'Emma'), (102, 'Oliver'), (103, 'Sophia');
INSERT INTO loans VALUES (1, 1, 101, '2023-06-01', '2023-06-15'),
                         (2, 2, 102, '2023-06-05', NULL),
                         (3, 3, 101, '2023-06-10', NULL);

-- INNER JOIN ระหว่าง 3 ตาราง
SELECT m.member_name, b.title, l.loan_date, l.return_date
FROM loans l
INNER JOIN members m ON l.member_id = m.member_id
INNER JOIN books b ON l.book_id = b.book_id;

-- LEFT JOIN เพื่อดูหนังสือที่ไม่ถูกยืม
SELECT b.title, l.loan_id
FROM books b
LEFT JOIN loans l ON b.book_id = l.book_id
WHERE l.loan_id IS NULL;
```

**ข้อควรระวังเมื่อใช้ JOIN:**

1. ประสิทธิภาพ: JOIN อาจทำให้ query ช้าลงเมื่อใช้กับข้อมูลจำนวนมาก ควรใช้ indexes ที่เหมาะสม
2. Cartesian Product: ระวังการเกิด Cartesian product ที่อาจเกิดขึ้นเมื่อไม่ระบุเงื่อนไข JOIN ที่ถูกต้อง
3. NULL values: ต้องระมัดระวังการจัดการกับ NULL values โดยเฉพาะใน OUTER JOINs

การใช้ JOIN อย่างมีประสิทธิภาพจะช่วยให้สามารถดึงข้อมูลที่ซับซ้อนจากหลายตารางได้อย่างมีประสิทธิภาพ ซึ่งเป็นทักษะสำคัญในการจัดการฐานข้อมูล

--- 

### แบบฝึกหัดการจัดการข้อมูลด้วย SQL สำหรับร้านขายสินค้า

สมมติว่าคุณมีฐานข้อมูลของร้านขายสินค้า ประกอบด้วย 4 ตารางดังนี้:
- `products` : เก็บข้อมูลสินค้า
- `customers` : เก็บข้อมูลลูกค้า
- `orders` : เก็บข้อมูลการสั่งซื้อ
- `order_items` : เก็บข้อมูลรายละเอียดการสั่งซื้อแต่ละรายการ

โครงสร้างของแต่ละตาราง:

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

**ข้อมูลตัวอย่าง:**

```sql
-- ข้อมูลสินค้า
INSERT INTO products VALUES 
(1, 'Laptop', 800.00), 
(2, 'Smartphone', 600.00), 
(3, 'Tablet', 300.00);

-- ข้อมูลลูกค้า
INSERT INTO customers VALUES 
(1, 'John Doe', 'john@example.com'), 
(2, 'Jane Smith', 'jane@example.com');

-- ข้อมูลการสั่งซื้อ
INSERT INTO orders VALUES 
(1, 1, '2024-06-01'), 
(2, 2, '2024-06-02');

-- ข้อมูลรายละเอียดการสั่งซื้อ
INSERT INTO order_items VALUES 
(1, 1, 1, 1), 
(2, 1, 3, 2), 
(3, 2, 2, 1);
```

### ข้อมูลตัวอย่างในทุกตาราง

#### ตาราง `products`

| product_id | product_name | price  |
|------------|--------------|--------|
| 1          | Laptop       | 800.00 |
| 2          | Smartphone   | 600.00 |
| 3          | Tablet       | 300.00 |
| 4          | Headphones   | 150.00 |

#### ตาราง `customers`

| customer_id | customer_name | email             |
|-------------|---------------|-------------------|
| 1           | John Doe      | john@example.com  |
| 2           | Jane Smith    | jane@example.com  |
| 3           | Alice Brown   | alice@example.com |

#### ตาราง `orders`

| order_id | customer_id | order_date |
|----------|-------------|------------|
| 1        | 1           | 2024-06-01 |
| 2        | 2           | 2024-06-02 |
| 3        | 3           | 2024-06-03 |

#### ตาราง `order_items`

| order_item_id | order_id | product_id | quantity |
|---------------|----------|------------|----------|
| 1             | 1        | 1          | 1        |
| 2             | 1        | 3          | 2        |
| 3             | 2        | 2          | 1        |
| 4             | 3        | 4          | 3        |
| 5             | 3        | 1          | 1        |


### แบบฝึกหัด

1. **เพิ่มข้อมูลสินค้าใหม่**

   เพิ่มข้อมูลสินค้าลงในตาราง `products` โดยเพิ่มสินค้าใหม่ชื่อ "Headphones" ราคาชิ้นละ 150 บาท

   <details>

   ```sql
   INSERT INTO products (product_id, product_name, price)
   VALUES (4, 'Headphones', 150.00);
   ```

   </details>

2. **ดึงข้อมูลลูกค้าที่สั่งซื้อสินค้า**

   ดึงข้อมูลชื่อลูกค้าและอีเมลของลูกค้าที่สั่งซื้อสินค้าชื่อ "Laptop"
   <details>

   ```sql
   SELECT c.customer_name, c.email
   FROM customers c
   JOIN orders o ON c.customer_id = o.customer_id
   JOIN order_items oi ON o.order_id = oi.order_id
   JOIN products p ON oi.product_id = p.product_id
   WHERE p.product_name = 'Laptop';
   ```

   </details>

3. **อัปเดตราคาสินค้า**

   อัปเดตราคาของสินค้าชื่อ "Tablet" เป็น 350 บาท
   <details>

   ```sql
   UPDATE products
   SET price = 350.00
   WHERE product_name = 'Tablet';
   ```

   </details>

4. **ลบข้อมูลการสั่งซื้อ**

   ลบข้อมูลการสั่งซื้อที่มี `order_id` เท่ากับ 2
   <details>

   ```sql
   DELETE FROM order_items
   WHERE order_id = 2;

   DELETE FROM orders
   WHERE order_id = 2;
   ```

   </details>

5. **ดึงข้อมูลรายงานการขาย**

   ดึงข้อมูลรายงานการขาย ประกอบด้วย ชื่อสินค้า จำนวนที่ขายได้ และยอดขายรวม โดยจัดกลุ่มตามชื่อสินค้า
   <details>

   ```sql
   SELECT p.product_name, SUM(oi.quantity) AS total_quantity, SUM(oi.quantity * p.price) AS total_sales
   FROM products p
   JOIN order_items oi ON p.product_id = oi.product_id
   GROUP BY p.product_name;
   ```

   </details>

## บทที่ 6: การสืบค้นข้อมูลขั้นสูง
```plaintext
┌──────────────┐     1     ┌──────────────┐
│  departments │◄─────────┤   employees  │
├──────────────┤     N     ├──────────────┤
│ dept_id (PK) │           │ employee_id  │
│ dept_name    │           │ employee_name│
└──────────────┘           │ department   │
                           │ manager_id   │
                           │ salary       │
                           └──────────────┘
                                 │ 1
                                 │
                                 │ N
                           ┌──────────────┐
                           │    sales     │
                           ├──────────────┤
                           │ sale_id (PK) │
                           │ employee_id  │
                           │ sale_date    │
                           │ sales_amount │
                           └──────────────┘

┌──────────────┐           ┌──────────────┐
│   articles   │           │    users     │
├──────────────┤           ├──────────────┤
│ article_id   │           │ user_id (PK) │
│ title        │           │ info (JSON)  │
│ body         │           └──────────────┘
└──────────────┘
```

### ความสัมพันธ์ระหว่างตาราง

1. **departments - employees**: One-to-Many (1:N)
   - หนึ่งแผนก (department) มีได้หลายพนักงาน (employees)
   - พนักงานแต่ละคนสังกัดเพียงหนึ่งแผนก

2. **employees (self-referencing)**: One-to-Many (1:N)
   - หนึ่งพนักงาน (employee) สามารถเป็นผู้จัดการ (manager) ของหลายพนักงานได้
   - แต่ละพนักงานมีผู้จัดการได้เพียงคนเดียว (หรือไม่มี ในกรณีของ CEO)

3. **employees - sales**: One-to-Many (1:N)
   - หนึ่งพนักงานสามารถมีหลายรายการขาย (sales)
   - แต่ละรายการขายเกี่ยวข้องกับพนักงานเพียงคนเดียว

4. **articles และ users**: ไม่มีความสัมพันธ์โดยตรงกับตารางอื่น (Stand-alone tables)

### คำอธิบายเพิ่มเติม

1. **Primary Keys (PK)**: ทุกตารางมี Primary Key ที่ไม่ซ้ำกัน
   - departments: dept_id
   - employees: employee_id
   - sales: sale_id
   - articles: article_id
   - users: user_id

2. **Foreign Keys (FK)**:
   - employees.department เป็น FK อ้างอิงถึง departments.dept_id
   - employees.manager_id เป็น FK อ้างอิงถึง employees.employee_id (self-referencing)
   - sales.employee_id เป็น FK อ้างอิงถึง employees.employee_id

3. **ตาราง articles**:
   - ใช้สำหรับการทำ Full-Text Search
   - ไม่มีความสัมพันธ์โดยตรงกับตารางอื่น

4. **ตาราง users**:
   - ใช้สำหรับการจัดเก็บข้อมูล JSON
   - ไม่มีความสัมพันธ์โดยตรงกับตารางอื่น

5. **การใช้งานพิเศษ**:
   - ตาราง articles สามารถใช้ในการสาธิต Full-Text Search
   - ตาราง users สามารถใช้ในการสาธิตการทำงานกับข้อมูล JSON

### 6.1 Subqueries

Subquery คือ query ที่อยู่ภายใน query อื่น สามารถใช้ใน SELECT, FROM, WHERE, และ HAVING clauses

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| employee_name | salary |
|---------------|--------|
| Alice Brown   | 70000  |
| John Doe      | 75000  |

### 6.2 Correlated Subqueries

Correlated subquery คือ subquery ที่อ้างอิงถึงคอลัมน์ในตารางของ outer query

```sql
SELECT e1.employee_name, e1.salary
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department = e1.department);
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| employee_name | salary |
|---------------|--------|
| Alice Brown   | 70000  |
| John Doe      | 75000  |

### 6.3 Common Table Expressions (CTE)

CTE ช่วยให้เราสร้าง named subquery ที่สามารถอ้างอิงได้หลายครั้งใน main query

```sql
WITH high_salary_employees AS (
    SELECT * FROM employees WHERE salary > 50000
)
SELECT department, COUNT(*) as count
FROM high_salary_employees
GROUP BY department;
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| department | count |
|------------|-------|
| IT         | 2     |
| HR         | 1     |

### 6.4 Window Functions

Window functions ทำการคำนวณบนชุดของแถวที่มีความสัมพันธ์กับแถวปัจจุบัน

```sql
SELECT 
    employee_name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) as avg_dept_salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
FROM employees;
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| employee_name | department | salary | avg_dept_salary | salary_rank |
|---------------|------------|--------|-----------------|-------------|
| Alice Brown   | IT         | 70000  | 62500           | 1           |
| Jane Smith    | IT         | 55000  | 62500           | 2           |
| John Doe      | HR         | 75000  | 75000           | 1           |

### 6.5 PIVOT และ UNPIVOT

PIVOT ใช้เพื่อแปลงข้อมูลจากแถวเป็นคอลัมน์ และ UNPIVOT ทำในทางตรงกันข้าม (หมายเหตุ: ไม่ทุก DBMS รองรับคำสั่งนี้โดยตรง)

```sql
-- ตัวอย่าง PIVOT (ในรูปแบบของ SQL Server)
SELECT *
FROM (
    SELECT department, job_title, salary
    FROM employees
) AS SourceTable
PIVOT (
    AVG(salary)
    FOR department IN ([HR], [IT], [Sales])
) AS PivotTable;
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| job_title | HR    | IT     | Sales |
|-----------|-------|--------|-------|
| Manager   | 75000 | NULL   | NULL  |
| Engineer  | NULL  | 62500  | NULL  |

### 6.6 Recursive Queries

Recursive queries ใช้สำหรับการ query ข้อมูลที่มีโครงสร้างแบบลำดับชั้น

```sql
WITH RECURSIVE subordinates AS (
    SELECT employee_id, manager_id, employee_name
    FROM employees
    WHERE employee_id = 1 -- root employee (CEO)
    UNION ALL
    SELECT e.employee_id, e.manager_id, e.employee_name
    FROM employees e
    INNER JOIN subordinates s ON s.employee_id = e.manager_id
)
SELECT * FROM subordinates;
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| employee_id | manager_id | employee_name |
|-------------|------------|---------------|
| 1           | NULL       | CEO           |
| 2           | 1          | Manager       |
| 3           | 2          | Engineer      |

### 6.7 Full-Text Search

Full-Text Search ช่วยในการค้นหาข้อความที่ซับซ้อนในฐานข้อมูล (การใช้งานจะแตกต่างกันไปในแต่ละ DBMS)

```sql
-- ตัวอย่างใน MySQL
SELECT * 
FROM articles 
WHERE MATCH(title, body) AGAINST('database optimization' IN BOOLEAN MODE);
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| article_id | title                      | body                  |
|------------|----------------------------|-----------------------|
| 1          | Database Optimization Tips | Learn how to optimize |

### 6.8 JSON Operations

การทำงานกับข้อมูล JSON ในฐานข้อมูล (ฟังก์ชันอาจแตกต่างกันในแต่ละ DBMS)

```sql
-- ตัวอย่างใน PostgreSQL
SELECT info->>'name' AS name, info->>'age' AS age
FROM users
WHERE (info->>'age')::int > 30;
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| name    | age |
|---------|-----|
| Alice   | 35  |
| John    | 45  |

## แบบฝึกหัดท้ายบท

### แบบฝึกหัด 1: Subqueries

เขียน query ที่ใช้ subquery เพื่อแสดงรายชื่อพนักงานที่มีเงินเดือนสูงกว่าค่าเฉลี่ยของแผนกของตัวเอง

```sql
SELECT employee_name
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department = e1.department);
```

### แบบฝึกหัด 2: Common Table Expressions (CTE)

สร้าง CTE ที่แสดงยอดขายรวมของแต่ละพนักงานในปีที่แล้ว และใช้ CTE นี้เพื่อหาพนักงานที่มียอดขายสูงสุด 5 อันดับแรก

```sql
WITH sales_last_year AS (
    SELECT employee_id, SUM(sales_amount) AS total_sales
    FROM sales
    WHERE sale_date BETWEEN '2023-01-01' AND '2023-12-31'
    GROUP BY employee_id
)
SELECT employee_id, total_sales
FROM sales_last_year
ORDER BY total_sales DESC
LIMIT 5;
```

### แบบฝึกหัด 3: Window Functions

ใช้ window function เพื่อแสดงเงินเดือนของพนักงาน, เงินเดือนเฉลี่ยของแผนก, และลำดับเงินเดือนของพนักงานในแผนกของตัวเอง

```sql
SELECT 
    employee_name,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS avg_dept_salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
FROM employees;
```

### แบบฝึกหัด 4: Recursive Queries

เขียน recursive query เพื่อแสดงโครงสร้างองค์กรแบบลำดับชั้น โดยเริ่มจาก CEO ลงไปถึงพนักงานระดับล่างสุด

```sql
WITH RECURSIVE org_chart AS (
    SELECT employee_id, manager_id, employee_name
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.manager_id, e.employee_name
    FROM employees e
    INNER JOIN org_chart o ON e.manager_id = o.employee_id
)
SELECT * FROM org_chart;
```

### แบบฝึกหัด 5: JSON Operations

สร้างตารางที่มีคอลัมน์ข้อมูล JSON และเขียน query เพื่อดึงข้อมูลจากคอลัมน์ JSON นั้น

```sql
-- สร้างตาราง
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    info JSON
);

-- เพิ่มข้อมูลตัวอย่าง
INSERT INTO users (user_id, info) VALUES 
(1, '{"name": "Alice", "age": 35, "city": "New York"}'),
(2, '{"name": "John", "age": 45, "city": "Los Angeles"}');

-- ดึงข้อมูลจากคอลัมน์ JSON
SELECT info->>'name' AS name, info->>'age' AS age
FROM users
WHERE (info->>'age')::int > 30;
```

**ผลลัพธ์ที่คาดว่าจะได้:**

| name  | age |
|-------|-----|
| Alice | 35  |
| John  | 45  |

## บทที่ 7: การรักษาความปลอดภัยฐานข้อมูล

7.1 **การจัดการผู้ใช้และสิทธิ์**

1. **การสร้างผู้ใช้ใหม่**

   a. การสร้างผู้ใช้พื้นฐาน:
   ```sql
   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
   ```

   b. การสร้างผู้ใช้ที่สามารถเข้าถึงจากทุก host:
   ```sql
   CREATE USER 'username'@'%' IDENTIFIED BY 'password';
   ```

   c. การสร้างผู้ใช้ด้วยการเข้ารหัสแบบ SHA-256:
   ```sql
   CREATE USER 'username'@'localhost' IDENTIFIED WITH sha256_password BY 'password';
   ```

2. **การกำหนดและเพิกถอนสิทธิ์**

   a. การให้สิทธิ์ทั้งหมดบนฐานข้อมูลเฉพาะ:
   ```sql
   GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
   ```

   b. การให้สิทธิ์เฉพาะบางอย่าง:
   ```sql
   GRANT SELECT, INSERT, UPDATE ON database_name.table_name TO 'username'@'localhost';
   ```

   c. การให้สิทธิ์ทั้งหมดบนทุกฐานข้อมูล (ระวังใช้):
   ```sql
   GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;
   ```

   d. การเพิกถอนสิทธิ์:
   ```sql
   REVOKE INSERT ON database_name.table_name FROM 'username'@'localhost';
   ```

   e. การเพิกถอนสิทธิ์ทั้งหมด:
   ```sql
   REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'username'@'localhost';
   ```

3. **การใช้ ROLES**

   a. การสร้าง Role:
   ```sql
   CREATE ROLE 'role_name';
   ```

   b. การให้สิทธิ์แก่ Role:
   ```sql
   GRANT SELECT, INSERT ON database_name.* TO 'role_name';
   ```

   c. การกำหนด Role ให้ผู้ใช้:
   ```sql
   GRANT 'role_name' TO 'username'@'localhost';
   ```

   d. การเปิดใช้งาน Role สำหรับ session ปัจจุบัน:
   ```sql
   SET ROLE 'role_name';
   ```

   e. การกำหนดให้ Role ทำงานอัตโนมัติเมื่อผู้ใช้เข้าสู่ระบบ:
   ```sql
   SET DEFAULT ROLE 'role_name' TO 'username'@'localhost';
   ```

   f. การเพิกถอน Role จากผู้ใช้:
   ```sql
   REVOKE 'role_name' FROM 'username'@'localhost';
   ```

4. **การตรวจสอบสิทธิ์**

   a. ตรวจสอบสิทธิ์ของผู้ใช้:
   ```sql
   SHOW GRANTS FOR 'username'@'localhost';
   ```

   b. ตรวจสอบสิทธิ์ของ Role:
   ```sql
   SHOW GRANTS FOR 'role_name';
   ```

5. **Best Practices**

   - ใช้หลักการ "least privilege" โดยให้สิทธิ์เฉพาะที่จำเป็น
   - ใช้ Roles เพื่อจัดการสิทธิ์เป็นกลุ่ม ทำให้ง่ายต่อการบริหารจัดการ
   - หลีกเลี่ยงการใช้ root account ในการทำงานประจำวัน
   - ทบทวนและตรวจสอบสิทธิ์ของผู้ใช้อย่างสม่ำเสมอ
   - ใช้รหัสผ่านที่ซับซ้อนและเปลี่ยนรหัสผ่านเป็นประจำ

6. **ตัวอย่างการใช้งานจริง**

   สมมติว่าเรามีแอปพลิเคชันที่ต้องการสิทธิ์ในการอ่านและเขียนข้อมูล แต่ไม่ต้องการให้ลบข้อมูล:

   ```sql
   CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'secure_password';
   CREATE ROLE 'app_read_write';
   GRANT SELECT, INSERT, UPDATE ON myapp_db.* TO 'app_read_write';
   GRANT 'app_read_write' TO 'app_user'@'localhost';
   SET DEFAULT ROLE 'app_read_write' TO 'app_user'@'localhost';
   ```

การจัดการผู้ใช้และสิทธิ์อย่างเหมาะสมเป็นพื้นฐานสำคัญของการรักษาความปลอดภัยฐานข้อมูล ช่วยป้องกันการเข้าถึงข้อมูลโดยไม่ได้รับอนุญาตและจำกัดความเสียหายที่อาจเกิดขึ้นจากการโจมตี

7.2 **การเข้ารหัสข้อมูล**

1. **การเข้ารหัสการเชื่อมต่อ (SSL/TLS)**

   a. การตั้งค่า SSL/TLS บน MySQL Server:
   ```sql
   -- ในไฟล์ my.cnf หรือ my.ini
   [mysqld]
   ssl-ca=/path/to/ca.pem
   ssl-cert=/path/to/server-cert.pem
   ssl-key=/path/to/server-key.pem
   ```

   b. การบังคับใช้ SSL สำหรับผู้ใช้:
   ```sql
   ALTER USER 'username'@'localhost' REQUIRE SSL;
   ```

   c. การเชื่อมต่อด้วย SSL จาก client:
   ```bash
   mysql --ssl-ca=/path/to/ca.pem --ssl-cert=/path/to/client-cert.pem --ssl-key=/path/to/client-key.pem
   ```

2. **การเข้ารหัสข้อมูลในฐานข้อมูล**

   a. การใช้ AES encryption:
   ```sql
   -- เข้ารหัส
   INSERT INTO secure_table (id, encrypted_data) 
   VALUES (1, AES_ENCRYPT('sensitive data', 'encryption_key'));

   -- ถอดรหัส
   SELECT id, AES_DECRYPT(encrypted_data, 'encryption_key') AS decrypted_data 
   FROM secure_table;
   ```

   b. การใช้ Transparent Data Encryption (TDE) (สำหรับ Enterprise Edition):
   ```sql
   -- เปิดใช้งาน TDE
   ALTER INSTANCE ROTATE INNODB MASTER KEY;
   
   -- สร้างตารางที่เข้ารหัส
   CREATE TABLE secure_table (
       id INT,
       sensitive_data VARCHAR(100)
   ) ENCRYPTION='Y';
   ```

7.3 **การสำรองและกู้คืนข้อมูล**

1. **วิธีการสำรองข้อมูล**

   a. การใช้ mysqldump:
   ```bash
   mysqldump -u username -p database_name > backup.sql
   ```

   b. การสำรองทั้งฐานข้อมูล:
   ```bash
   mysqldump -u username -p --all-databases > full_backup.sql
   ```

   c. การสำรองแบบ incremental ด้วย binary log:
   ```bash
   mysqlbinlog /path/to/binary/log > incremental_backup.sql
   ```

2. **การกู้คืนข้อมูล**

   a. การกู้คืนจากไฟล์ SQL:
   ```bash
   mysql -u username -p database_name < backup.sql
   ```

   b. การกู้คืนจาก binary log:
   ```bash
   mysqlbinlog /path/to/binary/log | mysql -u username -p database_name
   ```

3. **การวางแผนสำรองข้อมูล**

   a. กำหนดความถี่ในการสำรองข้อมูล:
   - Full backup: ทำสัปดาห์ละครั้ง
   - Incremental backup: ทำทุกวัน

   b. ใช้ cron job สำหรับการสำรองอัตโนมัติ:
   ```bash
   0 1 * * 0 /usr/bin/mysqldump -u username -p --all-databases > /backup/full_backup_$(date +\%Y\%m\%d).sql
   0 2 * * 1-6 /usr/bin/mysqlbinlog /var/lib/mysql/mysql-bin.* > /backup/incremental_$(date +\%Y\%m\%d).sql
   ```

   c. ทดสอบการกู้คืนข้อมูลเป็นประจำ:
   - สร้าง test environment
   - ทำการกู้คืนข้อมูลและตรวจสอบความถูกต้อง

   d. เก็บสำเนาข้อมูลสำรองไว้นอกสถานที่:
   - ใช้บริการ cloud storage
   - เก็บในสถานที่ปลอดภัยทางกายภาพ

   e. การเข้ารหัสข้อมูลสำรอง:
   ```bash
   mysqldump -u username -p database_name | gzip | openssl enc -aes-256-cbc -salt > encrypted_backup.sql.gz.enc
   ```

   f. การถอดรหัสและกู้คืนข้อมูล:
   ```bash
   openssl enc -d -aes-256-cbc -in encrypted_backup.sql.gz.enc | gunzip | mysql -u username -p database_name
   ```

สิ่งสำคัญในการรักษาความปลอดภัยฐานข้อมูลคือการใช้การเข้ารหัสที่แข็งแกร่งสำหรับทั้งการเชื่อมต่อและข้อมูลที่สำคัญ รวมถึงการมีแผนการสำรองและกู้คืนข้อมูลที่ครอบคลุมและทดสอบแล้ว การปฏิบัติตามแนวทางเหล่านี้จะช่วยป้องกันการรั่วไหลของข้อมูลและลดผลกระทบจากเหตุการณ์ที่ไม่คาดคิด เช่น การสูญหายของข้อมูลหรือการโจมตีทางไซเบอร์

7.4 **การตรวจสอบและบันทึกกิจกรรม**

1. **การเปิดใช้งาน Audit Logging**
   
   a. เปิดใช้งาน general query log:
   ```sql
   SET GLOBAL general_log = 'ON';
   SET GLOBAL general_log_file = '/path/to/mysql-general.log';
   ```

   b. เปิดใช้งาน slow query log:
   ```sql
   SET GLOBAL slow_query_log = 'ON';
   SET GLOBAL slow_query_log_file = '/path/to/mysql-slow.log';
   SET GLOBAL long_query_time = 2;
   ```

   c. การใช้ MySQL Enterprise Audit (สำหรับ Enterprise Edition):
   ```sql
   INSTALL PLUGIN audit_log SONAME 'audit_log.so';
   SET GLOBAL audit_log_policy = 'ALL';
   ```

2. **การวิเคราะห์ Log Files**
   
   - ใช้เครื่องมือเช่น `mysqlbinlog` หรือ `pt-query-digest` เพื่อวิเคราะห์ log files
   - ตรวจสอบ pattern ของ queries ที่ทำงานช้าหรือมีการเรียกใช้บ่อย
   - ใช้ระบบ SIEM (Security Information and Event Management) เพื่อวิเคราะห์ log แบบ real-time

7.5 **การป้องกัน SQL Injection**

1. **ความเสี่ยงของ SQL Injection**
   - แสดงตัวอย่างของ SQL Injection:
     ```sql
     -- ไม่ปลอดภัย
     $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
     ```

2. **วิธีการป้องกัน SQL Injection**
   
   a. ใช้ Prepared Statements:
   ```php
   $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
   $stmt->execute([$username, $password]);
   ```

   b. ใช้ Stored Procedures:
   ```sql
   DELIMITER //
   CREATE PROCEDURE getUserByCredentials(IN p_username VARCHAR(50), IN p_password VARCHAR(255))
   BEGIN
       SELECT * FROM users WHERE username = p_username AND password = p_password;
   END //
   DELIMITER ;
   ```

   c. การ Escape ข้อมูลที่รับเข้ามา:
   ```php
   $username = mysqli_real_escape_string($conn, $username);
   ```

7.6 **การจำกัดการเข้าถึงเครือข่าย**

1. **การตั้งค่า Firewall**
   
   a. ใช้ iptables บน Linux:
   ```bash
   iptables -A INPUT -p tcp --dport 3306 -s allowed_ip_address -j ACCEPT
   iptables -A INPUT -p tcp --dport 3306 -j DROP
   ```

   b. ตั้งค่า MySQL ให้รับการเชื่อมต่อเฉพาะจาก localhost:
   ```sql
   -- ใน my.cnf หรือ my.ini
   bind-address = 127.0.0.1
   ```

2. **การใช้ VPN สำหรับการเข้าถึงระยะไกล**
   
   - ตั้งค่า OpenVPN server
   - ให้ผู้ใช้เชื่อมต่อผ่าน VPN ก่อนที่จะสามารถเข้าถึง MySQL server

7.7 **การอัปเดตและแพทช์ความปลอดภัย**

1. **ความสำคัญของการอัปเดต**
   - อธิบายถึงความเสี่ยงของการใช้ซอฟต์แวร์เวอร์ชันเก่า
   - แนะนำให้ติดตามประกาศความปลอดภัยจาก MySQL อย่างสม่ำเสมอ

2. **วิธีการอัปเดตอย่างปลอดภัย**
   
   a. ทำการสำรองข้อมูลก่อนอัปเดต:
   ```bash
   mysqldump -u root -p --all-databases > backup_before_update.sql
   ```

   b. ตรวจสอบความเข้ากันได้ของแอปพลิเคชันกับเวอร์ชันใหม่

   c. อัปเดต MySQL:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade mysql-server
   ```

   d. ทดสอบการทำงานหลังอัปเดต
   
   e. มีแผนรองรับกรณีที่การอัปเดตมีปัญหา (rollback plan)

แบบฝึกหัดท้ายบท:

1. สร้างแผนการสำรองและกู้คืนข้อมูลสำหรับฐานข้อมูลที่มีขนาด 100GB โดยคำนึงถึงการทำงานแบบ 24/7

2. อธิบายวิธีการตรวจสอบและป้องกัน SQL Injection ในแอปพลิเคชัน PHP ที่เชื่อมต่อกับ MySQL

3. ออกแบบนโยบายการจัดการผู้ใช้และสิทธิ์สำหรับระบบ e-commerce ที่มีผู้ใช้หลายระดับ (เช่น admin, customer service, regular users)

4. เขียนสคริปต์ bash เพื่อทำการสำรองข้อมูล, เข้ารหัสไฟล์สำรอง, และอัปโหลดไปยัง cloud storage โดยอัตโนมัติ

5. อธิบายขั้นตอนการตั้งค่า SSL/TLS สำหรับการเชื่อมต่อ MySQL และวิธีการทดสอบว่าการเชื่อมต่อใช้การเข้ารหัสอย่างถูกต้อง

บทนี้ครอบคลุมหัวข้อสำคัญในการรักษาความปลอดภัยฐานข้อมูล MySQL ซึ่งเป็นทักษะที่จำเป็นสำหรับผู้ดูแลระบบและนักพัฒนาที่ทำงานกับฐานข้อมูล