"""
Facebook Graph API Utility for Auto-posting to Facebook Page
Includes Live Meta API call, Streamlit Secrets support, and Mock fallback.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Check Environment Variables first, then Streamlit Secrets fallback for Cloud Deployment
FB_PAGE_ID = os.getenv("FB_PAGE_ID", "")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "")
FB_API_VERSION = os.getenv("FB_API_VERSION", "v19.0")

# Streamlit Cloud Secrets Fallback
if not FB_PAGE_ID or not FB_PAGE_ACCESS_TOKEN:
    try:
        import streamlit as st
        if "FB_PAGE_ID" in st.secrets:
            FB_PAGE_ID = st.secrets["FB_PAGE_ID"]
        if "FB_PAGE_ACCESS_TOKEN" in st.secrets:
            FB_PAGE_ACCESS_TOKEN = st.secrets["FB_PAGE_ACCESS_TOKEN"]
        if "FB_API_VERSION" in st.secrets:
            FB_API_VERSION = st.secrets["FB_API_VERSION"]
    except Exception:
        pass


def post_to_facebook_page(message: str, link: str = None) -> dict:
    """
    ส่งข้อมูลโพสต์ไปยัง Facebook Page ผ่าน Meta Graph API
    """
    if not FB_PAGE_ID or not FB_PAGE_ACCESS_TOKEN or FB_PAGE_ID == "your_facebook_page_id_here":
        return {
            "success": True,
            "mock": True,
            "id": "mock_fb_post_123456789",
            "message": "ระบบทำงานในโหมด Simulative (ยังไม่ได้ใส่ FB_PAGE_ACCESS_TOKEN)"
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
