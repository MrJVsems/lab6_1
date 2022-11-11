from sqlalchemy_schemadisplay import create_schema_graph
import psycopg2
from sqlalchemy import (MetaData, Table, Column)
import pymysql
graph = create_schema_graph(metadata=MetaData("postgresql+psycopg2://ygbhhkvrjjncjc:4f706a9ed6fa5c879457da9d2f4f676d4"
                                              "9253f5605c56ab3e4f27b64a10cf9cb@ec2-34-200-205-45.compute-1.amazonaws."
                                              "com:5432/darc6fl64tvoiu"))
graph.write_png('erd_from_heroku.png')

graph = create_schema_graph(metadata=MetaData("mysql+pymysql://root:root@localhost/sidiscode"))
graph.write_png('erd_from_pc.png')