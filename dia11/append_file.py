from datetime import datetime

try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open("dia11/logs/error.log", "a+") as log:
        log.seek(0)
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(0)
        print(log.read())