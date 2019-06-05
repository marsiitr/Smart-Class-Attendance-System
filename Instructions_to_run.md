## Libraries 
#### 1. Python3
Python is a programming language of scripting type. The code is built for any Python3 version. If you work on ubuntu python2 is present as default while windows does not have python in it. So you need to download it yourself. Here are the instructions for installing python [on ubuntu](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/) and [for windows](https://www.howtogeek.com/197947/how-to-install-python-on-windows/).

#### 2. face_recognition 
The basic requirement for this code is the library called face_recognition. It is the core of the project. Here lies the bad news for the windows users since face_recognition is difficult to install on windows , even though to install face_recognition on windows [click here](https://github.com/ageitgey/face_recognition/issues/96). While for ubuntu simple pip insrall face_recognition will work.

#### 3. pip 
pip is the pyhton installation package. We recommend latest verison of pip installed in your system. a "pip install --update"
command in terminal will work to upgrade the pip in the system.

### Dependencies
#### 1. dlib
working of face_recognition depends on various dependencies , dlib is one of them. [This link](https://www.learnopencv.com/install-dlib-on-ubuntu/) is for installing dlib on ubuntu.

#### 2. opencv2
Another one is [installing opencv2](https://gist.github.com/arthurbeggs/06df46af94af7f261513934e56103b30)

#### 3. numpy
To install numpy the [instructions are here](https://askubuntu.com/questions/868599/how-to-install-scipy-and-numpy-on-ubuntu-16-04)

With this done you are ready to build your own system for recognising various people through the eyes of the computer. 
###### All the best!!!
