# Build the project
echo "Building the project..."
python -m pip3 install -r requirements.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
