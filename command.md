pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker-compuse up --build -d
docker exec -it django_container_mou /bin/sh