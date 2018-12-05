import zipfile, requests, shutil, os, sys

def makeFolder(path):
    # check if the folder exists
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
    except:
        print "Folder error:", sys.exc_info()[0]
        return False
    return True

    
def deleteExistingFiles(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
    except:
        print("cannot remove file")
        return False
    return True

def fetchZip(url, basePath, folder, filename):
    print("Fetch from: " + url)
    print("File destination: " + basePath + folder + "/" + filename)

    if deleteExistingFiles(basePath + folder + "/"):
        if makeFolder(basePath + folder + "/"):    
            #download file
            try:
                r = requests.get(url)
                with open(basePath + folder + "/" + filename, 'wb') as fd:
                    for chunk in r.iter_content(2000):
                        fd.write(chunk)

                #extract the zip
                zip_ref = zipfile.ZipFile(basePath + folder + "/" + filename, 'r')
                zip_ref.extractall(basePath + folder)
                zip_ref.close()

                print("def done")
            except:
                print "Unexpected error:", sys.exc_info()[0]
                print "Moving on"

 

try:
    basePath = "D:/ArcGIS_Work/python/DataUpdates/"

    jacksonFolder = "Jackson"
    url = 'https://opendata.arcgis.com/datasets/70b775d797184263972ed1763ca288be_3.zip'
    fetchZip(url, basePath, jacksonFolder, "JacksonTaxlots.zip")


    joStreets = 'JoCoStreets.zip'
    joFolder = "Josephine"
    
    #if os.path.exists(dest):
    #    shutil.rmtree(des)

    #if not os.path.exists(dest):
    #    os.makedirs(dest)

    url = 'http://alt.co.josephine.or.us/filedrop/gis/JoCo_Streets.zip'
    fetchZip(url, basePath, joFolder, joStreets)


    print "Done"
except OSError as e:
    raise
