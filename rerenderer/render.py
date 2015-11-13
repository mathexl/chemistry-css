f = open('box.css', 'w');

X = 1
Y = 1
while(X < 11):
    Y = 1
    while(Y < 21):
        f.write('div[box' + str(X) + '_' + str(Y) + ']{\n')
        f.write('left: ' + str((X-1)*100) + 'px;\n')
        f.write('top: ' + str((Y-1)*80) + 'px;\n')
        f.write('}\n')
        
        
        f.write('div[box' + str(X) + '_' + str(Y) + '] + hr{\n')
        f.write('left: ' + str(65 + (X-1)*100) + 'px;\n')
        f.write('top: ' + str(37 + (Y-1)*80) + 'px;\n')
        f.write('}\n')
        
        f.write('div[box' + str(X) + '_' + str(Y) + '] + hr + hr{\n')
        f.write('left: ' + str(65 + (X-1)*100) + 'px;\n')
        f.write('top: ' + str(37 + (Y-1)*80) + 'px;\n')
        f.write('}\n')
        
        
        f.write('div[box' + str(X) + '_' + str(Y) + '] + hr + hr + hr{\n')
        f.write('left: ' + str(65 + (X-1)*100) + 'px;\n')
        f.write('top: ' + str(37 + (Y-1)*80) + 'px;\n')
        f.write('}\n')
        
        
        f.write('div[box' + str(X) + '_' + str(Y) + '] + hr + hr + hr + hr{\n')
        f.write('left: ' + str(65 + (X-1)*100) + 'px;\n')
        f.write('top: ' + str(37 + (Y-1)*80) + 'px;\n')
        f.write('}\n')
        
        
        Y = Y + 1
    X = X + 1

f.close

