:: Script for setting up virtual environment and running jupyter notebook

@echo off
echo 'Creating virtual environment...'
CALL python -m venv personal_nb
echo 'Launching virtual environment...'
CALL personal_nb\Scripts\activate
echo 'Installing the dependencies...'
CALL pip install -U jupyter==1.0.0
echo 'Installing the packages to run the notebook...'
CALL pip install -r requirements.txt
echo 'Installing jupyter extensions...'
CALL pip install jupyter_contrib_nbextensions==0.5.1
CALL jupyter contrib nbextension install --sys-prefix
echo 'Enabling jupyter extensions...'
CALL jupyter nbextension enable toc2/main --sys-prefix
CALL jupyter nbextension enable table_beautifier/main --sys-prefix
CALL jupyter nbextension enable spellchecker/main --sys-prefix
echo 'Confirming the list of jupyter extensions installed...'
CALL jupyter nbextension list
echo 'SUCCESS! Your system is ready to use this notebook.'
CALL jupyter notebook
