:: Script for setting up virtual environment and running jupyter notebook

@echo off
echo 'Creating virtual environment...'
CALL python -m venv vir_env
echo 'Launching virtual environment...'
CALL vir_env\Scripts\activate
echo 'Installing the dependencies...'
@REM CALL pip install -U jupyter==1.0.0
@REM echo 'Installing the packages to run the notebook...'
CALL pip install -r requirements.txt
@REM echo 'Installing jupyter extensions...'
@REM CALL pip install jupyter_contrib_nbextensions==0.5.1
@REM CALL jupyter contrib nbextension install --sys-prefix
@REM echo 'Enabling jupyter extensions...'
@REM CALL jupyter nbextension enable toc2/main --sys-prefix
@REM CALL jupyter nbextension enable table_beautifier/main --sys-prefix
@REM CALL jupyter nbextension enable spellchecker/main --sys-prefix
@REM echo 'Confirming the list of jupyter extensions installed...'
@REM CALL jupyter nbextension list
echo 'SUCCESS! Your system is ready to use this notebook.'
@REM CALL jupyter notebook
