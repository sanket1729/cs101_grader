Please make sure you add your ssh-keys to each of the servers. You can find multiple online 
tutorials to help you do this. Use `ssh-keygen` to generate keys and `ssh-copy-id` to copy the keys. Also, make sure that the VPN is tunnel_all so that ssh traffic is also tunneled.

`sanket1729@sanket1729:~/cs101_grader$ ./get_grades.sh AYA lab08 smk7`

`get_grades.sh <section> <lab_number> <ta_netid>`

This would combine all the grades, print them in sorted way by netids. 