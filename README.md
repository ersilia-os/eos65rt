# Membrane permeability of fluorescent probes

A deep neural network was trained to predict the LogP value of small molecules and fluorescent probes using an experimentally annotated dataset of >13k molecules (OPERA). This dataset was complemented with fluorescent probes to improve the model accuracy in this space. Probes predicted impermeant to cell membranes consistently showed experimental LogP <1.

## Identifiers

* EOS model ID: `eos65rt`
* Slug: `deepfl-logp`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Experimental value`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: LogP values of > 1 indicate membrane permeability

## References

* [Publication](https://www.nature.com/articles/s41598-021-86460-3.epdf?sharing_token=zmYZd6qpwnDwc8tCOYGGf9RgN0jAjWel9jnR3ZoTv0OXuXXr_ZS6VuKQMyMJiA3PeIcqAJZTcpcNZJHblyChkQ2eTpzGXq23YsIcFlG8ayuEptKCJ1DeyIRGrh9O2d5JvvGGB9qG8cXgAuy_k-e1ncAMkAzpTegmR0XUbnftjv0%3D)
* [Source Code](https://github.com/k-soliman/DeepFl-LogP)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos65rt)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos65rt.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos65rt) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s41598-021-86460-3.epdf?sharing_token=zmYZd6qpwnDwc8tCOYGGf9RgN0jAjWel9jnR3ZoTv0OXuXXr_ZS6VuKQMyMJiA3PeIcqAJZTcpcNZJHblyChkQ2eTpzGXq23YsIcFlG8ayuEptKCJ1DeyIRGrh9O2d5JvvGGB9qG8cXgAuy_k-e1ncAMkAzpTegmR0XUbnftjv0%3D) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!