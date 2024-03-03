from dataclasses import dataclass, asdict
import time


def tictoc(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time() - t1

        print(f'{func.__name__} ran in {t2} seconds')
    return wrapper


@dataclass
class InfobipRequest():
    externalId: str
    date: str


@tictoc
def post(request: InfobipRequest) -> None:
    print('connecting...')
    time.sleep(3)
    print(f'saved {asdict(request)}')
    print('done')


def main() -> None:
    request = InfobipRequest('3', 'today')

    post(request)


if __name__ == '__main__':
    main()
