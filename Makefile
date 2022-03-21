run: ## Run the test server.
	python manage.py runserver_plus

shell: ## Launch the shell
	python manage.py shell_plus

install: ## Install the python requirements.
	pip install -r requirements.txt

migrations: ## Check for changes.
	python manage.py makemigrations

migrate: ## Run the migration.
	python manage.py migrate

superuser: ## Create a superuser to connect to the admin.
	python manage.py createsuperuser