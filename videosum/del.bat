@echo off

set folder="D:\AiTools\videosum\videos"
cd /d %folder%
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

rem pause