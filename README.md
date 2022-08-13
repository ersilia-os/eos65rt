# Membrane permeability of fluorescent probes

## Model Identifiers
- Slug: deepfl-logp
- Ersilia ID: eos65rt
- Tags: LogP, physchem, permeability

## Model Description
LogP (passive permeability) based on lipophilicy descriptors calculated with a deep neural network 
- Input: SMILES 
- Output: LogP 
- Model type: Regression
- Mode of training: Pretrained
- Training data: 10,749 compounds https://github.com/k-soliman/DeepFl-LogP/blob/master/Dataset.zip
- Experimentally validated: Yes 

## Source code
This model is published by Soliman, K., Grimm, F., Wurm, C.A. et al. Predicting the membrane permeability of organic fluorescent probes by the deep neural network based lipophilicity descriptor DeepFl-LogP. *Sci Rep 11*, 6991 (2021). https://doi.org/10.1038/s41598-021-86460-3
- Code: https://github.com/k-soliman/DeepFl-LogP
- Checkpoints: https://github.com/k-soliman/DeepFl-LogP/blob/master/2020_DNN_v44_epoch_78_r0.892_rms0.359.h5

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "Deepfl-LogP", located at `/model` and licensed under a GPL-v3 license

## History
- Model was downloaded on October 11, 2021
