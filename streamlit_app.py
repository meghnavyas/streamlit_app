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

# Adding a pick list so users can pick the fruit they want to include
strl.multiselect("Pick some fruits: ", list(fruit_list.index))

# Pulling the above imported data into a dataframe
strl.dataframe(fruit_list)

