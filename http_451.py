'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk


# get spreadsheet from here http://s3-us-west-1.amazonaws.com/umbrella-static/index.html
# more info https://en.wikipedia.org/wiki/HTTP_451
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
# NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
# DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
# WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Dont forget to tip your server!
# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

import csv
import requests
import random
import time
from fake_useragent import UserAgent
from termcolor import colored
import threading
ua = UserAgent()

top_lst = []
thread_lst = []
MAX_THREADS = 5
sema = threading.Semaphore(value=MAX_THREADS)

blacklisted_words = ["localhost", "mail.", "ntp.", "ftp.", "smtp.", "imap."]
scan_methods = ["quick", "deep", "ultimate"]
SCAN_METHOD_SET = ""

print("[+]visit ... https://github.com/tg12/ for more info about this tools and others")


def check_response(site):
    try:
        sema.acquire()
        r = requests.get("http://" + str(each), headers=headers, timeout=5)
        if int(r.status_code) == 200:
            print(colored("[+]debug, ok", 'green'))
        elif int(r.status_code) == 451:  # yes, 451
            b_censor = True
            print(colored("[+]debug, !!WARNING!!", 'yellow'))
            print(colored("[+]debug, !!Your ISP maybe censoring you!!", 'red'))
            print(colored("[+]debug, !!WARNING!!", 'yellow'))
            print(r.text)
        sema.release()
    except BaseException:
        pass
        sema.release()


while True:
    prompt = input("Pick one (quick,deep,ultimate): ")
    if any(s in str(prompt) for s in scan_methods):
        print(colored("You picked..." + str(prompt), 'green'))
        SCAN_METHOD_SET = prompt
        break
    else:
        print("Try again")

if SCAN_METHOD_SET == "quick":
    print(colored("[+]debug, !!WARNING!!", 'yellow'))
    print(
        colored(
            "[+]debug, Use this for testing mainly or run a few times",
            'red'))
    print(colored("[+]debug, !!WARNING!!", 'yellow'))
    hosts_to_scan = 50
elif SCAN_METHOD_SET == "deep":
    hosts_to_scan = 5000
elif SCAN_METHOD_SET == "ultimate":
    hosts_to_scan = 50000
else:
    hosts_to_scan = 1000000

fin = open(r"top-1m.csv")
cin = csv.reader(fin)

for row in cin:
    if any(s in str(row[1]) for s in blacklisted_words):
        print(colored("[-] debug, ignoring..." + str(row[1]), 'red'))
    else:
        top_lst.append(row[1])
fin.close()

# for each in sorted(top_lst):
# print (each + "\n")

headers = {'User-Agent': ua.random}
# print (headers)

b_censor = False

for each in random.choices(sorted(top_lst), k=hosts_to_scan):
    site = "http://" + str(each)
    thread_lst = [t for t in thread_lst if not t.is_alive()]
    if len(thread_lst) > 3:
        timeDelay = random.randrange(0, 15)
        time.sleep(timeDelay)
        print(colored("[+]debug, just waiting, thread sanity", 'yellow'))
    try:
        thread = threading.Thread(target=check_response, args=(site,))
        thread_lst.append(thread)
        thread.start()
    except BaseException:
        print(colored("[+]debug, scanning...", 'yellow'))
        pass

while True:
    if len(thread_lst) > 0:
        thread_lst = [t for t in thread_lst if not t.is_alive()]
        print(colored("[+]debug, just waiting, thread sanity", 'yellow'))
        timeDelay = random.randrange(0, 50)
        time.sleep(timeDelay)
    else:
        print(colored("[+]debug, finishing up!", 'yellow'))
        break

if b_censor:
    print(colored("[+]debug, !!WARNING!!", 'yellow'))
    print(colored("[+]debug, !!Your ISP maybe censoring you!!", 'red'))
    print(colored("[+]debug, !!WARNING!!", 'yellow'))
    print("[+]visit ... https://github.com/tg12/RUBC/ for more info")
else:
    print(colored("[+]debug, OK!", 'blue'))
    print(
        colored(
            "[+]debug, Consider donating to the eff or tor project or this project of many other projects that work tirelessly to protect your online freedom",
            'blue'))
