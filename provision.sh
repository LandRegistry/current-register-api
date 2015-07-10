source /tmp/.venv/current-register-api/bin/activate

export SETTINGS="config.DevelopmentConfig"

cd /vagrant/apps/current-register-api

python manage.py db upgrade
