# Problem Stats in Dynatrace

Problem Stats in Dynatrace is a Python Project to generate statistics on the MTTR (Mean Time To Resolution) and MTBF (Mean Time Between Failures) based on the Problems reported in Dynatrace.

MTTR example: A failure rate increase problem opens on a Monday at 2pm – 3:30 pm (90 minutes) and another at Tuesday at 9am – 9:30am (30 minutes). The MTTR calculates the mean of the time the problem statyed open until resolution, in this case: (90 + 30)/2 = 60 minutes.

MTBF example: Problem 1 (Monday 1pm – 2pm), problem 2 (Tuesday 10am-10:30am) and problem 3 (Wednesday 1pm-1:30pm). 20 hrs(1200 minutes) between problem 1 and 2, 25.5 hrs(1530 minutes) between 2 and 3, then the mean would be (1200 + 1530)/2 = 1365 minutes

## Prerequisites

Use the package manager pip3 to install the dependencies.

```bash
pip3 install -r requirements.txt
```

## Usage

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