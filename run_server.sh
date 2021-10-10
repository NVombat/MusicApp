#!/bin/bash
echo "[STARTING-SERVER] [PORT] 5000"

echo "Looking for application..."
cd server

#STARTING APPLICATION
exec ./manage.py runserver 127.0.0.1:5000

cd ../
echo "Running Django Server [5000]"