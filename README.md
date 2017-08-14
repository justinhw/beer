
### Instructions to populate DB manually (locally)

1) Run schema.sql to create the tables
2) Run the copy commands to import the data from CSV files to Postgres (order matters)

> copy categories from '<path_to>/categories.csv' DELIMITERS ',' CSV;

> copy styles from '<path_to>/styles.csv' DELIMITERS ',' CSV;

> copy breweries from '<path_to>/breweries.csv' DELIMITERS ',' CSV;

> copy beers from '<path_to>/beers.csv' DELIMITERS ',' CSV;

> copy geocodes from '<path_to>/geocodes.csv' DELIMITERS ',' CSV;

### Working locally for the first time

1) Create a virtualenv if you do not have one https://virtualenv.pypa.io/en/stable/installation/
2) cd into your project directory and run
> virtualenv venv
3) Activate the venv
> source venv/bin/activate
4) Install dependencies
> pip install -r requirements.txt
5) Make sure you have Heroku toolbelt installed
6) Add environment variables to PyCharm
> APP_SETTINGS = config.DevelopmentConfig
> DATABASE_URL = <the url>
7) Make sure PyCharm is using the correct Python interpreter
8) Run! 
