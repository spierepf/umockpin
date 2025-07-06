import os

import install

if 'unittest' not in os.listdir(install.libpath):
    import mip

    mip.install('unittest', target=install.libpath)

if 'mock.py' not in os.listdir(install.libpath + "/unittest"):
    import mip

    mip.install('github:spierepf/mip_packages/umock/package.json', target=install.libpath)

import unittest
# noinspection PyUnresolvedReferences
from tests.test_mock_pin import MockPinTestCase
# noinspection PyUnresolvedReferences
from tests.test_mock_pin_factory import MockPinFactoryTestCase
# noinspection PyUnresolvedReferences
from tests.test_mock_pin_net import MockPinNetTestCase, MockPinNetWithOnePinTestCase, MockPinNetWithTwoPinsTestCase

if __name__ == "__main__":
    unittest.main()
