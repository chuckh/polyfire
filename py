clear
echo Build and Load Polyfire with Python SimpleHTTPServer
echo
echo Starting Build Process
grunt build
echo
# printf "Rename Dist Index to index-v.html and copy app index.html in its' place (y/n)?"
# read INDEXCOPY
# if [ $INDEXCOPY == "y" ] ; then
#   echo Renamed and copying
#   mv dist/index.html dist/index-v.html
#   cp app/index.html dist/index.html
# fi
echo
echo Loading Python SimpleHTTPServer
cd dist
python -m SimpleHTTPServer 9000
cd ..
