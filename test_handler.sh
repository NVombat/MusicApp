#!/bin/bash

execution="\e[0;36m[INFO]\e[0m"

echo "$execution [STARTING TESTS]"

#Find tests
sleep 10s

cd server

python3 test_runner.py

echo "$execution [STOPPING AND CLEANING UP]"