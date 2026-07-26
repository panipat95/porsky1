import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ All-in-One Pastel Executive Ecosystem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Pastel Luxury & Interactive Effects System (ui-ux-pro-max compliant)
# ธีมพาสเทล หรูหรา สดใส สบายตา คอนทราสต์สูง อ่านง่าย 100%
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Base */
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, sans-serif !important;
        background: linear-gradient(135deg, #F8FAFC 0%, #EEF2FF 50%, #F0FDF4 100%) !important;
        color: #1E1B4B !important;
        -webkit-font-smoothing: antialiased !important;
    }
    
    .main .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1440px;
    }

    /* 🎨 Pastel Luxury Sidebar (โทนพาสเทล สดใส หรูหรา) */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F3E8FF 0%, #E0F2FE 50%, #F0FDF4 100%) !important;
        border-right: 2px solid #E0E7FF !important;
        box-shadow: 4px 0 25px rgba(139, 92, 246, 0.08) !important;
    }
    
    /* สีตัวอักษรตั้งต้นใน Sidebar */
    section[data-testid="stSidebar"] * {
        color: #4C1D95 !important;
        font-family: 'Prompt', sans-serif !important;
    }

    /* Brand Header Box ด้านซ้าย (การ์ดพาสเทลสีขาวบริสุทธิ์) */
    .brand-card-pastel {
        background: #FFFFFF !important;
        border: 2px solid #DDD6FE !important;
        border-radius: 20px !important;
        padding: 18px !important;
        margin-bottom: 22px !important;
        display: flex !important;
        align-items: center !important;
        gap: 14px !important;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.12) !important;
    }

    .brand-avatar-pastel {
        width: 50px;
        height: 50px;
        border-radius: 16px;
        background: linear-gradient(135deg, #8B5CF6 0%, #38BDF8 100%);
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
    }

    .brand-title-pastel {
        font-size: 18px;
        font-weight: 800;
        color: #5B21B6 !important;
        line-height: 1.2;
    }

    .brand-subtitle-pastel {
        font-size: 12px;
        color: #6D28D9 !important;
        font-weight: 600;
    }

    .brand-status-pastel {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #D1FAE5 !important;
        border: 1px solid #A7F3D0 !important;
        color: #047857 !important;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 12px;
        border-radius: 16px;
        margin-top: 4px;
    }

    /* ปุ่มเมนู Radio Buttons ใน Sidebar (สไตล์พาสเทลลอยตัว) */
    section[data-testid="stSidebar"] .stRadio label {
        background: rgba(255, 255, 255, 0.7) !important;
        border: 1.5px solid #DDD6FE !important;
        border-radius: 14px !important;
        padding: 12px 18px !important;
        margin-bottom: 6px !important;
        transition: all 0.25s ease !important;
        cursor: pointer !important;
    }

    section[data-testid="stSidebar"] .stRadio label p,
    section[data-testid="stSidebar"] .stRadio label span {
        color: #4C1D95 !important;
        font-size: 15px !important;
        font-weight: 700 !important;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: #FFFFFF !important;
        border-color: #A78BFA !important;
        transform: translateX(4px);
    }

    /* เมนูที่ถูกเลือก (Active Card): Gradient พาสเทลสีม่วงสด ตัวอักษรสีขาวสว่าง คอนทราสต์ 100% */
    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label {
        background: linear-gradient(135deg, #7C3AED 0%, #2563EB 100%) !important;
        border-color: #A78BFA !important;
        box-shadow: 0 8px 20px rgba(124, 58, 237, 0.35) !important;
    }

    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label p,
    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label span {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    /* Top Live Notification Hub Bar (Pastel Card) */
    .notif-bar-pastel {
        background: #FFFFFF;
        border: 2px solid #E0E7FF;
        border-left: 6px solid #8B5CF6;
        border-radius: 18px;
        padding: 16px 24px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.06);
    }

    .notif-text-pastel {
        font-size: 15px;
        font-weight: 700;
        color: #4C1D95;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .notif-tag-pastel {
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

# Top Live Notification Hub Bar (Pastel Luxury Style)
st.markdown(f"""
<div class="notif-bar-pastel">
    <div class="notif-text-pastel">
        <span style="font-size:20px;">🔔</span>
        <span><b>ศูนย์แจ้งเตือนด่วน (Live Notification Center):</b></span>
        <span style="color:#475569; font-weight:500;">
            ระบบเชื่อมต่อปกติ 🟢 | เพเพจ Facebook: <b>ห้องเรียนอารมณ์ดี (LIVE)</b>
        </span>
    </div>
    <div>
        <span class="notif-tag-pastel">⏳ คอนเทนต์รอกรองอนุมัติ: {len(pending_posts)} รายการ</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Brand Header Box in Sidebar (Pastel White Card)
st.sidebar.markdown("""
<div class="brand-card-pastel">
    <div class="brand-avatar-pastel">KP</div>
    <div>
        <div class="brand-title-pastel">ครูปอ Ecosystem</div>
        <div class="brand-subtitle-pastel">Executive Content Studio</div>
        <div class="brand-status-pastel">
            🟢 LIVE: ห้องเรียนอารมณ์ดี
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p style='font-size:12px; font-weight:800; color:#6D28D9 !important; letter-spacing:1.5px; margin-bottom:10px; margin-left:4px;'>NAVIGATION MENU</p>", unsafe_allow_html=True)

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
st.sidebar.caption("ครูปอ All-in-One Pastel Luxury Edition v4.0")

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
