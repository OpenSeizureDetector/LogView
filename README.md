OpenSeizureDetector LogView
===========================

This is a simple python script to view the alarm log files produced by
OpenSeizureDetector.   Obtain the files either from the OpenSeizureDetector
web interface or using the 'View Log Entries' menu option on the OpenSeizureDetector Android App.

![alt tag](https://github.com/OpenSeizureDetector/LogView/blob/master/Screenshot_2017-02-18_23-06-10.png)

Usage is simply ./LogView.py filename

The script provides a simple graphical interface to allow you to step through
the alarm records to see the key parameters that caused the alarm, including
the spectrum data.

This is not pretty and there is plenty of scope for improvement, including

* adding a bar graph of the spectrum - this just shows the numerical data
at the moment.
* filter out warnings to only show alarms
* jump to specified date/time or record number to make it easier to look at large files.

Please contact graham@openseizuredetector.org.uk for any further info.
