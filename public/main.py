from lxml import html
import requests
import time
import sendmail

url = "https://topmall.pt.aliexpress.com/store/group/Brazil-stock/527978_509576539.html"

def get_data():
    page = requests.get(url)
    tree = html.fromstring(page.content)

    sorry = tree.xpath("//span[@class='sorry']/text()")

    return "Lamentamos" not in sorry
def main():
    sent = False
    while True:
        here = get_data()
        if here:
            print "CHEGOU PORRA"
            if not sent:
                sendmail.send_email()
                sent = True
        else:
            print "AINDA NAO CHEGOU"
        time.sleep(10)
main()
