#components
from htmlcomponents import *
from csscomponents import *
#files
colors = open("pythongen/colors.csv","r")
html_file = open("custom/demo.html" , "w")
css_file = open("custom/customtag.css", "w")
colorlist = []
#adding default classes to the cssfile
css_file.write(defaultcomponents())
for color in colors:
    #removing whitespace and escape sequence character in each line 
    color = color.strip('\n').split(',') #separating values into a list
    colorlist.append(color)

html_file.write(top())
print(colorlist)
count = 0
for i in colorlist:
    if count%5 == 0:
        html_file.write("</tr><tr>")
    html_file.write(table(i[0]))
    count+=1
    
html_file.write("""</tr></table>""")

for i in range(len(colorlist)):
    #importing function from csscomponents and writing class to css file
    tagname = ".tag-" + colorlist[i][0]
    towrite = normalclass(tagname,colorlist[i][1]) + hollowclass(tagname+"-hollow",colorlist[i][1])
    css_file.write(towrite)

    normal = "tag-"+ colorlist[i][0]
    hollow = "tag-" + colorlist[i][0] + "-hollow"
    html_file.write(showcase(colorlist[i][0].title(),normal,hollow))
html_file.write(bottom())

#closing files
colors.close()
html_file.close()
css_file.close()