import pytest
from util import *
import numpy as np

#@pytest.fixture
#def normal_sample:
#    pass
@pytest.fixture(scope="session")
def seed():
    np.random.seed(0)
    return None

def test_normal_mean(seed):
    samples1 = np.random.normal(size=1000)
    samples2 = np.random.normal(size=100)
    samples3 = np.random.normal(loc=100, scale=1, size=100)

    pval, diff, ts = exact_mc_perm_test(samples1, samples2, 1000, mean_diff)

    pval1, diff1, ts1 = exact_mc_perm_test(samples1, samples3, 1000, mean_diff)

    assert pval > 0.05
    assert pval1 < 0.05

def test_normal_cdf(seed):
    samples1 = np.random.normal(size=1000)
    samples2 = np.random.normal(size=100)
    samples3 = np.random.normal(loc=100, scale=1, size=100)

    pval, diff, ts = exact_mc_perm_test(samples1, samples2, 1000, cdf_distance)

    pval1, diff1, ts1 = exact_mc_perm_test(samples1, samples3, 1000, cdf_distance)

    assert pval > 0.05
    assert pval1 < 0.05
