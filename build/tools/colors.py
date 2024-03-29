#!/usr/bin/env python
#
# Copyright (C) 2019 The Dirty Unicorns Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

# Colors
BOLD = '\033[1m'
CPASS = '\033[92m'
CWARN = '\033[93m'
CFAIL = '\033[91m'
CEND = '\033[0m'

def print_bold(msg):
    """ Bold """
    print(BOLD + msg + CEND)

def print_pass(msg):
    """ Green """
    print(CPASS + msg + CEND)

def print_warn(msg):
    """ Yellow """
    print(CWARN + msg + CEND)

def print_fail(msg):
    """ Red """
    print(CFAIL + msg + CEND)

