import xml.etree.ElementTree as et
import pandavro as pdx
import pandas as pd

def readfromxmltodict(path):
    tree = et.parse(path)
    root = tree.getroot()
    # for child in root:
    #   print(child.tag, child.attrib, sep=" | ")
    data = {}
    i = 0
    for child in root:
        data[i] = []
        for ch in child:
            if ch.text is "date":
                data[i].append("DATE HERE")
            else:
                data[i].append(ch.text)
        i+=1
    return data



dictData = readfromxmltodict("D:\\Personal Data\\My Documents\\OE-NIK\\2021_21_1\\Projektmunka III\\ff\\countries.xml")

OUTPUT_PATH = "D:\\Personal Data\\My Documents\\OE-NIK\\2021_21_1\\Projektmunka III\\ff\\example.avro"
pdx.to_avro(OUTPUT_PATH, pd.DataFrame.from_dict(dictData))
saved = pdx.read_avro(OUTPUT_PATH)
print(saved)


