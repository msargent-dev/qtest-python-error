# qtest-python-error
Demonstrate error when calling qTest API

To install:

`pip install -r requirements.txt`

When running `main.py`, the environment variable `QTEST_API_KEY` must be set with a valid bearer token. I got my valid
token from https://qtest.dev.tricentis.com/ by copying the `Access Token` field near the top of the page.

Example run with fake bearer token:

QTEST_API_KEY='bearer aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee' python main.py


Expected behavior being demonstrated:

Call to api returns with error -- ValueError: Invalid value for `properties`, must not be `None`
