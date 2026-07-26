import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """สร้างตารางในฐานข้อมูล SQLite ถ้ายังไม่มี"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. ตารางดูแลช่วยเหลือนักเรียน ม.1
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_code TEXT NOT NULL,
        full_name TEXT NOT NULL,
        classroom TEXT DEFAULT 'ม.1/1',
        gpa REAL DEFAULT 0.0,
        behavior_notes TEXT,
        assistance_needed TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. ตารางใบงาน/สื่อการสอน TPT
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS worksheets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        subject TEXT NOT NULL,
        grade_level TEXT DEFAULT 'ม.1',
        content_markdown TEXT,
        file_path TEXT,
        price REAL DEFAULT 0.0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. ตารางสินค้า Shopee Affiliate & สคริปต์ VDO
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS affiliate_products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        category TEXT,
        affiliate_url TEXT NOT NULL,
        vdo_script TEXT,
        caption TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 4. ตารางคิวโพสต์ Facebook Page (สำหรับ CEO ครูปอ ตรวจสอบและ Approve)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fb_posts_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_type TEXT NOT NULL, -- 'tpt_worksheet' หรือ 'shopee_affiliate'
        source_id INTEGER,
        title TEXT NOT NULL,
        content_formatted TEXT NOT NULL,
        media_url TEXT,
        status TEXT DEFAULT 'pending_approval', -- 'pending_approval', 'approved', 'posted', 'rejected'
        scheduled_at DATETIME,
        fb_post_id TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    conn.commit()
    conn.close()

# CRUD Functions for Students
def add_student(student_code, full_name, classroom, gpa, behavior_notes, assistance_needed):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (student_code, full_name, classroom, gpa, behavior_notes, assistance_needed)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (student_code, full_name, classroom, gpa, behavior_notes, assistance_needed))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return student_id

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# CRUD Functions for Worksheets
def add_worksheet(title, subject, grade_level, content_markdown, price=0.0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO worksheets (title, subject, grade_level, content_markdown, price)
        VALUES (?, ?, ?, ?, ?)
    """, (title, subject, grade_level, content_markdown, price))
    conn.commit()
    worksheet_id = cursor.lastrowid
    conn.close()
    return worksheet_id

def get_all_worksheets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM worksheets ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# CRUD Functions for Shopee Affiliate
def add_affiliate_product(product_name, category, affiliate_url, vdo_script, caption):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO affiliate_products (product_name, category, affiliate_url, vdo_script, caption)
        VALUES (?, ?, ?, ?, ?)
    """, (product_name, category, affiliate_url, vdo_script, caption))
    conn.commit()
    prod_id = cursor.lastrowid
    conn.close()
    return prod_id

def get_all_affiliate_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM affiliate_products ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# CRUD Functions for FB Posts Queue
def enqueue_fb_post(source_type, source_id, title, content_formatted, media_url=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO fb_posts_queue (source_type, source_id, title, content_formatted, media_url, status)
        VALUES (?, ?, ?, ?, ?, 'pending_approval')
    """, (source_type, source_id, title, content_formatted, media_url))
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
    return post_id

def get_fb_posts(status_filter=None):
    conn = get_connection()
    cursor = conn.cursor()
    if status_filter:
        cursor.execute("SELECT * FROM fb_posts_queue WHERE status = ? ORDER BY id DESC", (status_filter,))
    else:
        cursor.execute("SELECT * FROM fb_posts_queue ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def update_fb_post_status(post_id, status, fb_post_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    if fb_post_id:
        cursor.execute("UPDATE fb_posts_queue SET status = ?, fb_post_id = ? WHERE id = ?", (status, fb_post_id, post_id))
    else:
        cursor.execute("UPDATE fb_posts_queue SET status = ? WHERE id = ?", (status, post_id))
    conn.commit()
    conn.close()

def update_fb_post_content(post_id, new_content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE fb_posts_queue SET content_formatted = ? WHERE id = ?", (new_content, post_id))
    conn.commit()
    conn.close()
