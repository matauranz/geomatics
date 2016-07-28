#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
#!/usr/bin/env python

"""Static file server, using Python's CherryPy. 
   Should be used when Django's static development server
   just doesn't cut.         edit                         """
   
import cherrypy
from cherrypy.lib.static import serve_file
from cherrypy.process.plugins import PIDFile
import webbrowser


p = PIDFile(cherrypy.engine, "/sdcard/myapp.pid") 
p.subscribe()
cherrypy.engine.autoreload.files.add(__file__)
s=cherrypy.engine.autoreload
s.subscribe()



import os.path

class Root:
    @cherrypy.expose
    def index(self, name='contact_form.html'):
        #name='index.html'
        print '=' * 80 
        print 'file.....',os.path.join(static_dir, name)
        
        return serve_file(os.path.join(static_dir, name))

if __name__=='__main__':
    static_dir = os.path.dirname(os.path.abspath(__file__)) +'/static'  # Root static dir is this file's directory.
    
    print "\nstatic_dir: %s\n\n" % static_dir

    cherrypy.config.update( {  # I prefer configuring the server here, instead of in an external file.
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
            #'engine.autoreload_on': True, 
            'log.screen': True, 
                
             } )
    conf = {
        '/': {  # Root folder.
            'tools.staticdir.on':   True,  # Enable or disable this rule.
            'tools.staticdir.root': static_dir ,
            'tools.staticdir.dir':  '',
        }
    }

    cherrypy.quickstart(Root(), '/', config=conf)  # ..and LAUNCH ! :)
    webbrowser.open('http://127.0.0.0.1:8080')