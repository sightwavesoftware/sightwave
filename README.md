# Personal Website

The live application can be found at:
http://joshdwernychuk.com/


# Usage
Currently setup for python 3.6

## Create a Virtual Environment
```
cd agent-quotes
mkvirtualenv --python=$(which python3) agent-quotes
pip install -r requirements/local.txt
```

## Setup Up Postgres
1. Install Postgres [On a Mac: https://postgresapp.com/] - make sure to install the CLI tools as well.
2. Create a database with the dev credentials
```
# create user databaseuser with password 'databasepass';
# create database databasename;
# grant all privileges on database databasename to databaseuser;
```

3. Set up .env file in your local repository
```
vi .env
```
It should look something like this, except for with production credentials.
```
DEBUG=on
SECRET_KEY=SECRET_KEY
DATABASE_URL=psql://databaseuser:databasepass@127.0.0.1:5432/databasename
```
In our example case, it will look like so:
```
DEBUG=on
SECRET_KEY=SECRET_KEY
DATABASE_URL=psql://databaseuser:databasepass@127.0.0.1:5432/databasename
```

## Set up environment variables for VirtualEnv (with virtualenvwrapper)
You can automatically set env vars by adding this to ~/.virtualenvs/<your-virt-env-name>/bin/postactivate:
```
export DJANGO_SETTINGS_MODULE=config.settings.local
export DJANGO_READ_DOT_ENV_FILE=True
```

To make sure this gets cleaned up when you deactivate the virtualenv, add the following to ~/.virtualenv/<your-virt-env-name>/bin/postdeactivate:
```
unset DJANGO_SETTINGS_MODULE
unset DJANGO_READ_DOT_ENV_FILE=True
```

## Migrate
```
./manage.py migrate
```

## Start up Django
```
./manage.py runserver
```

The page should now be visible at:
`localhost:8000/`


## Running Tests
pytest is in use for testing. We can run tests by running:
```
pytest
```
from the agent-quotes directory.
To run tests on specific applications, run:
```
pytest path/to/app
```
Use the -s argument to account for ipdb statements when debugging


## Installing Linters
This repositiory is using Flake8 for Python Linting.
```
# outside your virtualenv
pip install flake8

# find your linter file
hash -r
which flake8 # confirm this returns something
```

## CI
```
tox
```

This will execute both py.test and flake8 linting and output the results (including code coverage numbers to stdout).

If you need to refresh your environment for new/outdated dependencies, run:
```
tox -r
```

CircleCI is currently set up for this repository.
