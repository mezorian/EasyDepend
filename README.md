# EasyDepend
A python tool to handle dependencies configured like in google-repo

## Requirements
### Install pip 
```
sudo apt-get -y install python3-pip

```

### Install Gitpython
```
pip3 install gitpython
```

## Usage
Import the EasyDepend module with 
```
import EasyDepend
```

And run the cloneDependency function for a path with manifest xml file inside like
```
EasyDepend.cloneDependencies(/home/anon/ProjectDir)
```

For this also have a look at example.py
