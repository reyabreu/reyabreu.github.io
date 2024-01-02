---
layout: post
title: Script for Creating New Posts
date: 2024-01-02 00:12:58
tags: web-dev cmd-line python blog
---

In [Jekyll's][jekyll-site] Minima theme, the creation of a new blog post must follow certain formatting rules so its displayed with the appropriate tmestamp. It is a manual process of naming the file accordingly and adding the timestamp, but this is something that definetely had to be automated. I modified a small Python script I found [here][bcongdon-blog] so that it prompts for title and categories and it creates the file just for you - in the right folder.

It's a Python 3 script, name it e.g. `new_post.py` and then run `$>python new_post.py` on the root folder of your your Jekyll site. You can find it at the bottom of this post.  

Remember to add an exclusion for the file in your `_config.yml` if you don't want it processed with the rest of the files in the generated `_site` folder. I am particularly fussy in keeping deployment outputs as tidy as possible. 

```
#new_post.py

from datetime import datetime

TEMPLATE = """\
---
layout: post
title: {0}
date: {1}
tags: {2}
---

"""

if __name__ == "__main__":

    title = input("Title: ")
    categories = input("Categories: ")

    timestamp = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    datestamp = datetime.today().strftime("%Y-%m-%d")

    file_name = datestamp + "-" + "-".join(title.lower().split(" ")) + ".md"

    with open("_posts/" + file_name, "w+") as file:
        file.write(TEMPLATE.format(title, timestamp, categories))
```

[gh-pages]: https://pages.github.com/ 
[markdown-site]: https://www.markdownguide.org/
[jekyll-site]: https://jekyllrb.com/
[bcongdon-blog]: https://benjamincongdon.me/blog/2016/03/21/Jekyll-New-Post-Script/