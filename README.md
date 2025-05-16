# Membrane permeability of fluorescent probes

A deep neural network was trained to predict the LogP value of small molecules and fluorescent probes using an experimentally annotated dataset of >13k molecules (OPERA). This dataset was complemented with fluorescent probes to improve the model accuracy in this space. Probes predicted impermeant to cell membranes consistently showed experimental LogP <1.

This model was incorporated on 2021-11-10.

## Information
### Identifiers
- **Ersilia Identifier:** `eos65rt`
- **Slug:** `deepfl-logp`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Not Applicable`
- **Tags:** `Permeability`, `ADME`, `LogP`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** LogP values of > 1 indicate membrane permeability

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| clogp | float | low | Calculated octanol-water partition coefficient (logP) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos65rt](https://hub.docker.com/r/ersiliaos/eos65rt)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos65rt.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos65rt.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/k-soliman/DeepFl-LogP](https://github.com/k-soliman/DeepFl-LogP)
- **Publication**: [https://www.nature.com/articles/s41598-021-86460-3](https://www.nature.com/articles/s41598-021-86460-3)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [LGPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos65rt
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos65rt
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
