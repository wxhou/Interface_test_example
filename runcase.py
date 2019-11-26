#!/usr/bin/env python3
# coding=utf-8
import sys
sys.path.append('.')
import pytest

if __name__ == '__main__':
    pytest.main(['--html=report.html', '--self-contained-html'])
