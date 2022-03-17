#!/usr/bin/env python3

import argparse
import sys
import yaml

import spack
import spack.cmd
import spack.store
from spack.database import InstallStatuses

description = ('Find all installed geant4-data packages and dump them into a '
               'package.yaml compatible format marking all geant4-data packages'
               ' as non-buildable external packages')
section = 'utilities'
level = 'short'

def setup_parser(subparser):
    subparser.add_argument('-o', '--output', default=sys.stdout,
                           type=argparse.FileType('w'),
                           help='where to dump the output')
    subparser.add_argument('--only-data', action='store_true', default=False,
                           help='Do not include the geant4-data bundle packages in the output')


def g4data(parser, args):
    query_args = {
        'installed': [InstallStatuses.INSTALLED],
        'explicit': False,
    }

    # Get all geant4-data packages
    g4data_specs = {}
    for s in spack.store.db.query('geant4-data', **query_args):
        # Only include the top-level bundle packages if desired
        if not args.only_data:
            g4data_specs[s.dag_hash()] = s
        for _, ds in s.traverse(root=False, depth=True):
            g4data_specs[ds.dag_hash()] = ds

    # Put everything into a dictionary that can be put into a packages.yaml file
    # when dumped
    packages = {}
    for _, spec in g4data_specs.items():
        spec_path = {
            'spec': spec.format('{name}@{version}'),
            'prefix': spec.format('{prefix}')
        }

        if spec.name not in packages:
            packages[spec.name] = {'externals': [], 'buildable': False}

        packages[spec.name]['externals'].append(spec_path)

    yaml.dump({'packages': packages}, args.output)
