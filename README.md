![NPD](https://github.com/miroine/npd_data/blob/master/docs/image/fasadelogo%20NPD.jpg)

## Introduction
npd_data is a module that extract petroleum data from the NPD website using API's
It does also extract shape files for map plotting and further posptocessing 
Detailed documentations and examples located on the notebookes: [npd wraper *docs* ](https://github.com/miroine/npd_data/tree/master/docs/notebooks)

Suggestions are welcome

## Feature summary: 
 * Python 3.6+ support 
 * Focus on high speed with API serving
 * Output mainly based on pandas and geopandas 
 * could be combined with shape files for better data insights
 * Supported in both Linux, Windows and Mac OS (might be some issues with VPN activated)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installation 
```
pip install npd-data
```

want to contribute ? use:
```
git clone https://github.com/miroine/npd_data/
```
## Quick Use
```
> from npd_data.npd_wraper import field
>
>df =field.get_field_production_yearly()
>
```
## License

Using [MIT license](https://github.com/miroine/npd_data/blob/master/LICENSE)
