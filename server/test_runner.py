import unittest

from authentication.tests import (
    test_models,
    test_jwt,
)
from tests import (
    test_models,
    test_apis,
)


def get_unittests(suite):
    suite.addTest(unittest.makeSuite(test_jwt.Test_JWT))
    suite.addTest(unittest.makeSuite(test_models.Test_Auth_Model))


def get_server_tests(suite):
    suite.addTest(unittest.makeSuite(test_models.TestModels))
    suite.addTest(unittest.makeSuite(test_apis.TestAPI))


def main():
    suite = unittest.TestSuite()
    get_unittests(suite)
    get_server_tests(suite)

    output = unittest.TextTestRunner(verbosity=2).run(suite)
    if output.errors or output.failures:
        print("Failing Tests")


if __name__ == "__main__":
    main()
