from elasticsearch import Elasticsearch
import random
import time
from threading import Thread



class SearchData():

    def __init__(self, thread_num:int = 1, query_per_second: int = 5, es: Elasticsearch = None, duration: int= 5):
        self.thread_num = thread_num
        self.query_per_second = query_per_second
        self.es = es
        self.duration = duration

    def search_data(self):
        # 開 thread_num 個執行緒
        self.threads = []
        start = time.time()
        print(">>>>>> 開始搜尋數據 <<<<<<<<")
        for i in range(self.thread_num):
            self.threads.append(Thread(target=self.search_data_thread))
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()

        print(f">>> 搜尋 {self.thread_num} 個執行緒，每秒 {self.query_per_second} 次，共花費 {time.time() - start} 秒 <<<")

    def search_data_thread(self):
        # 每秒查詢 query_per_second 次
        # 持續 duration 秒
        start = time.time()
        while time.time() - start < self.duration:
            for i in range(self.query_per_second):
                res = self.search()
                print(len(res["hits"]["hits"]))
                time.sleep(1 / self.query_per_second)
        print(">>> 執行緒結束 <<<")


    def search(self):
        query_body = self.get_query_body()
        index = "logstash-*"
        return self.es.search(index=index, body=query_body)    


    def get_query_body(self):
        # 照這個隨機搜一搜 應該要搜某東西的範圍
        # {"@timestamp":"2015-05-18T09:03:25.877Z","ip":"185.124.182.126","extension":"gif","response":"404","geo":{"coordinates":{"lat":36.518375,"lon":-86.05828083},"src":"PH","dest":"MM","srcdest":"PH:MM"},"@tags":["success","info"],"utc_time":"2015-05-18T09:03:25.877Z","referer":"http://twitter.com/error/william-shepherd","agent":"Mozilla/5.0 (X11; Linux x86_64; rv:6.0a1) Gecko/20110421 Firefox/6.0a1","clientip":"185.124.182.126","bytes":804,"host":"motion-media.theacademyofperformingartsandscience.org","request":"/canhaz/gemini-7.gif","url":"https://motion-media.theacademyofperformingartsandscience.org/canhaz/gemini-7.gif","@message":"185.124.182.126 - - [2015-05-18T09:03:25.877Z] \"GET /canhaz/gemini-7.gif HTTP/1.1\" 404 804 \"-\" \"Mozilla/5.0 (X11; Linux x86_64; rv:6.0a1) Gecko/20110421 Firefox/6.0a1\"","spaces":"this   is   a   thing    with lots of     spaces       wwwwoooooo","xss":"<script>console.log(\"xss\")</script>","headings":["<h3>f-i-j-nl-ng</h5>","http://facebook.com/success/lodewijk-van-den-berg"],"links":["daniel-tani@facebook.com","http://nytimes.com/security/kathryn-sullivan","www.nytimes.com"],"relatedContent":[{"url":"http://www.laweekly.com/news/cbs-crew-rat-fink-2368032","og:type":"article","og:title":"CBS Crew Rat Fink","og:description":"Near a couple of auto body shops (and a sharp new Space Invader mosaic that we&#039;ll post soon) near Temple and Westmoreland is a CBS wall with a nice Rat ...","og:url":"http://www.laweekly.com/news/cbs-crew-rat-fink-2368032","article:published_time":"2008-01-14T08:05:26-08:00","article:modified_time":"2014-10-28T14:59:52-07:00","article:section":"News","article:tag":"Mark Mauer","og:image":"http://IMAGES1.laweekly.com/imager/cbs-crew-rat-fink/u/original/2430299/img_2049.jpg","og:image:height":"360","og:image:width":"480","og:site_name":"LA Weekly","twitter:title":"CBS Crew Rat Fink","twitter:description":"Near a couple of auto body shops (and a sharp new Space Invader mosaic that we&#039;ll post soon) near Temple and Westmoreland is a CBS wall with a nice Rat ...","twitter:card":"summary","twitter:image":"http://IMAGES1.laweekly.com/imager/cbs-crew-rat-fink/u/original/2430299/img_2049.jpg","twitter:site":"@laweekly"},{"url":"http://www.laweekly.com/news/push-and-retna-in-koreatown-2368043","og:type":"article","og:title":"Push and Retna in Koreatown","og:description":"Yeah, I originally had this posted this morning as Push &amp; Ayer - Sorry. It looked like a Retna piece, but I saw the Ayer in there and thought that must ...","og:url":"http://www.laweekly.com/news/push-and-retna-in-koreatown-2368043","article:published_time":"2008-01-29T07:28:32-08:00","article:modified_time":"2014-10-28T14:59:54-07:00","article:section":"News","article:tag":"Shelley Leopold","og:image":"http://IMAGES1.laweekly.com/imager/push-and-retna-in-koreatown/u/original/2430376/img_3671.jpg","og:image:height":"360","og:image:width":"480","og:site_name":"LA Weekly","twitter:title":"Push and Retna in Koreatown","twitter:description":"Yeah, I originally had this posted this morning as Push &amp; Ayer - Sorry. It looked like a Retna piece, but I saw the Ayer in there and thought that must ...","twitter:card":"summary","twitter:image":"http://IMAGES1.laweekly.com/imager/push-and-retna-in-koreatown/u/original/2430376/img_3671.jpg","twitter:site":"@laweekly"},{"url":"http://www.laweekly.com/news/asylm-ruets-pdb-on-santa-monica-2368012","og:type":"article","og:title":"Asylm, Ruets, PDB on Santa Monica","og:description":"Not a new piece, but a well-hidden gem a little south of Santa Monica Blvd. in an alley off of Heliotrope or Edgemont. I&#039;ve been sitting on this for a w...","og:url":"http://www.laweekly.com/news/asylm-ruets-pdb-on-santa-monica-2368012","article:published_time":"2008-04-22T15:11:15-07:00","article:modified_time":"2014-10-28T14:59:48-07:00","article:section":"News","article:tag":"Culture and Lifestyle","og:image":"http://images1.laweekly.com/imager/asylm-ruets-pdb-on-santa-monica/u/original/2430137/img_5027.jpg","og:image:height":"360","og:image:width":"480","og:site_name":"LA Weekly","twitter:title":"Asylm, Ruets, PDB on Santa Monica","twitter:description":"Not a new piece, but a well-hidden gem a little south of Santa Monica Blvd. in an alley off of Heliotrope or Edgemont. I&#039;ve been sitting on this for a w...","twitter:card":"summary","twitter:image":"http://images1.laweekly.com/imager/asylm-ruets-pdb-on-santa-monica/u/original/2430137/img_5027.jpg","twitter:site":"@laweekly"},{"url":"http://www.laweekly.com/news/laurence-tribe-tangles-with-cbs-and-la-city-hall-2396867","og:type":"article","og:title":"Laurence Tribe Tangles with CBS and L.A. City Hall","og:description":"The United States Court of Appeals for the Ninth Circuit&rsquo;s Courtroom 3 - a miniature auditorium with comfortable, smoked salmon-colored seats - wa...","og:url":"http://www.laweekly.com/news/laurence-tribe-tangles-with-cbs-and-la-city-hall-2396867","article:published_time":"2008-06-04T14:16:10-07:00","article:modified_time":"2014-11-26T14:43:59-08:00","article:section":"News","og:site_name":"LA Weekly","twitter:title":"Laurence Tribe Tangles with CBS and L.A. City Hall","twitter:description":"The United States Court of Appeals for the Ninth Circuit&rsquo;s Courtroom 3 - a miniature auditorium with comfortable, smoked salmon-colored seats - wa...","twitter:card":"summary","twitter:site":"@laweekly"}],"machine":{"os":"win xp","ram":3221225472},"@version":"1"}
        # 搜尋 @timestamp 在某個範圍 不要太大
        #  搜尋 2015-05-18 到 2015-05-20 23:59:59 的數據
        # 根據上面的資料 找點能隨機搜出東西的 來建立 query_body
        query_body = {
            "size": 1000,
            "query": {
                "bool": {
                    "must": [ # must, filter, must_not, should
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": "2015-05-18",
                                    "lt": "2015-05-21"
                                }
                            }
                        }
                    ]
                }
            }
        }
        queries = [
            {
                "match": {
                    "response": "404"
                }
            },
            {
                "term": {  # 精準搜尋
                    "geo.src": "PH"
                }
            },
            {
                "match": { # 有 analysis的分數
                    "agent": "Mozilla"
                }
            },
            {
                "wildcard": {
                    "referer": "http*"
                }
            }
        ]
        
        query_condition = random.choice(queries)
        query_body["query"]["bool"]["must"].append(query_condition)
        
        return query_body

if __name__ == '__main__':
    thread_num = 10
    query_per_second = 25
    duration = 20
    es = Elasticsearch("http://localhost:9200")
    # 先測試連線 如果沒有就退出吧
    if not es.ping():
        print("Elasticsearch 連線失敗")
        exit()
    search_data = SearchData(thread_num, query_per_second, es, duration)
    search_data.search_data()