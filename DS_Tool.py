import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Data Visualization App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    # Load the data
    data = pd.read_csv(uploaded_file)

    st.write("### Uploaded Dataset")
    st.write(data.head())

    # Select column for visualization
    columns = data.columns.tolist()
    column = st.selectbox("Select a column to visualize", columns)

    # Select visualization type
    viz_type = st.radio("Select visualization type", ["Bar Chart", "Histogram"])

    # Identify column type
    if pd.api.types.is_numeric_dtype(data[column]):
        is_categorical = False
    else:
        is_categorical = True

    # Visualize the data
    if viz_type == "Bar Chart" and is_categorical:
        st.write(f"### Bar Chart for {column}")
        value_counts = data[column].value_counts()
        fig, ax = plt.subplots()
        value_counts.plot(kind="bar", ax=ax)
        plt.title(f"Bar Chart of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        st.pyplot(fig)

    elif viz_type == "Histogram" and not is_categorical:
        st.write(f"### Histogram for {column}")
        fig, ax = plt.subplots()
        data[column].plot(kind="hist", bins=25, ax=ax)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        st.pyplot(fig)

    else:
        st.error("Invalid visualization type for the selected column type.")
else:
    st.info("Please upload a CSV file to begin.")
