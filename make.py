#! /usr/bin/python

import conf
import lib
import os
import shutil
import subprocess


if os.path.exists(conf.OUTPUT_DIR):
    print '''The output has already generated.
If you would like to regenerate the output, please remove the "{0}" directory.'''.format(conf.OUTPUT_DIR)
 
else:
    print 'Create output directory:', conf.OUTPUT_DIR, 
    os.mkdir(conf.OUTPUT_DIR)
    print '=> OK'

    print 'Copy CSS files',
    shutil.copytree(conf.CSS_DIR, conf.OUTPUT_DIR + '/' + conf.CSS_DIR)
    print '=> OK' 

    print 'Copy JavaScript files',
    shutil.copytree(conf.JS_DIR, conf.OUTPUT_DIR + '/' + conf.JS_DIR)
    print '=> OK'

    print 'Copy Images',
    shutil.copytree(conf.IMG_DIR, conf.OUTPUT_DIR + '/' + conf.IMG_DIR)
    print '=> OK'

    for i, c in enumerate(conf.CATEGORIES):
        print 'Create {0} files ...'.format(c['name'])
        if 'generator' in c:
            if subprocess.call(['./' + c['generator'], str(i)]):
                break
            else:  
                print '===================> OK'
        else:
            with open(conf.OUTPUT_DIR + '/' + c['output'], 'w') as out:
                with open(c['input'], 'r') as f:
                    out.write(lib.head(c['title']))
                    out.write(lib.nav(i))
                    out.write('<div id="content">{0}</div>'.format(f.read()))
                    out.write(lib.foot())
            print '===================> OK'
                 
