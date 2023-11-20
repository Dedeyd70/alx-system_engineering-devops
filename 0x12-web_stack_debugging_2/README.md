# Web stack debugging #2

This marked the third installment in a sequence of web stack debugging assignments. In each of these projects, I was presented with malfunctioning or buggy web stacks enclosed within isolated containers. My objective was to rectify the issues and restore the web stack to a functional state. For every task, I crafted a script to automate the execution of commands required for the repair of the web stack.

## Questions :page_with_curl:

* **0. Run software as another user**
  * [0-iamsomeonelese](./0-iamsomeonelese): Bash script that runs the command
  `whoami` under the user passed as argument.
  * Usage: `./0-iamsomeonelese <user>`

* **1. Run Nginx as Nginx**
  * [1-run_nginx_as_nginx](./1-run_nginx_as_nginx): Bash script that fixes a
  web server to run Nginx listening on port `8080` as the `nginx` user.

* **2. 7 lines or less**
  * [100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less): Bash script
  that fixes a web server to run Nginx listening on port `8080` as the `nginx`
  user.
  * 7 lines long.
