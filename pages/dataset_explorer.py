import streamlit as st
import matplotlib.pyplot as plt
from utils.visualization import plot_label_distribution

st.set_page_config(page_title="Dataset Explorer", layout="wide")
st.title("Dataset Explorer")

# Access data from session state
df = st.session_state.df

# Show basic dataset info
st.subheader("Dataset Overview")
st.write(f"Number of samples: {df.shape[0]}")
st.write(f"Number of features: {df.shape[1]}")

# Display sample data
st.subheader("Sample Data")
st.dataframe(df.head())

# Show label distribution
st.subheader("Label Distribution")
cols = st.columns(3)
sentiment_columns = ['fuel', 'machine', 'part', 'others', 'price', 'service']

for idx, column in enumerate(sentiment_columns):
    with cols[idx % 3]:
        if column in df.columns:
            fig = plot_label_distribution(df, column)
            st.pyplot(fig)
        else:
            st.warning(f"Column '{column}' not found in dataset.")

# Sample translations by Sentiment
st.subheader("Sample Translations by Sentiment")

# Select sentiment to explore
sentiment_to_explore = st.selectbox(
    "Choose sentiment to explore:",
    sentiment_columns
)

if sentiment_to_explore not in df.columns:
    st.error(f"Sentiment column '{sentiment_to_explore}' not found in dataset.")
else:
    st.write(f"### {sentiment_to_explore.capitalize()} Sentiment Examples")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("#### Negative")
        for _, row in df[df[sentiment_to_explore] == 'negative'].head(3).iterrows():
            st.write(f"- {row['translated']}")

    with col2:
        st.write("#### Neutral")
        for _, row in df[df[sentiment_to_explore] == 'neutral'].head(3).iterrows():
            st.write(f"- {row['translated']}")

    with col3:
        st.write("#### Positive")
        for _, row in df[df[sentiment_to_explore] == 'positive'].head(3).iterrows():
            st.write(f"- {row['translated']}")
