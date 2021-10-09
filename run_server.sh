#!/bin/bash
echo "[STARTING-SERVER] [PORT] 8000"

echo "Looking for application..."
cd server

#STARTING APPLICATION
python3 manage.py runserver &

cd ../
echo "Running Django Server [8000]"