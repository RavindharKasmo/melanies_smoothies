# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col,when_matched
# Write directly to the app
st.title(f"Example Streamlit App :cup_with_straw: {st.__version__}")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)

st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write("""Choose the smoothie you want in your custom smoothie!""")

import streamlit as st

name_on_order = st.text_input("name of smoothie")
st.write("Name of your smoothie will be", name_on_order)
cnx=st.connection("snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredents_list=st.multiselect('choose upto 5 ingredents:',my_dataframe)
if ingredents_list:
    ingredents_string = ''
    for fruit_choose in ingredents_list:
        ingredents_string += fruit_choose + " "

    # st.write(ingredents_string)
    my_insert_smt = """insert into smoothies.public.orders(ingredients,name_on_order) values('""" + ingredents_string + """','"""+name_on_order+"""')"""
    st.write(my_insert_smt)
    time_to_insert=st.button("Submit Order")
    if time_to_insert:
        session.sql(my_insert_smt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)
   
    


