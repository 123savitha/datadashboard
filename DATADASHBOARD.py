import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard Title
st.title("✨ADVANCED DATA DASHBOARD✨")

# Moving Blue Gradient Background
moving_blue_gradient_style = """
    <style>
    .main {
        background: linear-gradient(270deg, #1e3c72, #2a5298, #6dd5ed, #2193b0);
        background-size: 400% 400%;
        animation: gradientAnimation 10s ease infinite;
        padding: 10px;
        border-radius: 10px;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .block-container {
        padding: 2rem 1rem;
    }
    </style>
"""
st.markdown(moving_blue_gradient_style, unsafe_allow_html=True)

# Custom Text Input and Button Style
text_input_style = """
    <style>
    .stTextInput>div>div>input {
        background-color: #e6f7ff;
        color: #333;
        font-size: 18px;
        border: 2px solid #1e3c72;
        border-radius: 10px;
        padding: 10px;
        transition: 0.3s;
    }

    .stTextInput>div>div>input:focus {
        border-color: #4a90e2;
        box-shadow: 0 0 10px rgba(30, 60, 114, 0.7);
    }

    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #6dd5ed;
        box-shadow: 0 0 15px rgba(30, 60, 114, 0.5);
    }
    </style>
"""
st.markdown(text_input_style, unsafe_allow_html=True)

# File Upload
upload = st.file_uploader("📂 Upload Your File", type="csv")

if upload is not None:
    df = pd.read_csv(upload)
    
    # Data Preview Section
    st.subheader("🔎 Data Preview")
    st.dataframe(df.head(5), height=200)

    st.divider()

    # Data Tail Section
    st.subheader("📊 Data Tail")
    st.dataframe(df.tail(5), height=200)

    st.divider()

    # Drop duplicates
    st.subheader("🧹 Data Cleaning")
    remove_duplicates = st.checkbox("Remove Duplicates")

    if remove_duplicates:
        original_rows = len(df)
        df = df.drop_duplicates()
        cleaned_rows = len(df)
        st.success(f"✅ Removed {original_rows - cleaned_rows} duplicate rows.")
    else:
        st.info("ℹ️ Duplicates not removed. Check the box to clean the data.")

    st.divider()

    # Data Summary Section
    st.subheader("📈 Data Summary")
    st.write(df.describe())
    
    st.divider()

    # Data Filter Section
    st.subheader("🎯 Filter Data")
    col = df.columns.to_list()
    select = st.selectbox("🔍 Select a column to filter:", col)
    
    unique_col = df[select].unique()
    unique_val = st.selectbox("🎛️ Choose a unique value:", unique_col)
    
    # Apply Filter
    filtered_df = df[df[select] == unique_val]
    st.dataframe(filtered_df, height=200)

    st.divider()

    # Plot Section
    st.subheader("📊 Plot Your Data")

    # Select X and Y columns for plotting
    x_col = st.selectbox("📌 Select X-axis:", col, index=0)
    y_col = st.selectbox("📌 Select Y-axis:", col, index=1)

    # Plotting Options
    plot_option = st.selectbox(
        "📈 Select Plot Type:",
        ["Line Plot", "Bar Chart", "Scatter Plot", "Histogram", "Pie Chart"]
    )

    # Generate Plot Button
    if st.button("🚀 Generate Plot"):
        # Plot based on user selection
        if plot_option == "Line Plot":
            fig, ax = plt.subplots()
            ax.plot(df[x_col], df[y_col], color="blue", linewidth=2)
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title("📈 Line Plot")
            st.pyplot(fig)

        elif plot_option == "Bar Chart":
            fig, ax = plt.subplots()
            ax.bar(df[x_col], df[y_col], color="skyblue")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title("📊 Bar Chart")
            st.pyplot(fig)

        elif plot_option == "Scatter Plot":
            fig, ax = plt.subplots()
            ax.scatter(df[x_col], df[y_col], c="red", alpha=0.7)
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title("🔎 Scatter Plot")
            st.pyplot(fig)

        elif plot_option == "Histogram":
            fig, ax = plt.subplots()
            ax.hist(df[y_col], bins=20, color="purple", alpha=0.7)
            ax.set_xlabel(y_col)
            ax.set_ylabel("Frequency")
            ax.set_title("📊 Histogram")
            st.pyplot(fig)

        elif plot_option == "Pie Chart":
            if df[y_col].dtype == "object":
                st.error("❌ Cannot create pie chart from non-numeric values. Select a numeric column.")
            else:
                pie_data = df[y_col].value_counts()
                fig, ax = plt.subplots()
                ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
                ax.set_title("🥧 Pie Chart")
                st.pyplot(fig)

else:
    st.warning("⚠️ Please upload a CSV file to get started!")
