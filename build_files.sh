echo "Build Start"
python3.10 -m pip install -r requirment.txt
python3.10 manage.py collecstatic --noinput --clear
echo "Build End"