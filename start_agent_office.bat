@echo off
echo ===================================================
echo 🎮 Kru Por AgentOffice - Thai Edition (LM Studio)
echo ===================================================
echo.
echo 1. อย่าลืมเปิดโปรแกรม LM Studio แล้วกด Start Server (http://127.0.0.1:1234)
echo 2. กำลังเริ่มต้นเปิดรันหน้าจอ AgentOffice...
echo.
cd /d "%~dp0Agent-office-thai"
cmd /c npm run dev
pause
