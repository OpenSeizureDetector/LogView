#!/usr/bin/python
#############################################################################
#
# Copyright Graham Jones, 2017
#
#
#   This file is part of OpenSeizureDetector.
#
#    OpenSeizureDetector is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with OpenSeizureDetector.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

__appname__ = "LogView"
__author__  = "Graham Jones"
__version__ = "0.1"
__license__ = "GNU GPL 3.0 or later"
__doc__ = "inline documentation"

import os,json
from pprint import pprint
import Tkinter as tk



class LogView:
    def onKeyPress(self,event):
        self.text.insert('end', 'You pressed %s\n' % (event.char, ))


    def __init__(self,inFile = None):
        print "LogView.__init__()"
        print os.path.realpath(__file__)
        self.jsonData = []
        f =  open(inFile)
        for s in f:
            try:
                self.jsonData.append(json.loads(s))
            except:
                print "****Error Reading Data from Line: %s" % s
        f.close()

        print self.jsonData

        self.curRec = 0

        if (len(self.jsonData)==0):
            print "**** ERROR - No Log Entries Found in File ****"
            return
        
        root = tk.Tk()
        root.title("OpenSeizureDetector LogView")
        #root.geometry('300x200')
        #self.text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
        #self.text.pack()

        # Put all of the data for the particular record in a frame
        recFrame = tk.Frame(root)
        tk.Label(recFrame,text="recNo:").grid(row=0,column=0)
        self.recNoText = tk.Label(recFrame,text="recNo")
        self.recNoText.grid(row=0,column=1)
        self.alarmPhraseText = tk.Label(recFrame,text="recNo")
        self.alarmPhraseText.grid(row=1,column=0)
        self.dateTimeText = tk.Label(recFrame,text="dateTime")
        self.dateTimeText.grid(row=1,column=1)

        powerFrame = tk.Frame(recFrame)
        tk.Label(powerFrame,text="specPower:").grid(row=0,column=0)
        self.specPowerText = tk.Label(powerFrame,text="specPower")
        self.specPowerText.grid(row=0,column=1)
        tk.Label(powerFrame,text="roiPower:").grid(row=0,column=2)
        self.roiPowerText = tk.Label(powerFrame,text="roiPower")
        self.roiPowerText.grid(row=0,column=3)
        powerFrame.grid(row=3,column=1)

        ratioFrame = tk.Frame(recFrame)
        tk.Label(ratioFrame,text="ratiox10:").grid(row=0,column=0)
        self.ratioText = tk.Label(ratioFrame,text="ratio")
        self.ratioText.grid(row=0,column=1)
        tk.Label(ratioFrame,text="ratioThreshold:").grid(row=0,column=2)
        self.ratioThreshText = tk.Label(ratioFrame,text="ratio")
        self.ratioThreshText.grid(row=0,column=3)
        ratioFrame.grid(row=4,column=1)

        specFrame = tk.Frame(recFrame)
        self.specTexts = []
        for x in range(0, 10):
            tk.Label(specFrame,text=x+1).grid(row=0,column=x)
            self.specTexts.append(tk.Label(specFrame,text="%05d"%x,\
                                           font=('Courier',10)))
            self.specTexts[x].grid(row=1,column=x)
        tk.Label(recFrame,text="spectrum:").grid(row=5,column=0)
        specFrame.grid(row=5,column=1)
        # and add the record frame to the main window.
        recFrame.grid(row=0)

        controlsFrame = tk.Frame(root)
        prevButton = tk.Button(controlsFrame, text="Prev", command=self.prevRec)
        prevButton.grid(row=0,column=0)
        nextButton = tk.Button(controlsFrame, text="Next", command=self.nextRec)
        nextButton.grid(row=0,column=1)
        controlsFrame.grid(row=1)
        

        #root.bind('<KeyPress>', self.onKeyPress)

        self.showRec(self.curRec)
        root.mainloop()

    def showRec(self,recNo):
        print "showRec %d" % recNo
        print self.jsonData[recNo]
        self.recNoText['text']=recNo
        self.alarmPhraseText['text']=self.jsonData[recNo]['alarmPhrase']
        self.dateTimeText['text']=self.jsonData[recNo]['dataTime']
        self.specPowerText['text']=self.jsonData[recNo]['specPower']
        self.roiPowerText['text']=self.jsonData[recNo]['roiPower']
        self.ratioText['text']=10*self.jsonData[recNo]['roiPower'] / \
                                self.jsonData[recNo]['specPower']
        self.ratioThreshText['text']=self.jsonData[recNo]['alarmRatioThresh']
        for x in range(0,10):
            self.specTexts[x]['text'] = '{:_>6}'.format(self.jsonData[recNo]['simpleSpec'][x])
        
    def nextRec(self):
        print "nextRec"
        self.curRec = self.curRec+1
        if (self.curRec>=len(self.jsonData)):
            self.curRec = len(self.jsonData)-1
        print self.curRec
        self.showRec(self.curRec)

    def prevRec(self):
        print "prevRec"
        self.curRec-=1
        if (self.curRec<=0):
            self.curRec = 0;
        print self.curRec
        self.showRec(self.curRec)
    
if __name__=="__main__":
    # Boilerplate code from https://gist.github.com/ssokolow/151572
    from optparse import OptionParser
    parser = OptionParser(version="%%prog v%s" % __version__,
            usage="%prog [options] <argument> ...",
            description=__doc__.replace('\r\n', '\n').split('\n--snip--\n')[0])
    parser.add_option('-s', '--save', action="count", dest="save",
        default=0, help="Save a new background image.")
    parser.add_option('-f', '--file', dest="fname",
        help="Save a new background image.")
 
    opts, args  = parser.parse_args()
 
    print opts
    print args

    if len(args) != 1:
        parser.error("you must specify the log file to read")

    
    #if (opts.save):
    #    print "Saving new background Image"
    #    BenFinder(save=True)
    #    print "Done!"
    #elif (opts.fname):
    #    print "Running from file (not live kinect)"
    #    BenFinder(inFile=opts.fname)
    #else:
    #    BenFinder(save=False)

    LogView(args[0])
