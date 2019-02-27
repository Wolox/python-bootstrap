"""docker-compose.yml service as fixture representation."""

service = """

  {0}:
    build: 
      context: ./{0}/
      dockerfile: ./docker/development/Dockerfile
    command: python ./src/__init__.py
    volumes:
      - .:/{0}
    env_file:
      - ./{0}/docker/development/env/public
      - ./{0}/docker/development/env/private
    ports:
      - "{1}:{1}" """