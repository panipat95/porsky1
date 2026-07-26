import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ All-in-One Ecosystem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sky-Blue & Pure White Design System (Custom CSS Injection)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&display=swap');
    
    /* 1. Kinetic Animations */
    @keyframes statusGlow {
        0% { box-shadow: 0 0 5px rgba(255, 255, 255, 0.4); }
        50% { box-shadow: 0 0 15px rgba(255, 255, 255, 0.9); }
        100% { box-shadow: 0 0 5px rgba(255, 255, 255, 0.4); }
    }

    /* Global Canvas */
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, sans-serif !important;
        background-color: #F0F9FF; /* Sky 50 */
    }
    
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    /* Sky-Blue & White Premium Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0284C7 0%, #0369A1 100%) !important;
        border-right: 1px solid #0284C7;
        box-shadow: 4px 0 25px rgba(2, 132, 199, 0.15);
    }
    
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
        font-family: 'Prompt', sans-serif !important;
    }

    /* Brand Header Box in Sidebar */
    .sidebar-brand-card {
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 24px;
        backdrop-filter: blur(12px);
        display: flex;
        align-items: center;
        gap: 14px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    }

    .brand-avatar {
        width: 52px;
        height: 52px;
        border-radius: 16px;
        background: #FFFFFF;
        color: #0284C7;
        font-weight: 800;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    }

    .brand-title {
        font-size: 18px;
        font-weight: 800;
        color: #FFFFFF !important;
        line-height: 1.2;
    }

    .brand-subtitle {
        font-size: 12px;
        color: #E0F2FE !important;
    }

    /* Live Status Pill */
    .live-status-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.5);
        color: #FFFFFF !important;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        margin-top: 6px;
        animation: statusGlow 3s infinite;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #FFFFFF;
    }

    /* Modern Navigation Radio Buttons */
    section[data-testid="stSidebar"] .stRadio > div {
        gap: 10px;
    }

    section[data-testid="stSidebar"] .stRadio label {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 14px !important;
        padding: 14px 18px !important;
        transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        cursor: pointer;
        font-weight: 600 !important;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255, 255, 255, 0.25) !important;
        border-color: #FFFFFF !important;
        transform: translateX(6px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    }

    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label {
        background: #FFFFFF !important;
        color: #0284C7 !important;
        border-color: #FFFFFF !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2) !important;
        font-weight: 800 !important;
    }

    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label * {
        color: #0284C7 !important;
    }

    /* Dividers */
    hr {
        border-color: #E0F2FE !important;
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

st.sidebar.markdown("<p style='font-size:12px; font-weight:700; color:#E0F2FE !important; letter-spacing:1.2px; margin-left:4px;'>NAVIGATION MENU</p>", unsafe_allow_html=True)

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
💡 **7 Design Paradigms Active:**
- Sky-Blue & Pure White Theme
- Scrollytelling & Bento Grid
- Glassmorphism & Micro-interactions
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
