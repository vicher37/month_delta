# month_delta
A Python module to calculate the delta between months without considering days.
Useful when the desired accuracy of calculation is month instead of days, such as when you need to get data for all months involved.
If the months interested are relatively far away from each other and don't involve February, it's usually fine to just use <a href="https://docs.python.org/2/library/datetime.html#datetime.timedelta">datetime.timedelta</a> or <a href="https://labix.org/python-dateutil#head-ba5ffd4df8111d1b83fc194b97ebecf837add454">dateutil.relativedelta</a>. 

However, if you use them to calculate delta between, for example, Feb 28 2015 and Mar 3 2015, they would tell you the delta is less than 1 month. That's not the desired output sometimes. Sometimes the desired output is '1 month' for this case. This module can solve this problem for you while making sure all the regular calculations (those without idiosyncrasies) are nicely resolved too.
