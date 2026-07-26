@echo off
echo ===================================================
echo 🎮 Kru Por AgentOffice - Thai Edition (LM Studio)
echo ===================================================
echo.
echo 1. อย่าลืมเปิดโปรแกรม LM Studio แล้วกด Start Server (http://127.0.0.1:1234)
echo 2. กำลังเริ่มต้นเปิดรัน Backend Server และ Frontend UI...
echo.
cd /d "%~dp0Agent-office-thai"

rem Start Backend Server in background window
start "AgentOffice Backend Server" cmd /c "npm run start --workspace=@agent-office/server"

timeout /t 3 /nobreak >nul

rem Start Frontend UI
start "AgentOffice Frontend UI" cmd /c "npm run dev --workspace=@agent-office/ui"

echo ===================================================
echo 🟢 ระบบเปิดรันเรียบร้อยแล้ว!
echo 🌐 เปิดหน้าจอที่: http://localhost:5173/
echo ===================================================
pause
