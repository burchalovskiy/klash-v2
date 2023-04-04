#!/usr/bin/env sh

set -o errexit
set -o nounset

pyclean() {
  # Cleaning cache:
  find . -path ./etc -prune -false |
    grep -E '(__pycache__|\.hypothesis|\.perm|\.cache|\.static|\.py[cod]$)' |
    xargs rm -rf
}

run_ci() {
  echo '[ci started]'
  set -x # we want to print commands during the CI process.
  # Checking if all the dependencies are secure and do not have any
  # known vulnerabilities:
  if [ "$1" = 'fix' ]
  then
    poetry run task isort
    black .
  fi

  if [ "$1" = 'lint' ]
  then
    poetry run task lint
  fi

  if [ "$1" = 'black-lint' ]
  then
    poetry run task black-lint
  fi

  if [ "$1" = 'tests' ]
  then
    poetry run task tests --junitxml=test-reports/report.xml
  fi

  if [ "$1" = 'mypy' ]
  then
    poetry run task mypy-lint
  fi

  if [ "$1" = 'check' ]
  then
    poetry run safety check --full-report

    # Checking `pyproject.toml` file contents:
    poetry check

    # Checking dependencies status:
    pip check
  fi

  set +x

  echo '[ci finished]'
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_ci "$1"
