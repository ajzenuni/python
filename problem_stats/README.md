# Dynatrace Problem Stats KPI

## Overview
*Dynatrace Problem Stats KPI* is a Python Project to generate statistics on the MTTR (Mean Time To Resolution) and MTBF (Mean Time Between Failures)

* **MTTR** example: 
    * A failure rate increase problem opens on a Monday at 2pm – 3:30 pm (1hr 30 minutes) and another at Tuesday at 9am – 9:30am (30 minutes). 
    * The mean of time of the problem being open, in this case: 90 + 30 / 2 = **60 min**. 

* **MTBF** example: 
    * Three problems happen - problem 1 (Monday 1pm – 2pm), problem 2 (Tuesday 10am-10:30am) and problem 3 (Wednesday 1pm-1:30pm). 
    * 20 hrs (1200 min) between problem 1 and 2, 25.5 hrs (1530 min) between 2 and 3, the mean would be (1200 + 1530)/ 2 = 1365 minutes.


## Prerequisites

* Python 3.7+
* Requires your tenant URL – https://{uuid}.live.dynatrace.com, and an api-token, with access to problem feed.
* Use the package manager pip3 to install the dependencies.

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

* Update the params.json file with the tenant URL, api-token.
* Also in that params.json is a relativetime field which can contain one of the following values: 10mins, 15mins, 2hours, 30mins, 3days, 5mins, 6hours, day, hour, min, month, week. 
* And then the tags section can either be left empty or you can apply tag values specific to your environment such as [“Environment:PROD”,”App:MY_APP_TAG_NAME”]
* Running 
    ```bash
    python problem_stats.py
    ```
    
    ```powershell
    python.exe .\problem_stats.py
    ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)