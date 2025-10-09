from bluer_sandbox.ai4k.experiments import dict_of_experiments


def test_ai4k_experiments(experiment_name: str):
    experiment = dict_of_experiments[experiment_name]

    assert "name" in experiment
