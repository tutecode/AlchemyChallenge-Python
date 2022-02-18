# AlchemyChallenge-Python
 Challenge Data Analytics - Python

## 1. Create Virtual ENV

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
 
## 2. Install libraries

- Create requirements.txt

```bash
touch requirements.txt
```

- Install libraries

```bash
pip3 install -r requirements.txt
```


## 3. Create and connect to the PostgreSQL database server via psql

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
create database cultural;

    CREATE DATABASE
    postgres=#
```

- List of databases

```bash
\l
```

- Connect to database (db)

```bash
\c cultural

    You are now connected to database "gov_db" as user "postgres".
```

- If you want to exit postgresql

```bash
exit
```

## 4. Run

- Run on Terminal

```bash
python3 main.py
```

## Connect to the PostgreSQL database using the psycopg2

- Connect to (db)

```bash
mkdir requirements.txt
```

- Install libraries

```bash
pip3 install -r requirements.txt
```
