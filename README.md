# 🌀 bluer-sandbox

🌀 A sandbox for ideas and experiments.

```bash
pip install bluer-sandbox
```

```mermaid
graph LR

    notebooks_build["@notebooks<br>build<br>&lt;notebook-name&gt;"]

    notebooks_code["@notebooks<br>code<br>&lt;notebook-name&gt;"]
    
    notebooks_connect["@notebooks<br>connect<br>ip=&lt;ip-address&gt;"]

    notebooks_create["@notebooks<br>create<br>&lt;notebook-name&gt;"]

    notebooks_host["@notebooks<br>host"]

    notebooks_open["@notebooks<br>open<br>&lt;notebook-name&gt;"]

    notebook["📘 notebook"]:::folder
    ip_address["🛜 <ip-address>"]:::folder

    notebook --> notebooks_build

    notebook --> notebooks_code

    ip_address --> notebooks_connect

    notebooks_host --> ip_address

    notebooks_create --> notebook

    notebook --> notebooks_open
```

|   |   |
| --- | --- |
| [``@notebooks``](./bluer_sandbox/assets/template.ipynb) [![image](https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true)](./bluer_sandbox/assets/template.ipynb) jupyter Notebooks | [`offline LLM`](./bluer_sandbox/docs/offline_llm.md) [![image](https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true)](./bluer_sandbox/docs/offline_llm.md) using [llama.cpp](https://github.com/ggerganov/llama.cpp) |

---

> 🌀 [`blue-sandbox`](https://github.com/kamangir/blue-sandbox) for the [Global South](https://github.com/kamangir/bluer-south).

---


[![pylint](https://github.com/kamangir/bluer-sandbox/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/bluer-sandbox/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/bluer-sandbox/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/bluer-sandbox/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/bluer-sandbox/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/bluer-sandbox/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/bluer-sandbox.svg)](https://pypi.org/project/bluer-sandbox/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/bluer-sandbox)](https://pypistats.org/packages/bluer-sandbox)

built by 🌀 [`bluer README`](https://github.com/kamangir/bluer-objects/tree/main/bluer_objects/README), based on 🌀 [`bluer_sandbox-5.39.1`](https://github.com/kamangir/bluer-sandbox).
