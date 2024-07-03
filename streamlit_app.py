import pandas as pd
import streamlit as st

st.set_page_config(page_title="Recreating the fast food database on Streamlit", page_icon="🍟")
st.title("🍟 fast food")
st.write(
    """
    Recreating an academic project on fast food nutrition info.
    """
)


# Load the data 
@st.cache_data  # What's the importance of this line?
def load_data():
    df = pd.read_csv("data/fastfood.csv")
    return df


df = load_data()


chains = st.multiselect(
    "Fast Food chains",
    df.restaurant.unique(), 
    ["Mcdonalds", "Chick Fil-A", "Sonic", "Arbys", "Burger King", "Dairy Queen", "Subway", "Taco Bell"],
)

cals = st.slider("Calories", 20, 2430, (20, 2430))

option = st.selectbox("Sort by: ", ("restaurant", "calories") )
if (option == "restaurant"):
    index="restaurant"
    columns="calories"
    values="item"
    aggfunc=','.join
    
elif (option == "calories"):
    index="calories"
    columns="restaurant"
    values="item"
    aggfunc=','.join
    

df_filtered = df[(df["restaurant"].isin(chains)) & (df["calories"].between(cals[0], cals[1]))]


df_reshaped = df_filtered.pivot_table(
    #index="calories", columns="restaurant", values="item"
    #index="restaurant", columns="calories", values="item", aggfunc=','.join, fill_value=""
    index=index, columns=columns, values=values, aggfunc=aggfunc, fill_value=""
)
df_reshaped = df_reshaped.sort_values(by=index, ascending=True)


st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"restaurant": st.column_config.TextColumn("restaurant")},
)



