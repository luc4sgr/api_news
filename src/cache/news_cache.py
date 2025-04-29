from cachetools import TTLCache

# Máximo de 100 entradas, cada uma dura 300 segundos (5 minutos)
news_cache = TTLCache(maxsize=100, ttl=300)
