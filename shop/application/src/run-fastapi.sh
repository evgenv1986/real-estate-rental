#!/bin/bash

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

#echo -e "${YELLOW}Running tests...${NC}"

# Запускаем тесты
#cd /Users/evgeny/Documents/Projects/real_estate_rental/shop/application/src
#
#if [ -f "test/test_main.py" ]; then
#    PYTHONPATH=. python -m pytest test/test_main.py -v
#else
#    echo -e "${YELLOW}No tests found, skipping...${NC}"
#fi

# Проверяем результат тестов
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Tests passed! Starting server...${NC}"
    echo -e "${YELLOW}📡 Server will be available at: http://localhost:8000${NC}"
    echo -e "${YELLOW}📋 API docs: http://localhost:8000/docs${NC}"
    echo "──────────────────────────────────────"

    # Запускаем основное приложение
    python main/main.py
else
    echo -e "${RED}❌ Tests failed! Fix the issues before starting the server.${NC}"
    exit 1
fi