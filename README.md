# check-mk-web-api [![CircleCI](https://circleci.com/gh/robert-r-meyer/check-mk-web-api.svg?style=svg)](https://circleci.com/gh/robert-r-meyer/check-mk-web-api)
## Installation
- From source code
```
git clone https://github.com/brennerm/check-mk-web-api
cd check-mk-web-api
sudo python setup.py install
```

- With pip
```
pip install check_mk_web_api
```

## [API Documentation](https://brennerm.github.io/check-mk-web-api/check_mk_web_api/)

## Quickstart
#### Initialization
```
import check_mk_web_api
api = check_mk_web_api.WebApi('http://checkmk.company.com/check_mk/webapi.py', username='automation', secret='123456')
```

#### Add Host
```
>>> api.add_host('webserver00.com')
```

#### Add Host in an existing WATO folder
```
>>> api.add_host('webserver00.com', folder='webservers')
```
Note there is no leading '/' on the folder name.

#### Edit Host
```
>>> api.edit_host('webserver00.com', ipaddress='192.168.0.100')
```

#### Delete Host
```
>>> api.delete_host('webserver00.com')
```

#### Get Host
```
>>> api.get_host('webserver00.com')
{
    'hostname': 'webserver00.com',
    'attributes': {
        'ipaddress': '192.168.0.100'
    },
    'path': ''
}
```

#### Get All Hosts
```
>>> api.get_all_hosts()
{
    'webserver00.com': {
        'hostname': 'webserver00.com',
        'attributes': {
            'ipaddress': '192.168.0.100'
        },
        'path': ''
    },
    'webserver01.com': {
        'hostname': 'webserver01.com',
        'attributes': {
            'ipaddress': '192.168.0.101'
        },
        'path': ''
    }
}
```

#### Discover Services
```
>>> api.discover_services('webserver00.com')
{'removed': '0', 'new_count': '16', 'added': '16', 'kept': '0'}
```

#### Bake Agents
```
>>> api.bake_agents()
```

#### Activate Changes
```
>>> api.activate_changes()
```


# Testing
## Testing uses pytest

### Running tests
To execute all tests in a CI environment, this project uses `pytest-vcr`

In order to run tests execute
```bash
pytest --vcr-record=none
```

### Test credentials
Tests are expected to be run using the ENV vars.
These vars are required due to the way that VCR records cassetts.
Without the use of these ENV vars, test will fail due to mismatched url params.

ENV var file for testing can be found at `<root>/.envrc.test`

[.envrc.test](./tests/.envrc.test)

```
CHECK_MK_USER=automation
CHECK_MK_URL=http://localhost/checkmd2/
CHECK_MK_SECRET=not_a_secret
```


# Generating Documentation

## Tooling

Documentation is generated using the `pydocmd` package.


## Building documentation locally

Documentation can be generated by running `pydocmd build` in the `doc` directory.

This will build a set of documentation based on comments in the code.

Documentation will be generated in `doc/_build/site/index.html`



## Contributors:

[Max Brennerm: brennerm](https://github.com/brennerm)

[Robert Meyer: robert-r-meyer](https://github.com/robert-r-meyer)

[Carissa Morrow: cmorrowTaos](https://github.com/cmorrowTaos)

