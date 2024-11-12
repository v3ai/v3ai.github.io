start = '''<!DOCTYPE HTML>
<html>
	<head>
		<link rel="stylesheet" href="style-list.css">

	</head>
	<body>
    <h1 class="top" >Todo List</h1>
'''

end = '''
	</body>
</html>

'''
flag = 0

with open('list', 'r') as file1:
    with open('list.html', 'w') as file2:
        file2.write(start)
       
        for line in file1:
            if((line[0] != '\n') and (line[0] != '-')):
                file2.write('<h3>' + line.strip() + '</h3>\n')
            if (line[0] == '\n'):
                file2.write('<br>\n')
            if( (line[0] == '-') and (line[1] == '-') and (line[0] == '-') ):
                if(flag == 0):
                    file2.write('<hr>\n')
                    file2.write('<ul>\n')
                    flag = 1
                elif(flag == 1):
                    file2.write('</ul>\n')
                    file2.write('<hr>\n')
                    flag = 0
            if((line[0] == '-') and (line[1] != '-')):    
                file2.write('<li>' + line[2:].strip() + '</li>\n')    
                    

                
        file2.write(end)
