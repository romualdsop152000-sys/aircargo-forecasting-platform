from prometheus_client import Counter


PREDICTIONS_TOTAL = Counter(
    "aircargo_predictions_total",
    "Total number of ML predictions made"
)

FLIGHTS_CACHE_HITS = Counter(
    "aircargo_flights_cache_hits_total",
    "Total cache hits for /flights endpoint"
)

FLIGHTS_CACHE_MISSES = Counter(
    "aircargo_flights_cache_misses_total",
    "Total cache misses for /flights endpoint"
)