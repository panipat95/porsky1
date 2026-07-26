import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from models.database import get_fb_posts, get_all_worksheets, get_all_affiliate_products

load_dotenv()

# Check Environment Variables & Streamlit Secrets
FB_PAGE_ID = os.getenv("FB_PAGE_ID", "")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "")

if not FB_PAGE_ID or not FB_PAGE_ACCESS_TOKEN:
    try:
        if "FB_PAGE_ID" in st.secrets:
            FB_PAGE_ID = st.secrets["FB_PAGE_ID"]
        if "FB_PAGE_ACCESS_TOKEN" in st.secrets:
            FB_PAGE_ACCESS_TOKEN = st.secrets["FB_PAGE_ACCESS_TOKEN"]
    except Exception:
        pass

def fetch_facebook_page_info():
    """ดึงข้อมูลสถานะเพจสดจาก Facebook Graph API"""
    if not FB_PAGE_ID or not FB_PAGE_ACCESS_TOKEN:
        return {"connected": False, "reason": "ยังไม่ได้ใส่ FB_PAGE_ACCESS_TOKEN"}
        
    url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}?fields=id,name,link,fan_count,followers_count&access_token={FB_PAGE_ACCESS_TOKEN}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            data["connected"] = True
            return data
        else:
            return {"connected": False, "reason": r.json().get("error", {}).get("message", "API Error")}
    except Exception as e:
        return {"connected": False, "reason": str(e)}


def render_fb_page_status_module():
    st.title("📘 โมดูล 4: สถานะ & สถิติเพจ Facebook (Live Page Health)")
    st.caption("ตรวจสอบรายละเอียดการเชื่อมต่อ จำนวนโพสต์ทั้งหมด และระบบเชื่อมโยงระหว่างโมดูลกับเพจ Facebook")
    
    # 1. Page Connection Banner
    page_info = fetch_facebook_page_info()
    
    if page_info.get("connected"):
        st.success(f"🟢 **เชื่อมต่อเพจ Facebook สำเร็จ!** | ชื่อเพจ: **{page_info.get('name', 'ห้องเรียนอารมณ์ดี')}** (ID: {page_info.get('id')})")
    else:
        st.warning(f"⚠️ **สถานะการเชื่อมต่อ API:** {page_info.get('reason', 'โปรดตรวจสอบ Token ใน .env หรือ Secrets')}")

    st.divider()

    # 2. Key Page Metrics (การเชื่อมโยงระบบทั้งหมด)
    all_fb_posts = get_fb_posts()
    posted_items = [p for p in all_fb_posts if p['status'] == 'posted']
    approved_items = [p for p in all_fb_posts if p['status'] == 'approved']
    pending_items = [p for p in all_fb_posts if p['status'] == 'pending_approval']
    
    worksheets = get_all_worksheets()
    affiliates = get_all_affiliate_products()

    st.subheader("📊 สรุปสถิติโพสต์และการเชื่อมโยงทั้งหมด (System Overview)")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🚀 โพสต์ขึ้นเพจสำเร็จแล้ว", f"{len(posted_items)} ครั้ง")
    col2.metric("⏳ รอตรวจ (Pending)", f"{len(pending_items)} รายการ")
    col3.metric("📚 สื่อ TPT ในคลัง", f"{len(worksheets)} ชิ้น")
    col4.metric("🛒 สินค้า Reels ในคลัง", f"{len(affiliates)} รายการ")

    st.divider()

    # 3. Detailed Facebook Post Log Table & Direct Links
    st.subheader("📋 รายละเอียดประวัติการโพสต์ทั้งหมด (FB Post History & Status)")
    
    if all_fb_posts:
        posts_data = []
        for p in all_fb_posts:
            source = "📚 สื่อการสอน TPT" if p["source_type"] == "tpt_worksheet" else "🎬🛒 Shopee Reels"
            status_label = "🚀 โพสต์แล้ว" if p["status"] == "posted" else ("✅ อนุมัติแล้ว" if p["status"] == "approved" else "⏳ รอกรอง")
            
            fb_link = f"https://facebook.com/{p['fb_post_id']}" if p.get('fb_post_id') else "ยังไม่ได้โพสต์"
            
            posts_data.append({
                "ID": f"#{p['id']}",
                "หัวข้อคอนเทนต์": p["title"],
                "หมวดหมู่": source,
                "สถานะ": status_label,
                "FB Post ID": p.get("fb_post_id") or "-",
                "วันที่สร้าง": p.get("created_at", "-")
            })
            
        df_posts = pd.DataFrame(posts_data)
        st.dataframe(df_posts, use_container_width=True)
    else:
        st.info("ยังไม่มีประวัติการโพสต์ ลองสร้างคอนเทนต์ในโมดูล 1 หรือ 2 แล้วกด Approve ในโมดูล 3 ได้เลยครับ!")

    st.divider()

    # 4. Cross-Module System Map (แผนผังการเชื่อมโยงระบบทั้งหมด)
    st.subheader("🔗 แผนผังการเชื่อมโยงระบบทั้งหมด (All-in-One Integration Architecture)")
    st.markdown("""
    ```mermaid
    graph LR
        M1[🎓 โมดูล 1: สื่อ TPT] -->|สร้างใบงาน PDF & แคปชั่น| QUEUE[(🎛️ คิวโพสต์ fb_posts_queue)]
        M2[🎬 โมดูล 2: Shopee Reels] -->|สร้างสคริปต์ Reels & Affiliate| QUEUE
        QUEUE -->|ครูปอกด Approve| M3[🎛️ โมดูล 3: FB Manager]
        M3 -->|ยิง Meta Graph API| FB_PAGE[📘 เพจ Facebook: ห้องเรียนอารมณ์ดี]
        FB_PAGE -->|ดึงสถิติสด| M4[📊 โมดูล 4: สถานะเพจ FB]
    ```
    """)
