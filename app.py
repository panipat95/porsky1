import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ All-in-One Ecosystem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Ultra-Modern UI Design System (Custom CSS Injection)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');
    
    /* Global Base */
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, sans-serif !important;
        background-color: #F8FAFC;
    }
    
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    /* Ultra-Modern Custom Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%) !important;
        border-right: 1px solid #334155;
    }
    
    section[data-testid="stSidebar"] * {
        color: #F8FAFC !important;
        font-family: 'Prompt', sans-serif !important;
    }

    /* Brand Header Box in Sidebar */
    .sidebar-brand-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .brand-avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: #FFFFFF;
        font-weight: 700;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.5);
    }

    .brand-title {
        font-size: 17px;
        font-weight: 700;
        color: #FFFFFF !important;
        line-height: 1.2;
    }

    .brand-subtitle {
        font-size: 12px;
        color: #94A3B8 !important;
    }

    .live-status-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(5, 150, 105, 0.2);
        border: 1px solid rgba(16, 185, 129, 0.4);
        color: #34D399 !important;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        margin-top: 6px;
    }

    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background-color: #34D399;
        box-shadow: 0 0 8px #34D399;
    }

    /* Custom Radio Buttons in Sidebar */
    section[data-testid="stSidebar"] .stRadio > div {
        gap: 8px;
    }

    section[data-testid="stSidebar"] .stRadio label {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease-in-out !important;
        cursor: pointer;
        font-weight: 500 !important;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255, 255, 255, 0.08) !important;
        border-color: #3B82F6 !important;
        transform: translateX(4px);
    }

    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label {
        background: linear-gradient(135deg, #1E40AF 0%, #2563EB 100%) !important;
        border-color: #60A5FA !important;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4) !important;
    }

    /* Dividers */
    hr {
        border-color: #E2E8F0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Import Database & Modules
from models.database import init_db
from modules.analytics_dashboard import render_analytics_dashboard_module
from modules.student_care_tpt import render_student_care_tpt_module
from modules.shopee_affiliate import render_shopee_affiliate_module
from modules.fb_page_manager import render_fb_page_manager_module
from modules.fb_page_status import render_fb_page_status_module

# Initialize Database Schema
init_db()

# Custom Brand Card Header in Sidebar
st.sidebar.markdown("""
<div class="sidebar-brand-card">
    <div class="brand-avatar">KP</div>
    <div>
        <div class="brand-title">ครูปอ Ecosystem</div>
        <div class="brand-subtitle">CEO Content Studio</div>
        <div class="live-status-pill">
            <span class="status-dot"></span> LIVE: ห้องเรียนอารมณ์ดี
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p style='font-size:12px; font-weight:600; color:#94A3B8 !important; letter-spacing:1px; margin-left:4px;'>NAVIGATION MENU</p>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "เลือกโมดูลการทำงาน:",
    [
        "📊 หน้าหลัก & บทวิเคราะห์ธุรกิจ",
        "🎓 1. ผลิตสื่อ ม.1 & ใบงาน TPT",
        "🎬🛒 2. FB Reels & Shopee Affiliate",
        "🎛️ 3. ศูนย์คุมเพจ (FB Page Manager)",
        "📘 4. สถานะ & สถิติเพจ Facebook"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.info("""
💡 **Quick Guide:**
- **โมดูล 1:** สร้างใบงาน ม.1 & PDF
- **โมดูล 2:** สคริปต์ Reels 15-30 วิ
- **โมดูล 3:** อนุมัติโพสต์ Auto-Post
- **โมดูล 4:** ดูสถิติเพจสด
""")

# Route to selected module
if menu == "📊 หน้าหลัก & บทวิเคราะห์ธุรกิจ":
    render_analytics_dashboard_module()

elif menu == "🎓 1. ผลิตสื่อ ม.1 & ใบงาน TPT":
    render_student_care_tpt_module()

elif menu == "🎬🛒 2. FB Reels & Shopee Affiliate":
    render_shopee_affiliate_module()

elif menu == "🎛️ 3. ศูนย์คุมเพจ (FB Page Manager)":
    render_fb_page_manager_module()

elif menu == "📘 4. สถานะ & สถิติเพจ Facebook":
    render_fb_page_status_module()
