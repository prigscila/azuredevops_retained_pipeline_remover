# Azure DevOps Retained Pipeline Remover

This script aims to facilitate the exclusion of retained builds on pipelines at Azure DevOps.
What it does:
- enables you to retrieve builds of pipelines based on properties described [here](https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/pipelines/list?view=azure-devops-rest-7.0#pipeline)
- deletes all existing retentions for these builds
- deletes all runs for the pipelines that were found


## How to use
In order to use is you must:
- install dependencies with `pip`
- rename the `.env_sample` file to `.env`
- set the variables on `.env` file
- run from python CLI with `python main.py`

The following should be shown:

![carbon](https://user-images.githubusercontent.com/18142156/207431295-e8461f3b-b505-4d60-9a76-c887dcbe52e2.png)
Image generated with https://carbon.now.sh/
