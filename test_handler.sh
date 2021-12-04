#!/bin/bash

execution="\e[0;36m[INFO]\e[0m"

start=$(date +%s)

echo "$execution [RUNNING SERVER]"
#START SERVER
. ./run_server.sh

echo "$execution [SERVER-BOOT-COMPLETE]"
#Find tests
sleep 10s

echo "$execution [STARTING TESTS]"

cd server

echo "$execution [RUNNING TESTS]"

python3 test_runner.py

echo "$execution [STOPPING AND CLEANING UP]"

end=$(date +%s)

echo "Runtime:- $((end - start)) seconds"
