import fire
import json
import re

INPUT = 'Spdxv2.3-example.json'


def ver_to_semver(v2ver: str) -> str:
    if m := re.match(r'^SPDX-(\d+)\.(\d+)(?:\.(\d+))?$', v2ver):
        mp = m.group(3) if m.group(3) else '0'
        return f'{m.group(1)}.{m.group(2)}.{mp}'
    raise(ValueError, f'invalid SPDXv2 version {v2ver}')


def get_creator(cstring: str) -> dict:
    if m := re.match(r'^\s*(\w+):\s*(.*?)\s*$', cstring):
        # return {'type': m.group(1), 'value': m.group(2)}
        return element
    raise (ValueError, f'invalid creator: "{cstring}"')


def load_spdxv2(filename: str=INPUT):
    elements = []
    with open(filename) as fp:
        src = json.load(fp)
    ns = src['documentNamespace'] + '#'
    ci = src['creationInfo']
    creators = [get_creator(v) for v in ci['creators']]
    creation_info = {
        'specVersion': ver_to_semver(src['spdxVersion']),
        'comment': ci['comment'],
        'created': ci['created'],
        'createdBy': [],
        'createdUsing': [],
        'profile': ['Core'],
        'dataLicense': src['dataLicense']
    }
    print(creation_info)


if __name__ == '__main__':
    fire.Fire(load_spdxv2)