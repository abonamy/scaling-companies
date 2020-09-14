# Setup

## Virtual Environment

Create a virtual environment
```sh
# outside the repository

python3 -m venv venv3
source venv3/bin/activate
pip install --upgrade pip
```

## Requirements

Create the database
```sh
pip install -r requirements.txt
python manage.py migrate
```

Populate the database
```sh
# move the json file next to the script "db_script.py"
# rename the json file to "data.json"

python db_script.py
```

## Test

```sh
# to keep the test database between each run, add the option "--keepdb"

python manage.py test
```

## Run

```sh
python manage.py runserver
```

# Usage

## Navigation

company list: http://127.0.0.1:8000/company/  
company detail: http://127.0.0.1:8000/company/123/

## API

### Browsable API  

The API uses a pagination system to send up to ten elements per call.  
http://127.0.0.1:8000/api/  
http://127.0.0.1:8000/api/company/  
http://127.0.0.1:8000/api/company/123/  

http://127.0.0.1:8000/api/company.json  
http://127.0.0.1:8000/api/company/123.json  
