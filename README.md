# Run the application

First install [uv](https://docs.astral.sh/uv/getting-started/installation/).

When running for the first time, run

uv sync

then to run the app, run

uv run flask --app secret_santa run

## Initialising the database

Before initialising the database, check the set up values in the instance/user-config.ini file. You must update
the admin email and password to your own values first.

The following command initialises the database and adds an admin user and an event using the values in the user-cofig.ini file:

flask --app secret_santa init-db

This will also clear any existing tables and add new ones, so will delete any exisisting data.

## Testing

To run the tests, run:

uv run pytest

To run test coverage, run:

uv run coverage run -m pytest

uv run coverage report

uv run coverage html
