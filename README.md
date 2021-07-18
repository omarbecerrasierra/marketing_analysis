# Marketing Analysis


In the file you can find 6 files:

- DataAnalysis.ipynb
- MLmodels.ipynb
- FastApi.py
- testApi.py
- arquitecture.pdf
- requirements.txt

You can view the video for an explanation of the execution in [Video](https://youtu.be/sTCPts6Xceo)

The first file is made data analysis and this file generate a file named *traindata.csv*
this file is the input of the *MLmodels.ipynb* in this file is provided an analysis of several models of machine learning, which we use to select the model with a high score.

The file *FasApi* has as input the *traindata.csv* deploy the API in the host: *0.0.0.0* in the port *8000* this API has a function predict, that is then used for requesting the API.

the file "testApi.py" have a request example for make to the API (is an easy form to make this, only execute the python file) in this case is use a customer that not accept the campaign
the output exected is:

**No acepta la campaña**

In the file architecture are a description to the architecture proposed for the case of use

the file requirements have the version of the packages of python use


## Systems characteristics use for the develoment
- OS: Ubuntu 20.04.2 LTS x86_64 
- Host: Presario CQ43 Notebook PC 
- Kernel: 5.8.0-59-generic 
- Shell: bash 5.0.17 
- CPU: Celeron T3500 (2) @ 2.094GHz 
- GPU: Intel Mobile 4 Series Chipset 
- Memory: 5847MB
- Python 3.8.10