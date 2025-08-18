# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col,when_matched
import requests
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


name_on_order = st.text_input("name of smoothie")
st.write("Name of your smoothie will be", name_on_order)
cnx=st.connection("snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('search_on'))
#st.dataframe(data=my_dataframe, use_container_width=True)
#st.stop()
pd_df=my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()

ingredents_list=st.multiselect('choose upto 5 ingredents:',my_dataframe)
if ingredents_list:
    ingredents_string = ''
    for fruit_choose in ingredents_list:
        ingredents_string += fruit_choose + " "
        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        st.write('The search value for ', fruit_chosen,' is ', search_on, '.')

        st.subheader(fruit_choose+'Nutrition Information')
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/"+fruit_choose)
        sf_df=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)
        
    my_insert_smt = """insert into smoothies.public.orders(ingredients,name_on_order) values('""" + ingredents_string + """','"""+name_on_order+"""')"""
    st.write(my_insert_smt)
    time_to_insert=st.button("Submit Order")
    if time_to_insert:
        session.sql(my_insert_smt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")


    


