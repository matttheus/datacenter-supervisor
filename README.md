# Datacenter Supervisor

This is a prototype of monitoring of a datacenter.

## Getting Started
```
git clone https://github.com/matttheus/DatacenterSupervisor.git
```

### Prerequisites

What things you need to install to run the project

* [Download Arduino](https://www.arduino.cc/en/Main/Software)

```
sudo apt install -y gcc postgresql postgresql-10 python3-dev libpq-dev virtualenv

sudo service postgresql start
```

### Installing

Create and active the python environment

```
virtualenv venv -p python3

source venv/bin/activate
```

Install the [requirements](https://github.com/matttheus/DatacenterSupervisor/blob/master/requirements.txt)

```
pip install -r requirements.txt
```

Create database. By default the database name which django look for it's `datacentersupervisor` with the password `postgres`. But you
can change this in [settings](https://github.com/matttheus/DatacenterSupervisor/blob/master/datacentersupervisor/datacentersupervisor/settings.py) (in a dictionary called DATABASES) file.

```
sudo su - postgres

psql

ALTER USER postgres WITH password 'postgres';

create database datecentersupervisor;
```

## Demo

First, go the main directory where is the [folder](https://github.com/matttheus/DatacenterSupervisor/tree/master/datacentersupervisor) that contains the `manage.py`, the below command to create the pre-build database tables based in ORM:

```
python manage.py makemigrations

python manage.py migrate
```

Run [module](https://github.com/matttheus/DatacenterSupervisor/blob/master/collects.py) which collect the data from arduino. Localized in root project directory. Remember of change the serial settings in this module.

``` 
python collects.py
```

Run the server

``` 
python manage.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/)
* [Arduino](https://www.arduino.cc/reference/en/)

## Authors

* **Matheus**
* **Roberto**

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/matttheus/DatacenterSupervisor/blob/master/LICENSE) file for details

## Motivation

* This project was created for my class work.
