FROM prom/prometheus:latest

COPY prometheus.yml /etc/prometheus/prometheus.yml

CMD [
  "prometheus",
  "--config.file=/etc/prometheus/prometheus.yml",
  "--storage.tsdb.path=/prometheus",
  "--web.listen-address=0.0.0.0:10000"
]