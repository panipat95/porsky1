import streamlit as st
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="ครูปอ Ecosystem - Executive Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (ui-ux-pro-max Executive Light Mode System)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Prompt', -apple-system, sans-serif !important;
    }
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        color: #1E40AF;
        margin-bottom: 0px;
    }
    .sidebar-subtitle {
        font-size: 13px;
        color: #64748B;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Import Database & Modules
from models.database import init_db
from modules.analytics_dashboard import render_analytics_dashboard_module
from modules.student_care_tpt import render_student_care_tpt_module
from modules.shopee_affiliate import render_shopee_affiliate_module
from modules.fb_page_manager import render_fb_page_manager_module

# Initialize Database Schema
init_db()

# Sidebar Navigation
st.sidebar.markdown('<div class="sidebar-title">🎓 ครูปอ All-in-One</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-subtitle">Executive Business Dashboard & Content Studio</div>', unsafe_allow_html=True)

menu = st.sidebar.radio(
    "📌 เลือกโมดูลการทำงาน:",
    [
        "📊 หน้าหลัก & บทวิเคราะห์ธุรกิจ",
        "🎓 1. ผลิตสื่อ ม.1 & ใบงาน TPT",
        "🎬🛒 2. FB Reels & Shopee Affiliate",
        "🎛️ 3. ศูนย์คุมเพจ (FB Page Manager)"
    ]
)

st.sidebar.divider()
st.sidebar.info("""
💡 **คำแนะนำการใช้งาน:**
- **📊 หน้าหลัก:** วิเคราะห์กราฟรายได้ & คำแนะนำการตัดสินใจ
- **🎓 โมดูล 1:** เจนใบงาน ม.1 ด้วย AI & ออกไฟล์ PDF
- **🎬🛒 โมดูล 2:** เจนสคริปต์ Facebook Reels + แคปชั่น Affiliate
- **🎛️ โมดูล 3:** ตรวจพรีวิวโพสต์ อนุมัติยิงโพสต์ขึ้น Facebook
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
