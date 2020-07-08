# _*_ coding: utf-8 _*_
from django.test import TestCase
from validate_docbr import CPF, CNPJ

cpf = CPF()
cnpj = CNPJ()


class TestValidate(TestCase):
    def test_cpf_true(self):
        """ Testing cpf validation. """
        self.assertTrue(cpf.validate("146.212.130-67"))

    def test_cpf_false(self):
        """ Testing cpf validation. """
        self.assertFalse(cpf.validate("146.234.830-67"))

    def test_cnpj_true(self):
        """ Testing cnpj validation. """
        self.assertTrue(cnpj.validate("46.773.756/0001-74"))

    def test_cnpj_false(self):
        """ Testing cnpj validation. """
        self.assertFalse(cnpj.validate("46.553.736/0001-74"))

    def test_cpf_false_equal(self):
        """ Testing cnpj validation. """
        self.assertFalse(cpf.validate("111.111.111-11"))

    def test_cnpj_false_equal(self):
        """ Testing cnpj validation. """
        self.assertFalse(cnpj.validate("11.111.111/1111-11"))
