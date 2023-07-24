import os.path

import fire
import json
import re

INPUT = 'Spdxv2.3-example.json'


def ver_to_semver(v2ver: str) -> str:
    if m := re.match(r'^SPDX-(\d+)\.(\d+)(?:\.(\d+))?$', v2ver):
        mp = m.group(3) if m.group(3) else '0'
        return f'{m.group(1)}.{m.group(2)}.{mp}'
    raise ValueError(f'invalid SPDXv2 version {v2ver}')


def get_agent(cstring: str) -> list:
    if m := re.match(r'^\s*(\w+):\s*([-.\w\s]+?)\s*(\([^)]*\))?\s*$', cstring):
        return [m.group(1), m.group(2).replace(' ', ''), m.group(3)]
    raise ValueError(f'invalid creator: "{cstring}"')


def load_spdxv2(filename: str = INPUT):
    elements = []
    with open(filename) as fp:
        src = json.load(fp)
    ns = src['documentNamespace'] + '#'
    ci = src['creationInfo']
    creation_info = {
        'specVersion': ver_to_semver(src['spdxVersion']),
        'comment': ci['comment'],
        'created': ci['created'],
        'createdBy': [],
        'createdUsing': [],
        'profile': ['Core'],
        'dataLicense': src['dataLicense']
    }
    cmap = {'Person': 'createdBy', 'Organization': 'createdBy', 'Tool': 'createdUsing'}
    for c in ci['creators']:
        cr = get_agent(c)
        creation_info[cmap[cr[0]]].append(ns + cr[1])
    for c in ci['creators']:
        cr = get_agent(c)
        elements.append({
            'spdxId': ns + cr[1],
            'type': cr[0],
            'creationInfo': creation_info
        })
    """
    Need to Process:
      externalDocumentRefs
      hasExtractedLicensingInfo
      annotations
      documentDescribes
      packages
      files
      snippets
      relationships
    """
    for c in src['externalDocumentRefs']:
        elements.append({
            'spdxId': ns + c['externalDocumentId'],
            'type': 'SpdxDocument',
            'element': [c['spdxDocument'] + '#SPDXRef-DOCUMENT'],
            'name': c['externalDocumentId'],
            'verifiedUsing': {'hash': {
                'algorithm': c['checksum']['algorithm'],
                'hashValue': c['checksum']['checksumValue']
            }},
            'creationInfo': creation_info
        })

    for n, c in enumerate(src['annotations'], start=1):
        ci = dict(creation_info)    # make a copy
        ci.update({'created': c['annotationDate']})
        cr = get_agent(c['annotator'])
        elements.append({
            'spdxId': f'{ns}annotation-{n}',
            'type': 'Annotation',
            'subject': ns + src['SPDXID'],  # Annotations are not attached to individual components
            'annotationType': 'review' if c['annotationType'].lower() == 'review' else 'other',
            'statement': c['comment'],
            'creationInfo': creation_info
        })

    elements.insert(0, {
        'spdxId': ns + src['SPDXID'],
        'type': 'Sbom',
        'name': src['name'],
        'element': [e['spdxId'] for e in elements],
        'creationInfo': creation_info
    })

    for k, v in creation_info.items():
        print(f'  {k}: {v}')

    of, oe = os.path.splitext(filename)
    with open(of + '_v3' + oe, 'w') as fp:
        json.dump(elements, fp, indent=2)


if __name__ == '__main__':
    fire.Fire(load_spdxv2)
