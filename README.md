# 🎓 ครูปอ All-in-One Ecosystem (System Architecture & WebApp)

ระบบนิเวศรวมศูนย์ (All-in-One Ecosystem) สำหรับครูปอ เพื่อรวมระบบดูแลช่วยเหลือนักเรียน ม.1, ระบบสร้างสื่อการสอนขาย TPT, ระบบหารายได้เสริม Shopee Affiliate & สคริปต์ VDO และระบบคุมเพจ Facebook Page Manager ไว้ในแอปพลิเคชันเดียว

---

## 📁 โครงสร้างโปรเจกต์ (Directory Structure)

```
d:/porsky1/
├── .env.example                # ตัวอย่างไฟล์ตั้งค่า Token & API Keys
├── requirements.txt            # รายชื่อ Python Packages ที่ต้องใช้
├── README.md                   # คู่มือเริ่มต้นใช้งานโปรเจกต์
├── app.py                      # Main Entrypoint ของ Streamlit WebApp
├── database.db                 # SQLite Database (สร้างให้อัตโนมัติเมื่อรัน)
├── models/
│   └── database.py             # SQLite Data Models & CRUD Functions
├── modules/
│   ├── student_care_tpt.py     # โมดูล 1: ดูแลช่วยเหลือนักเรียน ม.1 + AI สร้างใบงาน TPT
│   ├── shopee_affiliate.py     # โมดูล 2: สคริปต์ Shopee VDO + แคปชั่น + Affiliate Link
│   └── fb_page_manager.py      # โมดูล 3: Dashboard คุมเพจสำหรับ CEO ครูปอ (Approve & Post)
└── utils/
    ├── ai_agent.py             # AI Helper (สร้างใบงาน สคริปต์ และแคปชั่น)
    ├── facebook_api.py          # Facebook Graph API Client (รองรับ Auto-post)
    └── pdf_generator.py        # Helper แปลงใบงานเป็น PDF (พร้อมแจก/ขาย)
```

---

## ⚡ วิธีการติดตั้งและเริ่มต้นใช้งาน (Installation & Setup)

1. **เปิด Terminal / Command Prompt** เข้าไปยังโฟลเดอร์โปรเจกต์:
   ```bash
   cd d:\porsky1
   ```

2. **ติดตั้ง Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **เริ่มต้นรัน WebApp**:
   ```bash
   streamlit run app.py
   ```

4. **เข้าใช้งาน WebApp**:
   เปิด Web Browser แล้วไปที่ `http://localhost:8501`

---

## 🔑 การตั้งค่า Facebook Graph API สำหรับ Auto-Posting (อนาคต)

1. คัดลอกไฟล์ `.env.example` เป็น `.env`:
   ```bash
   cp .env.example .env
   ```
2. กรอก `FB_PAGE_ID` และ `FB_PAGE_ACCESS_TOKEN` ที่ได้จาก Meta Developer Dashboard
3. เมื่อกรอกแล้ว ระบบใน **โมดูล 3 (Facebook Page Manager)** จะยิงโพสต์ขึ้น Facebook Page จริงให้อัตโนมัติทันทีที่กดปุ่ม **"🚀 อนุมัติ & ยิงโพสต์ขึ้น Facebook"** (หากยังไม่ใส่ Token ระบบจะทำงานในโหมด Simulative Mock เพื่อให้ทดลองเล่นได้ปลอดภัย)
