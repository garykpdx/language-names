import json
from argparse import ArgumentParser

import panlex

ART_274 = 7257


def query_all_langs(source_uid):
    params = {'trans_langvar': ART_274, 'include': ['trans_txt', 'uid'], 'cache': False, 'sort': 'trans_txt',
              'trans_txt':source_uid}
    for result in panlex.query_iter('/expr', params):
        yield {'name':result['txt'], 'lang':result['trans_txt'], 'name_lang':result['uid'], 'langvar':result['langvar']}


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--source-lang')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    all_names = query_all_langs(args.source_lang)

    result_count = 0
    for name in all_names:
        print(name)
        result_count += 1

    print('total results: {}'.format(result_count))
