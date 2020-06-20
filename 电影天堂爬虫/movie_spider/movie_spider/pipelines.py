# -*- coding: utf-8 -*-
import json

class MovieSpiderPipeline:
    def process_item(self, item, spider):
        #print(item)
        with open('电影.json', "a", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")
