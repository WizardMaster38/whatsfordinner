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
            recipes: tuple((int, str, int, int, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str))[1] = {
                tuple((0, "Omelette", 6, 1, "Egg", "2", "Water", "2 Tbsp", "Salt", "Pinch", "Pepper", "Pinch", "", "", "", "", "", "", "", "", "", "", "", "", "https://www.eggs.ca/recipes/basic-omelette")),
                
            }
            for recipe in recipes:
                cursor.execute('''INSERT INTO RECIPES VALUES {}'''.format(recipe))


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