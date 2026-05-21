FROM prom/prometheus:latest

COPY monitoring/prometheus-render/prometheus.yml /etc/prometheus/prometheus.yml

CMD ["--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.path=/prometheus", "--web.listen-address=0.0.0.0:10000"]