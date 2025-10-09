import pytest

from bluer_sandbox.ai4k.experiments import dict_of_experiments


@pytest.mark.parametrize(
    ["experiment_name"],
    [[experiment_name] for experiment_name in dict_of_experiments],
)
def test_ai4k_experiments(experiment_name: str):
    experiment = dict_of_experiments[experiment_name]

    assert "description" in experiment
    assert "marquee" in experiment
