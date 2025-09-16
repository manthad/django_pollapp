#!/usr/bin/env python3
import socket, time

host = "db"
port = 5432

while True:
    try:
        s = socket.create_connection((host, port), 2)
        s.close()
        print("PostgreSQL started")
        break
    except Exception:
        print("Waiting for postgres...")
        time.sleep(1)