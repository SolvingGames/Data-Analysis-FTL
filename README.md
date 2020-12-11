# Data-Analysis-FTL
This repository provides the code used for a data analysis youtube project:

 video link

 An excel report is created in order to compare your in game performance against your previously collected experience in order to analyze your decisions.

## How To Install

In order to utilize this repository, you will need to install:
* [.Net Core](https://dotnet.microsoft.com/download/dotnet-core)
* [FTLAV](https://github.com/Niels-NTG/FTLAV)
* [depotdownloader](https://github.com/SteamRE/DepotDownloader)  

You will need to downgrade your FTL installation to version 1.5.13 [212681\4710954] for FTLAV to work properly, which is used to record the initial data, which will be aggregated and manipulated.

After that is done, feel free to download this repo and install the rest of the requirements listed in requirements.txt via pip or environment.yml via conda.

## How To Use

All runs need to be saved with FTLAV into /Data/ in order to be aggregated by aggregate.py into analysis.xlsx.

After that, feel free to run create_report.py in order to refresh the analysis with the newest data. (The last row in the sheet called "aggregation" will be considered.)
