import pandas as pd

def get_dataframe_from_web(url):
    """
    This function takes a URL of a webpage containing an HTML table and returns a pandas DataFrame.
    In particular, the firts table of the webpage is returned.

    Parameters:
    url (str): The URL of the webpage containing the HTML table.

    Returns:
    df (DataFrame): A pandas DataFrame containing the data from the HTML table.

    Raises:
    ValueError: If the URL does not contain a valid HTML table, or if other error occurs during the reading process.
    """
    try:
        # Use the pandas read_html function to read the HTML table into a list of DataFrames
        dfs = pd.read_html(url)

        # Check if any tables were found
        if not dfs:
            raise ValueError("No tables found at the provided URL")

        # Return the first table found
        return dfs[0]

    except Exception as e:
        # If an error occurs, raise it
        raise ValueError(f"An error occurred while trying to read the HTML table: {e}")

