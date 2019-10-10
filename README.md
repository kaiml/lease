# env_python

Python project template at VAAK.

## Dependencies:

- [Install Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

## Instructions on how to build the environment:

1. Clone this repository and remove the `.git` dir
2. Rename the repository to a name of your choice
3. Run `pipenv sync --dev` to build the virtual environment

## When In Development:

### 1. Preparing for Local Development

1. Clone the `master` branch of the repository to your local computer
2. Checkout to the branch of your choice
3. Run `git commit --allow-empty -m "init branch"`
to specify that the branch has been created
4. Make a pull-request with the project template
5. If code-review is necessary, request the manager for it

### 2. Before Pushing the Commits:

Before you push your commits, make sure you run the following commands

- `pipenv run format` to automatically format the code
- `pipenv run check` to check if there are any errors

If the CI/CD is properly setup, your code test will fail anyways.

### 3. To run the test locally:

- `pipenv run tox` to invoke testing

## Packages Used for the Python Environment:

- `black` for automatic code formatting
- `flake8` for automatic code review
- `mypy` for automatic type checking
- `tox` for automatic code testing
- `invoke` for invoking command execution
