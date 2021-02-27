# Epileptic Seizure Recognition

Use various time series analysis techniques to detect epileptic seizures at electroencephalogram readings.

## Data

We use a dataset from [here](http://epileptologie-bonn.de/cms/front_content.php?idcat=193).

To download it, just type:

```shell
python download.py
```

The script will save 5 `.npy` files to `data/`. These are matrices whose rows are single-channel EEG segments, each one
having 23.6-second duration. The matrices correspond to 5 subsets of the dataset:

* The sets are denoted as `Z`, `O`, `N`, `F`, and `S`.
* `Z` - healthy volunteers, surface EEG recordings, eyes open.
* `O` - healthy volunteers, surface EEG recordings, eyes closed.
* `F` - patients, seizure-free intervals, epileptogenic zone.
* `N` - patients, seizure-free intervals, hippocampal formation of the opposite hemisphere of the brain.
* `S` - patients, seizure activity.