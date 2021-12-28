import requests
import bs4


def open_url(url):
    """打开指定url链接的网页

    Args:
        url (string): 网页地址

    Returns:
        response: 页面响应的内容(utf-8)
    """
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    return res

def main():
    # 首页的新闻标题单独处理
    res = open_url('http://www.zsc.edu.cn/newscenter/xxyw/')
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    news = soup.select('#paging > ul > li > span.title > a')
    news_title = []
    for eacher in news:
        news_title.append(eacher.text)

    # 第2~27页的新闻标题单独处理
    for i in range(2,28):
        url = 'http://www.zsc.edu.cn/newscenter/xxyw/index-{}.html'.format(i)
        res = open_url(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        news = soup.select('#paging > ul > li > span.title > a')
        for eacher in news:
            news_title.append(eacher.text)


    # 将提取出来的数据保存到本地记事本
    f = open('news.txt', 'w', encoding='utf-8')
    for eacher in news_title:
        f.write(eacher)
        f.write('\n')
    f.close()



if __name__ == '__main__':
    main()
