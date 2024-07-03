import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
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

# Show a multiselect widget with the chains using `st.multiselect`.
chains = st.multiselect(
    "Fast Food chains",
    df.restaurant.unique(),  # What does this line do?
    ["Mcdonalds", "Chick Fil-A", "Sonic", "Arbys", "Burger King", "Dairy Queen", "Subway", "Taco Bell"],
)

'''

# Show a slider widget with the years using `st.slider`.
years = st.slider("Years", 1986, 2006, (2000, 2016))

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["genre"].isin(chains)) & (df["year"].between(years[0], years[1]))]
df_reshaped = df_filtered.pivot_table(
    index="year", columns="genre", values="gross", aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="year", ascending=False)


# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"year": st.column_config.TextColumn("Year")},
)

# Display the data as an Altair chart using `st.altair_chart`.
df_chart = pd.melt(
    df_reshaped.reset_index(), id_vars="year", var_name="genre", value_name="gross"
)
chart = (
    alt.Chart(df_chart)
    .mark_line()
    .encode(
        x=alt.X("year:N", title="Year"),
        y=alt.Y("gross:Q", title="Gross earnings ($)"),
        color="genre:N",
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)

'''