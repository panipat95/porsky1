import streamlit as st
import pandas as pd
from models.database import get_fb_posts, update_fb_post_status, update_fb_post_content
from utils.facebook_api import post_to_facebook_page

def render_fb_page_manager_module():
    st.title("🎛️ โมดูล 3: Facebook Page Manager Dashboard (CEO Room)")
    st.caption("ศูนย์กลางสำหรับครูปอ ตรวจสอบ อนุมัติ และจัดรูปแบบคอนเทนต์ก่อนยิงขึ้นเพจ Facebook")
    
    # Overview Metrics
    all_posts = get_fb_posts()
    pending_posts = get_fb_posts(status_filter="pending_approval")
    approved_posts = get_fb_posts(status_filter="approved")
    posted_posts = get_fb_posts(status_filter="posted")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("คิวทั้งหมด", len(all_posts))
    m2.metric("⏳ รอตรวจ (Pending)", len(pending_posts))
    m3.metric("✅ อนุมัติแล้ว (Approved)", len(approved_posts))
    m4.metric("🚀 โพสต์แล้ว (Posted)", len(posted_posts))
    
    st.divider()
    
    # Filter Controls
    filter_status = st.radio("เลือกดูสถานะ:", ["รอกรอง (Pending)", "อนุมัติแล้ว (Approved)", "โพสต์เรียบร้อย (Posted)", "ทั้งหมด"], horizontal=True)
    
    if filter_status == "รอกรอง (Pending)":
        target_posts = pending_posts
    elif filter_status == "อนุมัติแล้ว (Approved)":
        target_posts = approved_posts
    elif filter_status == "โพสต์เรียบร้อย (Posted)":
        target_posts = posted_posts
    else:
        target_posts = all_posts
        
    if not target_posts:
        st.info("ไม่มีรายการคอนเทนต์ในหมวดหมู่นี้ครับ คุณครูสามารถสร้างเนื้อหาใหม่ได้ที่ โมดูล 1 หรือ โมดูล 2")
        return
        
    st.subheader(f"📋 รายการคอนเทนต์ ({len(target_posts)} รายการ)")
    
    for post in target_posts:
        post_id = post["id"]
        source_badge = "📚 สื่อการสอน TPT" if post["source_type"] == "tpt_worksheet" else "🛒 Shopee Affiliate"
        
        with st.expander(f"📌 [{source_badge}] {post['title']} (ID: #{post_id}) | สถานะ: {post['status'].upper()}", expanded=(post['status']=='pending_approval')):
            col_edit, col_preview = st.columns(2)
            
            with col_edit:
                st.markdown("**✏️ แก้ไขข้อความคอนเทนต์ (จัดเว้นวรรค & Emoji)**")
                edited_text = st.text_area(
                    "ปรับแต่งข้อความก่อนโพสต์",
                    value=post["content_formatted"],
                    height=300,
                    key=f"text_{post_id}"
                )
                if st.button("💾 เซฟข้อความที่แก้ไข", key=f"save_{post_id}"):
                    update_fb_post_content(post_id, edited_text)
                    st.success("อัปเดตข้อความเรียบร้อยแล้ว!")
                    st.rerun()
                    
            with col_preview:
                st.markdown("**📱 พรีวิวการแสดงผลบน Facebook Page**")
                # Custom CSS simulated FB Post Card
                st.markdown(f"""
                <div style="background-color: #18191a; color: #e4e6eb; border-radius: 8px; padding: 16px; font-family: sans-serif; border: 1px solid #3a3b3c;">
                    <div style="display: flex; align-items: center; margin-bottom: 12px;">
                        <div style="width: 40px; height: 40px; border-radius: 50%; background-color: #0866ff; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 10px;">
                            KP
                        </div>
                        <div>
                            <div style="font-weight: bold; color: #e4e6eb;">ครูปอ - Learning & Lifestyle</div>
                            <div style="font-size: 12px; color: #b0b3b8;">เมื่อสักครู่ · 🌐 Public</div>
                        </div>
                    </div>
                    <div style="white-space: pre-wrap; font-size: 14px; line-height: 1.5; color: #e4e6eb;">
{edited_text}
                    </div>
                </div>
                """, unsafe_allow_ascii=False, unsafe_allow_html=True)
                
            st.divider()
            
            # Action Buttons
            btn_col1, btn_col2, btn_col3 = st.columns(3)
            
            with btn_col1:
                if st.button("🚀 อนุมัติ & ยิงโพสต์ขึ้น Facebook", key=f"post_{post_id}", type="primary"):
                    with st.spinner("กำลังเชื่อมต่อยิงโพสต์ขึ้น Facebook Page..."):
                        result = post_to_facebook_page(edited_text)
                        if result["success"]:
                            update_fb_post_status(post_id, status="posted", fb_post_id=result.get("id"))
                            if result.get("mock"):
                                st.warning("⚠️ " + result["message"])
                            st.balloons()
                            st.success(f"อนุมัติและยิงโพสต์สำเร็จแล้ว! (FB Post ID: {result.get('id')})")
                            st.rerun()
                        else:
                            st.error(f"เกิดข้อผิดพลาด: {result.get('error')}")

            with btn_col2:
                if st.button("✅ อนุมัติไว้ก่อน (ยังไม่ยิงโพสต์)", key=f"approve_{post_id}"):
                    update_fb_post_status(post_id, status="approved")
                    st.success("เปลี่ยนสถานะเป็น APPROVED แล้ว!")
                    st.rerun()

            with btn_col3:
                if st.button("❌ ปฏิเสธ/ลบคอนเทนต์", key=f"reject_{post_id}"):
                    update_fb_post_status(post_id, status="rejected")
                    st.info("เปลี่ยนสถานะเป็น REJECTED แล้ว")
                    st.rerun()
