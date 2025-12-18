from queue import Queue
from time import sleep
from random import uniform


class Request:
    id = 0

    @classmethod
    def increase_id(cls):
        cls.id += 1
        return cls.id

    def __init__(self):
        self.id = Request.increase_id()

    def __str__(self):
        return f'Request #{self.id}'


def main():
    queue = Queue()

    def generate_request():
        request = Request()
        print(f'Generated request {request}')
        queue.put(request)

    def process_request():
        if queue.empty():
            print('No requests to process')
        else:
            request = queue.get()
            print(f'Processed request {request}')

    try:
        while True:
            if uniform(0, 1) < 0.5:
                generate_request()
            else:
                process_request()
            print(f"{queue.qsize()} requests in queue")
            sleep(uniform(0.5, 1))
    except KeyboardInterrupt:
        print("\nStopped by user.")


if __name__ == '__main__':
    main()
