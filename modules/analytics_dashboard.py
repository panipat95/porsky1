import streamlit as st
import pandas as pd
import altair as alt
from models.database import get_all_worksheets, get_all_affiliate_products, get_fb_posts

def render_analytics_dashboard_module():
    # Google Font Prompt & ui-ux-pro-max Light Mode Styling
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"], .stApp {
            font-family: 'Prompt', -apple-system, sans-serif !important;
            background-color: #F8FAFC !important;
            color: #0F172A !important;
        }

        /* Executive Card Design with Glass Border */
        .exec-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.04);
            transition: all 0.2s ease-in-out;
            margin-bottom: 20px;
        }
        .exec-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 30px -10px rgba(30, 64, 175, 0.08);
            border-color: #CBD5E1;
        }

        .metric-title {
            font-size: 13px;
            font-weight: 600;
            color: #64748B;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            margin-bottom: 8px;
        }
        .metric-value {
            font-size: 34px;
            font-weight: 700;
            color: #1E40AF;
            line-height: 1.1;
        }
        .metric-sub {
            font-size: 13px;
            color: #059669;
            font-weight: 500;
            margin-top: 8px;
        }
        .metric-sub-neutral {
            font-size: 13px;
            color: #64748B;
            margin-top: 8px;
        }

        /* Status Badges */
        .status-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }
        .badge-pending { background-color: #FEF3C7; color: #D97706; }
        .badge-approved { background-color: #DBEAFE; color: #1D4ED8; }
        .badge-posted { background-color: #D1FAE5; color: #059669; }

        /* Modern Insight Box */
        .insight-box {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-left: 4px solid #2563EB;
            border-radius: 12px;
            padding: 20px 24px;
            margin-top: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px -3px rgba(0,0,0,0.03);
        }
        .insight-title {
            font-weight: 600;
            color: #1E40AF;
            font-size: 16px;
            margin-bottom: 6px;
        }
        .insight-text {
            color: #334155;
            font-size: 14px;
            line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.title("📊 Executive Business Dashboard")
    st.caption("ศูนย์รวมสถิติมุมมองระดับผู้บริหารและการตัดสินใจทางธุรกิจ (เริ่มต้นระบบ 0 รายการ)")

    # Data Fetching
    worksheets = get_all_worksheets()
    affiliates = get_all_affiliate_products()
    fb_posts = get_fb_posts()

    # Reset Metrics (Clean zero-state)
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

    # Executive KPI Cards (Row 1)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="exec-card">
            <div class="metric-title">💰 คาดการณ์รายได้รวม/เดือน</div>
            <div class="metric-value">฿{total_projected_rev:,.0f}</div>
            <div class="metric-sub-neutral">เป้าหมาย: ฿30,000 / เดือน</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="exec-card">
            <div class="metric-title">📚 สื่อ TPT ในคลัง</div>
            <div class="metric-value">{total_ws_count} สื่อ</div>
            <div class="metric-sub-neutral">เฉลี่ย ฿{avg_ws_price:.0f} / ชิ้น</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="exec-card">
            <div class="metric-title">🎬 FB Reels & Affiliate</div>
            <div class="metric-value">{total_aff_count} สินค้า</div>
            <div class="metric-sub-neutral">พร้อมสคริปต์ป้ายยา 0%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="exec-card">
            <div class="metric-title">🎛️ คิวโพสต์ Facebook</div>
            <div class="metric-value">{total_fb_count} รายการ</div>
            <div class="metric-sub-neutral">รอตรวจ: <span class="status-badge badge-pending">{pending_count}</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Visual Analytics Section (Charts)
    c_left, c_right = st.columns([6, 4])
    
    with c_left:
        st.subheader("📈 ประมาณการสัดส่วนรายได้ตามโมเดลธุรกิจ (Revenue Stream Breakdown)")
        
        rev_data = pd.DataFrame({
            "โมเดลธุรกิจ": ["ขายใบงานสื่อการสอน TPT", "ค่าคอมมิชชั่น Shopee Affiliate (FB Reels)"],
            "คาดการณ์รายได้ (บาท)": [projected_tpt_rev, projected_aff_rev]
        })

        chart_rev = alt.Chart(rev_data).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
            x=alt.X('โมเดลธุรกิจ:N', title=None, axis=alt.Axis(labelAngle=0)),
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
        
        chart_funnel = alt.Chart(funnel_df).mark_arc(innerRadius=60).encode(
            theta=alt.Theta(field="จำนวน", type="quantitative"),
            color=alt.Color(field="สถานะ", type="nominal", scale=alt.Scale(range=['#D97706', '#1D4ED8', '#059669'])),
            tooltip=['สถานะ', 'จำนวน']
        ).properties(height=300)
        
        st.altair_chart(chart_funnel, use_container_width=True)

    st.divider()

    # Strategic Business Analysis
    st.subheader("🧠 บทวิเคราะห์เชิงกลยุทธ์สำหรับการตัดสินใจต่อไป (Strategic Decision Report)")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">💡 1. โอกาสสร้างรายได้ตั้งต้น (Zero-to-One Strategy)</div>
            <div class="insight-text">
                • <b>เริ่มต้นสร้างสื่อใบงาน ม.1 แรกในโมดูล 1:</b> เพื่อเริ่มเปิดตัวบนเว็บ TPT และเพจ Facebook ห้องเรียนอารมณ์ดี<br>
                • <b>เลือกของใช้ในบ้าน 1 ชิ้นในโมดูล 2:</b> ให้ AI สรุปสคริปต์ Facebook Reels 15-30 วินาที เพื่อสร้างรายได้คอมมิชชั่นแรกทันที
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown(f"""
        <div class="insight-box" style="border-left-color: #059669; background-color: #F0FDF4;">
            <div class="insight-title" style="color: #047857;">📈 เป้าหมายระยะยาว (Target Milestone)</div>
            <div class="insight-text">
                สร้างคลังสื่อการสอน 10 ชิ้น + สคริปต์ Reels 10 ชิ้น ภายใน 30 วันแรก คาดการณ์สร้างรายได้เสริม <b>฿30,000+ / เดือน</b> ผ่านระบบอัตโนมัตินี้ครับ!
            </div>
        </div>
        """, unsafe_allow_html=True)
