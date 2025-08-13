#!/bin/bash

# PharmExtract Docker Deployment Script

echo "🚀 Starting PharmExtract Docker deployment..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Build the Docker image
echo "🔨 Building Docker image..."
docker build -t pharmextract:latest .

if [ $? -ne 0 ]; then
    echo "❌ Docker build failed!"
    exit 1
fi

echo "✅ Docker image built successfully!"

# Stop and remove existing container if it exists
echo "🔄 Stopping existing container..."
docker stop pharmextract-app 2>/dev/null || true
docker rm pharmextract-app 2>/dev/null || true

# Run the new container
echo "🚀 Starting PharmExtract container..."
docker run -d \
    --name pharmextract-app \
    -p 5000:5000 \
    --env-file .env \
    --restart unless-stopped \
    pharmextract:latest

if [ $? -eq 0 ]; then
    echo "✅ PharmExtract is now running!"
    echo "🌐 Access the application at: http://localhost:5000"
    echo "📊 Container status:"
    docker ps | grep pharmextract-app
else
    echo "❌ Failed to start container!"
    exit 1
fi

echo ""
echo "📋 Useful commands:"
echo "  View logs: docker logs pharmextract-app"
echo "  Stop app: docker stop pharmextract-app"
echo "  Restart app: docker restart pharmextract-app"
echo "  Remove app: docker rm -f pharmextract-app"
