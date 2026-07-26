import streamlit as st
import pandas as pd
import os
from models.database import add_worksheet, get_all_worksheets, enqueue_fb_post
from utils.ai_agent import generate_tpt_worksheet, format_for_facebook
from utils.pdf_generator import create_worksheet_pdf

def render_student_care_tpt_module():
    st.title("🎓 โมดูล 1: ผลิตสื่อการสอน ม.1 & ใบงาน TPT")
    st.caption("AI Agent ช่วยออกแบบใบงานและสื่อการสอน ม.1 พร้อมระบบแปลงเป็น PDF เพื่อนำไปขายบน TPT หรือโพสต์ลง Facebook Page")
    
    tab1, tab2 = st.tabs([
        "📝 AI สร้างใบงาน TPT & ม.1", 
        "📚 คลังสื่อการสอนทั้งหมด"
    ])
    
    # TAB 1: AI สร้างใบงาน TPT
    with tab1:
        st.subheader("🪄 AI Agent สร้างใบงานและสื่อการสอน ม.1")
        col_a, col_b = st.columns(2)
        with col_a:
            subject = st.text_input("ชื่อรายวิชา", value="วิทยาศาสตร์ / สังคมศึกษา")
            topic = st.text_input("หัวข้อบทเรียน/เนื้อหาใบงาน", value="ระบบนิเวศและการปรับตัวของสิ่งมีชีวิต")
        with col_b:
            grade_level = st.selectbox("ระดับชั้น", ["ม.1", "ม.2", "ม.1-ม.3 Integrated"])
            price = st.number_input("ราคาขายตั้งต้นบน TPT / เพจ (บาท)", min_value=0.0, value=59.0, step=10.0)
            
        if st.button("✨ ให้ AI เจนเนื้อหาใบงานแบบ All-in-One"):
            with st.spinner("AI กำลังคิดและออกแบบใบงานคุณภาพสูง..."):
                worksheet_content = generate_tpt_worksheet(subject, topic, grade_level)
                st.session_state["generated_worksheet"] = worksheet_content
                st.session_state["worksheet_title"] = f"ใบงาน {topic} ({grade_level})"
                st.session_state["worksheet_subject"] = subject
                st.session_state["worksheet_price"] = price

        if "generated_worksheet" in st.session_state:
            st.success("สร้างเนื้อหาใบงานสำเร็จแล้ว! ตรวจสอบรายละเอียดด้านล่าง:")
            edited_content = st.text_area("ปรับแก้ไขเนื้อหาใบงานก่อนเซฟ", value=st.session_state["generated_worksheet"], height=300)
            
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("💾 บันทึกลงคลังสื่อ"):
                    ws_id = add_worksheet(
                        st.session_state["worksheet_title"],
                        st.session_state["worksheet_subject"],
                        grade_level,
                        edited_content,
                        st.session_state["worksheet_price"]
                    )
                    st.success(f"บันทึกสื่อลงคลังเรียบร้อย! (ID: {ws_id})")
                    
            with c2:
                if st.button("📄 สร้างไฟล์ PDF (พร้อมขาย)"):
                    pdf_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "exports")
                    pdf_filename = f"worksheet_{topic}.pdf"
                    pdf_path = os.path.join(pdf_dir, pdf_filename)
                    create_worksheet_pdf(st.session_state["worksheet_title"], edited_content, pdf_path)
                    st.success(f"สร้าง PDF สำเร็จที่: {pdf_filename}")
                    
            with c3:
                if st.button("📲 ส่งเข้าคิวโพสต์ Facebook Page"):
                    fb_text = format_for_facebook(
                        title=st.session_state["worksheet_title"],
                        body_text=f"แจกและเปิดขายใบงานคุณภาพ! เรื่อง {topic} สำหรับนักเรียนชั้น {grade_level}\n\nเนื้อหากระชับ มีกิจกรรมกลุ่มและคำถามชวนคิดครบถ้วน!",
                        link="https://www.teacherspayteachers.com/Store/Kru-Por-Studio",
                        post_type="tpt"
                    )
                    post_id = enqueue_fb_post(
                        source_type="tpt_worksheet",
                        source_id=1,
                        title=st.session_state["worksheet_title"],
                        content_formatted=fb_text
                    )
                    st.balloons()
                    st.success(f"ส่งเข้าคิวรอตรวจของครูปอแล้ว! (Queue ID: {post_id})")

    # TAB 2: คลังสื่อการสอน
    with tab2:
        st.subheader("📚 คลังใบงานสื่อการสอนทั้งหมด")
        worksheets = get_all_worksheets()
        if worksheets:
            df_ws = pd.DataFrame(worksheets)
            st.dataframe(df_ws, use_container_width=True)
        else:
            st.info("ยังไม่มีสื่อในคลัง ลองใช้ AI สร้างใน Tab 1 ดูครับ")
