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


def check_page_num(number):
    if number == 0:
        return False
    else:
        return True


def res_page_num(number, check):
    if check:
        number[0] += 1
    else:
        number[0] -= 1


def show_data(web_url):
    list_post = requests_data(web_url)
    web_url_change = web_url[:len(web_url) - 1]
    pos_page = [1]

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
    page_text = StringVar()
    page_text.set("Page: " + str(pos_page[0]))
    lab_num_page = tk.Label(win, textvariable=page_text).place(x=250, y=430)

    def refill_table(list_post_):
        page_text.set("Page: " + str(pos_page[0]))
        for i in range(len(list_post_)):
            table.insert(parent='', index='end', iid=i, text='',
                         values=(
                             str((30*(pos_page[0]-1)) + i + 1), list_post_[i].get_title(), str(list_post_[i].get_point()),
                             list_post_[i].get_creator(),
                             (list_post_[i].get_comments())))

    def show_next_table():
        res_page_num(pos_page, True)
        table.delete(*table.get_children())  # Xoa het du lieu cua table
        list_post_next = requests_data(web_url_change + str(pos_page[0]))
        refill_table(list_post_next)
   

    def show_previous_table():
        if pos_page[0] != 1:
            res_page_num(pos_page, False)
            table.delete(*table.get_children())  # Xoa het du lieu cua table
            list_post_pre = requests_data(web_url_change + str(pos_page[0]))
            refill_table(list_post_pre)

    butt_next = tk.Button(win, text="Next page", width=40, command=show_next_table)
    butt_next.place(x=600, y=430)
    butt_back = tk.Button(win, text="Previous page", width=40, command=show_previous_table)
    butt_back.place(x=300, y=430)

    refill_table(list_post)
    table.pack()
    win.mainloop()
