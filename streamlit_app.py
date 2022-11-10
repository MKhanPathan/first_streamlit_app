import streamlit
import pandas
import requests

streamlit.title('Breakfast Favorites!')
streamlit.header('Breakfast Menu')
streamlit.text('🍜 Omega 3 & Blueberry Datmeal')
streamlit.text('🌽 Kale, Spinach, Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🍎 Apples')
streamlit.header('🍌 🍑 Build Your Own Fruit Smoothie 🍈 🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display Fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#Normalizing JSON version
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Output to screen as a table
streamlit.dataframe(fruityvice_normalized)
