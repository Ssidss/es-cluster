from elasticsearch import Elasticsearch, helpers
import json
from tqdm import tqdm

# 連接 Elasticsearch
es = Elasticsearch("http://localhost:9200") 

# 定義 Index 名稱
INDEX_PREFIX = "logstash-"

# {"index":{"_index":"logstash-2015.05.18","_type":"log"}}
# {"@timestamp":"2015-05-18T09:03:25.877Z","ip":"185.124.182.126","extension":"gif","response":"404","geo":{"coordinates":{"lat":36.518375,"lon":-86.05828083},"src":"PH","dest":"MM","srcdest":"PH:MM"},"@tags":["success","info"],"utc_time":"2015-05-18T09:03:25.877Z","referer":"http://twitter.com/error/william-shepherd","agent":"Mozilla/5.0 (X11; Linux x86_64; rv:6.0a1) Gecko/20110421 Firefox/6.0a1","clientip":"185.124.182.126","bytes":804,"host":"motion-media.theacademyofperformingartsandscience.org","request":"/canhaz/gemini-7.gif","url":"https://motion-media.theacademyofperformingartsandscience.org/canhaz/gemini-7.gif","@message":"185.124.182.126 - - [2015-05-18T09:03:25.877Z] \"GET /canhaz/gemini-7.gif HTTP/1.1\" 404 804 \"-\" \"Mozilla/5.0 (X11; Linux x86_64; rv:6.0a1) Gecko/20110421 Firefox/6.0a1\"","spaces":"this   is   a   thing    with lots of     spaces       wwwwoooooo","xss":"<script>console.log(\"xss\")</script>","headings":["<h3>f-i-j-nl-ng</h5>","http://facebook.com/success/lodewijk-van-den-berg"],"links":["daniel-tani@facebook.com","http://nytimes.com/security/kathryn-sullivan","www.nytimes.com"],"relatedContent":[{"url":"http://www.laweekly.com/news/cbs-crew-rat-fink-2368032","og:type":"article","og:title":"CBS Crew Rat Fink","og:description":"Near a couple of auto body shops (and a sharp new Space Invader mosaic that we&#039;ll post soon) near Temple and Westmoreland is a CBS wall with a nice Rat ...","og:url":"http://www.laweekly.com/news/cbs-crew-rat-fink-2368032","article:published_time":"2008-01-14T08:05:26-08:00","article:modified_time":"2014-10-28T14:59:52-07:00","article:section":"News","article:tag":"Mark Mauer","og:image":"http://IMAGES1.laweekly.com/imager/cbs-crew-rat-fink/u/original/2430299/img_2049.jpg","og:image:height":"360","og:image:width":"480","og:site_name":"LA Weekly","twitter:title":"CBS Crew Rat Fink","twitter:description":"Near a couple of auto body shops (and a sharp new Space Invader mosaic that we&#039;ll post soon) near Temple and Westmoreland is a CBS wall with a nice Rat ...","twitter:card":"summary","twitter:image":"http://IMAGES1.laweekly.com/imager/cbs-crew-rat-fink/u/original/2430299/img_2049.jpg","twitter:site":"@laweekly"},{"url":"http://www.laweekly.com/news/push-and-retna-in-koreatown-2368043","og:type":"article","og:title":"Push and Retna in Koreatown","og:description":"Yeah, I originally had this posted this morning as Push &amp; Ayer - Sorry. It looked like a Retna piece, but I saw the Ayer in there and thought that must ...","og:url":"http://www.laweekly.com/news/push-and-retna-in-koreatown-2368043","article:published_time":"2008-01-29T07:28:32-08:00","article:modified_time":"2014-10-28T14:59:54-07:00","article:section":"News","article:tag":"Shelley Leopold","og:image":"http://IMAGES1.laweekly.com/imager/push-and-retna-in-koreatown/u/original/2430376/img_3671.jpg","og:image:height":"360","og:image:width":"480","og:site_name":"LA Weekly","twitter:title":"Push and Retna in Koreatown","twitter:description":"Yeah, I originally had this posted this morning as Push &amp; Ayer - Sorry. It looked like a Retna piece, but I saw the Ayer in there and thought that must ...","twitter:card":"summary","twitter:image":"http://IMAGES1.laweekly.com/imager/push-and-retna-in-koreatown/u/original/2430376/img_3671.jpg","twitter:site":"@laweekly"},{"url":"http://www.laweekly.com/news/asylm-ruets-pdb-on-santa-monica-2368012","og:type":"article","og:title":"Asylm, Ruets, PDB on Santa Monica","og:description":"Not a new piece, but a well-hidden gem a little south of Santa Monica Blvd. in an alley off of Heliotrope or Edgemont. I&#039;ve been sitting on this for a w...","og:url":"http://www.laweekly.com/news/asylm-ruets-pdb-on-santa-monica-2368012","article:published_time":"2008-04-22T15:11:15-07:00","article:modified_time":"2014-10-28T14:59:48-07:00","article:section":"News","article:tag":"Culture and Lifestyle","og:image":"http://images1.laweekly.com/imager/asylm-ruets-pdb-on-santa-monica/u/original/2430137/img_5027.jpg","og:image:height":"360","og:image:width":"480","og:site_name":"LA Weekly","twitter:title":"Asylm, Ruets, PDB on Santa Monica","twitter:description":"Not a new piece, but a well-hidden gem a little south of Santa Monica Blvd. in an alley off of Heliotrope or Edgemont. I&#039;ve been sitting on this for a w...","twitter:card":"summary","twitter:image":"http://images1.laweekly.com/imager/asylm-ruets-pdb-on-santa-monica/u/original/2430137/img_5027.jpg","twitter:site":"@laweekly"},{"url":"http://www.laweekly.com/news/laurence-tribe-tangles-with-cbs-and-la-city-hall-2396867","og:type":"article","og:title":"Laurence Tribe Tangles with CBS and L.A. City Hall","og:description":"The United States Court of Appeals for the Ninth Circuit&rsquo;s Courtroom 3 - a miniature auditorium with comfortable, smoked salmon-colored seats - wa...","og:url":"http://www.laweekly.com/news/laurence-tribe-tangles-with-cbs-and-la-city-hall-2396867","article:published_time":"2008-06-04T14:16:10-07:00","article:modified_time":"2014-11-26T14:43:59-08:00","article:section":"News","og:site_name":"LA Weekly","twitter:title":"Laurence Tribe Tangles with CBS and L.A. City Hall","twitter:description":"The United States Court of Appeals for the Ninth Circuit&rsquo;s Courtroom 3 - a miniature auditorium with comfortable, smoked salmon-colored seats - wa...","twitter:card":"summary","twitter:site":"@laweekly"}],"machine":{"os":"win xp","ram":3221225472},"@version":"1"}


# 設定 Ingest Pipeline 這邊要有一台 node 有 ingest 角色
def create_ingest_pipeline():
    pipeline = {
        "description": "根據@timestamp 設定 index",
        "processors": [
            {
                "date_index_name": {
                    "field": "@timestamp",
                    "index_name_prefix": INDEX_PREFIX,
                    "date_formats": ["yyyy-MM-dd'T'HH:mm:ss.SSSX"],
                    "index_name_format": "yyyy.MM.dd",
                    "date_rounding": "d"
                }
            }
        ]
    }
    es.ingest.put_pipeline(id="attachment", body=pipeline)

def set_index_template():
    template = {
        "index_patterns": ["logstash-*"],
        "priority": 100,  # 設定優先級，數字越大越優先
        "template": {  # settings 和 mappings 要包在 template 裡
            "settings": {
                "number_of_shards": 2, # 設定分片數
                "number_of_replicas": 1
            },
            "mappings": {
                "properties": {
                    "@timestamp": { "type": "date" },
                    "ip": { "type": "ip" },
                    "clientip": { "type": "ip" },
                    "geo.coordinates": { "type": "geo_point" },
                    "bytes": { "type": "long" },
                    "machine.ram": { "type": "long" },
                    "relatedContent": {
                        "properties": {
                            "article:published_time": { "type": "date" },
                            "article:modified_time": { "type": "date" },
                            "og:image:height": { "type": "integer" },
                            "og:image:width": { "type": "integer" }
                        }
                    }
                }
            }
        }
    }

    es.indices.put_index_template(name="logstash-template", body=template)

def upload_data(file_path):
    
    # 讀取 JSONL 檔案
    actions = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        
        for i in tqdm(range(0, len(lines), 2)):  # 每兩行一組
            
            index_meta = json.loads(lines[i])  # 第一行是索引資訊 這邊因為有用pipeline 去分析 不需要這行的資訊了
            doc = json.loads(lines[i + 1])     # 第二行是文檔資料
            action = {
                "_op_type": "index",           # 操作類型
                "_index": "placeholder",       # 臨時索引名稱（會被 pipeline 覆蓋）
                "pipeline": "attachment",      # 指定 pipeline
                "_source": doc                 # 文檔內容
            }
            actions.append(action)
            # 每 50 筆上傳一次
            if len(actions) == 50:
                try :
                    helpers.bulk(es, actions)
                except helpers.BulkIndexError as e:
                    print(e)
                actions = []

    # 批次上傳
    try :
        helpers.bulk(es, actions)
    except helpers.BulkIndexError as e:
        print(e)


if __name__ == '__main__':
    create_ingest_pipeline()
    set_index_template()
    upload_data("logs.jsonl")
    print("上傳完成")