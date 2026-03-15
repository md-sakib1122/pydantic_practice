import time

def fetch_time(pram):
    print("start fetching")
    time.sleep(int(pram))
    print(f"finish fetching->{pram}")
    return int(time.time())


t1 = time.perf_counter()


def main():
    fetch_time(1)
    fetch_time(2)
if __name__ == "__main__":
     main()
t2 = time.perf_counter()

print(f"time taken to the execution is {t2-t1:.2f}")

