rm db.sqlite3
rm -rf flairsou_api/migrations
rm -rf flairsou_api/__pycache__
rm -rf mock_portail/migrations
rm -rf mock_portail/__pycache__
python manage.py makemigrations flairsou_api
python manage.py migrate

python manage.py shell < create_test_db.py
