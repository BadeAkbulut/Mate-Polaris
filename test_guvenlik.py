import re

def sifre_guclu_mu(sifre):
    regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).+$'
    return bool(re.match(regex, sifre))


def test_dogru_sifre():
    assert sifre_guclu_mu("Abc123!") == True


def test_eksik_sifre():
    assert sifre_guclu_mu("Abc123") == False


def test_hatali_sifre():
    assert sifre_guclu_mu("abc123") == False

