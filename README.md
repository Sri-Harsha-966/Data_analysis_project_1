# Crime Data Analysis

This project performs exploratory data analysis (EDA) on crime data downloaded from data.gov.in and visualizes the results using a Streamlit dashboard.

## Description

This project involves downloading a CSV file containing crime data from data.gov.in, using the Pandas library to conduct exploratory data analysis (EDA) on the dataset, and creating an interactive Streamlit dashboard to visualize the crime data.  This allows users to explore and understand trends and patterns in the crime data.

**Note:** This is my first data analysis project. I welcome any feedback and suggestions for improvement!

## Features

* **Data Acquisition**: Downloads crime data from data.gov.in.
* **Exploratory Data Analysis (EDA)**: Uses Pandas to analyze the data, including cleaning, transforming, and summarizing the data. The EDA code is available in the `Analysis.ipynb` Jupyter Notebook.
* **Data Visualization**: Creates an interactive Streamlit dashboard to visualize the data.
* **CSV File Handling**: Reads and processes data from a CSV file.
* **Interactive Dashboard**: Streamlit dashboard with visualizations, including:
    * Crime type distribution (pie chart)
    * Crime locations (map)
    * Crime trends over time (bar charts for year, month, and hour)
* **Crime Type Filtering**: The Streamlit dashboard includes a sidebar that allows you to filter the data by crime type.

## Installation

1.  **Prerequisites:**

    * Python 3 or above
    * pip
    * Jupyter Notebook (For running the EDA script)

2.  **Installation:**

    * Clone the repository:

        ```bash
        git clone [https://github.com/Sri-Harsha-966/Crime_data_analysis](https://github.com/Sri-Harsha-966/Crime_data_analysis)
        ```

    * Navigate to the project directory:

        ```bash
        cd Crime_data
        ```

    * Install the required dependencies:

        ```bash
        pip install pandas streamlit plotly-express streamlit_folium folium
        ```

        *(Ensure you have all the necessary libraries, including `pandas`, `streamlit`, `plotly-express`, `streamlit_folium`, and `folium`.)*

## Usage

1.  **Download the project:**

    * Download the CSV file from https://catalog.data.gov/dataset/crime-data-from-2020-to-present and paste it in the same directory as the scripts.

2.  **Run the scripts:**

    * The project contains the following scripts:
        * `Analysis.ipynb`: A Jupyter Notebook containing the code for Exploratory Data Analysis (EDA).
        * `Dashboard.py`: A Python script that runs the Streamlit dashboard.

    * Run the scripts in the following order:

        1.  **Run the EDA script:** If you want to perform the exploratory data analysis, open and run the `Analysis.ipynb` Jupyter Notebook. This will generate the "Cleaned_Crime_Data.csv" file, which is required for the Streamlit app.
        2.  **Run the Streamlit application:** To start the Streamlit dashboard, use the following command in your terminal:

            ```bash
            streamlit run Dashboard.py
            ```

            

3.  **Interact with the dashboard:**

    * The Streamlit dashboard will open in your web browser. You can then:
        * Filter crime types using the sidebar on the left.
        * View the crime distribution as a pie chart.
        * Explore crime locations on the map.
        * Analyze crime trends over time using the bar charts.

## Contributing

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Submit a pull request with a clear description of your changes.


## Acknowledgments

* Data source: [data.gov.in](https://catalog.data.gov/dataset/crime-data-from-2020-to-present)
* Libraries:
    * [Pandas](https://pandas.pydata.org/)
    * [Streamlit](https://streamlit.io/)
    * [Plotly](https://plotly.com/)
    * [Folium](https://python-visualization.github.io/folium/)
    * [streamlit-folium](https://github.com/randyzwitch/streamlit-folium)
