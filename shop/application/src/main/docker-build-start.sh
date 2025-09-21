#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

APP_NAME="fastapi-app"
CONTAINER_NAME="fastapi-container"
PORT=8000

echo -e "${BLUE}Building Docker image...${NC}"

# Stop and remove existing container if it exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo -e "${BLUE}Stopping existing container...${NC}"
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Build the Docker image
docker build -t $APP_NAME .

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Docker image built successfully!${NC}"

    echo -e "${BLUE}Starting container...${NC}"
    docker run -d \
        --name $CONTAINER_NAME \
        -p $PORT:8000 \
        -v $(pwd)/app:/app/app \
        $APP_NAME

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Container started successfully!${NC}"
        echo -e "${GREEN}Application is running at: http://localhost:$PORT${NC}"
        echo -e "${GREEN}API documentation: http://localhost:$PORT/docs${NC}"
        echo -e "${GREEN}Alternative API docs: http://localhost:$PORT/redoc${NC}"

        # Show container logs
        echo -e "\n${BLUE}Container logs:${NC}"
        docker logs -f $CONTAINER_NAME
    else
        echo -e "${RED}Failed to start container!${NC}"
        exit 1
    fi
else
    echo -e "${RED}Failed to build Docker image!${NC}"
    exit 1
fi