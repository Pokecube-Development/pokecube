if exist "./docs" rd /s /q "./docs"
cmd /c make html
rename "./html" "./docs"
pause