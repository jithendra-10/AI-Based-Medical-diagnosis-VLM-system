@echo off
title Backend Server
echo Starting backend server...
cd backend
npm install
echo Backend dependencies installed.
echo Starting Node server...
node server.js