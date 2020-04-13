Please make sure you add your ssh-keys to each of the servers. You can find multiple online 
tutorials ([example](http://www.linuxproblem.org/art_9.html)) to help you do this. Use `ssh-keygen` to generate keys and `ssh-copy-id` to copy the keys. Also, make sure that the VPN is tunnel_all so that ssh traffic is also tunneled.

`sanket1729@sanket1729:~/cs101_grader$ ./get_grades.sh AYA lab08 smk7`

`get_grades.sh <section> <lab_number> <ta_netid>`

This would combine all the grades, print them in sorted way by netids. 

-------------

**Alternate one-liner bash script to fetch all lab grades for all your sections**

`grading.sh` fetches all lab grades for all your sections and adds the raw scores to `.csv` grade file. I handle `AYI` and `AYJ` so I'll use that for examples.

1. Download your section's grades inside this repository as `{section}_grades.csv` (for example, `AYI_grades.csv`). This naming convention is used in `add_to_csv.py`.

2. Add your sections and the labs you wish to grade in `grading.sh` and `add_to_csv.py`. Add your `netid` to `grading.sh`

Snippet for `grading.sh`:

```
labsToGrade=("lab05" "lab06" "lab07" "lab08")
sections=("AYI" "AYJ")
ta="yournetid"
```
Note: arrays in bash are space separated. No commas here. 

Snippet for `add_to_csv.py`:
```
sections = ["AYI", "AYJ"]
labs = ["lab05", "lab06", "lab07", "lab08"]
```
Note: You should have pandas installed in your python environment.

3. That's it, now run `./grading.sh`:

```
chmod +x grading.sh
./grading.sh
```
This step will download grades for all labs for all sections and add raw scores in new columns like `lab05_lab` to your `{section}_grades.csv` grade file. Now you can use Excel formulae (divide by max, multiply by 2) to get the final score. Remember to only upload columns with final score to Compass. 

