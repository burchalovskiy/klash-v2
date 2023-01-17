import multiprocessing
import os

from environs import Env

env_file = os.getenv('GUNICORN_ENV_FILE', '.env')

env = Env()
env.read_env(env_file)

workers_per_core = env.int('WORKERS_PER_CORE', 1)
max_workers = env.int('MAX_WORKERS', None)
use_max_workers = bool(max_workers)
web_concurrency = env.int('WEB_CONCURRENCY', None)

host = env('HOST', '0.0.0.0')
port = env('PORT', 80)
bind_env = env('BIND', None)
use_loglevel = env('LOG_LEVEL', 'info')
use_bind = bind_env or f'{host}:{port}'
cores = multiprocessing.cpu_count()
default_web_concurrency = workers_per_core * cores

if web_concurrency:
    assert web_concurrency > 0
else:
    web_concurrency = max(default_web_concurrency, 2)
    if use_max_workers:
        web_concurrency = min(web_concurrency, use_max_workers)

accesslog_var = env('ACCESS_LOG', '-')
use_accesslog = accesslog_var or None
errorlog_var = env('ERROR_LOG', '-')
use_errorlog = errorlog_var or None

# Gunicorn config variables
loglevel = use_loglevel
workers = web_concurrency
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = '/dev/shm'
accesslog = use_accesslog
graceful_timeout = env.int('GRACEFUL_TIMEOUT', 120)
timeout = env.int('TIMEOUT', 120)
keepalive = env.int('KEEP_ALIVE', 5)
