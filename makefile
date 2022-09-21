docker-up:
	docker compose up --build -d
	docker exec -it python-pandas-kata python userInterface.py

docker-down:
	docker compose down