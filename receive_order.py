import telebot
from telebot import types
import sqlite3
from settings import *
import time
from app import db, app

# def data1():
#     # 1 option
#     
#     conn = sqlite3.connect(PATH_INSTANCE + "coffee_house.db")
#     cursor = conn.cursor()
#     list_of_all_orders = []
#     cursor.execute('''SELECT * FROM receive_order''')
#     data = cursor.fetchall()
#     #print(data) 
#     #return f"{data}"    # data should return as a string otherwise output will be ( 1 )
# 
#     for order in data:
#         #print(order)
#         order_id = order[0]
#         #print(order_id)
#         print(order[0])
#         print(list_of_all_orders)
#         if order[0] in list_of_all_orders:
#             print(1)
#             # list_of_all_orders.append(order_id) # add order id to the list so it won't repeat
#             #print(list_of_all_orders)
#         else:
#             print(5)
#             
#             list_of_all_orders.append(order_id) # add order id to the list so it won't repeat
#             #list_of_all_orders.append(order_id) # add order id to the list so it won't repeat
#             
#             order_details = f"               NEW ORDER | {order[0]} |\n---------------------------------------\n\nOrder details:\n\n{order[8]}                                               ${order[7]} total\n\nCustomer info:\n\n{order[1]}\n{order[2]}\n{order[3]}\n{order[4]}\n{order[5]}\n{order[6]}\n\n---------------------------------------" 
#             #print(order_details)
#         return order_details  

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

    
#while True:
    # data1()
    #data2()
while True:
    data2()