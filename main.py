from tkinter import *
import jsonpickle
import socket


IP = '127.0.0.1'
PORT = 4000


def send_request(action, username=None, password=None):
    request = {
        "action": action,
        "username": username,
        "password": password
    }

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    client.send(jsonpickle.encode(request).encode('utf-8'))

    response_data = client.recv(4096).decode('utf-8')
    response = jsonpickle.decode(response_data)
    client.close()

    return response


root = Tk()
root.title("Admin Panel")

get_info_btn = Button(root, text="Get User Info", command=show_user_info)
get_info_btn.pack(pady=10)

user_listbox = Listbox(root, width=50, height=15)
user_listbox.pack(padx=10, pady=10)


root.mainloop()