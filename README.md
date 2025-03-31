# hs-list-delete
 Python script that takes a list of ILS IDs and deletes them and writes output to a log file.
 
 Uses bearer token authorisation.
 Add your bearer token to the file by replacing 'XXX'.
 
 Requires requests [pip install requests]
 
 ILS (nor record ID) should be stored as a single list in list.txt
 Output is written to log.txt
 
 To follow the script progress use:
 tail -n 20 -f log.txt

Run the script by calling list-clean.py
