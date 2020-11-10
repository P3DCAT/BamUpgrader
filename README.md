# Beta BAM Upgrader

This Beta BAM Upgrader tool can be used to convert old Panda3D BAM version 3.3 models to the newest format.

All nodes and curves are currently implemented, however, characters and animations cannot be converted yet.

* Use the `--bam-version` flag to set a target BAM version. Please note that your Panda3D version must have the ability to output this BAM version. For example: `--bam-version 6.42`
* Use the `--model-path` flag to specify the target folder that contains legacy BAM files that must be converted.

## Installation

Your Python version must be at least 3.6, but newer versions are appreciated.

Make sure you've got Panda3D installed. The newer, the better.

You must clone the repository, and install all dependencies from `requirements.txt` afterwards.

```
git clone https://github.com/P3DCAT/BamUpgrader
python -m pip install --upgrade -r requirements.txt
cd BamUpgrader
```

## Running

```
usage: python -m bamupgrader.Main [-h] [--model-path MODEL_PATH] [--bam-version BAM_VERSION]

This script can be used to convert old Panda3D BAM version 3.3 models to the new BAM system.

optional arguments:
  -h, --help            show this help message and exit
  --model-path MODEL_PATH
                        The model path to convert all BAM files in.
  --bam-version BAM_VERSION
                        The bam version to use while writing BAM files. For example: 6.24
```

For example, to convert all legacy BAM models in C:\Data\OldBams (will write to C:\Data\OldBams-upgraded), using BAM version 6.24:

```
python -m bamupgrader.Main --model-path C:\Data\OldBams --bam-version 6.24
```

## Caveats

Characters and animations are not yet supported.

## Known Bugs

Characters will not convert properly, this is because their ComputedVertices are not processed (this is part of Character information).
