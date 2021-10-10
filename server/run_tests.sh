start=$(date +%s)
t=10

echo "[STARTING-DJANGO-SERVER]"
python3 manage.py runserver &

sleep 5
python3 -m unittest tests/test_apis.py

sleep $t
python3 -m unittest tests/test_models.py

end=$(date +%s)

echo "Runtime:- $((end - start)) seconds"