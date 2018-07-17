# coding: utf-8

import pbr.version

from marketaccess-intraday-power-python._marketaccess-intraday-power-python import MyPublicClass


def version():
    return pbr.version.VersionInfo('marketaccess-intraday-power-python').release_string()

## Uncomment the following line to declare a __version__ in your root module. Beware the evaluation
## of the version may impact the load time of your module
#
# __version__ = version()
#
#
__all__ = [
    'version',
    'MyPublicClass',
]
