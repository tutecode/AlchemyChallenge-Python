# AlchemyChallenge-Python
 Challenge Data Analytics - Python

## Create Virtual ENV

1. Open Terminal
2. cd Desktop
3. mkdir AlchemyChallenge-Python
4. cd AlchemyChallenge-Python

- Create env

```bash
virtualenv env
```

https://stackoverflow.com/questions/12728004/error-no-module-named-psycopg2-extensions

- Activate env

```bash
source env/bin/activate
```
 
## Install libraries

- Create requirements.txt

```bash
mkdir requirements.txt
```

- Install libraries

```bash
pip3 install -r requirements.txt
```


## Create and connect to the PostgreSQL database server via psql

- Connect to postgres

```bash
sudo -i -u postgres
```

- Access to PostgreSQL

```bash
psql
```

- Create database (db)

```bash
create database gov_db;

    CREATE DATABASE
    postgres=#
```

- Connect to database (db)

```bash
\c gov_db

    You are now connected to database "gov_db" as user "postgres".
```

- If you want to exit postgresql

```bash
exit
```


## Install libraries

- Create requirements.txt

```bash
mkdir requirements.txt
```

- Install libraries

```bash
pip3 install -r requirements.txt
```