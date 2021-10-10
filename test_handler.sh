#!/bin/bash

execution="\e[0;36m[INFO]\e[0m"

echo "$execution [STARTING TESTS]"

#Find tests
sleep 10s

cd server

. ./run_tests.sh

echo "$execution [STOPPING AND CLEANING UP]"