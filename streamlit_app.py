import streamlit as strl
import pandas as pd

strl.title("My Mom's New Healthy Diner")

strl.header('Breakfast Favorites')
strl.text('🥣 Omega 3 & Blueberry Oatmeal')
strl.text('🥗 Kale, Spinach & Rocket Smoothie')
strl.text('🐔 Hard-Boiled Free-Range Egg')
strl.text('🥑🍞 Avocado Toast')

strl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Importing file from S3 bucket using pandas
fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Set fruit as index
fruit_list = fruit_list.set_index('Fruit')

# Adding a pick list so users can pick the fruit they want to include; pre-selected some fruits as an example
fruits_selected = strl.multiselect("Pick some fruits: ", list(fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]

# Pulling the above imported data into a dataframe; display table on app
strl.dataframe(fruits_to_show)

import snowflake.connector
