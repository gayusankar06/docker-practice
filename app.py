import os
import time

app_env = os.getenv("APP_ENV", "dev")
db_host = os.getenv("DB_HOST", "localhost")
log_level = os.getenv("LOG_LEVEL", "info")

print(f"Environment: {app_env}")
print(f"DB Host: {db_host}")
print(f"Log Level: {log_level}")

while True:
    print("Application Running...")
    time.sleep(5)