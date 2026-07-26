"""
Facebook Graph API Utility for Auto-posting to Facebook Page
Includes Live Meta API call and Mock fallback for testing without credentials.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

FB_PAGE_ID = os.getenv("FB_PAGE_ID", "")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "")
FB_API_VERSION = os.getenv("FB_API_VERSION", "v19.0")

def post_to_facebook_page(message: str, link: str = None) -> dict:
    """
    ส่งข้อมูลโพสต์ไปยัง Facebook Page ผ่าน Meta Graph API
    หากยังไม่มี Token จะทำการ Mock ส่งสำเร็จเพื่อให้ทดลองระบบได้
    """
    if not FB_PAGE_ID or not FB_PAGE_ACCESS_TOKEN or FB_PAGE_ID == "your_facebook_page_id_here":
        # Mock Response สำหรับทดสอบ
        return {
            "success": True,
            "mock": True,
            "id": "mock_fb_post_123456789",
            "message": "ระบบทำงานในโหมด Simulative (ยังไม่ได้ใส่ FB_PAGE_ACCESS_TOKEN ใน .env)"
        }
    
    url = f"https://graph.facebook.com/{FB_API_VERSION}/{FB_PAGE_ID}/feed"
    payload = {
        "message": message,
        "access_token": FB_PAGE_ACCESS_TOKEN
    }
    if link:
        payload["link"] = link
        
    try:
        response = requests.post(url, data=payload, timeout=10)
        res_json = response.json()
        if response.status_code == 200 and "id" in res_json:
            return {
                "success": True,
                "mock": False,
                "id": res_json["id"],
                "message": "โพสต์ลง Facebook Page เรียบร้อยแล้ว!"
            }
        else:
            return {
                "success": False,
                "mock": False,
                "error": res_json.get("error", {}).get("message", "Unknown Facebook API error")
            }
    except Exception as e:
        return {
            "success": False,
            "mock": False,
            "error": str(e)
        }
