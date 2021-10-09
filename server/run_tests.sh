start=$(date +%s)
t=15

echo "[STARTING-DJANGO-SERVER]"
python3 manage.py runserver &

sleep 5
python3 -m unittest server/tests/test_app.py

# sleep $t
# python3 -m unittest server/tests/.py

end=$(date +%s)

echo "Runtime:- $((end - start)) seconds"