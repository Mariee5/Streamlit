import streamlit as st
import pandas as pd
import streamlit_option_menu
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Who are we?", "Upload Data", "Visualize"],
        icons=["house", "book", "envelope", "cloud-upload", "table", "bar-chart"],
        menu_icon="cast",
        default_index=0,
    )

# Home Section
if selected == "Home":
    st.title("Welcome to Visualize Easy! 📊")
    st.header("Your own Graph Visualizer")
    st.write("***A handy option for you to analyse and visualize your data one click away!***")
    
    st.image("E:\\graph (2).png")
    st.markdown("-------------------------")
    st.header("All you have to do is 3 simple steps!")
    st.markdown("<h3 style='color:red;'>1. Upload your dataset</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:yellow;'>2. Choose your requirements from the drop-down</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:green;'>3. Voila! Here is your Chart!</h3>", unsafe_allow_html=True)
    

# Projects Section
elif selected == "Who are we?":
    st.title("Who are we? 🌍")
    st.header("Our Journey 🚀")
    st.write("We started **Visualize Easy** with a simple goal: to make data visualization **accessible and intuitive** for everyone! 📊")
    
    col1, col2 = st.columns([1,2,])
    with col1:
        st.image("C:\\Users\\shobh\\Desktop\\APP\\who_image.jpg",width=500)

    with col2:
        st.image("C:\\Users\\shobh\\Desktop\\APP\\graph33.png",width=500)

    
    st.header("Why Choose Us?")
    st.markdown("✅ **User-Friendly Interface** - Simple and interactive design for ease of use.")
    st.markdown("✅ **Multiple Graph Options** - Choose from bar charts, scatter plots, pie charts, and more.")
    st.markdown("✅ **Quick & Efficient** - Get your data visualized in just a few clicks!")
    
    st.write("Join us in making data more **insightful and fun!**")

elif selected == "Upload Data":
    st.title("📂 Upload Your Dataset")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"], help="Upload a CSV file to explore data and visualize graphs.")
    if uploaded_file is not None:
        st.session_state['df'] = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")

    if st.button("View Data"):
        if 'df' in st.session_state:
            st.dataframe(st.session_state['df'].head())
        else:
            st.warning("⚠️ No file uploaded yet. Please upload a CSV file first.")

        

# Visualization Section
elif selected == "Visualize":
    st.title("📈 Visualize Data with Different Graphs")
    if 'df' in st.session_state:
        df = st.session_state['df']
        df_numeric = df.select_dtypes(include=['number'])  # Ensure only numeric data is used for correlations
        columns = df.columns.tolist()
        
        col_x = st.selectbox("🔹 Select X-axis", columns)
        col_y = st.selectbox("🔹 Select Y-axis", columns)
        chart_type = st.selectbox("📊 Select Chart Type", ["All", "Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "Heatmap"])
        
        st.subheader("🖼️ Generated Graphs")
        
        if chart_type == "All":
            col1, col2 = st.columns(2)
            with col1:
                fig, ax = plt.subplots()
                sns.barplot(x=df[col_x], y=df[col_y], ax=ax, palette="coolwarm")
                st.pyplot(fig)
            with col2:
                fig, ax = plt.subplots()
                sns.lineplot(x=df[col_x], y=df[col_y], ax=ax, color="blue")
                st.pyplot(fig)
            
            col3, col4 = st.columns(2)
            with col3:
                fig, ax = plt.subplots()
                sns.scatterplot(x=df[col_x], y=df[col_y], ax=ax, color="green")
                st.pyplot(fig)
            with col4:
                fig = px.pie(df, names=col_x, values=col_y, color_discrete_sequence=px.colors.sequential.RdBu)
                st.plotly_chart(fig)
            
            st.subheader("📊 Heatmap of Correlations")
            fig, ax = plt.subplots()
            sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            fig, ax = plt.subplots()
            if chart_type == "Bar Chart":
                sns.barplot(x=df[col_x], y=df[col_y], ax=ax, palette="coolwarm")
            elif chart_type == "Line Chart":
                sns.lineplot(x=df[col_x], y=df[col_y], ax=ax, color="blue")
            elif chart_type == "Scatter Plot":
                sns.scatterplot(x=df[col_x], y=df[col_y], ax=ax, color="green")
            elif chart_type == "Pie Chart":
                fig = px.pie(df, names=col_x, values=col_y, color_discrete_sequence=px.colors.sequential.RdBu)
                st.plotly_chart(fig)
                fig = None
            elif chart_type == "Heatmap":
                fig, ax = plt.subplots()
                sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", ax=ax)
            
            if fig:
                st.pyplot(fig)
    else:
        st.warning("⚠️ No file uploaded yet. Please upload a CSV file first.")
