from module_package.modules import *


def main():
    web_url = "https://news.ycombinator.com/news"
    list_post = requests_data(web_url)
    show_data(list_post)


if __name__ == '__main__':
    main()
