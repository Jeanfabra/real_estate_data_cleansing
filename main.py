import pandas as pd
import numpy as np
import time

def cleaning(df):
    # Cleaning non necessary columns
    df.drop('Unnamed: 0', axis = 1, inplace = True)

    # Separating neighbourhood from city in the location column
    neighbourhood_list = [i.split('-')[0].strip() for i in df['Location']]
    city_list = [i.split('-')[1].strip() for i in df['Location']]
    # Adding new columns to the df
    df.insert(loc = 1, column = 'City', value = city_list)
    df.insert(loc = 2, column = 'Neighbourhodd', value = neighbourhood_list)
    # Deletting the location column which is no longer needed
    df.drop('Location', axis = 1, inplace = True)

    # Cleaning the price column
    df['Price'] = [i.lstrip('$').replace('.','') for i in df['Price']]
    df['Price'] = df['Price'].astype('int64')
    df.rename(columns = {'Price':'Price($)'}, inplace = True)

    # Cleaning the size column
    df['Size'] = [i.replace(',','.').replace('m\u00b2','') for i in df['Size']]
    df['Size'] = df['Size'].astype(float)
    df.rename(columns = {'Size':'Size(m\u00b2'}, inplace = True)

    # Cleaning the rooms column
    df['Rooms'] = [i.replace('ha', '').replace('.','') for i in df['Rooms']]

    # Cleaning the bathrroms column
    df['Bathrooms'] = [i.replace('ba.','').replace('.','').strip() for i in df['Bathrooms']]

    clean_df = df
    return clean_df

def load_file(source):
    df = pd.read_csv(source, encoding = 'utf-8')
    return df

def run():
    source = r"C:\Users\jeanf\OneDrive\Desktop\Estudios\Personal Projects\Finca Raiz\finca_raiz_apartments.csv"
    df = load_file(source)
    print('File loaded')
    clean_df  = cleaning(df)
    print('File cleaned')
    print('Exporting new CSV...')
    clean_df.to_csv('finca_raiz_clean_v1.csv', encoding = 'utf-8', index = False)
    print('File exported.')
    
if __name__ == "__main__":
    run()