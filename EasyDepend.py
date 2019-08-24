from git import Repo
import os
import xml.etree.ElementTree as ET

tree = ET.parse('default.xml')
for elem in tree.iter():
    print(elem)
    

dirpath = os.getcwd()


#cloned_repo = repo.clone(os.path.join(rw_dir, 'to/this/path'))

#import git
#git.Git(dirpath).clone("git://gitorious.org/git-python/mainline.git")
#from git import Rep

Repo.clone_from("git@github.com:mezorian/EasyDepend.git", dirpath+"/EasyDepend")

print("Hello World!")
