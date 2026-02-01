bind = "0.0.0.0:10000"

workers = 1
worker_class = "gthread"
threads = 4

timeout = 0        # 🔴 CRITICAL: disables worker timeout
graceful_timeout = 0
