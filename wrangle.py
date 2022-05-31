import env
import pandas as pd
import os

def get_zillow():
    '''
    This function acquires the requisite zillow data from the Codeup SQL database and caches it locally it for future use in a csv 
    document; once the data is accessed the function then returns it as a dataframe.
    '''

    filename = "zillow.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT 
            bedroomcnt, 
            bathroomcnt, 
            calculatedfinishedsquarefeet, 
            taxvaluedollarcnt, 
            yearbuilt, 
            taxamount, 
            fips
        FROM 
            properties_2017 
        JOIN
            propertylandusetype USING (propertylandusetypeid)
        WHERE
            propertylandusedesc = 'Single Family Residential';        
        '''
        url = env.get_db_url('zillow')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  

def wrangle_zillow(df):
    '''
    This function takes in an uncleaned zillow dataframe and peforms various cleaning functions. It returns a cleaned zillow dataframe.
    '''

    # Dropping ALL nulls from the dataset
    df = df.dropna()

    # Getting rid of invalid, wrong, or incorrectly entered data
    df = df[(df.bedroomcnt != 0) & (df.bathroomcnt != 0) & (df.landtaxvaluedollarcnt != 1) & (df.calculatedfinishedsquarefeet >= 70)]

    return df
    