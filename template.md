# 🌀 bluer-sandbox

🌀 A sandbox for ideas and experiments.

## installation

```bash
pip install bluer-sandbox
```

## aliases

[@assets](./bluer_sandbox/docs/aliases/assets.md), 
[@docker](./bluer_sandbox/docs/aliases/docker.md), 
[@notebooks](./bluer_sandbox/docs/aliases/notebooks.md), 
[@offline_llm](./bluer_sandbox/docs/aliases/offline_llm.md).

```mermaid
graph LR

    arvancloud_ssh["@arvan ssh"]
    arvancloud_set_ip["@arvan set_ip <ip-address>"]


    assets_publish["@assets publish extensions=png+txt,push <object-name>"]


    docker_browse["@docker browse"]

    docker_build["@docker build"]

    docker_clear["@docker clear"]

    docker_eval["@docker eval~~- <command-line>"]

    docker_push["@docker push"]

    docker_run["@docker run"]

    docker_seed["@docker seed"]


    notebooks_build["@notebooks build <notebook-name>"]

    notebooks_code["@notebooks code <notebook-name>"]
    
    notebooks_connect["@notebooks connect ip=<ip-address>"]

    notebooks_create["@notebooks create <notebook-name>"]

    notebooks_host["@notebooks host"]

    notebooks_open["@notebooks open <notebook-name>"]


    offline_llm_build["@offline_llm build"]

    offline_llm_model_download["@offline_llm model download"]

    offline_llm_prompt["@offline_llm prompt~~- <prompt> <object-name>"]

    speedtest["@speedtest"]

    object["📂 object"]:::folder
    prompt["🗣️ prompt"]:::folder
    notebook["📘 notebook"]:::folder
    ip_address["🛜 <ip-address>"]:::folder
    docker_image["📂 docker image"]:::folder
    docker_com["🕸️ docker.com"]:::folder
    command_line["🗣️ <command-line>"]:::folder
    clipboard["📋 clipboard"]:::folder
    llm["🧠 llm"]:::folder
    llama_cpp["🛠️ llama_cpp"]:::folder
    arvancloud_machine["🖥️ arvancloud"]:::folder


    arvancloud_ssh --> arvancloud_machine

    arvancloud_set_ip --> ip_address


    object --> assets_publish


    docker_seed["@docker seed"]

    docker_browse --> docker_com

    docker_build --> docker_image

    docker_clear

    command_line --> docker_eval
    docker_image --> docker_eval

    docker_image --> docker_push 
    docker_push --> docker_com

    docker_image --> docker_run

    docker_seed --> clipboard


    notebook --> notebooks_build

    notebook --> notebooks_code

    ip_address --> notebooks_connect

    notebooks_host --> ip_address

    notebooks_create --> notebook

    notebook --> notebooks_open


    offline_llm_build --> llama_cpp

    offline_llm_model_download --> llm

    prompt --> offline_llm_prompt
    llama_cpp --> offline_llm_prompt
    llm --> offline_llm_prompt
    offline_llm_prompt --> object
```

items:::

---

> 🌀 [`blue-sandbox`](https://github.com/kamangir/blue-sandbox) for the [Global South](https://github.com/kamangir/bluer-south).

---

signature:::