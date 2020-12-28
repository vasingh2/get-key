# GET Key from object

 Function that you accepts  in the object and a key path and gets back the value


### Requirement
1. Python Version Installed > 3.5
2. Pip Installed for Python3.


### Install Dependencies
Install the dependecies using pip.

```python
pip3 install pytest

```

### Usage

To run the unit test
```python

python3 -m pytest -q getkey_test.py
```
To call the function

```python
from getkey import getKey
def test:
    object = {“a”:{“b”:{“c”:”d”}}}
    key = a/b/c
    instance = getkey(object,key)
    instance.get_key_value_at_path()
```



