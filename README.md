# University Management System
-- Team Tondy

## Members
* Ganeshan M
* Ron Jacob Varghese
* R Ashwin
* Siva Sai Gopaal

## Tech Stack
* Python
* MySQL
* Tkinter

## Setup instructions

### Python
1. Install all requirements from requirements.txt

### MySQL
1. Install MySQL server from official site.
2. Start MySQL server and login as root using `mysql -u root`. 
3. Create a new user named `admin` with password `password`, and grant privileges to all databases.
   ```
   CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';
   ```
4. Login to MySQL with the new account via `mysql -u admin -p` and entering the password set earlier, and create a new database named `univmgmt`
    ```
    CREATE DATABASE univmgmt;
    ```