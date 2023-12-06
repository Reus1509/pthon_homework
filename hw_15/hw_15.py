import os
from collections import namedtuple
from logging import FileHandler, Formatter, Logger

FileInfo = namedtuple('FileInfo', 'name extension is_dir parent_dir')


def collect_info(path):
    for root, dirs, files in os.walk(path):
        for name in sorted(dirs + files):
            full_path = os.path.join(root, name)
            is_dir = os.path.isdir(full_path)
            extension = name.split('.')[-1] if is_dir else None
            parent_dir = root if os.path.abspath(root) == path else os.path.relpath(root, path)
            yield FileInfo(name, extension, is_dir, parent_dir)


def main():
    log_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log = Logger('collect_info')
    file_handler = FileHandler('info.log')
    file_handler.setFormatter(log_format)
    log.addHandler(file_handler)
    with open('info.log', 'w') as f:
        log.info('Starting information collection...')
        for file_info in collect_info(input('Enter directory path: ')):
            print(f'{file_info.name=} {file_info.extension=} {file_info.is_dir=} {file_info.parent_dir=}')
            log.info(
                f'File info: {file_info.name=} {file_info.extension=} {file_info.is_dir=} {file_info.parent_dir=}')


if __name__ == "__main__":
    main()
