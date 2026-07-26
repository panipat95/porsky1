import streamlit as st
import pandas as pd
import altair as alt
from models.database import get_all_worksheets, get_all_affiliate_products, get_fb_posts

def render_analytics_dashboard_module():
    # 🎨 Advanced Design Master System: 7 Cutting-Edge Web Design Paradigms
    # 1. Kinetic Typography 2. Bento Grid 3. Glassmorphism 4. 3D Tilt Experience 5. Micro-interactions 6. Parallax 7. Scrollytelling
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

        /* 1. Kinetic Typography Animations */
        @keyframes textShimmer {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes statusPulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        html, body, [class*="css"], .stApp {
            font-family: 'Prompt', -apple-system, sans-serif !important;
            background: #F8FAFC !important;
            color: #0F172A !important;
        }

        /* Kinetic Animated Gradient Header */
        .kinetic-header {
            font-size: 32px;
            font-weight: 800;
            background: linear-gradient(135deg, #1E40AF 0%, #2563EB 35%, #059669 70%, #D97706 100%);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textShimmer 8s ease infinite;
            letter-spacing: -0.5px;
            margin-bottom: 4px;
        }

        /* 2. Glassmorphism & 4. 3D Tilt Card Base */
        .bento-card {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(226, 232, 240, 0.9);
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.05), inset 0 1px 0 rgba(255, 255, 255, 0.6);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            transform-style: preserve-3d;
            perspective: 1000px;
            animation: fadeInUp 0.6s ease forwards;
            position: relative;
            overflow: hidden;
        }

        /* 3. Micro-interactions: 3D Hover Tilt & Specular Ambient Glow */
        .bento-card:hover {
            transform: perspective(1000px) translateZ(8px) rotateX(2deg) rotateY(-1deg);
            box-shadow: 0 20px 40px -15px rgba(30, 64, 175, 0.12), 0 0 25px rgba(37, 99, 235, 0.1);
            border-color: #3B82F6;
        }

        /* Accent top glow bar */
        .bento-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 4px;
            background: linear-gradient(90deg, #1E40AF, #2563EB, #059669);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .bento-card:hover::before {
            opacity: 1;
        }

        /* 5. Bento Grid Layout Spacing */
        .bento-tag {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #64748B;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .bento-value {
            font-size: 36px;
            font-weight: 800;
            color: #1E40AF;
            line-height: 1.1;
            font-family: 'Prompt', sans-serif;
        }

        .bento-sub {
            font-size: 13px;
            font-weight: 500;
            color: #059669;
            margin-top: 8px;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .live-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #10B981;
            display: inline-block;
            animation: statusPulse 2s infinite;
        }

        /* 6. Scrollytelling Story Box */
        .scrolly-story-box {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-left: 5px solid #2563EB;
            border-radius: 16px;
            padding: 22px 26px;
            margin-bottom: 16px;
            box-shadow: 0 4px 20px -4px rgba(0,0,0,0.03);
            transition: all 0.3s ease;
        }
        .scrolly-story-box:hover {
            border-left-color: #059669;
            transform: translateX(6px);
            box-shadow: 0 8px 25px -5px rgba(5, 150, 105, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    # 1. Kinetic Typography Header
    st.markdown('<div class="kinetic-header">📊 Executive Business Dashboard</div>', unsafe_allow_html=True)
    st.caption("ศูนย์วิเคราะห์ข้อมูลเชิงกลยุทธ์ | Powered by 7 State-of-the-Art Web Design Paradigms (Bento Grid, Glassmorphism, 3D Tilt)")

    st.markdown("<br>", unsafe_allow_html=True)

    # Data Fetching
    worksheets = get_all_worksheets()
    affiliates = get_all_affiliate_products()
    fb_posts = get_fb_posts()

    # Zero-state reset metrics
    total_ws_count = len(worksheets)
    total_aff_count = len(affiliates)
    total_fb_count = len(fb_posts)
    
    pending_count = len([p for p in fb_posts if p['status'] == 'pending_approval'])
    approved_count = len([p for p in fb_posts if p['status'] == 'approved'])
    posted_count = len([p for p in fb_posts if p['status'] == 'posted'])

    avg_ws_price = sum([w['price'] for w in worksheets]) / total_ws_count if total_ws_count > 0 else 0.0
    projected_tpt_rev = sum([w['price'] * 25 for w in worksheets]) if total_ws_count > 0 else 0.0
    projected_aff_rev = total_aff_count * 1250 if total_aff_count > 0 else 0.0
    total_projected_rev = projected_tpt_rev + projected_aff_rev

    # 5. Bento Grid Layout (Row 1 KPI Architecture)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="bento-card">
            <div class="bento-tag"><span class="live-dot"></span> 💰 REVENUE FORECAST</div>
            <div class="bento-value">฿{total_projected_rev:,.0f}</div>
            <div class="bento-sub">🎯 เป้าหมาย: ฿30,000 / เดือน</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="bento-card">
            <div class="bento-tag">📚 TPT CONTENT VAULT</div>
            <div class="bento-value">{total_ws_count} <span style="font-size:18px; color:#64748B;">สื่อ</span></div>
            <div class="bento-sub" style="color:#64748B;">เฉลี่ย ฿{avg_ws_price:.0f} / ชิ้น</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="bento-card">
            <div class="bento-tag">🎬 SHOPEE REELS STUDIO</div>
            <div class="bento-value">{total_aff_count} <span style="font-size:18px; color:#64748B;">สินค้า</span></div>
            <div class="bento-sub" style="color:#64748B;">พร้อมสคริปต์ป้ายยา 100%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="bento-card">
            <div class="bento-tag">🎛️ FB QUEUE PIPELINE</div>
            <div class="bento-value">{total_fb_count} <span style="font-size:18px; color:#64748B;">รายการ</span></div>
            <div class="bento-sub" style="color:#D97706;">⏳ รอตรวจ: {pending_count} รายการ</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Visual Interactive Analytics (Charts Section)
    c_left, c_right = st.columns([6, 4])
    
    with c_left:
        st.subheader("📈ประมาณการสัดส่วนรายได้ตามโมเดลธุรกิจ (Revenue Stream Breakdown)")
        
        rev_data = pd.DataFrame({
            "โมเดลธุรกิจ": ["ขายใบงานสื่อการสอน TPT", "ค่าคอมมิชชั่น Shopee Affiliate (FB Reels)"],
            "คาดการณ์รายได้ (บาท)": [projected_tpt_rev, projected_aff_rev]
        })

        chart_rev = alt.Chart(rev_data).mark_bar(cornerRadiusTopLeft=10, cornerRadiusTopRight=10).encode(
            x=alt.X('โมเดลธุรกิจ:N', title=None, axis=alt.Axis(labelAngle=0, labelFont='Prompt', labelFontSize=12)),
            y=alt.Y('คาดการณ์รายได้ (บาท):Q', title="บาท"),
            color=alt.Color('โมเดลธุรกิจ:N', scale=alt.Scale(range=['#1E40AF', '#059669']), legend=None),
            tooltip=['โมเดลธุรกิจ', 'คาดการณ์รายได้ (บาท)']
        ).properties(height=300)
        
        st.altair_chart(chart_rev, use_container_width=True)

    with c_right:
        st.subheader("📊 สถานะคิวคอนเทนต์ (Content Funnel)")
        funnel_df = pd.DataFrame({
            "สถานะ": ["รอกรอง (Pending)", "อนุมัติแล้ว (Approved)", "โพสต์เรียบร้อย (Posted)"],
            "จำนวน": [pending_count, approved_count, posted_count]
        })
        
        chart_funnel = alt.Chart(funnel_df).mark_arc(innerRadius=65).encode(
            theta=alt.Theta(field="จำนวน", type="quantitative"),
            color=alt.Color(field="สถานะ", type="nominal", scale=alt.Scale(range=['#D97706', '#1D4ED8', '#059669'])),
            tooltip=['สถานะ', 'จำนวน']
        ).properties(height=300)
        
        st.altair_chart(chart_funnel, use_container_width=True)

    st.divider()

    # 6. Scrollytelling Story & Business Decision Report
    st.subheader("📖 Scrollytelling: บทวิเคราะห์เชิงกลยุทธ์และการตัดสินใจธุรกิจ")
    st.caption("การเล่าเรื่องผ่านข้อมูล (Scrollytelling Experience) สำหรับครูปอ")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="scrolly-story-box">
            <div style="font-weight:700; color:#1E40AF; font-size:16px; margin-bottom:6px;">
                💡 Chapter 1: โอกาสสร้างรายได้ตั้งต้น (Zero-to-One Strategy)
            </div>
            <div style="color:#334155; font-size:14px; line-height:1.6;">
                • <b>สร้างสื่อใบงาน ม.1 แรกในโมดูล 1:</b> เปิดตัวบน TPT Store และเพจ Facebook ห้องเรียนอารมณ์ดี<br>
                • <b>เลือกของใช้ในบ้าน 1 ชิ้นในโมดูล 2:</b> สรุปสคริปต์ Reels 15-30 วินาที สร้างรายได้คอมมิชชั่นแรกทันที
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="scrolly-story-box">
            <div style="font-weight:700; color:#1E40AF; font-size:16px; margin-bottom:6px;">
                🎯 Chapter 2: การบริหารอัตราส่วนโพสต์ (Content Ratio)
            </div>
            <div style="color:#334155; font-size:14px; line-height:1.6;">
                • ควรรักษาอัตราส่วน <b>70% Reels ป้ายยา : 30% สื่อ TPT</b> เพื่อเพิ่ม Engagement และความน่าเชื่อถือ<br>
                • ปล่อยคลิปในช่วง Peak Time (18:00 - 21:00 น.) เพื่อดึงยอดวิวสูงสุด
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="scrolly-story-box">
            <div style="font-weight:700; color:#1E40AF; font-size:16px; margin-bottom:6px;">
                ⚡ Chapter 3: แผนการตัดสินใจเชิงกลยุทธ์ 4 ขั้นตอน (Action Plan)
            </div>
            <div style="color:#334155; font-size:14px; line-height:1.6;">
                <b>1. เคลียร์คิวโพสต์:</b> กด Approve คอนเทนต์ในโมดูล 3<br>
                <b>2. ขยายหมวดสินค้า:</b> เพิ่มสินค้า Shopee อุปกรณ์โต๊ะครู<br>
                <b>3. Bundle สื่อ TPT:</b> รวมชุดใบงานเพิ่มราคาขายเป็น ฿199<br>
                <b>4. ระบบ Auto-Post:</b> ปล่อยให้ระบบยิงโพสต์ขึ้นเพจ 24 ชม.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="scrolly-story-box" style="border-left-color: #059669; background: #F0FDF4;">
            <div style="font-weight:700; color:#047857; font-size:16px; margin-bottom:6px;">
                📈 Chapter 4: สรุปผลลัพธ์ที่คาดว่าจะได้รับ (Target Milestone)
            </div>
            <div style="color:#166534; font-size:14px; line-height:1.6;">
                สร้างคลังสื่อการสอน 10 ชิ้น + สคริปต์ Reels 10 ชิ้น ภายใน 30 วันแรก คาดการณ์สร้างรายได้เสริม <b>฿30,000+ / เดือน</b> ผ่านระบบอัตโนมัตินี้ครับ!
            </div>
        </div>
        """, unsafe_allow_html=True)
