from git import Repo
import os
import xml.etree.ElementTree as ET

def cloneDependencies(path):
    if os.path.exists(path+'/default.xml'):
        tree = ET.parse(path+'/default.xml')
        manifest = tree.getroot();
        for child in manifest:
            if child.tag == "project":
                projectName = child.get('name')
                projectRemote = child.get('remote')
                projectRevision = child.get('revision')
                for child2 in manifest:
                    if child2.tag == "remote":
                        remoteName = child2.get('name')
                        if remoteName == projectRemote:
                            projectFetch = child2.get('fetch')
                print("Clone to",path+"/"+projectName)
                Repo.clone_from(projectFetch+"/"+projectName+".git", path+"/"+projectName)
                cloneDependencies(path+"/"+projectName)

currentPath = os.getcwd()
cloneDependencies(currentPath)
