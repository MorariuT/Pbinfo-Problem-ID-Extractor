import re

import requests

base_url = "https://www.pbinfo.ro/probleme/";

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

title_to_id = {};
id_to_title = {};

for i in range(1, 4000):
    try:
        req = requests.get(base_url + str(i), headers=headers);

        if(req.status_code != 200): raise Exception("Problem not avalible");

        html = req.text;
        print(base_url + str(i));
        title_find = re.findall(
            pattern=r'<title>.*?</title>',
            string=html
        );

        title = title_find[0].split('|')[0].strip().split(' ')[-1];

        id_to_title[i] = title;
        title_to_id[title] = i;
    except Exception as e:
        print(e)

itt_file = open("pbinfo_id_to_title_map", 'w');
tti_file = open("pbinfo_title_to_id_map", 'w');

itt_file.write(str(id_to_title));
tti_file.write(str(title_to_id));

