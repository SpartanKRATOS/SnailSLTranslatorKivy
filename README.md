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

##For the Action Detection Tutorial.ipynb
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

