import os
import random
import string

import pytest

from check_mk_web_api.web_api_base import WebApiBase
from check_mk_web_api.web_api_hostgroup import WebApiHostGroup
from check_mk_web_api.exception import CheckMkWebApiException

api = WebApiHostGroup(
    os.environ['CHECK_MK_URL'],
    os.environ['CHECK_MK_USER'],
    os.environ['CHECK_MK_SECRET']
)


@pytest.mark.vcr()
class TestHostGroup():
    def setup(self):
        api.delete_all_hostgroups()


    def test_get_hostgroup(self):
        api.add_hostgroup('vm', 'VM')
        api.get_hostgroup('vm')


    def test_get_all_hostgroups(self):
        api.add_hostgroup('vm', 'VM')
        api.add_hostgroup('physical', 'Physical')
        groups = api.get_all_hostgroups()
        assert 'vm' in groups
        assert 'physical' in groups


    def test_get_nonexistent_hostgroup(self):
        with pytest.raises(KeyError):
            api.get_hostgroup('vm')


    def test_add_hostgroup(self):
        api.add_hostgroup('vm', 'VM')
        assert api.get_hostgroup('vm')['alias'] == 'VM'


    def test_add_duplicate_hostgroup(self):
        with pytest.raises(CheckMkWebApiException):
            api.add_hostgroup('vm', 'VM')
            api.add_hostgroup('vm', 'VM')

    def test_edit_hostgroup(self):
        api.add_hostgroup('vm', 'VM')
        assert api.get_hostgroup('vm')['alias'] == 'VM'
        api.edit_hostgroup('vm', 'VMs')
        assert api.get_hostgroup('vm')['alias'] == 'VMs'


    def test_edit_nonexisting_hostgroup(self):
        with pytest.raises(CheckMkWebApiException):
            api.edit_hostgroup('vm', 'VM')


    def test_delete_hostgroup(self):
        api.add_hostgroup('vm', 'VM')
        assert 'vm' in api.get_all_hostgroups()
        api.delete_hostgroup('vm')
        assert 'vm' not in api.get_all_hostgroups()


    def test_delete_nonexistent_hostgroup(self):
        with pytest.raises(CheckMkWebApiException):
            api.delete_hostgroup('vm')


