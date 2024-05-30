---
title: Bear Classifier
emoji: 👀
colorFrom: blue
colorTo: gray
sdk: gradio
sdk_version: 4.32.0
app_file: app.py
pinned: false
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

jupyter: https://jupyenv.io/documentation/how-to/

poetry export -f requirements.txt --output requirements.txt
poetry run python app.py
poetry add --lock
poetry update --lock / poetry lock (--no-update)
poetry env list
poetry env remove env/--all
poetry cache list
poetry cache clear name --all
n.b. '~/.cache/pypoetry/artifacts' not auto-removed
