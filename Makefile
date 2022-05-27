# Set the default goal if no targets were specified on the command line
.DEFAULT_GOAL = help

server2: ## Runs server
	cd src && ./manage.py makemigrations && ./manage.py migrate && ./manage.py createsuperuser && ./manage.py seed --mode=refresh

server: ## Runs server
	cd src && ./manage.py migrate && ./manage.py runserver

server3: ## Runs server
	cd src && ./manage.py makemigrations && ./manage.py migrate && ./manage.py runserver

seed: ## Seeds database
	cd src && ./manage.py seed --mode=refresh

#clean: ## Cleans up database
#	cd src && ./manage.py clean
help:  ## Display this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;32m%-30s\033[0m %s\n", $$1, $$2}'