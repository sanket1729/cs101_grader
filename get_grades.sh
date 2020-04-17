#!/bin/bash
ssh $3@cs101-dev-01.cs.illinois.edu "cd /class/cs101/grading; 
/opt/anaconda3/bin/python3 grade.py $1 $2" > $1_$2_dev1.out
ssh $3@cs101-dev-02.cs.illinois.edu "cd /class/cs101/grading; 
/opt/anaconda3/bin/python3 grade.py $1 $2" > $1_$2_dev2.out
ssh $3@cs101-dev-03.cs.illinois.edu "cd /class/cs101/grading; 
/opt/anaconda3/bin/python3 grade.py $1 $2" > $1_$2_dev3.out
ssh $3@linux.ews.illinois.edu "cd /class/cs101/grading; 
/class/cs101/software/python-3.8.1/bin/python3 grade.py $1 $2" > $1_$2_ews.out
python3 combine_grades.py $1 $2 $3 $4
