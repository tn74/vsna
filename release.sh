cd frontend 
yarn run build
cd ..
python manage.py migrate
python manage.py collectstatic
