import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelcase.camelcase('hello world'))
        self.assertEqual('', camelcase.camelcase(''))
        self.assertEqual('!@#$%^&*()', camelcase.camelcase('!@#$%^&*()'))
        self.assertEqual('helloWorld', camelcase.camelcase('Hello World!'))
        self.assertEqual('helloWorld', camelcase.camelcase('HELLO WORLD!'))