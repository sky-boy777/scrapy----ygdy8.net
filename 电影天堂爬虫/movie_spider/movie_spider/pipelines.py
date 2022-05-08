# -*- coding: utf-8 -*-
import json


class MovieSpiderPipeline:
    def process_item(self, item, spider):
        """保存数据"""
        # 写入数据到json文档
        with open('movie.json', "a", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")
