from urllib import request

sample_url = 'http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    #guarantee that data is string
    csv_string = str(csv)
    lines = csv_string.split("\\n")
    dest_url = r'sample.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(sample_url)

'''
Writing files
'''
fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

'''
Reading files
'''
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()