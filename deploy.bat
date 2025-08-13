@echo off
chcp 65001 >nul
echo 🚀 Starting PharmExtract Docker deployment...

REM Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not running. Please start Docker and try again.
    pause
    exit /b 1
)

REM Build the Docker image
echo 🔨 Building Docker image...
docker build -t pharmextract:latest .

if %errorlevel% neq 0 (
    echo ❌ Docker build failed!
    pause
    exit /b 1
)

echo ✅ Docker image built successfully!

REM Stop and remove existing container if it exists
echo 🔄 Stopping existing container...
docker stop pharmextract-app 2>nul
docker rm pharmextract-app 2>nul

REM Run the new container
echo 🚀 Starting PharmExtract container...
docker run -d --name pharmextract-app -p 5000:5000 --env-file .env --restart unless-stopped pharmextract:latest

if %errorlevel% equ 0 (
    echo ✅ PharmExtract is now running!
    echo 🌐 Access the application at: http://localhost:5000
    echo 📊 Container status:
    docker ps | findstr pharmextract-app
) else (
    echo ❌ Failed to start container!
    pause
    exit /b 1
)

echo.
echo 📋 Useful commands:
echo   View logs: docker logs pharmextract-app
echo   Stop app: docker stop pharmextract-app
echo   Restart app: docker restart pharmextract-app
echo   Remove app: docker rm -f pharmextract-app

pause
