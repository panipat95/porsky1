import streamlit as st
import pandas as pd
import time
from models.database import get_all_worksheets, get_all_affiliate_products, get_fb_posts, add_worksheet, add_affiliate_product, enqueue_fb_post
from utils.ai_agent import generate_tpt_worksheet, generate_fb_reels_script, format_for_facebook
from utils.facebook_api import post_to_facebook_page

def render_pixel_office_module():
    # Pixel Art Retro 2D Office Styling & Sprite Animations
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Press+Start+2P&display=swap');

        .pixel-title {
            font-family: 'Prompt', sans-serif;
            font-size: 30px;
            font-weight: 800;
            color: #0369A1;
            margin-bottom: 4px;
        }

        /* 2D Pixel Art Office Scene Container */
        .pixel-office-container {
            background: linear-gradient(180deg, #E0F2FE 0%, #BAE6FD 100%);
            border: 4px solid #0284C7;
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 12px 30px rgba(2, 132, 199, 0.15);
            position: relative;
            overflow: hidden;
            margin-bottom: 24px;
        }

        /* Pixel Art Grid Floor Pattern */
        .pixel-floor {
            background-image: 
                linear-gradient(rgba(2, 132, 199, 0.08) 1px, transparent 1px),
                linear-gradient(90deg, rgba(2, 132, 199, 0.08) 1px, transparent 1px);
            background-size: 32px 32px;
            border-radius: 12px;
            padding: 20px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
        }

        /* Agent Workstation Desk Box */
        .agent-desk {
            background: #FFFFFF;
            border: 3px solid #0284C7;
            border-radius: 16px;
            padding: 16px;
            box-shadow: 0 6px 0 #0284C7;
            transition: all 0.2s ease;
            position: relative;
        }

        .agent-desk:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 0 #0369A1;
            border-color: #0369A1;
        }

        .agent-avatar {
            font-size: 32px;
            margin-right: 8px;
            display: inline-block;
        }

        .agent-name {
            font-weight: 700;
            font-size: 15px;
            color: #0369A1;
        }

        .agent-role {
            font-size: 12px;
            color: #64748B;
            margin-bottom: 8px;
        }

        /* Speech Bubble */
        .speech-bubble {
            position: relative;
            background: #0284C7;
            border-radius: 12px;
            padding: 8px 12px;
            color: #FFFFFF;
            font-size: 12px;
            font-weight: 600;
            margin-top: 8px;
        }
        .speech-bubble::after {
            content: '';
            position: absolute;
            top: -6px;
            left: 20px;
            width: 0;
            height: 0;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-bottom: 6px solid #0284C7;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="pixel-title">🎮 สำนักงานเสมือน Pixel Art AI Agent Office (Kru Por Studio)</div>', unsafe_allow_html=True)
    st.caption("การจำลองสภาพแวดล้อมสำนักงาน 2D Pixel Art พร้อมทีมงาน AI Agent 5 ตัว ทำงานและเชื่อมต่อระบบจริง 100%")

    st.divider()

    # Data counts
    worksheets = get_all_worksheets()
    affiliates = get_all_affiliate_products()
    fb_posts = get_fb_posts()
    posted_posts = [p for p in fb_posts if p['status'] == 'posted']

    # 2D Pixel Art Office Grid Display
    st.markdown("""
    <div class="pixel-office-container">
        <div style="font-weight:700; color:#0369A1; font-size:16px; margin-bottom:12px;">
            🏢 แผนผังสำนักงานเสมือน (Interactive 2D Office Map)
        </div>
        <div class="pixel-floor">
            <div class="agent-desk">
                <div><span class="agent-avatar">👨‍💼</span><span class="agent-name">CEO ครูปอ</span></div>
                <div class="agent-role">ผู้บริหารสูงสุด & วางกลยุทธ์</div>
                <div class="speech-bubble">💬 "คุมภาพรวมสำนักงาน และตรวจสถิติเพจสด"</div>
            </div>
            <div class="agent-desk">
                <div><span class="agent-avatar">📚</span><span class="agent-name">Agent 1: น้องวิชาการ</span></div>
                <div class="agent-role">ฝ่ายผลิตสื่อการสอน ม.1 (TPT)</div>
                <div class="speech-bubble">💬 "พร้อมออกแบบใบงาน ม.1 ใหม่ใน 1 คลิก"</div>
            </div>
            <div class="agent-desk">
                <div><span class="agent-avatar">🎬</span><span class="agent-name">Agent 2: น้องการตลาด</span></div>
                <div class="agent-role">ฝ่ายสคริปต์ Reels & Shopee</div>
                <div class="speech-bubble">💬 "พร้อมเขียนสคริปต์ Reels 15-30 วินาที"</div>
            </div>
            <div class="agent-desk">
                <div><span class="agent-avatar">🎛️</span><span class="agent-name">Agent 3: น้องคุมเพจ</span></div>
                <div class="agent-role">ฝ่ายตรวจพรีวิว & Auto-Post</div>
                <div class="speech-bubble">💬 "พร้อมยิงโพสต์เข้าเพจ ห้องเรียนอารมณ์ดี"</div>
            </div>
            <div class="agent-desk">
                <div><span class="agent-avatar">📘</span><span class="agent-name">Agent 4: น้องไอที</span></div>
                <div class="agent-role">ฝ่ายเฝ้าระบบ API & เพจสด</div>
                <div class="speech-bubble">💬 "สถานะเพจสด: LIVE (เชื่อมต่อ 100%)"</div>
            </div>
            <div class="agent-desk" style="background:#F0F9FF; border-style:dashed;">
                <div><span class="agent-avatar">🤖</span><span class="agent-name">Agent 5: ผู้ช่วย AI</span></div>
                <div class="agent-role">ฝ่ายวิเคราะห์ข้อมูลเชิงลึก</div>
                <div class="speech-bubble">💬 "ประมวลผลข้อมูลและสรุปแผนงาน"</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Agent Action Console (สั่งงาน Agent ประจำโต๊ะ)
    st.subheader("🕹️ คอนโซลสั่งงานทีม AI Agent ประจำโต๊ะ (Real-time Agent Action Console)")
    
    t1, t2, t3 = st.tabs([
        "📚 สั่ง Agent 1 สร้างใบงาน TPT",
        "🎬 สั่ง Agent 2 เขียนสคริปต์ Reels",
        "🚀 สั่ง Agent 3 ยิงโพสต์ขึ้นเพจ"
    ])
    
    with t1:
        st.markdown("**สั่ง Agent 1 (น้องวิชาการ) ออกแบบสื่อการสอน ม.1**")
        col_ws1, col_ws2 = st.columns(2)
        with col_ws1:
            ws_subject = st.text_input("ชื่อรายวิชา", value="วิทยาศาสตร์ / สังคมศึกษา", key="px_subj")
            ws_topic = st.text_input("หัวข้อบทเรียน", value="โครงสร้างเซลล์และการทำงานของพืช ม.1", key="px_topic")
        with col_ws2:
            ws_grade = st.selectbox("ระดับชั้น", ["ม.1", "ม.2", "ม.1-ม.3 Integrated"], key="px_grade")
            ws_price = st.number_input("ราคาขายตั้งต้น (บาท)", value=59.0, key="px_price")
            
        if st.button("✨ ให้ Agent 1 ลงมือสร้างใบงานทันที", key="px_btn_ws"):
            with st.spinner("Agent 1 กำลังนั่งโต๊ะค้นคว้าและออกแบบใบงาน ม.1..."):
                time.sleep(1)
                content = generate_tpt_worksheet(ws_subject, ws_topic, ws_grade)
                title = f"ใบงาน {ws_topic} ({ws_grade})"
                ws_id = add_worksheet(title, ws_subject, ws_grade, content, ws_price)
                
                # Auto enqueue to FB Page queue
                fb_text = format_for_facebook(title, f"แจกและเปิดขายใบงาน ม.1 เรื่อง {ws_topic}", link="https://teacherspayteachers.com", post_type="tpt")
                q_id = enqueue_fb_post("tpt_worksheet", ws_id, title, fb_text)
                
                st.balloons()
                st.success(f"🎉 Agent 1 สร้างใบงานและส่งต่อให้ Agent 3 เรียบร้อยแล้ว! (Worksheet ID: #{ws_id} | Queue ID: #{q_id})")
                st.text_area("เนื้อหาใบงานที่สร้างสำเร็จ:", value=content, height=200)

    with t2:
        st.markdown("**สั่ง Agent 2 (น้องการตลาด) เขียนสคริปต์ Facebook Reels & Shopee Affiliate**")
        col_aff1, col_aff2 = st.columns(2)
        with col_aff1:
            prod_name = st.text_input("ชื่อสินค้าป้ายยา", value="โคมไฟ LED ถนอมสายตาสำหรับโต๊ะทำงานครู", key="px_prod")
            prod_cat = st.selectbox("หมวดหมู่", ["ของใช้ในบ้าน", "เครื่องเขียน/อุปกรณ์เรียน", "ไอที"], key="px_cat")
        with col_aff2:
            prod_url = st.text_input("ลิงก์ Affiliate", value="https://shope.ee/ledlamp_example", key="px_url")
            prod_features = st.text_area("จุดเด่นสินค้า", value="ปรับระดับแสงได้ 3 ระดับ, ถนอมสายตาขณะตรวจข้อสอบ, พับเก็บง่าย", key="px_feat")
            
        if st.button("🚀 ให้ Agent 2 ลงมือแต่งสคริปต์ Reels ทันที", key="px_btn_aff"):
            with st.spinner("Agent 2 กำลังร่างสคริปต์ Reels 15-30 วินาที..."):
                time.sleep(1)
                res = generate_fb_reels_script(prod_name, prod_features, "259")
                script_text = res["script"]
                caption_text = res["caption"].replace("[AFFILIATE_LINK_PLACEHOLDER]", prod_url)
                
                prod_id = add_affiliate_product(prod_name, prod_cat, prod_url, script_text, caption_text)
                fb_formatted = format_for_facebook(f"Reels: {prod_name}", caption_text, link=prod_url, post_type="affiliate")
                q_id = enqueue_fb_post("shopee_affiliate", prod_id, prod_name, fb_formatted)
                
                st.balloons()
                st.success(f"🎉 Agent 2 เขียนสคริปต์สำเร็จ และส่งต่อให้ Agent 3 เรียบร้อยแล้ว! (Product ID: #{prod_id} | Queue ID: #{q_id})")
                st.text_area("สคริปต์ Facebook Reels:", value=script_text, height=200)

    with t3:
        st.markdown("**สั่ง Agent 3 (น้องคุมเพจ) ตรวจทานและยิงโพสต์ขึ้นเพจ 'ห้องเรียนอารมณ์ดี'**")
        pending_posts = [p for p in fb_posts if p['status'] == 'pending_approval']
        
        if pending_posts:
            st.info(f"มีคอนเทนต์รอกรอง {len(pending_posts)} รายการ")
            for post in pending_posts[:3]: # Show top 3 pending
                st.markdown(f"**📌 #{post['id']} - {post['title']}**")
                st.code(post["content_formatted"][:150] + "...")
                
                if st.button(f"🚀 ให้ Agent 3 อนุมัติยิงขึ้นเพจทันที (Post #{post['id']})", key=f"px_post_{post['id']}", type="primary"):
                    with st.spinner("Agent 3 กำลังยิง Meta Graph API ขึ้นเพจ Facebook..."):
                        result = post_to_facebook_page(post["content_formatted"])
                        if result["success"]:
                            st.balloons()
                            st.success(f"🎉 โพสต์ลงเพจ 'ห้องเรียนอารมณ์ดี' สำเร็จ! (Post ID: {result.get('id')})")
                            st.rerun()
                        else:
                            st.error(f"ข้อผิดพลาด: {result.get('error')}")
        else:
            st.info("ไม่มีคอนเทนต์ค้างรอกรองในขณะนี้ สามารถสั่ง Agent 1 หรือ 2 สร้างใหม่ได้ใน Tab ด้านข้างครับ!")
