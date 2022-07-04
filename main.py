import sqlite3
from tkinter import *
from math import *


class InputManager:
    str = "a"


class Ingredient:
    def __init__(self, name, amount, units):
        self.name = name
        self.amount = amount
        self.units = units


class DBSetup:
    def SetupDB(recipeDatabase, cursor):
        if cursor:
            print('Writing to DB..')
            try:
                cursor.execute("DROP TABLE IF EXISTS RECIPES")
                # i hate sql still
                # nvm i forgot to finish the other one :skull:
                table = """CREATE TABLE RECIPES ( 
                        RecipeID INTEGER PRIMARY KEY NOT NULL,
                        RecipeName TEXT NOT NULL,
                        TimeToCook INTEGER NOT NULL,
                        Servings INTEGER NOT NULL,
                        Ingredient1 VARCHAR(255) NOT NULL,
                        Amount1 TEXT NOT NULL,
                        Ingredient2 VARCHAR(255) NOT NULL,
                        Amount2 TEXT NOT NULL,
                        Ingredient3 TEXT,
                        Amount3 TEXT,
                        Ingredient4 TEXT,
                        Amount4 TEXT,
                        Ingredient5 TEXT,
                        Amount5 TEXT,
                        Ingredient6 TEXT,
                        Amount6 TEXT,
                        Ingredient7 TEXT,
                        Amount7 TEXT,
                        Ingredient8 TEXT,
                        Amount8 TEXT,
                        Ingredient9 TEXT,
                        Amount9 TEXT,
                        Ingredient10 TEXT,
                        Amount10 TEXT,
                        Link TEXT
                    );
                    """
                cursor.execute(table)
                recipes: tuple((int, str, int, int, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str))[10] = {
                    tuple((0, "Omelette", 6, 1, "Egg", "2", "Water", "2 Tbsp", "Salt", "0.0625 Tsp", "Pepper", "0.0625 Tsp",
                           "", "", "", "", "", "", "", "", "", "", "", "", "https://www.eggs.ca/recipes/basic-omelette")),
                    tuple((1, "Pan-Seared Steak", 20, 4, "New York Strip Steaks", "2 lbs", "Cooking Oil", "0.5 Tbsp", "Sea Salt", "1.5 Tsp", "Black Pepper", "1 Tsp",
                           "Unsalted Butter", "2 Tbsp", "Quartered Onions", "2 Cloves", "Rosemary", "1 sprig", "", "", "", "", "", "", "https://natashaskitchen.com/pan-seared-steak/")),
                    tuple((2, "Prime Ribs", 10, 95, "Beef Prime Rib", "5 lbs", "Rosemary", "2 Tsp", "Olive Oil", "0.25 Cups",
                          "Sea Salt", "", "Black Pepper", "2 Tsp", "Minced Garlic", "8 cloves", "Thyme", "1 Tsp", "", "", "", "", "", "", "https://tastesbetterfromscratch.com/prime-rib/#recipe"))


                }
            except sqlite3.Error as error:
                print('Failed to execute.', error)

            try:
                for recipe in recipes:
                    cursor.execute(
                        '''INSERT INTO RECIPES VALUES {}'''.format(recipe))
            except sqlite3.Error as error:
                print('Failed to write to DB.', error)

            try:
                recipeDatabase.commit()
                print('Wrote into DB.')
            except sqlite3.Error as error:
                print('Failed to commit to DB.', error)
        else:
            print('Cursor is broken! Please re-run this code and try again.')
            exit(1)


class DatabaseManager:
    def ConnectToServer():
        print('Initializing DB...')
        try:
            recipeDatabase = sqlite3.connect("recipe.db")
            cursor = recipeDatabase.cursor()
            print('DB Initialized.')
        except sqlite3.Error as error:
            print('Failed to connect with DB.', error)
        finally:
            if recipeDatabase == None:
                return

            if recipeDatabase:
                DBSetup.SetupDB(recipeDatabase, cursor)
                try:
                    cursor.execute('''SELECT * FROM RECIPES''')
                    output = cursor.fetchall()
                    for row in output:
                        print(row)
                except sqlite3.Error as error:
                    print('Failed to read data. ', error)
                finally:
                    if recipeDatabase:
                        recipeDatabase.close()


def Main():
    DatabaseManager.ConnectToServer()


if __name__ == "__main__":
    Main()
