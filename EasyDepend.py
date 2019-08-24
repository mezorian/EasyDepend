from git import Repo
import git
import os
import xml.etree.ElementTree as ET

def cloneDependencies(path):
    # open xml manifest file
    if os.path.exists(path+'/default.xml'):
        tree = ET.parse(path+'/default.xml')
        manifest = tree.getroot();

        # loop over all "project" child elements
        for child in manifest:
            if child.tag == "project":
                # clear variables
                projectName     = ""
                projectRemote   = ""
                projectRevision = ""
                projectPath     = ""
                projectFetch    = ""
                cloneToPath     = ""

                # get attribute information
                projectName     = child.get('name')
                projectRemote   = child.get('remote')
                projectRevision = child.get('revision')
                projectPath     = child.get('path')

                # loop again over all elements to find the remote fetch url
                for child2 in manifest:
                    if child2.tag == "remote":
                        remoteName = child2.get('name')
                        if remoteName == projectRemote:
                            projectFetch = child2.get('fetch')
                            break # skip other iterations of this loop

                if projectFetch == "":
                    raise Exception("No fetch url defined for remote '" + projectRemote + "' in manifest file")

                # if the path attribute is set, clone to this path
                # otherwise use the project name as path
                if projectPath is not None:
                    cloneToPath = projectPath
                else:
                    cloneToPath = projectName

                # clone the project and checkout revision and pull latest version
                print("##### Found project",projectName,"from remote",projectFetch, "#####")
                print("##### Cloned project to",path+"/"+cloneToPath,"#####")
                repo = Repo.clone_from(projectFetch+"/"+projectName+".git", path+"/"+cloneToPath)
                repo.git.checkout(projectRevision)
                print("##### Checked out revision",projectRevision,"#####")

                # recursively call this function again for the previously cloned directory
                # if this repository again contains a manifest, again all
                # dependencies are cloned
                cloneDependencies(path+"/"+cloneToPath)
