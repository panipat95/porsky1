import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ All-in-One Executive Ecosystem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 ธีมฟ้า-ขาว สว่าง สดใส (Ultra-Bright Sky-Blue & Crisp White Theme)
# แก้ไขปัญหาตัวอักษรกลืนกับพื้นหลัง 100% ด้วยสีสดใส คอนทราสต์สูง อ่านง่ายที่สุด
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700;800&display=swap');
    
    /* Global Base */
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, sans-serif !important;
        background-color: #F0F9FF !important; /* Sky 50 สว่าง สดใส */
        color: #0F172A !important;
    }
    
    .main .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1440px;
    }

    /* สว่าง คมชัด: Sidebar โทนฟ้าสดใส */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0284C7 0%, #0369A1 100%) !important;
        border-right: 2px solid #0284C7 !important;
        box-shadow: 4px 0 20px rgba(2, 132, 199, 0.15) !important;
    }
    
    /* บังคับสีตัวอักษรทุกตัวใน Sidebar เป็นสีขาวสว่าง 100% คมชัด */
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
        font-family: 'Prompt', sans-serif !important;
        opacity: 1 !important;
    }

    /* Brand Header Box ด้านซ้าย (การ์ดสีขาวบริสุทธิ์ คอนทราสต์สูงสุด) */
    .brand-card-bright {
        background: #FFFFFF !important;
        border: 2px solid #E0F2FE !important;
        border-radius: 18px !important;
        padding: 18px !important;
        margin-bottom: 20px !important;
        display: flex !important;
        align-items: center !important;
        gap: 14px !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15) !important;
    }
    
    .brand-card-bright * {
        color: #0F172A !important;
    }

    .brand-avatar-bright {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }

    .brand-title-bright {
        font-size: 18px;
        font-weight: 800;
        color: #0369A1 !important;
        line-height: 1.2;
    }

    .brand-subtitle-bright {
        font-size: 12px;
        color: #64748B !important;
        font-weight: 600;
    }

    .brand-status-bright {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #D1FAE5 !important;
        border: 1px solid #A7F3D0 !important;
        color: #047857 !important;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 16px;
        margin-top: 4px;
    }

    /* ปรับแต่ง ปุ่มเมนู Radio Buttons ให้สว่าง ตัวอักษรใหญ่ คมกริบ */
    section[data-testid="stSidebar"] .stRadio label {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 14px !important;
        padding: 12px 18px !important;
        margin-bottom: 6px !important;
        cursor: pointer !important;
    }

    section[data-testid="stSidebar"] .stRadio label p,
    section[data-testid="stSidebar"] .stRadio label span {
        color: #FFFFFF !important;
        font-size: 15px !important;
        font-weight: 700 !important;
    }

    /* เมนูที่ถูกเลือก (Active Card): การ์ดสีขาวบริสุทธิ์ ตัวอักษรสีฟ้าเข้ม อ่านง่าย 100% */
    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label {
        background: #FFFFFF !important;
        border-color: #FFFFFF !important;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2) !important;
    }

    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label p,
    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label span {
        color: #0284C7 !important;
        font-weight: 800 !important;
    }

    /* Top Live Notification Bar */
    .notif-bar-bright {
        background: #FFFFFF;
        border: 1px solid #E0F2FE;
        border-left: 6px solid #0284C7;
        border-radius: 16px;
        padding: 16px 24px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 6px 20px rgba(2, 132, 199, 0.06);
    }

    .notif-text-bright {
        font-size: 15px;
        font-weight: 700;
        color: #0F172A;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .notif-tag-bright {
        background: #FEF3C7;
        border: 1px solid #FDE68A;
        color: #B45309;
        font-weight: 800;
        font-size: 13px;
        padding: 6px 16px;
        border-radius: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Import Database & Modules
from models.database import init_db, get_fb_posts, get_all_worksheets, get_all_affiliate_products
from modules.pixel_office import render_pixel_office_module
from modules.analytics_dashboard import render_analytics_dashboard_module
from modules.student_care_tpt import render_student_care_tpt_module
from modules.shopee_affiliate import render_shopee_affiliate_module
from modules.fb_page_manager import render_fb_page_manager_module
from modules.fb_page_status import render_fb_page_status_module

# Initialize Database Schema
init_db()

# Fetch live notifications data
fb_posts = get_fb_posts()
pending_posts = [p for p in fb_posts if p['status'] == 'pending_approval']

# Top Live Notification Hub Bar (Bright Executive Style)
st.markdown(f"""
<div class="notif-bar-bright">
    <div class="notif-text-bright">
        <span style="font-size:20px;">🔔</span>
        <span><b>ศูนย์แจ้งเตือนด่วน (Live Notification Center):</b></span>
        <span style="color:#475569; font-weight:500;">
            ระบบเชื่อมต่อปกติ 🟢 | เพจ Facebook: <b>ห้องเรียนอารมณ์ดี (LIVE)</b>
        </span>
    </div>
    <div>
        <span class="notif-tag-bright">⏳ คอนเทนต์รอกรองอนุมัติ: {len(pending_posts)} รายการ</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Brand Header Box in Sidebar (White Card with Ocean Blue Text)
st.sidebar.markdown("""
<div class="brand-card-bright">
    <div class="brand-avatar-bright">KP</div>
    <div>
        <div class="brand-title-bright">ครูปอ Ecosystem</div>
        <div class="brand-subtitle-bright">Executive Content Studio</div>
        <div class="brand-status-bright">
            🟢 LIVE: ห้องเรียนอารมณ์ดี
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p style='font-size:12px; font-weight:800; color:#E0F2FE !important; letter-spacing:1.5px; margin-bottom:10px; margin-left:4px;'>NAVIGATION MENU</p>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "เลือกเมนูการทำงาน:",
    [
        "📊 หน้าหลัก & บทวิเคราะห์ธุรกิจ",
        "🎮 สำนักงานเสมือน Pixel AI Studio",
        "🎓 1. ผลิตสื่อ ม.1 & ใบงาน TPT",
        "🎬🛒 2. FB Reels & Shopee Affiliate",
        "🎛️ 3. ศูนย์คุมเพจ (FB Page Manager)",
        "📘 4. สถานะ & สถิติเพจ Facebook"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.caption("ครูปอ All-in-One Bright Sky Edition v3.0")

# Route to selected module
if menu == "📊 หน้าหลัก & บทวิเคราะห์ธุรกิจ":
    render_analytics_dashboard_module()

elif menu == "🎮 สำนักงานเสมือน Pixel AI Studio":
    render_pixel_office_module()

elif menu == "🎓 1. ผลิตสื่อ ม.1 & ใบงาน TPT":
    render_student_care_tpt_module()

elif menu == "🎬🛒 2. FB Reels & Shopee Affiliate":
    render_shopee_affiliate_module()

elif menu == "🎛️ 3. ศูนย์คุมเพจ (FB Page Manager)":
    render_fb_page_manager_module()

elif menu == "📘 4. สถานะ & สถิติเพจ Facebook":
    render_fb_page_status_module()
