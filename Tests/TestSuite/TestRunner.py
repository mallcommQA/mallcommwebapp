__author__ = 'Chidozie Amefule'

from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Scripts.SignIn import TestSignIn
from Tests.Scripts.RegisterNewUser import TestRegistration
from Tests.Scripts.LaunchPage import TestURLLaunch
from Tests.Scripts.UserProfile import TestUserProfile
from Tests.Scripts.HeaderTab import TestHeaderTab
from Tests.Scripts.ForgotPassword import TestForgotPassword
from Tests.Scripts.SwitchCentre import TestCentreSwitch
from Tests.Scripts.ChangePassword import TestChangePassword
from Tests.Scripts.HomeURLChangeLanguage import TestChangeLanguage
from Tests.Scripts.CountryDialCode import TestCountryCodeSwitch
from Tests.Scripts.Settings import TestSettings
from Tests.Scripts.RegisterForAnotherStore import TestRegisterForAnotherStore
from Tests.Scripts.LockedAccount import TestLockedAccount
from Tests.Scripts.HelpButton import TestHelpButton


if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestURLLaunch),
        loader.loadTestsFromTestCase(TestChangeLanguage),
        loader.loadTestsFromTestCase(TestCountryCodeSwitch),
        loader.loadTestsFromTestCase(TestRegistration),
        loader.loadTestsFromTestCase(TestSignIn),
        loader.loadTestsFromTestCase(TestForgotPassword),
        loader.loadTestsFromTestCase(TestHeaderTab),
        loader.loadTestsFromTestCase(TestCentreSwitch),
        loader.loadTestsFromTestCase(TestUserProfile),
        loader.loadTestsFromTestCase(TestChangePassword),
        loader.loadTestsFromTestCase(TestSettings),
        loader.loadTestsFromTestCase(TestHelpButton),
        loader.loadTestsFromTestCase(TestRegisterForAnotherStore),
        loader.loadTestsFromTestCase(TestLockedAccount)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)




