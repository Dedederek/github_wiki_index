import os
from urllib.parse import quote

def createIndexFile(startpath, indexFile):
    for root, dirs, files in os.walk(startpath):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        level = root.replace(startpath, '').count(os.sep) - 1
        indent = ' ' * 2 * (level)
        directory = os.path.basename(root)
        if directory != '.':
            indexFile.write('{}- {}\n'.format(indent, '<details>\n'+indent+'  <summary>'+os.path.basename(root)+'</summary>\n'))
            subindent = ' ' * 2 * (level + 1)
            for f in files:
                indexFile.write('{}- [{}]({})\n'.format(subindent, f[:-3], quote(f[:-3],encoding='UTF-8')))
            for i in range(level,0,-1):
                indexFile.write('{}  </details>\n'.format(' ' * 2 * (level)))

indexFile = open('_Sidebar.md', 'w')
createIndexFile(".", indexFile)
indexFile.close()
