print "Android/SL4A Balloon Camera Auto Shooter"
print "Created by Gerry Gabrisch GISP, GIS Manager Lummi Indian Business Council"
print "geraldg@lummi-nsn.gov" 
print "Copy? Right! 2014, No rights reserved." 
import androidhelper as android 
import time 

droid = android.Android() 
delay = droid.dialogGetInput('Input 1','Delay before starting?','1').result
numberOfShots = droid.dialogGetInput('Input 2','Total images to capture?', '3').result 
delayBetweenShots =droid.dialogGetInput('Input 3','Delay (Seconds) between captures','2').result 
droid.ttsSpeak('taking pictures in'+ delay +'seconds') 
time.sleep(int(delay)) 
counter = 1 
droid.ttsSpeak('taking pictures now') 

while counter <=int(numberOfShots) : 
	droid.cameraCapturePicture('/sdcard/'+str(counter)+ "-droid.jpg") 
	counter +=1 
	if counter != int(numberOfShots): 
	    time.sleep(int(delayBetweenShots)) 
print "done without error..." 
droid.ttsSpeak('Finished without error...') 
del droid
