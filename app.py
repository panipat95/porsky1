import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ All-in-One Executive Ecosystem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Clean Streamlined Modern Minimalist System
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, sans-serif !important;
        background-color: #F8FAFC !important; /* Pure Slate 50 */
        color: #0F172A !important;
    }
    
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1300px;
    }

    /* Clean Royal Navy Sidebar */
    section[data-testid="stSidebar"] {
        background: #0F172A !important;
        border-right: 1px solid #1E293B !important;
    }
    
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {
        color: #F8FAFC !important;
        font-family: 'Prompt', sans-serif !important;
    }

    /* Clean Brand Header Card */
    .clean-brand-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .clean-brand-avatar {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        background: #2563EB;
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .clean-brand-title {
        font-size: 17px;
        font-weight: 800;
        color: #FFFFFF !important;
        line-height: 1.2;
    }

    .clean-brand-subtitle {
        font-size: 12px;
        color: #94A3B8 !important;
    }

    .clean-brand-status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.2);
        color: #34D399 !important;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 12px;
        margin-top: 4px;
    }

    /* Clean Active Menu Pill */
    section[data-testid="stSidebar"] .stRadio label {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        margin-bottom: 6px !important;
        cursor: pointer !important;
    }

    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label {
        background: #2563EB !important;
        border-color: #3B82F6 !important;
    }

    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label p,
    section[data-testid="stSidebar"] .stRadio div[aria-checked="true"] label span {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }
</style>
""", unsafe_allow_html=True)

# Import Database & Core Modules
from models.database import init_db
from modules.analytics_dashboard import render_analytics_dashboard_module
from modules.student_care_tpt import render_student_care_tpt_module
from modules.shopee_affiliate import render_shopee_affiliate_module
from modules.fb_page_manager import render_fb_page_manager_module

# Initialize Database Schema
init_db()

# Clean Brand Header Card in Sidebar
st.sidebar.markdown("""
<div class="clean-brand-card">
    <div class="clean-brand-avatar">KP</div>
    <div>
        <div class="clean-brand-title">ครูปอ Ecosystem</div>
        <div class="clean-brand-subtitle">Executive Content Studio</div>
        <div class="clean-brand-status">
            🟢 LIVE: ห้องเรียนอารมณ์ดี
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p style='font-size:12px; font-weight:800; color:#64748B !important; letter-spacing:1px; margin-bottom:8px; margin-left:4px;'>MAIN MENU</p>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "เลือกเมนูการทำงาน:",
    [
        "📊 1. หน้าหลัก & แดชบอร์ดสรุปรายได้",
        "🎓 2. ผลิตสื่อ ม.1 & ใบงาน TPT",
        "🎬🛒 3. สคริปต์ Reels & Shopee Affiliate",
        "🎛️ 4. ศูนย์คุมเพจ Facebook (Auto-Post)"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.caption("ครูปอ All-in-One Streamlined Core v5.0")

# Route to selected core module
if menu == "📊 1. หน้าหลัก & แดชบอร์ดสรุปรายได้":
    render_analytics_dashboard_module()

elif menu == "🎓 2. ผลิตสื่อ ม.1 & ใบงาน TPT":
    render_student_care_tpt_module()

elif menu == "🎬🛒 3. สคริปต์ Reels & Shopee Affiliate":
    render_shopee_affiliate_module()

elif menu == "🎛️ 4. ศูนย์คุมเพจ Facebook (Auto-Post)":
    render_fb_page_manager_module()
