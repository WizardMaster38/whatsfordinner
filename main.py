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
    print('Initializing DB...')
    try:
        recipeDatabase = sqlite3.connect("recipe.db")
        cursor = recipeDatabase.cursor()
        print('DB Initialized.')
    except sqlite3.Error as error:
        print('Failed to connect with DB.', error)
    finally:
        if recipeDatabase:
            cursor.execute("DROP TABLE IF EXISTS RECIPES")
            # i hate working with SQL
            table = """CREATE TABLE RECIPES (
                RecipeID INTEGER NOT NULL,
                RecipeName TEXT NOT NULL,
                TimeToCook INTEGER NOT NULL,
                Ingredient1 VARCHAR(255) NOT NULL,
                Ingredient2 VARCHAR(255) NOT NULL,
                Ingredient3 VARCHAR(255),
                Ingredient4 VARCHAR(255),
                Ingredient5 VARCHAR(255),
                Ingredient6 VARCHAR(255),
                Ingredient7 VARCHAR(255),
                Ingredient8 VARCHAR(255),
                Ingredient9 VARCHAR(255),
                Ingredient10 VARCHAR(255)
            );
            """



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
                recipeDatabase.close()
                DBSetup();
    
    

def Main():
    DatabaseManager.ConnectToServer() 
    

if __name__ == "__main__":
    Main();