echo "Build Start"
python3 -m pip install -r requirment.txt
python3 manage.py collecstatic --noinput --clear
echo "Build End"