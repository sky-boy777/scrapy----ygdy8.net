import os
import json
from datetime import datetime
from pymysql import connect


# 连接到MySQL数据库
con = connect(host='localhost', user='root', password='mysql', port=3306,
              db='blog', charset='utf8mb4')
# 创建游标对象
cur = con.cursor()

# 文件正常运行结束标志
flag = False

# 打开文件，循环插入数据库
with open('movie.json', 'r', encoding='utf8') as movies:
    for movie in movies:
        # json转换为dict
        movie = json.loads(movie)
        try:
            sql = """
                    insert into 
                    movie(is_delete,create_time,update_time,title,name,time,image,detail,url,IMDb_score,douban_score) 
                    values(%s, %s, %s, %s,%s,%s,%s, %s, %s,%s,%s);
                    """
            # create_time和update_time字段
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            res = cur.execute(sql, args=[
                        0,     # is_delete
                        time,  # create_time
                        time,  # update_time
                        movie['title'],
                        movie['name'],
                        movie['time'],
                        movie['image'],
                        movie['detail'],
                        movie['url'],
                        movie['IMDb_score'],
                        movie['douban_score']
            ])
            con.commit()  # 提交到数据库
        except Exception as e:
            # 错误写入日志
            with open('error.log', 'a', encoding='utf8') as error:
                error.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                error.write(e)
                error.write('\n')
            continue
    else:
        flag = True
if flag:
    os.rename('movie.json', 'movie'+datetime.now().strftime("%Y%m%d")+'.json')
else:
    os.rename('movie.json', 'movie' + datetime.now().strftime("%Y%m%d") + 'X.json')

cur.close()  # 关闭游标
con.close()  # 关闭连接
