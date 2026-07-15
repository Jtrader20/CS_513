# CS 513 Project

## About the Repository
This repository is intended store what we've worked on in this project for CS 513

## Data Quality Issues
### July 14, 2026
The potential violations file is to big to push to github. You will have to generate it yourselves to view it. 

To generate the data quality issues report, do the following:
1. Download and extract:
    * Dish.csv
    * Menu.csv
    * MenuItem.csv
    * MenuPage.csv

    And place them inside the `Data/NYPL-menus` directory

2. Pip install `pandas`
3. In the terminal, navigate to `Data Quality Issues`
4. Run `python main.py`
5. The `violations.json` file will be generated

The file `violations.json` should generated a very large file (about 2334175 lines). The JSON document follows this particular format:

```yaml
    files: # list of files
        file: 
            - name
            - columns:
                column:
                    - name
                    - violations:
                        violation:
                            - name
                            - count
                            - row_indexes 
                                # This is honestly where the bulk of the size of the file comes from
                                # If we don't need the row indexes for any cleaning in the future, we can get rid of this by changing the output of each of the violations found in the violation folder
```

Hopefully the file structure of this project works is easy to understand. I've tried to make it so adding/removing what violations should be tested on a column is easy to do, as well as adding new potential violation types.

I've put `violations.json` in the git ignore (for now) as well as the `*.csv` files since I can't push them to github.

I have yet to go through OpenRefine and do a look there at potential spots for cleaning, but I will add a write up of what I find there before the 17th and commit it as soon as I have it done.