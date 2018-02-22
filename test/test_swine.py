
from mhcnames import (
    parse_allele_name,
    AlleleName,
)
from nose.tools import eq_

def test_SLA_1_0101_with_seps():
    eq_(
        parse_allele_name("SLA-1*01:01"),
        AlleleName("SLA", "1", "01", "01"))

def test_SLA_1_HB01():
    eq_(
        parse_allele_name("SLA-1-HB01"),
        AlleleName("SLA", "1", "HB", "01"))

def test_SLA_1_0101_no_seps():
    eq_(
        parse_allele_name("SLA-10101"),
        AlleleName("SLA", "1", "01", "01"))
