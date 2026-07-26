import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ All-in-One Executive Ecosystem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2026 Silicon Valley Next-Gen Executive Design System (Ultra-High Contrast & Crisp Typography)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,700&display=swap');
    
    /* Global Base & Ultra-Crisp Typography */
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        background-color: #F8FAFC !important; /* Pure Slate 50 */
        color: #0F172A !important; /* Deep Slate 900 */
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
    }
    
    .main .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1440px;
    }

    /* Next-Gen Deep Slate Indigo Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%) !important;
        border-right: 1px solid #334155 !important;
        box-shadow: 4px 0 30px rgba(15, 23, 42, 0.15);
    }
    
    section[data-testid="stSidebar"] * {
        font-family: 'Prompt', sans-serif !important;
    }

    /* Brand Header Box in Sidebar */
    .brand-card-2026 {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 22px;
        backdrop-filter: blur(12px);
        display: flex;
        align-items: center;
        gap: 14px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
    }
    
    .brand-avatar-2026 {
        width: 50px;
        height: 50px;
        border-radius: 14px;
        background: linear-gradient(135deg, #2563EB 0%, #0284C7 100%);
        color: #FFFFFF;
        font-weight: 800;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }

    .brand-title-2026 {
        font-size: 19px;
        font-weight: 800;
        color: #FFFFFF !important;
        line-height: 1.2;
        letter-spacing: -0.3px;
    }

    .brand-subtitle-2026 {
        font-size: 13px;
        color: #94A3B8 !important;
        font-weight: 500;
    }

    .brand-status-2026 {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.2);
        border: 1px solid rgba(52, 211, 153, 0.5);
        color: #34D399 !important;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 12px;
        border-radius: 20px;
        margin-top: 6px;
    }

    /* Sidebar Radio Buttons Styling */
    section[data-testid="stSidebar"] .stRadio label {
        color: #F1F5F9 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
        border-radius: 12px !important;
        transition: all 0.2s ease !important;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        color: #38BDF8 !important;
    }

    /* Top Live Notification Bar */
    .notif-hub-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 6px solid #2563EB;
        border-radius: 16px;
        padding: 18px 24px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 10px 30px -10px rgba(37, 99, 235, 0.08);
    }

    .notif-text {
        font-size: 15px;
        font-weight: 700;
        color: #0F172A;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .notif-tag {
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

# Top Live Notification Hub Bar (2026 Executive Style)
st.markdown(f"""
<div class="notif-hub-card">
    <div class="notif-text">
        <span style="font-size:20px;">🔔</span>
        <span><b>ศูนย์แจ้งเตือนด่วน (Live Notification Center):</b></span>
        <span style="color:#475569; font-weight:500;">
            ระบบเชื่อมต่อปกติ 🟢 | เพจ Facebook: <b>ห้องเรียนอารมณ์ดี (LIVE)</b>
        </span>
    </div>
    <div>
        <span class="notif-tag">⏳ คอนเทนต์รอกรองอนุมัติ: {len(pending_posts)} รายการ</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Brand Header Box in Sidebar
st.sidebar.markdown("""
<div class="brand-card-2026">
    <div class="brand-avatar-2026">KP</div>
    <div>
        <div class="brand-title-2026">ครูปอ Ecosystem</div>
        <div class="brand-subtitle-2026">Executive Content Studio</div>
        <div class="brand-status-2026">
            <span style="width:7px; height:7px; border-radius:50%; background:#34D399; display:inline-block;"></span>
            LIVE: ห้องเรียนอารมณ์ดี
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p style='font-size:12px; font-weight:800; color:#64748B !important; letter-spacing:1.5px; margin-bottom:10px; margin-left:4px;'>NAVIGATION MENU</p>", unsafe_allow_html=True)

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
st.sidebar.caption("ครูปอ All-in-One Next-Gen Ecosystem v2.5")

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
