# scgen: A Random supply chain generator

scgen provides a simple way to generate synthetic supply chain data for various uses. For example it can create supply chain topologies and capacity values.

## Try it out directly
You can try scgen directly in the browser (everything ready to start in a Jupyter Lab environment): [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/erikdiessel/scgen/master?filepath=notebooks%2FGettingStarted.ipynb)

## Applications
- Creating example models for supply chains
- Creating benchmarks for supply chain optimization algorithms
- Experimental studies of effects in supply chains

## Motivation
To study modeling and optimization of supply chains realistic data is essential. In order to study various effects in supply chain, the quick generation of corresponding data is an important step. Typically data is created in an ad-hoc fashion, making comparisons with other studies and a precise description of the generation difficult.
By integrating various types of supply chain data this tool provides a flexible, extensible and easy-to-use way for generating data.
By using simple human-readable JSON-configurations this helps to achieve the following goals for research:
- Reproducibility: A small file provides the exact details of the data generation that can be easily reproduced.
- Sharing: Configuration-files are small JSON files that are easy to distribute.
- Experimentation: By providing a base set of important types of supply chain data, experiments can be done quickly and easily using the generated JSON-files.

## Architecture
scgen uses an architecture that allows an easy extension by new types of data (called `modules`) and parts of the supply chain (called `components`).

### Components
Each type of an entity (both physical and abstract) in the supply chain corresponds to a `component`.
Some basic examples include:
- suppliers
- plants
- time periods

### Modules
A type of data along with its rules for generation are put together into a `module`.
Some basic modules are built into scgen, for example
- demand
- shipping cost
- supplier capacity
- transportation times

## Usage

### Stand-alone usage
From the top-level folder of scgen, run in a terminal:

    python -m scgen.main.Main < myInput.json > myOutput.json
where `myInput.json` should be the file containing the configuration and myOutput.json the file where the output is stored. The part `> myOuput.json` can also be removed for direct output to the terminal.
Thus, to create the example file `simpleSettings.json` run:
    
    python -m scgen.main.Main < examples/mitigation_examples/allocationSettingsSimple.json > examples/outputs/mitigation_examples/allocationSettingsSimple.json

## Further features

- Optional output to Excel: creates separate sheets with a formatted for each type of data

## Dependencies
- Python: Version 3.7
- Pandas: Version 0.25
- openpyxl: Version 3.0

## Background
Created at [Fraunhofer ITWM, Optimization division](https://www.itwm.fraunhofer.de/)
