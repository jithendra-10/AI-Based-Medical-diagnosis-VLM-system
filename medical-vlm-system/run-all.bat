@echo off
start "Backend Server" cmd /k "cd backend && npm install && node server.js"
start "Frontend Server" cmd /k "cd frontend && npm install && npm start"