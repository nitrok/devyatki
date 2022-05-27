# Set the default goal if no targets were specified on the command line
.DEFAULT_GOAL = help

run-bot:  ## Runs telegram bot
	pipenv run python bot/main.py

docker-run-bot:
	python3 bot/main.py

#clean: ## Cleans up database
#	cd src && ./manage.py clean
help:  ## Display this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;32m%-30s\033[0m %s\n", $$1, $$2}'