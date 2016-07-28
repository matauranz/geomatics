#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
#!/usr/bin/env python

"""Static file server, using Python's CherryPy. 
   Should be used when Django's static development server
   just doesn't cut."""
   
import cherrypy
import os.path
from cherrypy.lib.static import serve_file
from cherrypy.process.plugins import PIDFile 
from cherrypy.process.plugins import Monitor,Autoreloader
import datetime

#publish.......
PIDFile(cherrypy.engine, "/sdcard/geomatics.pid").subscribe()
#cherrypy.engine.autoreload.files.add(__file__)

Autoreloader(cherrypy.engine,frequency=5)


def mycall():
    print 'mycall....config_server.py has login....'
    print 'mycall   ', datetime.datetime.now().strftime("%c")
		 #print 'geomatics-cherrypy-logs-mycall ....' , datetime.now().strftime("%Y-%m-%d-%H-%M-%S") 	

class Root:
    @cherrypy.expose
    def index(self,name='index.html'):
        #name='index.html'
        print '=' * 80 
        print 'file.....',os.path.join(static_dir, name)
        out='''    <link rel="stylesheet" href="assets/css/main.css" />
                    <form     action="https://formspree.io/matauranz@gmail.com " method="POST" >
                    <input type="text" name="name">
    
                    <input type="submit" value="Send......">
            </form>
            '''

        return serve_file(os.path.join(static_dir, name))
        #return out

if __name__=='__main__':
    static_dir = os.path.dirname(os.path.abspath(__file__))  # Root static dir is this file's directory.
    #'/sdcard' put index in sdc.. to render
    print "\nstatic_dir..................: %s\n\n" % static_dir

    p=cherrypy.config.update( {  # I prefer configuring the server here, instead of in an external file.
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8080,
            'engine.autoreload_on': True, 
            'log.screen': True, 
                
             } )
             
    print p        
    
    conf = {
            	'/': {  # Root folder.
            'tools.staticdir.on':   True,  # Enable or disable this rule.
            'tools.staticdir.root': static_dir,
            'tools.staticdir.dir':  '',
        }
    }
    print conf 
    Monitor( cherrypy.engine, mycall,frequency=30).subscribe()
    cherrypy.quickstart(Root(), '/', config=conf)  # ..and LAUNCH ! :)