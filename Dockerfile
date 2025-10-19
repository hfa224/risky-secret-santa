FROM astral/uv:python3.12-bookworm-slim

# copy the .env file in with a volume

# Copy the project into the image
ADD . /app

EXPOSE 8080

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked
# TODO: add .venv to dockerignore file so it's not copied in

# init-db
RUN uv run flask --app secret_santa init-db

# then run app
CMD ["uv", "run", "waitress-serve", "--port=8080", "--call", "secret_santa:create_app"]
