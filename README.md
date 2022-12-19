# Tubi Scraper #

Scrapes all genres in Tubi and populates a MySQL database.

## Uses

As for the specific use, I'm not fully sure. I think some money could be made for anyone
willing to take the time to turn this into a webservice and offer it as a Tubi api.
I don't have the time, but my original thoughts on that we're to use Docker Compose and FastAPI
to pull results and serve them. Idk tho.

## Setup

Before program setup, msedge driver should be set in PATH. Follow the below for
instructions:

https://www.ibm.com/docs/en/rtw/9.0.1?topic=rwut-running-web-ui-tests-in-microsoft-edge-browser

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