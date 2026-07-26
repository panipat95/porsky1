import streamlit as st
import pandas as pd
import altair as alt
from models.database import get_all_worksheets, get_all_affiliate_products, get_fb_posts

def render_analytics_dashboard_module():
    # 🎨 Pastel Luxury & Interactive Effects System (ui-ux-pro-max compliant)
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&display=swap');

        /* Pastel Shimmer Keyframes */
        @keyframes pastelShimmer {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes pulseGlow {
            0% { box-shadow: 0 0 0 0 rgba(167, 139, 250, 0.6); }
            70% { box-shadow: 0 0 0 12px rgba(167, 139, 250, 0); }
            100% { box-shadow: 0 0 0 0 rgba(167, 139, 250, 0); }
        }

        /* Pastel Base Canvas */
        html, body, [class*="css"], .stApp {
            font-family: 'Prompt', -apple-system, sans-serif !important;
            background: linear-gradient(135deg, #F8FAFC 0%, #EEF2FF 50%, #F0FDF4 100%) !important;
            color: #1E1B4B !important;
        }

        /* Kinetic Pastel Title Header */
        .pastel-title-header {
            font-size: 32px;
            font-weight: 800;
            background: linear-gradient(135deg, #7C3AED 0%, #2563EB 35%, #059669 70%, #DB2777 100%);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: pastelShimmer 7s ease infinite;
            letter-spacing: -0.5px;
            margin-bottom: 4px;
        }

        /* Bento Pastel Card (3D Tilt & Glassmorphism Effects) */
        .pastel-bento-card {
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 2px solid #E0E7FF;
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 10px 30px -10px rgba(99, 102, 241, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.8);
            transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
            transform-style: preserve-3d;
            perspective: 1000px;
            position: relative;
            overflow: hidden;
        }

        /* Interactive 3D Hover Tilt & Ambient Pastel Glow */
        .pastel-bento-card:hover {
            transform: perspective(1000px) translateZ(10px) rotateX(3deg) rotateY(-2deg);
            box-shadow: 0 20px 40px -10px rgba(124, 58, 237, 0.2), 0 0 25px rgba(56, 189, 248, 0.2);
            border-color: #C084FC;
        }

        .pastel-bento-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 5px;
            background: linear-gradient(90deg, #A78BFA, #38BDF8, #34D399, #F472B6);
            opacity: 0.85;
        }

        .pastel-tag {
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.8px;
            color: #6D28D9;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .pastel-value {
            font-size: 38px;
            font-weight: 800;
            color: #4C1D95;
            line-height: 1.1;
        }

        .pastel-sub {
            font-size: 13px;
            font-weight: 600;
            color: #2563EB;
            margin-top: 8px;
        }

        .pulse-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background-color: #8B5CF6;
            display: inline-block;
            animation: pulseGlow 2s infinite;
        }

        /* Funnel Card List */
        .funnel-pastel-box {
            background: #FFFFFF;
            border: 2px solid #E0E7FF;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.05);
        }

        .funnel-pastel-item {
            background: #F8FAFC;
            border: 1px solid #EEF2FF;
            border-radius: 14px;
            padding: 14px 18px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.25s ease;
        }
        .funnel-pastel-item:hover {
            border-color: #C084FC;
            background: #FFFFFF;
            transform: translateX(6px);
            box-shadow: 0 4px 15px rgba(167, 139, 250, 0.15);
        }
        .funnel-pastel-label {
            font-weight: 700;
            font-size: 14px;
            color: #4C1D95;
        }
        .funnel-pastel-badge {
            padding: 5px 16px;
            border-radius: 20px;
            font-weight: 800;
            font-size: 13px;
        }
        .badge-pending-pastel { background: #FEF3C7; color: #B45309; border: 1px solid #FDE68A; }
        .badge-approved-pastel { background: #EDE9FE; color: #6D28D9; border: 1px solid #DDD6FE; }
        .badge-posted-pastel { background: #D1FAE5; color: #047857; border: 1px solid #A7F3D0; }

        /* Scrollytelling Pastel Cards */
        .scrolly-pastel-card {
            background: #FFFFFF;
            border: 2px solid #E0E7FF;
            border-left: 6px solid #8B5CF6;
            border-radius: 18px;
            padding: 22px 26px;
            margin-bottom: 16px;
            box-shadow: 0 6px 20px rgba(139, 92, 246, 0.06);
            transition: all 0.3s ease;
        }
        .scrolly-pastel-card:hover {
            border-left-color: #EC4899;
            transform: translateX(8px);
            box-shadow: 0 10px 30px rgba(236, 72, 153, 0.15);
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="pastel-title-header">📊 Executive Business Analytics Dashboard</div>', unsafe_allow_html=True)
    st.caption("ศูนย์วิเคราะห์ข้อมูลเชิงกลยุทธ์ | ธีมพาสเทลหรูหรา (Pastel Luxury System & 3D Interactive Effects)")

    st.markdown("<br>", unsafe_allow_html=True)

    # Data Fetching
    worksheets = get_all_worksheets()
    affiliates = get_all_affiliate_products()
    fb_posts = get_fb_posts()

    # Metrics
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

    # Bento Grid Cards (Pastel 3D Tilt)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="pastel-bento-card">
            <div class="pastel-tag"><span class="pulse-dot"></span> 💰 REVENUE FORECAST</div>
            <div class="pastel-value">฿{total_projected_rev:,.0f}</div>
            <div class="pastel-sub">🎯 เป้าหมาย: ฿30,000 / เดือน</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="pastel-bento-card">
            <div class="pastel-tag">📚 TPT CONTENT VAULT</div>
            <div class="pastel-value">{total_ws_count} <span style="font-size:18px; color:#64748B;">สื่อ</span></div>
            <div class="pastel-sub" style="color:#64748B;">เฉลี่ย ฿{avg_ws_price:.0f} / ชิ้น</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="pastel-bento-card">
            <div class="pastel-tag">🎬 SHOPEE REELS STUDIO</div>
            <div class="pastel-value">{total_aff_count} <span style="font-size:18px; color:#64748B;">สินค้า</span></div>
            <div class="pastel-sub" style="color:#64748B;">สคริปต์ป้ายยา 100%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="pastel-bento-card">
            <div class="pastel-tag">🎛️ FB QUEUE PIPELINE</div>
            <div class="pastel-value">{total_fb_count} <span style="font-size:18px; color:#64748B;">รายการ</span></div>
            <div class="pastel-sub" style="color:#B45309;">⏳ รอตรวจ: {pending_count} รายการ</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Visual Pastel Analytics (Charts Section)
    c_left, c_right = st.columns([6, 4])
    
    with c_left:
        st.subheader("📈ประมาณการสัดส่วนรายได้ตามโมเดลธุรกิจ (Pastel Revenue Breakdown)")
        
        rev_data = pd.DataFrame({
            "โมเดลธุรกิจ": ["ขายใบงานสื่อการสอน TPT", "ค่าคอมมิชชั่น Shopee Affiliate (FB Reels)"],
            "คาดการณ์รายได้ (บาท)": [projected_tpt_rev, projected_aff_rev]
        })

        chart_rev = alt.Chart(rev_data).mark_bar(cornerRadiusTopLeft=12, cornerRadiusTopRight=12).encode(
            x=alt.X('โมเดลธุรกิจ:N', title=None, axis=alt.Axis(labelAngle=0, labelFont='Prompt', labelFontSize=12)),
            y=alt.Y('คาดการณ์รายได้ (บาท):Q', title="บาท"),
            color=alt.Color('โมเดลธุรกิจ:N', scale=alt.Scale(range=['#8B5CF6', '#38BDF8']), legend=None),
            tooltip=['โมเดลธุรกิจ', 'คาดการณ์รายได้ (บาท)']
        ).properties(height=280)
        
        st.altair_chart(chart_rev, use_container_width=True)

    with c_right:
        st.subheader("📊 สถานะคิวคอนเทนต์ (Content Funnel Status)")
        st.markdown(f"""
        <div class="funnel-pastel-box">
            <div class="funnel-pastel-item">
                <span class="funnel-pastel-label">⏳ รอกรอง (Pending Approval)</span>
                <span class="funnel-pastel-badge badge-pending-pastel">{pending_count} รายการ</span>
            </div>
            <div class="funnel-pastel-item">
                <span class="funnel-pastel-label">✅ อนุมัติแล้ว (Approved)</span>
                <span class="funnel-pastel-badge badge-approved-pastel">{approved_count} รายการ</span>
            </div>
            <div class="funnel-pastel-item">
                <span class="funnel-pastel-label">🚀 โพสต์เรียบร้อย (Published)</span>
                <span class="funnel-pastel-badge badge-posted-pastel">{posted_count} รายการ</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Scrollytelling Report (Pastel Style)
    st.subheader("📖 Scrollytelling: บทวิเคราะห์เชิงกลยุทธ์และการตัดสินใจธุรกิจ")
    st.caption("การเล่าเรื่องผ่านข้อมูลพาสเทลหรูหรา สำหรับครูปอ")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="scrolly-pastel-card">
            <div style="font-weight:800; color:#6D28D9; font-size:16px; margin-bottom:6px;">
                💡 Chapter 1: โอกาสสร้างรายได้ตั้งต้น (Zero-to-One Strategy)
            </div>
            <div style="color:#334155; font-size:14px; line-height:1.6;">
                • <b>สร้างสื่อใบงาน ม.1 แรกในโมดูล 1:</b> เปิดตัวบน TPT Store และเพจ Facebook ห้องเรียนอารมณ์ดี<br>
                • <b>เลือกของใช้ในบ้าน 1 ชิ้นในโมดูล 2:</b> สรุปสคริปต์ Reels 15-30 วินาที สร้างรายได้คอมมิชชั่นแรกทันที
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="scrolly-pastel-card">
            <div style="font-weight:800; color:#6D28D9; font-size:16px; margin-bottom:6px;">
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
        <div class="scrolly-pastel-card">
            <div style="font-weight:800; color:#6D28D9; font-size:16px; margin-bottom:6px;">
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
        <div class="scrolly-pastel-card" style="border-left-color: #10B981; background: #F0FDF4;">
            <div style="font-weight:800; color:#047857; font-size:16px; margin-bottom:6px;">
                📈 Chapter 4: สรุปผลลัพธ์ที่คาดว่าจะได้รับ (Target Milestone)
            </div>
            <div style="color:#166534; font-size:14px; line-height:1.6;">
                สร้างคลังสื่อการสอน 10 ชิ้น + สคริปต์ Reels 10 ชิ้น ภายใน 30 วันแรก คาดการณ์สร้างรายได้เสริม <b>฿30,000+ / เดือน</b> ผ่านระบบอัตโนมัตินี้ครับ!
            </div>
        </div>
        """, unsafe_allow_html=True)
