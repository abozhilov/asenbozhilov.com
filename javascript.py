#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import conf
import lib

#Articles 
articles = [
    lib.Article(
        title        = '<code>evalJSON(JSONStr, reviver);</code>', 
        date         = '2011-02-14', 
        description  = 'JSON parser according the defined JSON Lexical Grammar by ECMA-262-5 standard.',
        toc          = '',
        article_path = 'articles/json.html',
        output_file  = 'json.html' 
    ),
    
    lib.Article(
        title        = 'JSON.parse compatibility table', 
        date         = '2010-11-17', 
        description  = 'It tests <code>JSON.parse</code> for conformance implementation of JSON Lexical Grammar.',
        toc          = '',
        article_path = 'articles/json-parse.html',
        output_file  = 'json-parse.html' 
    ),
    
    lib.Article(
        title        = 'Javascript syntax highlighter', 
        date         = '2010-11-12', 
        description  = 'Syntax highlighter has been built by <a href="https://github.com/abozhilov/SourceText">SourceText</a> library.',
        toc          = '',
        article_path = 'articles/colorize.html',
        output_file  = 'colorize.html' 
    ),
    
    lib.Article(
        title        = 'ECMAScript Idеntifiers - validator and compatibility table', 
        date         = '2010-10-18',
        article_path = 'articles/es-identifiers.html',
        output_file  = 'es-identifiers.html',          
        description  = '',
        toc          = """<ul class="home-contents contents"> 
                            <li><a href="es-identifiers.html#validator">Identifier validator</a></li> 
                            <li><a href="es-identifiers.html#compat-table">Compatibility table</a></li> 
                        </ul>"""
    ),
        
    lib.Article(
        title        = 'Javascript quiz', 
        date         = '2010-06-29', 
        description  = 'Test your knowledge in ECMA-262-3 with 10 questions.',
        toc          = '',
        article_path = 'articles/quiz.html',
        output_file  = 'quiz.html' 
    ),
    
    lib.Article(
        title        = 'Javascript identifiers', 
        date         = '2010-03-08',
        article_path = 'articles/identifiers-en.html',
        output_file  = 'identifiers-en.html',          
        description  = '',
        
        lang         = [lib.Article('Български', '', '', '', article_path = 'articles/identifiers.html', output_file  = 'identifiers.html')],
        
        toc          = """<ul class="home-contents contents"> 
	                <li><a href="identifiers-en.html#introduction">Introduction</a></li> 
 
	                <li> 
		                <a href="identifiers-en.html#reserved_words">Reserved words from the language</a> 
		                <ul> 
			                <li><a href="identifiers-en.html#keywords">Keywords</a></li>	
			                <li><a href="identifiers-en.html#future_reserved">Reserved words for future use</a></li> 
			                <li><a href="identifiers-en.html#bool_literal">Boolean literal</a></li> 
			                <li><a href="identifiers-en.html#null_literal">Null literal</a></li> 
 
		                </ul> 
	                </li> 
	                <li> 
		                <a href="identifiers-en.html#ids_name">Identifier names</a> 
		                <ul> 
			                <li> 
				                <a href="identifiers-en.html#identifier_start">First character in identifier</a> 
				                <ul> 
 
					                <li><a href="identifiers-en.html#underscore">Underscore sign "_"</a></li>	
					                <li><a href="identifiers-en.html#dollar_sign">$</a></li> 
					                <li><a href="identifiers-en.html#unicode_letter">Letter from the Unicode table</a></li> 
					                <li><a href="identifiers-en.html#unicode_escape_sequences">Unicode escape sequence</a></li> 
				                </ul>						
			                </li>	
			                <li><a href="identifiers-en.html#identifier_part">The rest of the identifier name</a></li> 
		                </ul> 
	                </li> 
	
	
	                <li> 
		                <a href="identifiers-en.html#property_names">Names and object property accessing</a> 
		                <ul> 
			                <li><a href="identifiers-en.html#dot_notation">Dot notation</a></li>	
			                <li><a href="identifiers-en.html#square_bracket">Square bracket notation</a></li> 
		                </ul>				
	                </li> 
 
	                <li> 
		                <a href="identifiers-en.html#object_literals">Object initialization ({ })</a> 
		                <ul> 
			                <li><a href="identifiers-en.html#oi_property_name">Prоperty name in object literal</a></li>
		                </ul> 
	                </li> 
	                <li><a href="identifiers-en.html#conclusion">Conclusion</a></li> 
 
	                <li><a href="identifiers-en.html#literature">Useful materials</a></li> 
                </ul>"""
    )                   
]

ACTIVE_CATEGORY = int(sys.argv[1])
CATEGORY = conf.CATEGORIES[ACTIVE_CATEGORY]

category = lib.ArticleCategory(CATEGORY['name'], articles, CATEGORY['output'], CATEGORY['title'], ACTIVE_CATEGORY)
category.build()


   
    
