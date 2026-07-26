"""
AI Agent Utility Module for Kru Por's All-in-One Ecosystem
Provides structured AI generation for Worksheets, FB Reels Scripts, and FB Captions.
"""

def generate_tpt_worksheet(subject: str, topic: str, grade_level: str = "ม.1") -> str:
    """จำลอง/เรียกใช้ AI ในการสร้างใบงานและสื่อการสอน"""
    content = f"""# ใบงานเรื่อง: {topic}
**วิชา:** {subject} | **ระดับชั้น:** {grade_level}

---

## 📌 จุดประสงค์การเรียนรู้
1. มีความเข้าใจพื้นฐานเกี่ยวกับ {topic}
2. สามารถประยุกต์ใช้ความคิดสร้างสรรค์ในการแก้ปัญหาได้
3. มีวินัยและใฝ่เรียนรู้

---

## 📝 ตอนที่ 1: ตอบคำถามชวนคิด (5 ข้อ)
1. {topic} มีความสำคัญอย่างไรต่อชีวิตประจำวันของนักเรียน?
   *(ตอบ): ................................................................................................*

2. ให้นักเรียนยกตัวอย่างเกี่ยวกับ {topic} มา 3 ข้อ
   *(ตอบ): 1. ..................... 2. ..................... 3. .....................*

3. หากพบปัญหาเกี่ยวกับ {topic} นักเรียนจะมีวิธีแก้ไขอย่างไร?
   *(ตอบ): ................................................................................................*

---

## 🎯 ตอนที่ 2: กิจกรรมปฏิบัติการกลุ่ม
ให้นักเรียนจับคู่ สรุปองค์ความรู้เรื่อง **"{topic}"** เป็นผังความคิด (Mind Map) พร้อมตกแต่งให้สวยงาม

---
*จัดทำโดย: ครูปอ | สื่อการสอนคุณภาพ พร้อมจำหน่ายบน TPT & FB Page*
"""
    return content


def generate_fb_reels_script(product_name: str, key_features: str, price: str = "") -> dict:
    """สร้างสคริปต์ Facebook Reels (15-30 วินาที) พร้อมแคปชั่นป้ายยาสำหรับ FB Reels"""
    
    script = f"""🎬 **สคริปต์ Facebook Reels (15-30 วินาที): {product_name}**

⏱️ **00:00 - 00:03 (Hook หยุดฟีด FB):**
- **มุมกล้อง/ภาพ:** ถือ {product_name} โชว์หน้ากล้องแบบเห็นชัดๆ หรือทำท่าตกใจ!
- **เสียงพูด/ข้อความบนจอ:** "หยุดฟีดก่อน! ใครมีปัญหานี้อยู่ ต้องดูคลิปนี้เลย!"

⏱️ **00:03 - 00:15 (Showcase & Solution):**
- **มุมกล้อง/ภาพ:** สาธิตใช้งานจริงในบ้าน ซูมจุดเด่น: {key_features}
- **เสียงพูด:** "อันนี้คือ {product_name} ลองใช้แล้วชีวิตดีขึ้นมาก จุดเด่นคือ {key_features} งานเนี๊ยบสุดๆ"

⏱️ **00:15 - 00:25 (Call to Action ป้ายยาลงคอมเมนต์/แคปชั่น):**
- **มุมกล้อง/ภาพ:** ชี้ไปที่ช่อง Comment หรือข้อความแคปชั่น
- **เสียงพูด:** "{f'ราคาดีมากแค่ {price} บาท' if price else 'ราคาน่ารักมาก'} พิกัดสั่งซื้อกดที่ลิงก์ในคอมเมนต์ใต้คลิป Reels นี้ได้เลยครับ!"
"""

    caption = f"""🎬✨ Facebook Reels ป้ายยาของดีต้องมีติดบ้าน! 🏡🔥

ใครกำลังตามหา **{product_name}** ตัวนี้ตอบโจทย์มากครับ! ⚡

🌟 **ไฮไลท์เด็ด:**
✅ {key_features}
✅ {f'ราคามิตรภาพ เพียง {price} บาท' if price else 'คุ้มค่าใช้งานยาวนาน'}
✅ ส่งไว สั่งง่ายผ่าน Shopee

👇 **พิกัดสั่งซื้อ (กดลิงก์ด้านล่างหรือในคอมเมนต์ได้เลยครับ):**
[AFFILIATE_LINK_PLACEHOLDER]

---
#FacebookReels #Reels #ShopeeAffiliate #ครูปอป้ายยา #ของดีบอกต่อ #รีวิวของใช้ในบ้าน
"""

    return {
        "script": script,
        "caption": caption
    }


def format_for_facebook(title: str, body_text: str, link: str = "", post_type: str = "general") -> str:
    """จัดฟอร์แมตข้อความให้เหมาะกับการโพสต์ Facebook (มีเว้นวรรค มี Emoji ดึงดูดสายตา)"""
    
    emoji_header = "📚✨" if post_type == "tpt" else "🎬🛒"
    
    formatted = f"""{emoji_header} [{title.upper()}] {emoji_header}

{body_text.strip()}
"""
    if link:
        formatted += f"""

👉 **พิกัด / สนใจดูรายละเอียดเพิ่มเติมกดที่นี่:**
🔗 {link}
"""

    formatted += """

---
💙 ถูกใจฝากกด Like 👍 กด Share ↪️ และติดตาม Facebook Reels ของครูปอด้วยนะครับ!
#ครูปอ #สื่อการสอน #FacebookReels #ShopeeAffiliate #ของดีบอกต่อ
"""
    return formatted
