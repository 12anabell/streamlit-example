import pandas as pd
import streamlit as st
from pymongo import MongoClient
import certifi


st.title("Probando conexion a Mongo DB")

def conection():
    return MongoClient("mongodb+srv://anabell2:vtFGJ8w37tzeIDs3@prediccion2024.hq8qgjl.mongodb.net/",tlsCAFile=certifi.where())

conexion = conection()

def getData():
    db = conexion.get_database("Oprediccion")
    collection = db.get_collection("ejemplo1")
    items = collection.find()
    return list(items)

datos = getData()
st.subheader("Datos")
st.dataframe(pd.DataFrame(datos))

dfInventory = pd.read_csv("datoss/Inventory.csv")
st.dataframe(dfInventory.head())

inventoryCollection = dfInventory.to_dict()
