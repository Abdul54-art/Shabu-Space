from cryptography.fernet import Fernet
import webbrowser
import os

def run_my_app():
    # ให้คนจ้างกรอก Key ที่คุณส่งให้ทางแชท
    user_key = input("กรุณาใส่ Key เพื่อเข้าถึงงาน: ").strip().encode()
    
    try:
        with open('chabu_locked.bin', 'rb') as f:
            encrypted_data = f.read()
        
        fernet = Fernet(user_key)
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # สร้างหน้าเว็บชั่วคราวเพื่อโชว์งาน
        with open('demo.html', 'wb') as f:
            f.write(decrypted_data)
        
        print("✅ ปลดล็อคสำเร็จ! กำลังเปิดหน้าเว็บ...")
        webbrowser.open('file://' + os.path.realpath('demo.html'))
        
    except:
        print("❌ Key ไม่ถูกต้อง! ไม่สามารถดูโค้ดได้")

if __name__ == "__main__":
    run_my_app()