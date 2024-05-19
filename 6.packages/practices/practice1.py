# เขียนโปรแกรมที่รับวันที่จากผู้ใช้ในรูปแบบ "YYYY-MM-DD" และแสดงผลลัพธ์เป็นชื่อวันในสัปดาห์ เช่น "Monday", "Tuesday", ฯลฯ(ใช้ datetime)
from datetime import date

user_input = input("Enter date (YYYY-MM-DD): ")

date_input = date.fromisoformat(user_input)

print("วันที่ user input เข้ามาตรงกับ ", date_input.strftime('%A'))
