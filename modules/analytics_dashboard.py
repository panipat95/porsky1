import streamlit as st
import pandas as pd
import altair as alt
from models.database import get_all_worksheets, get_all_affiliate_products, get_fb_posts

def render_analytics_dashboard_module():
    # Streamlined Minimalist Executive Theme
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"], .stApp {
            font-family: 'Prompt', -apple-system, sans-serif !important;
            background: #F8FAFC !important;
            color: #0F172A !important;
        }

        .clean-title {
            font-size: 28px;
            font-weight: 800;
            color: #0F172A;
            margin-bottom: 4px;
        }

        /* Clean KPI Bento Cards */
        .clean-kpi-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
            transition: all 0.2s ease;
        }

        .clean-kpi-card:hover {
            border-color: #2563EB;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(37, 99, 235, 0.08);
        }

        .clean-kpi-label {
            font-size: 13px;
            font-weight: 700;
            color: #64748B;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }

        .clean-kpi-value {
            font-size: 34px;
            font-weight: 800;
            color: #2563EB;
            line-height: 1.1;
        }

        .clean-kpi-sub {
            font-size: 13px;
            font-weight: 600;
            color: #059669;
            margin-top: 6px;
        }

        /* Clean Funnel Items */
        .clean-funnel-box {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 20px;
        }

        .clean-funnel-item {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .badge-pending { background: #FEF3C7; color: #B45309; padding: 4px 12px; border-radius: 16px; font-weight: 700; font-size: 12px; }
        .badge-approved { background: #DBEAFE; color: #1D4ED8; padding: 4px 12px; border-radius: 16px; font-weight: 700; font-size: 12px; }
        .badge-posted { background: #D1FAE5; color: #047857; padding: 4px 12px; border-radius: 16px; font-weight: 700; font-size: 12px; }

        .clean-story-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-left: 5px solid #2563EB;
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="clean-title">📊 หน้าหลัก & แดชบอร์ดสรุปรายได้ (Executive Dashboard)</div>', unsafe_allow_html=True)
    st.caption("ศูนย์รวมการวิเคราะห์ข้อมูลและเป้าหมายรายได้ สไตล์คลีน มินิมอล อ่านง่าย คมชัด 100%")

    st.markdown("<br>", unsafe_allow_html=True)

    # Data Fetching
    worksheets = get_all_worksheets()
    affiliates = get_all_affiliate_products()
    fb_posts = get_fb_posts()

    # Core Metrics
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

    # Clean Bento Cards Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="clean-kpi-card">
            <div class="clean-kpi-label">💰 ประมาณการรายได้รวม</div>
            <div class="clean-kpi-value">฿{total_projected_rev:,.0f}</div>
            <div class="clean-kpi-sub">🎯 เป้าหมาย: ฿30,000 / เดือน</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="clean-kpi-card">
            <div class="clean-kpi-label">📚 คลังสื่อการสอน TPT</div>
            <div class="clean-kpi-value">{total_ws_count} <span style="font-size:18px; color:#64748B;">ชิ้น</span></div>
            <div style="font-size:13px; color:#64748B; margin-top:6px;">เฉลี่ย ฿{avg_ws_price:.0f} / ชิ้น</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="clean-kpi-card">
            <div class="clean-kpi-label">🎬 คลังสินค้า Reels</div>
            <div class="clean-kpi-value">{total_aff_count} <span style="font-size:18px; color:#64748B;">รายการ</span></div>
            <div style="font-size:13px; color:#64748B; margin-top:6px;">พร้อมสคริปต์ 100%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="clean-kpi-card">
            <div class="clean-kpi-label">🎛️ คิวโพสต์ Facebook</div>
            <div class="clean-kpi-value">{total_fb_count} <span style="font-size:18px; color:#64748B;">รายการ</span></div>
            <div style="font-size:13px; color:#B45309; margin-top:6px;">⏳ รออนุมัติ: {pending_count} รายการ</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Visual Analytics & Clean Funnel
    c_left, c_right = st.columns([6, 4])
    
    with c_left:
        st.subheader("📈 สัดส่วนรายได้ตามโมเดลธุรกิจ (Revenue Stream Breakdown)")
        
        rev_data = pd.DataFrame({
            "โมเดลธุรกิจ": ["ขายใบงานสื่อ TPT", "ค่าคอม Shopee Affiliate"],
            "คาดการณ์รายได้ (บาท)": [projected_tpt_rev, projected_aff_rev]
        })

        chart_rev = alt.Chart(rev_data).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
            x=alt.X('โมเดลธุรกิจ:N', title=None, axis=alt.Axis(labelAngle=0, labelFont='Prompt', labelFontSize=13)),
            y=alt.Y('คาดการณ์รายได้ (บาท):Q', title="บาท"),
            color=alt.Color('โมเดลธุรกิจ:N', scale=alt.Scale(range=['#2563EB', '#059669']), legend=None),
            tooltip=['โมเดลธุรกิจ', 'คาดการณ์รายได้ (บาท)']
        ).properties(height=260)
        
        st.altair_chart(chart_rev, use_container_width=True)

    with c_right:
        st.subheader("📊 สถานะคิวคอนเทนต์ (Content Funnel)")
        st.markdown(f"""
        <div class="clean-funnel-box">
            <div class="clean-funnel-item">
                <span style="font-weight:700; color:#334155; font-size:14px;">⏳ รอกรองอนุมัติ (Pending)</span>
                <span class="badge-pending">{pending_count} รายการ</span>
            </div>
            <div class="clean-funnel-item">
                <span style="font-weight:700; color:#334155; font-size:14px;">✅ อนุมัติเรียบร้อย (Approved)</span>
                <span class="badge-approved">{approved_count} รายการ</span>
            </div>
            <div class="clean-funnel-item">
                <span style="font-weight:700; color:#334155; font-size:14px;">🚀 โพสต์ขึ้นเพจแล้ว (Published)</span>
                <span class="badge-posted">{posted_count} รายการ</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Clean Strategic Action Plan
    st.subheader("📖 บทวิเคราะห์เชิงกลยุทธ์และการตัดสินใจธุรกิจ (Action Plan)")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="clean-story-card">
            <div style="font-weight:800; color:#1D4ED8; font-size:15px; margin-bottom:4px;">
                💡 Chapter 1: โอกาสสร้างรายได้ตั้งต้น (Zero-to-One Strategy)
            </div>
            <div style="color:#475569; font-size:14px; line-height:1.6;">
                • <b>สร้างสื่อใบงาน ม.1 ในโมดูล 2:</b> เปิดตัวขายบน TPT Store และโปรโมตลงเพจ<br>
                • <b>สร้างสคริปต์ Reels ในโมดูล 3:</b> ทำคลิป Reels 15-30 วิ ป้ายยาสินค้า Shopee
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="clean-story-card">
            <div style="font-weight:800; color:#1D4ED8; font-size:15px; margin-bottom:4px;">
                🎯 Chapter 2: อัตราส่วนคอนเทนต์ที่เหมาะสม (70/30 Content Ratio)
            </div>
            <div style="color:#475569; font-size:14px; line-height:1.6;">
                • เน้นลงคลิป Reels ป้ายยา <b>70%</b> สลับกับใบงานสื่อการสอน <b>30%</b><br>
                • ปล่อยคลิปเวลา 18:00 - 21:00 น. เพื่อยอด Engagement สูงสุด
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="clean-story-card">
            <div style="font-weight:800; color:#1D4ED8; font-size:15px; margin-bottom:4px;">
                ⚡ Chapter 3: แผนปฏิบัติงาน 4 ขั้นตอน (Action Steps)
            </div>
            <div style="color:#475569; font-size:14px; line-height:1.6;">
                <b>1. เคลียร์คิว:</b> กด อนุมัติยิงโพสต์ขึ้นเพจในโมดูล 4<br>
                <b>2. เพิ่มสินค้า:</b> เลือกของใช้ในบ้าน/โต๊ะครูมาทำสคริปต์ Reels<br>
                <b>3. Bundle สื่อ:</b> รวมชุดใบงานเพิ่มราคาขายเป็น ฿199<br>
                <b>4. ยิงโพสต์อัตโนมัติ:</b> ปล่อยระบบยิงโพสต์ 24 ชม.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="clean-story-card" style="border-left-color: #059669; background: #F0FDF4;">
            <div style="font-weight:800; color:#047857; font-size:15px; margin-bottom:4px;">
                📈 Chapter 4: เป้าหมายรายได้ที่คาดว่าจะได้รับ
            </div>
            <div style="color:#166534; font-size:14px; line-height:1.6;">
                สร้างสื่อ TPT 10 ชิ้น + สคริปต์ Reels 10 ชิ้น ภายใน 30 วัน คาดการณ์สร้างรายได้เสริม <b>฿30,000+ / เดือน</b> ผ่านระบบอัตโนมัตินี้ครับ!
            </div>
        </div>
        """, unsafe_allow_html=True)
