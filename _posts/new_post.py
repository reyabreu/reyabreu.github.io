#new_post.py

from datetime import datetime

TEMPLATE = """\
---
layout:     post
title:      {0}
date:       {1}
tags:       {2}
---

"""

if __name__ == "__main__":

    title = input("Title:\n")
    categories = input("Categories:\n")

    timestamp = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    datestamp = datetime.today().strftime("%Y-%m-%d")

    file_name = datestamp + "-" + "-".join(title.split(" ")) + ".md"

    with open(file_name, "w+") as file:
        file.write(TEMPLATE.format(title, timestamp, categories))