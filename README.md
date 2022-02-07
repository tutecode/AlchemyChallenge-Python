# AlchemyChallenge-Python
 Challenge Data Analytics - Python

## Crear Entorno Virtual

1. Open Terminal
2. cd Desktop
3. mkdir AlchemyChallenge-Python
4. cd AlchemyChallenge-Python
5. virtualenv env
6. source enn/bin/activate

## Create GobData-Track

mkdir GobData-Track
cd GobData-Track
mkdir data
mkdir db
touch create_table.sql

## Create database and connect to the PostgreSQL database server via psql

- Connecto to postgres

```bash
sudo -i -u postgres
```

- Access the PostgreSQL

```bash
psql
```

- Create database (db)

```bash
create database govdb;

    CREATE DATABASE
    postgres=#
```

- Connect to database (db)

```bash
\c govdb

    You are now connected to database "govdb" as user "postgres".
```

exit