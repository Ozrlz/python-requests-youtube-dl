import requests
import re
from os import system
from time import sleep

from pdb import set_trace as debug

BASE_URL = 'https://www.reddit.com/r/BlancNoir/comments/8azvhl/blancnoirmissnoir_all_videos/'
PATTERN = re.pattern = re.compile(r'https://openload.co/f/[a-zA-Z0-9-]+')
PATH_FOLDER = '/home/content/'
MINUTES_2_DELAY = 5

body_request = requests.get(BASE_URL, headers={'User-agent': 'Mozilla xd'})

if body_request.ok:
    links_list = re.findall(PATTERN, str(body_request.content) )
    for i in range(len (links_list) ):
        print (links_list[i])
        system('youtube-dl ' + links_list[i] + " --output '/home/content/%(title)s.%(ext)s'")
        sleep(MINUTES_2_DELAY * 60)
        