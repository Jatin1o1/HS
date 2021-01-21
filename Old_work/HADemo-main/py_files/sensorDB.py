from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy import select

import time

engine = create_engine('sqlite:///sensors.db',echo = False)

meta=MetaData()

sensors = Table(
   'sensors', meta, 
   Column('sensor_name', String, primary_key = True), 
   Column('board_no', Integer, ), 
   Column('sensor_data', Integer),
   Column('sensor_interval', Integer), ) 

def create_table():
    meta.create_all(engine)


def insert_sensor(name,boardno,data='',interval=''):
    conn= engine.connect()
    com=sensors.insert().values(sensor_name = name, board_no =boardno,sensor_data= data, sensor_interval = interval)
    result=conn.execute(com)

def show_allsensor():
    conn=engine.connect()
    com=sensors.select()
    result=conn.execute(com)
    for _ in result:
        print(_)

def read_sensor(name):
    conn=engine.connect()
    com=sensors.select().where(sensors.c.sensor_name==name)
    result=conn.execute(com)
    m=[i for i in result]
    return m

def update_board_no(name,boardNo ):
    conn=engine.connect()
    com=sensors.update().where(sensors.c.sensor_name==name).values(board_no=boardNo)
    result=conn.execute(com)
    #return result

def update_sensor_data(name,data ):
    conn=engine.connect()
    com=sensors.update().where(sensors.c.sensor_name==name).values(sensor_data=data)
    result=conn.execute(com)
    #return result

def update_sensor_interval(name,interval ):
    conn=engine.connect()
    com=sensors.update().where(sensors.c.sensor_name==name).values(sensor_interval=interval)
    result=conn.execute(com)
    #return result

def delete_sensor(name):
    conn=engine.connect()
    com=sensors.delete().where(sensors.c.sensor_name==name)
    result=conn.execute(com)
    #return result

    
