# SnailSLTranslatorKivy
Install python 3.9 and pip on your machine

## Steps
<br />
<b>Step 1.</b> Clone this repository: https://github.com/SpartanKRATOS/SnailSLTranslatorKivy
<br/><br/>
<b>Step 2.</b> Create a new virtual environment 
<pre>
python -m venv action
</pre> 
<br/>
<b>Step 3.</b> Activate your virtual environment
<pre>
source action/bin/activate # Linux
.\action\Scripts\activate # Windows 
</pre>
<br/>
<b>Step 4.</b> Install dependencies and add virtual environment to the Python Kernel
<pre>
python -m pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=action
pip install tensorflow tensorflow-gpu opencv-python mediapipe sklearn matplotlib
</pre>
<br/>
<b>Step 5.</b> Install kivy framework
<pre>
pip install kivy[full] kivy_examples
</pre>
<br/>
<b>Step 6.</b> Run the project with 
<pre>
python action.py
</pre>
<br/>

## For the Action Detection Tutorial.ipynb (inspired by https://github.com/nicknochnack/ActionDetectionforSignLanguage repo) 
<br />
<b>Step 1.</b> do the steps above
<br/><br/>
<br />
<b>Step 2.</b> install and run jupyter notebook
<pre>
pip install notebook
jupyter notebook command or python-m jupyter notebook
</pre>
<br/>
<br/><br/>

## actionDetection.py script is the detection script cleaned up
<b>execute it wit.</b> python actionDetection.py

## For the Raspberry Pi 4 
<br />
<b>Step 1.</b> you'll need python 3.8, upgrade you Raspberry Pi config
<br/><br/>
<br />
<b>Step 2.</b> install dependencies with python 3.8 and pip3
<pre>
install tensorflow2.1 on your RPI4 using this video https://www.youtube.com/watch?v=GNRg2P8Vqqs
sudo pip3 install mediapipe-rpi4
sudo apt-get install libhdf5-dev -y 
sudo apt-get install libhdf5-serial-dev –y 
sudo apt-get install libatlas-base-dev –y 
sudo apt-get install libjasper-dev -y 
sudo apt-get install libqtgui4 –y
sudo apt-get install libqt4-test –y
pip3 install opencv-contrib-python==4.1.0.25
sudo apt-get install python3-numpy
sudo apt-get install libblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install python3-dev 
sudo apt-get install libatlas-base-dev
sudo apt-get install gfortran
sudo apt-get install python3-setuptools
sudo apt-get install python3-scipy
sudo apt-get update
sudo apt-get install python3-h5py
pip3 install --upgrade scipy
pip3 install --upgrade cython
pip3 install keras 
</pre>
<br/>
<br/><br/>
