# first solution
cat event_history.csv | grep serdar | grep -i Terminateinstance | grep -Eo "i-[a-zA-Z0-9]{17}" | sort | uniq -c > /tmp/result.txt

#second solution

cat event_history.csv | grep serdar | grep -i Terminateinstance | grep -Eo "i-.{17}" | sort | uniq -c > /tmp/result.txt