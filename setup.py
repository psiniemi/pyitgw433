# Copyright 2018 Pasi Niemi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
from setuptools import setup

setup(name='pyitgw433',
      version='0.1',
      description='Library and tools for talking with InterTechno ITGW-433 lan gateway',
      url='http://github.com/psiniemi/pyitgw433',
      download_url='https://github.com/psiniemi/pyitgw433/tarball/0.1',
      author='Pasi Niemi',
      author_email='pasi.niemi@iki.gi',
      license='Apache 2.0',
      packages=['pyitgw433'],
      include_package_data=True,
      scripts=[],
      entry_points={
          'console_scripts': [],
      },
      setup_requires=[
          'pytest-runner'
      ],
      install_requires=[
          'pyaml',
          'argcomplete'
      ],
      tests_require=[
          'pytest',
          'pytest-mock',
          'pytest-cov'
      ],
      zip_safe=False)
