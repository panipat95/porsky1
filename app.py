import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ All-in-One Executive Ecosystem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Pristine High-Contrast Sky-Blue & White Design System
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, sans-serif !important;
        background-color: #F0F9FF !important; /* Sky 50 */
        color: #0F172A !important;
    }
    
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    /* Clean Modern Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0369A1 !important;
        border-right: 1px solid #0284C7;
    }

    /* Clean Brand Header Card */
    .brand-box {
        background: #0284C7;
        border: 1px solid #38BDF8;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .brand-avatar {
        width: 46px;
        height: 46px;
        border-radius: 12px;
        background: #FFFFFF;
        color: #0284C7;
        font-weight: 800;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }

    .brand-name {
        font-size: 18px;
        font-weight: 800;
        color: #FFFFFF !important;
        line-height: 1.2;
    }

    .brand-sub {
        font-size: 12px;
        color: #E0F2FE !important;
        font-weight: 500;
    }

    .brand-status {
        display: inline-block;
        background: #059669;
        color: #FFFFFF !important;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 12px;
        margin-top: 6px;
    }

    /* Top Live Notification Bar */
    .notif-bar {
        background: #FFFFFF;
        border: 1px solid #E0F2FE;
        border-left: 5px solid #0284C7;
        border-radius: 14px;
        padding: 14px 20px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.05);
    }

    .notif-title {
        font-weight: 700;
        color: #0369A1;
        font-size: 14px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .notif-badge {
        background: #FEF3C7;
        color: #D97706;
        font-weight: 700;
        font-size: 12px;
        padding: 4px 12px;
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
worksheets = get_all_worksheets()
affiliates = get_all_affiliate_products()

# Top Live Notification Hub Bar
st.markdown(f"""
<div class="notif-bar">
    <div class="notif-title">
        🔔 <b>ศูนย์แจ้งเตือนด่วน (Live Notification Hub):</b> 
        <span style="color:#334155; font-weight:400;">
            ระบบทำงานปกติ 🟢 | เพจ Facebook: <b>ห้องเรียนอารมณ์ดี (LIVE)</b>
        </span>
    </div>
    <div>
        <span class="notif-badge">⏳ คอนเทนต์รอกรอง: {len(pending_posts)} รายการ</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Brand Header Box in Sidebar
st.sidebar.markdown("""
<div class="brand-box">
    <div style="display:flex; align-items:center; gap:12px;">
        <div class="brand-avatar">KP</div>
        <div>
            <div class="brand-name">ครูปอ Ecosystem</div>
            <div class="brand-sub">Executive Content Studio</div>
            <div class="brand-status">🟢 LIVE: ห้องเรียนอารมณ์ดี</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p style='font-size:12px; font-weight:700; color:#E0F2FE !important; letter-spacing:1px; margin-bottom:8px;'>NAVIGATION MENU</p>", unsafe_allow_html=True)

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
st.sidebar.caption("ครูปอ All-in-One Executive Studio v2.0")

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
