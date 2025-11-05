cd /d "%~dp0"
D:
cd D:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\
gmad create -folder "%~dp0\" -out "%~dp0\myaddon.gma"
gmpublish create -addon "%~dp0\myaddon.gma" -icon "%~dp0\"

pause
cd /d "%~dp0"
del myaddon.gma