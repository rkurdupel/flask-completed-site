import telebot
from telebot import types
import sqlite3
from settings import *
import time
from app import db, app


def data2():
    conn = sqlite3.connect(PATH_INSTANCE + "coffee_house.db")
    cursor = conn.cursor()
    list_of_all_orders = []
    cursor.execute('''SELECT * FROM receive_order''')
    data = cursor.fetchall()
    #print(data)

    last_order = []
    for order in data:
        print(order[0])
        if order[0] not in last_order:
            #print(1)
            order_details = f"               NEW ORDER | {order[0]} |\n---------------------------------------\n\nOrder details:\n\n{order[8]}                                               ${order[7]} total\n\nCustomer info:\n\n{order[1]}\n{order[2]}\n{order[3]}\n{order[4]}\n{order[5]}\n{order[6]}\n\n---------------------------------------"   
            #print(order_details)
            last_order.append(order[0])
            print(last_order)
        else:
            #print(5)
            print(5)

    
#
while True:
    data2()