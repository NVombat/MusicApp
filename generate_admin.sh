#!/bin/bash
echo "Creating Admin..."

echo "Finding Script..."

cd server
cd admins

echo "Running Admin Generation Script..."

python3 create_admin.py

cd ..
cd ..

echo "Going Back to Project Root..."
