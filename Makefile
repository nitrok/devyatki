# Set the default goal if no targets were specified on the command line
.DEFAULT_GOAL = help

run-bot:  ## Runs telegram bot
	cd src && ./manage.py migrate && pipenv run python bot/main.py

docker-run-bot:
	./manage.py migrate && python3 bot/main.py

fetchdb:
	scp nibbler:/srv/devyatki/storage/devyatki.sqlite storage/


#clean: ## Cleans up database
#	cd src && ./manage.py clean
help:  ## Display this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;32m%-30s\033[0m %s\n", $$1, $$2}'