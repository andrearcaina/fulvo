# fulvo
CPS 510 Database Web UI

## Preamble
This project is a web application that allows users to interact with an Oracle database with populated data. The application will be built using Python and Flask, with SQLAlchemy as the ORM.

## User Requirements
The user will be able to:

1. view all the tables in our database
2. click on buttons that essentially does SQL queries (for example, select all that are skill level advanced)
3. be able to create, read, update, and delete records
4. be able to search for specific records

## Installation Process

Before installing, you will need python installed in your local machine.

```bash
# clone this repo 
> git clone https://github.com/andrearcaina/fulvo

# create a .venv
> python3 -m venv .venv

# activate .venv
> source .venv/bin/activate # with linux or macos
> .venv\Script\activate # with windows

# install dependencies
> pip install -r requirements.txt

# run app
> py app.py
# or
> flask run --debug

```
