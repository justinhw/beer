
### Instructions to populate DB manually

1) Run schema.sql to create the tables
2) Run the copy commands to import the data from CSV files to Postgres (order matters)

> copy categories from '<path_to>/categories.csv' DELIMITERS ',' CSV;

> copy styles from '<path_to>/styles.csv' DELIMITERS ',' CSV;

> copy breweries from '<path_to>/breweries.csv' DELIMITERS ',' CSV;

> copy beers from '<path_to>/beers.csv' DELIMITERS ',' CSV;

> copy geocodes from '<path_to>/geocodes.csv' DELIMITERS ',' CSV;

### Working locally

> source env/bin/activate

