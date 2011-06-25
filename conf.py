OUTPUT_DIR = 'site'
CSS_DIR = 'css'
JS_DIR = 'js'
IMG_DIR =  'images'

ARTICLES_PER_PAGE = 10

CATEGORIES = [
    {
        'name' : 'Javascript', 
        'output' : 'index.html', 
        'generator' : 'javascript.py', 
        'title' : 'Personal page of Asen Bozhilov'
    },
    {
        'name' : 'Resources', 
        'output' : 'resources.html',
        'input'  : 'pages/resources.html', 
        'title' : 'Resources'
    },
    {
        'name' : 'About', 
        'output' : 'about.html',
        'input'  : 'pages/about.html', 
        'title' : 'About me'
    }
]
