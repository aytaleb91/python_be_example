# nodeBE
django backend

## Installation

sudo docker-compose run web  python manage.py makemigrations store --name init_models
sudo docker-compose run web  python manage.py migrate
sudo docker-compose run web  python manage.py loaddata fixture.json

## Usage
