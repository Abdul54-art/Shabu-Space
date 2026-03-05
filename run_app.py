from cryptography.fernet import Fernet
import webbrowser
import os
import time

def run_secured_app():
    print("--- 🍲 Shabu Space Booking System (Secured) ---")
    # 1. รับ Key จากผู้ใช้ (คนจ้าง)
    user_key = input("🔑 กรุณาใส่ Key เพื่อเข้าถึงงาน: ").strip().encode()
    
    try:
        # 2. อ่านไฟล์ที่ถูกล็อคไว้
        with open('chabu_locked.bin', 'rb') as f:
            encrypted_data = f.read()
        
        # 3. ใช้ Key ถอดรหัส
        fernet = Fernet(user_key)
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # 4. สร้างหน้าเว็บชั่วคราวเพื่อแสดงผล
        temp_file = "view_demo.html"
        with open(temp_file, 'wb') as f:
            f.write(decrypted_data)
        
        print("✅ ปลดล็อคสำเร็จ! กำลังเปิดหน้าเว็บใน Browser...")
        webbrowser.open('file://' + os.path.realpath(temp_file))
        
        # รอสักพักแล้วลบไฟล์ทิ้งเพื่อความปลอดภัย (ไม่ให้คนจ้างก๊อปไฟล์ HTML ไปได้ง่ายๆ)
        time.sleep(5) 
        # os.remove(temp_file) # เอาเครื่องหมาย # ออกถ้าต้องการให้ลบไฟล์ทันทีหลังเปิด
        
    except Exception as e:
        print("❌ Key ไม่ถูกต้อง! ไม่สามารถเข้าถึงซอร์สโค้ดได้")

if __name__ == "__main__":
    run_secured_app()