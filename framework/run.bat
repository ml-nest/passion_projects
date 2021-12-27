:: Running virtual environment and running jupyter notebook

@echo off
@REM CALL python -m venv vir_env
CALL vir_env\Scripts\activate
@REM CALL jupyter contrib nbextension install --sys-prefix
@REM echo 'Enabling jupyter extensions...'
@REM CALL jupyter nbextension enable toc2/main --sys-prefix
@REM CALL jupyter nbextension enable table_beautifier/main --sys-prefix
@REM CALL jupyter nbextension enable spellchecker/main --sys-prefix
@REM echo 'Confirming the list of jupyter extensions installed...'
@REM CALL jupyter nbextension list
@REM echo 'SUCCESS! Your system is ready to use this notebook.'
@REM CALL jupyter notebook