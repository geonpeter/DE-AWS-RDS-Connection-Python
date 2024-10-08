﻿# MySQL RDS Connection and Database Creation Script

This Python script connects to an Amazon RDS MySQL instance and creates a new database if it doesn't already exist.

## Features
- Connects to an Amazon RDS MySQL instance using the mysql-connector-python library.
- Creates a database named temp_db if it does not already exist.
- Displays all available databases on the MySQL instance.
- Closes the connection after execution.

## Prerequisites
- Python 3.x
- mysql-connector-python library (Install via pip install mysql-connector-python)
```sql
python python_rds_connection.py

```
## Usage
- Clone the repository.

- Update the host, user, and password variables in the connect_and_create_db() function with your RDS credentials.

- Run the script:
```sql
python python_rds_connection.py

```
