import btree

class Datapages():
    def __init__(self,name):
        try:
            self.f = open(name, "r+b")
        except OSError:
            self.f = open(name, "w+b")

    def openDB(self):
        try:
            self.db = btree.open(self.f)
            print('db open')
        except:
            print('error in open db')

    def openPage(self,pageName):
        page = self.db[str(pageName)]
        return self.mountPage(page)

    def mountPage(self,page):
        pageMount = b'HTTP/1.0 200 OK\r\n Content-Type:text/html; charset=UTF-8\r\n\r\n'+page
        return pageMount

    def addPage(self,name,page):
        self.db[b""+str(name)]= b""+page
        self.db.flush()

    def dbClose(self):
        self.db.close()
    def bancoClose(self):
        self.f.close()
