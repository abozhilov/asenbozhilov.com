import conf

def head(title = '', is_home_page = False, css_files = [], js_files = []):  

    #Generate HTML code for CSS files 
    css_str = '<link rel="stylesheet" type="text/css" href="{0}">\n'
    all_css = ''
    for i in css_files:
        all_css = all_css + css_str.format(i)    
    
    #Generate HTML code for JavaScript files 
    js_str = '<script type="text/javascript" src="{0}"></script>\n'
    all_js = ''
    for i in js_files:
        all_js = all_js + js_str.format(i)
    
    name = 'asenbozhilov.com'
    if not is_home_page:
        name = '<a href="index.html">' + name + '</a>'
    
    return """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" 
"http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
		<title>{0}</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">
		<link rel="stylesheet" type="text/css" href="{1}/site.css">\n
		{2}
		{3}
	</head>
	<body>
        <div id="container">

            <div id="header">
                <h1 id="logo">{4}</h1>
                <p class="slogan">Personal page of Asen Bozhilov</p>
                
                <a class="doc-banner" href='https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Array' title='JavaScript Array concat'><img src='images/promotejsh.png' alt='JavaScript Array concat'></a>
            </div>""".format(title, conf.CSS_DIR, all_css, all_js, name)
#END

def nav(active_cat = -1):
    html_code = '<ul id="navigation">'
    cat_item = '\n<li><a {2} href="{1}">{0}</a></li>'
    
    for i, c in enumerate(conf.CATEGORIES):
        if i == active_cat:
            html_code = html_code + cat_item.format(c['name'], c['output'], 'id="active_cat"')
        else:
            html_code = html_code + cat_item.format(c['name'], c['output'], '')
    
    return html_code + '\n</ul>'         
#END         
        
def foot():
    return """            <div id="footer">
                          <span class="icons"><a href="http://www.python.org/"><img src="images/icon-python.png" alt="Powerd by Python"></a></span>
                Copyright &copy; 2010 - 2011 Asen Bozhilov - All Rights Reserved
                
            </div>
        </div>

	</body>
</html>"""
#END

class Article:
    def __init__(self, title, date, description, toc, article_path, output_file, lang = [], css_str = '', js_files = []):
        self.title = title
        self.date = date
        self.description = description
        self.toc = toc #Table Of Contents
        self.article_path = article_path
        self.output_file = output_file
        self.lang = lang
        self.css_str = css_str
        self.js_files = js_files                     
    
    def basicHTML(self):
        """Get the basic info of the article
        
        It generates html code for the basic view of the article
        """
        if self.description != '':
           description = '<p class="article-desc">' + self.description + '</p>'
        else:
            description = ''
        
        lang_str = ''
        for article in self.lang:
            lang_str = lang_str + ' (<a href="{0}">{1}</a>)'.format(article.output_file, article.title)
            
        return """<h2 class="article-title"><a href="{0}">{1}</a>{2}</h2>
        <em>{3}</em>
        {4}
        {5}
        """.format(self.output_file, self.title, lang_str, self.date, description, self.toc)
           
    def export(self, category):
        self.write(category)
        for article in self.lang:
            Article.write(article, category)
            
    def write(self, category):
        with open(self.article_path, 'r') as f:
            with open(conf.OUTPUT_DIR + '/' + self.output_file, 'w') as out:
                out.write(head(self.title))
                out.write(nav(category))
                out.write('<div id="content">{0}</div>'.format(f.read()))
                out.write(foot())                      
#END 

class ArticleCategory:
    def __init__(self, name, articles, output_name, title, cat_id):
        self.name = name
        self.articles = articles
        self.output_name = output_name
        self.title = title
        self.id = cat_id

    def content(self, content):
        return """
                <div id="content"> 
                    <h1>{0}</h1>
                    {1}
                </div>""".format(self.name, content)  

    def buildPage(self, output_name, prev_name = '', next_name = '', start_pos = 0, end_pos = 0):
        print '->', output_name, 
        with open(conf.OUTPUT_DIR + '/' + output_name, 'w') as f:
             f.write(head(self.title, prev_name == ''))
             f.write(nav(self.id))
             
             cnt_str = ''
             for i in range(start_pos, end_pos):
                article = self.articles[i]
                cnt_str = cnt_str + article.basicHTML() 
             
             if prev_name != '' or next_name != '':
                cnt_str = cnt_str + '<p class="paging">'
                if prev_name != '':
                    cnt_str = cnt_str + '<a href="' + prev_name + '">&laquo; Newer Entries</a> '
                if next_name != '':
                    cnt_str = cnt_str + '<a href="' + next_name + '">Older Entries &raquo;</a> '        
                cnt_str = cnt_str + '</p>'
                      
             f.write(self.content(cnt_str))
             f.write(foot())
        print 'OK' 

    def build(self):
        articles_len = len(self.articles)
        pages = articles_len / conf.ARTICLES_PER_PAGE
        exact_articles = articles_len % conf.ARTICLES_PER_PAGE == 0    
        i = 0    
        if pages:
            self.buildPage(self.output_name, '', '1' + self.output_name, 0, conf.ARTICLES_PER_PAGE) 
            
            for i in range(1, pages):
                start_pos = i * conf.ARTICLES_PER_PAGE
                if exact_articles and i == pages - 1:
                    self.buildPage('{0}{1}'.format(i, self.output_name), '{0}{1}'.format(i - 1 or '', self.output_name), '', start_pos, start_pos + conf.ARTICLES_PER_PAGE)
                else:
                    self.buildPage('{0}{1}'.format(i, self.output_name), '{0}{1}'.format(i - 1 or '', self.output_name), '{0}{1}'.format(i + 1, self.output_name), start_pos, start_pos + conf.ARTICLES_PER_PAGE)
            
            if  not exact_articles:
                self.buildPage('{0}{1}'.format(i + 1, self.output_name), '{0}{1}'.format(i or '', self.output_name), '', conf.ARTICLES_PER_PAGE + (i * conf.ARTICLES_PER_PAGE), articles_len)
        else:
            self.buildPage(self.output_name, '', '', 0, articles_len)
            
        #Export articles
        print 'Export articles'
        for article in self.articles:
            print '--->', article.output_file,
            article.export(self.id)
            print 'OK'
#END 
