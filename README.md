# lease

## How to setup jupyter docker environment with linting and formatting

### Setup

Make sure that the port 8888 of your local computer is open.

```bash
docker-compose pull && docker-compose up --build
```

### OPTIONAL: Build from local Dockerfile

When making changes to Dockerfile to build from it.

```bash
docker-compose -f docker-compose.local.yml up --build
```

### Snippets

```py
%load_ext pycodestyle_magic
%flake8_on
```
