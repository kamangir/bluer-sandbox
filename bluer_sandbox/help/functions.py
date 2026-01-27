from bluer_ai.help.generic import help_functions as generic_help_functions
from bluer_sandbox.help.arvancloud import help_functions as help_arvancloud
from bluer_sandbox.help.docker import help_functions as help_docker
from bluer_sandbox.help.interview import help_functions as help_interview
from bluer_sandbox.help.notebooks import help_functions as help_notebooks
from bluer_sandbox.help.offline_llm import help_functions as help_offline_llm
from bluer_sandbox.help.speedtest import help_speedtest
from bluer_sandbox.help.village import help_functions as help_village

from bluer_sandbox import ALIAS


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "arvancloud": help_arvancloud,
        "docker": help_docker,
        "interview": help_interview,
        "notebooks": help_notebooks,
        "offline_llm": help_offline_llm,
        "speedtest": help_speedtest,
        "village": help_village,
    }
)
