import requests
import re

BASE_URL = 'https://www.reddit.com/r/BlancNoir/comments/8azvhl/blancnoirmissnoir_all_videos/'
PATTERN = re.pattern = re.compile(r'https://openload.co/f/[a-zA-Z0-9]*')

body_request = requests.get(BASE_URL, headers={'User-agent': 'Mozilla xd'})

if body_request.ok:
    print (re.findall(PATTERN, str(body_request.content) ))
    