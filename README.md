# Tubi Scraper #

Scrapes all genres in Tubi and populates a MySQL database.

## Setup

1. Install dependencies with ```pip install -r requirements.txt``` OR run 'setup.bat'
2. Install MySQL, and create a new file in the configs directory called "db.json".
3. Populate the db.json file:

    ```
    {
        "host": "<localhost or remote database address>",
        "database": "<desired database name>",
        "user": "<username>",
        "password": "<password>"
    }

    ```
4. run the main.py file with ```python main.py``` OR run 'run.bat'

## If the above doesn't work:

idc lol i made it for myself

ok, i kind of care.