def read_file  (_path):
    f = open(_path,mode="r",encoding="utf-8")
    _content = f.read()
    f.close()
    return _content
    