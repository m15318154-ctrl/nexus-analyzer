
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="NEXUS Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("NEXUS Analyzer")
st.caption("Smart Data Analysis Platform")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("File uploaded successfully!")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", len(df))
        col2.metric("Columns", len(df.columns))
        col3.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

        st.subheader("Data Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("Statistics")
        st.dataframe(df.describe())

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        if numeric_columns:
            selected = st.selectbox(
                "Choose a column",
                numeric_columns
            )

            fig = px.histogram(
                df,
                x=selected,
                title=f"Analysis of {selected}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.download_button(
            "Download analyzed data",
            df.to_csv(index=False).encode("utf-8"),
            "nexus_data.csv",
            "text/csv"
        )

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Upload a CSV file to begin.")
      
