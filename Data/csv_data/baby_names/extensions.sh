

test='test.txt'
#$test | cut -d"." -f1
NEW="$(echo $test | cut -d'.' -f1)"
echo $test
echo $NEW


for f in national_data/*.txt
do
  NEW_f="$(echo $f | cut -d'.' -f1)"
  mv $f $NEW_f.csv
done
