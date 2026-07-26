import streamlit as st
import pandas as pd
from models.database import add_affiliate_product, get_all_affiliate_products, enqueue_fb_post
from utils.ai_agent import generate_fb_reels_script, format_for_facebook

def render_shopee_affiliate_module():
    st.title("🎬🛒 โมดูล 2: Facebook Reels & Shopee Affiliate Studio")
    st.caption("AI Agent ช่วยดึงไอเดียสินค้า (เน้นของใช้ในบ้าน/ทั่วไป) สรุปสคริปต์ Facebook Reels + แคปชั่นป้ายยาและลิงก์ Affiliate")
    
    tab1, tab2 = st.tabs([
        "🎬 สร้างสคริปต์ Facebook Reels & แคปชั่นป้ายยา",
        "📦 คลังสินค้า Affiliate ที่เคยบันทึก"
    ])
    
    with tab1:
        st.subheader("💡 กรอกข้อมูลสินค้าที่ต้องการสร้างคลิป Facebook Reels")
        
        col1, col2 = st.columns(2)
        with col1:
            product_name = st.text_input("ชื่อสินค้า (ของใช้ในบ้าน/ทั่วไป)", value="แก้วเก็บความเย็นสแตนเลส 304 พร้อมหลอด")
            category = st.selectbox("หมวดหมู่สินค้า", ["ของใช้ในบ้าน", "เครื่องเขียน/อุปกรณ์เรียน", "ไอที/อิเล็กทรอนิกส์", "แฟชั่น/ทั่วไป"])
            affiliate_url = st.text_input("ลิงก์ Shopee Affiliate ของคุณ", value="https://shope.ee/example_affiliate_link")
            
        with col2:
            price = st.text_input("ราคาสินค้า (บาท)", value="159")
            key_features = st.text_area(
                "จุดเด่นสินค้า / คุณสมบัติหลัก", 
                value="เก็บความเย็นได้นาน 24 ชม., ไร้หยดน้ำเกาะข้างแก้ว, มีหูหิ้วพกพาสะดวก, วัสดุสแตนเลสเกรดอาหาร 304"
            )
            
        if st.button("🚀 ให้ AI สรุปสคริปต์ Facebook Reels + แคปชั่นป้ายยา"):
            with st.spinner("AI กำลังวิเคราะห์สินค้าและแต่งสคริปต์ Reels เรียกยอดวิว..."):
                res = generate_fb_reels_script(product_name, key_features, price)
                st.session_state["fb_reels_script_res"] = res
                st.session_state["aff_prod_name"] = product_name
                st.session_state["aff_category"] = category
                st.session_state["aff_url"] = affiliate_url
                
        if "fb_reels_script_res" in st.session_state:
            st.divider()
            res = st.session_state["fb_reels_script_res"]
            
            c_script, c_caption = st.columns(2)
            with c_script:
                st.subheader("🎬 สคริปต์ Facebook Reels (15-30 วินาที)")
                vdo_script_text = st.text_area("สคริปต์สำหรับถ่ายคลิป Facebook Reels", value=res["script"], height=320)
                
            with c_caption:
                st.subheader("✍️ แคปชั่น Facebook Reels พร้อมวางโพสต์")
                final_caption = res["caption"].replace("[AFFILIATE_LINK_PLACEHOLDER]", st.session_state["aff_url"])
                caption_text = st.text_area("แคปชั่น + ลิงก์ Affiliate + Hashtag", value=final_caption, height=320)
                
            st.divider()
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("💾 บันทึกลงคลังสินค้า Affiliate"):
                    prod_id = add_affiliate_product(
                        st.session_state["aff_prod_name"],
                        st.session_state["aff_category"],
                        st.session_state["aff_url"],
                        vdo_script_text,
                        caption_text
                    )
                    st.success(f"บันทึกสินค้าเรียบร้อย! (ID: {prod_id})")
                    
            with col_b2:
                if st.button("📲 ส่งเข้าคิว Facebook Page Manager"):
                    fb_formatted = format_for_facebook(
                        title=f"Facebook Reels ป้ายยา: {st.session_state['aff_prod_name']}",
                        body_text=caption_text,
                        link=st.session_state["aff_url"],
                        post_type="affiliate"
                    )
                    q_id = enqueue_fb_post(
                        source_type="shopee_affiliate",
                        source_id=1,
                        title=f"FB Reels: {st.session_state['aff_prod_name']}",
                        content_formatted=fb_formatted
                    )
                    st.balloons()
                    st.success(f"ส่งเรื่องเข้าศูนย์ควบคุมเพจแล้ว! (Queue ID: {q_id})")

    with tab2:
        st.subheader("📦 สินค้า Shopee Affiliate ทั้งหมด")
        products = get_all_affiliate_products()
        if products:
            df_prod = pd.DataFrame(products)
            st.dataframe(df_prod, use_container_width=True)
        else:
            st.info("ยังไม่มีรายการสินค้า ลองเพิ่มไอเดียแรกใน Tab 1 ได้เลยครับ!")
