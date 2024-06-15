# Care-mAHP project

<center><img src="" width=70%"></center>

## Framework
`Care-mAHP`: Framework developed for patient engagement analysis, based on PM4PY and Eng4Py libraries
#### `Demo:` www.molic-avci.com.br
## Library
`Eng4Py`: Library to support the patient engagement analysis based on AHP
## Authors

[@gustavoriz](https://github.com/gustavoriz), `Ph.D student in Health Technology (PPGTS/PUCPR)`
## About

| Function             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| pyAHPeng() | Main function to use to calculate the AHP model |

## How to use
You need to use the `Eng4py` library and call the main function `pyAHPeng()`

A new Python library has been developed, named `ENG4PY (Engagement for Python)`, with the specific goal of assessing the engagement of patients with chronic diseases. The library is highly configurable, allowing users to customize its parameters during function calls. To construct `ENG4PY`, the standard Python libraries `sys, numpy, and csv` were utilized.

The main function of ENG4PY is `pyAHPeng`, which takes three mandatory parameters. The first parameter is the number of criteria to be evaluated, the second is the name of the MCDA model, composed of the full path to the location of the model, while the third parameter is the patient's ID to be evaluated, extracted through PM4PY.

The MCDA model should be in `.csv format` and corresponds to the AHP matrix containing the expert-assigned criterion evaluations. By calculating both the priority index of the AHP model and the individual engagement level of the patient, as well as each criterion's level of engagement for the evaluated patient, ENG4PY aids in identifying key areas for improving patient engagement.

## License and referencing

To use this library, please use the following reference: 

`Riz, Gustavo, ENG4PY: Library to support the patient engagement analysis based on AHP, GitHub. (n.d.). https://github.com/HAILab-PUCPR/ENG4PY`

Please, do not use for commercial proposes. Research only.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
