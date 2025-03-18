# Elasticsearch Cluster

A demo of deploying an Elasticsearch cluster using Docker, along with monitoring using Prometheus + Grafana.

### Elasticsearch Cluster

Deploy 4 Elasticsearch nodes with the following roles:

* Master
* Data
* Master + Data
* Ingest + Data

Use Nginx as the entry point.

### init_data.py

Create an index template and a pipeline, and write sample log(logs.jsonl) data.


### search_data.py

Run search with multi threads

## Deployment


Deploy the docker-compose.yml file under the project directory.

```sh
docker-compose up -d
```

Then deploy node4

```sh
cd node4
docker-compose up -d
```

nginx
```sh
cd ../nginx
docker-compose up -d
```

prometheus_grafana
```sh
cd ../prometheus_grafana
docker-compose up -d
```
