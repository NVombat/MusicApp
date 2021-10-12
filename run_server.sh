#!/bin/bash
echo "[STARTING-SERVER] [PORT] 8000"

echo "Looking for application..."
cd server

#STARTING APPLICATION
python3 manage.py runserver 127.0.0.1:8000 &

cd ../
echo "Running Django Server [8000]"