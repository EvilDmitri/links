from grab import Grab


def TrackBack():
    g = Grab()

    g.setup(post='title=Foo+Bar&url=http://www.bar.com/&excerpt=My+Excerpt&blog_name=Foo')

    g.go(url='http://www.bbqchickenatl.com/?document_srl=1062&act=trackback&key=72c')


def FormFind():
    from grab.ext.form import FormExtension
    g = Grab()

    g.setup(timeout=30000)

    g.go('http://www.zjxysy.com/Shownews.asp?id=109445')
    #form = g._lxml_tree.forms[0]


    g.choose_form(xpath='//form[@action="Comment.asp?id=109445"]')
    fields = g.form_fields() # check it
    g.set_input_by_xpath('//textarea', 'sample text')
    g.set_input_by_xpath('//input[@type="text"]', 'sample title')
    g.submit()
