import time

import my_module

if __name__ == "__main__":
    print("Starting up ...")
    time.sleep(10)
    print("Startup complete")

    while True:
        print("Hello from My Service")
        time.sleep(5)
