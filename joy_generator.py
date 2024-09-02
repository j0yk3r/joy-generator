import time


def main():
    try:
        while True:
            print("Joy", end=' ', flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
