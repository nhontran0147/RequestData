import requests
from bs4 import BeautifulSoup
from models.post_model import Post
import tkinter as tk
from tkinter import ttk
from tkinter import *


def num_value(text_value):
    temp = text_value.split()
    if len(temp) == 2:
        return int(temp[0])
    else:
        return 0


def requests_data(web_url):
    response = requests.get(web_url)  # Crawl data
    #
    soup = BeautifulSoup(response.content, "html.parser")  # Tach du lieu
    titles = soup.findAll('a', class_='titlelink')  # Phan tich du lieu (title)
    subtexts = soup.findAll('td', class_='subtext')  # Phan tich du lieu (subtext)
    #
    list_post = []
    # # Lan luot lay title, point, creator, comments cua tung Post
    for element_title, element_subtexts in zip(titles, subtexts):
        title = element_title.text
        points_t = element_subtexts.find('span', class_='score')
        points = 0
        comments = 0
        creator = ""
        if points_t is not None:  # Kiem tra Post co point thi se co creator va comment
            points = num_value(points_t.text)
            comments = num_value(element_subtexts.findChildren('a')[3].text)
            creator = element_subtexts.find('a', class_='hnuser').text
        post = Post(title, points, creator, comments)  # khoi tao Post
        list_post.append(post)  # add Post vao Post list
    return list_post


def show_data(list_post):
    win = tk.Tk()
    win.title("Web Data")
    win.geometry("1200x550")

    win.resizable(False, False)
    table = ttk.Treeview(win, height=20)
    table['columns'] = ('post_id', 'post_title', 'post_point', 'post_creator', 'post_comments')

    table.column("#0", width=0, stretch=NO)
    table.column("post_id", anchor=CENTER, width=100)
    table.column("post_title", anchor=CENTER, width=700)
    table.column("post_point", anchor=CENTER, width=100)
    table.column("post_creator", anchor=CENTER, width=100)
    table.column("post_comments", anchor=CENTER, width=100)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("post_id", text="Id", anchor=CENTER)
    table.heading("post_title", text="Title", anchor=CENTER)
    table.heading("post_point", text="Point", anchor=CENTER)
    table.heading("post_creator", text="Creator", anchor=CENTER)
    table.heading("post_comments", text="Comments", anchor=CENTER)

    for i in range(len(list_post)):
        table.insert(parent='', index='end', iid=i + 1, text='',
                     values=(
                         str(i), list_post[i].get_title(), str(list_post[i].get_point()), list_post[i].get_creator(),
                         (list_post[i].get_comments())))
    table.pack()
    win.mainloop()

