jsonfile = 'data.json'
outfile = 'output.txt'

# get a file object and read it in as a string
fileobj = open(jsonfile)
jsonstr = fileobj.read()
fileobj.close()

# do character conversion here
if jsonstr.endswith('\n'):
    jsonstr = jsonstr[:-1]
outstr = jsonstr.replace('\t','\\t').replace('\n', '\\n')

fileobj = open(outfile, 'w+');
fileobj.write(outstr)
fileobj.close

print("OK!")