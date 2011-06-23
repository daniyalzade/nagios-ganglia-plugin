Introduction
------------

`check_ganglia_metrics` is a [Nagios](http://nagios.com/) plugin that checks values for specified
metrics from [Ganglia](http://ganglia.sourceforge.net/) and raises erros if need.

This tool is inspired by @vvuksan's blog post (http://bit.ly/qVu8Z)


Usage
-----

    > python ganglia_metric_checker.py -H <hostname> -M <metric> --critical=<critical value> --warning=<warning value>


Dependencies
------------

* [python 2.5+](http://python.org/)


Issues
------
Please report issues via [github issues](https://github.com/daysleeper/nagios-ganglia-plugin/issues)


To Do
-----

* suggestions?
