import unittest

from admins.tests import test_jwt_adm, test_models_adm
from authentication.tests import test_jwt, test_models
from tests import test_app_apis, test_app_models, test_auth


def get_unittests(suite):
    suite.addTest(unittest.makeSuite(test_jwt_adm.Test_Admin_JWT))
    suite.addTest(unittest.makeSuite(test_models_adm.Test_Admin_Model))
    suite.addTest(unittest.makeSuite(test_jwt.Test_JWT))
    suite.addTest(unittest.makeSuite(test_models.Test_Auth_Model))


def get_server_tests(suite):
    suite.addTest(unittest.makeSuite(test_app_models.TestAppModels))
    suite.addTest(unittest.makeSuite(test_auth.TestAuthentication))
    suite.addTest(unittest.makeSuite(test_app_apis.TestAppAPI))


def main():
    suite = unittest.TestSuite()
    get_unittests(suite)
    get_server_tests(suite)

    output = unittest.TextTestRunner(verbosity=2).run(suite)
    if output.errors or output.failures:
        print("Failing Tests")


if __name__ == "__main__":
    main()
