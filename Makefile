# Set the default goal if no targets were specified on the command line
.DEFAULT_GOAL = run
# Makes shell non-interactive and exit on any error
.SHELLFLAGS = -ec

PROJECT_NAME=devyatki_appmi


.PHONY: \
  docker-run-dev \
  docker-run-production \
  run-dev \
  run-queue \
  run-bot \
  docker-run-bot \
  run-uvicorn \
  requirements \
  help \
  lint \
  migrate \
  build-frontend \
  test-ci \
  redeploy-production