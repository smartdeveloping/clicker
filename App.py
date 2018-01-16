from subprocess import Popen, PIPE
import time

script = '''
    activate application "Citrix Viewer"
    tell application "System Events"
    	tell process "Citrix Viewer"
    		click at {400, 400}
            tell application "System Events" to keystroke "a" using command down
            delay 2
    	end tell
    end tell
    return true
'''

while True:
    
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(script)
    print "Clicking!"
    print (p.returncode, stdout, stderr)
    print "Sleeping..."
    time.sleep(5)