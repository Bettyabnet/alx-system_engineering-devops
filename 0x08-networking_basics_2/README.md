## : 0x08-networking_basics_2
0x08-networking_basics_1: Network Fundamentals
This project covers the basics of networking, focusing on understanding fundamental concepts like local hosts, IP addresses, and the hosts file.

Project Details:

Course: SE Foundations
Weight: 1
Project Dates: Nov 1, 2023 - Nov 3, 2023
Author: Sylvain Kalache
Learning Objectives:

By the end of this project, you should be able to explain, without using external resources, the following concepts:

What is localhost/127.0.0.1?
What is 0.0.0.0?
What is the /etc/hosts file?
How to display your machine's active network interfaces
Requirements:

Code Editors: vi, vim, or emacs
Operating System: Ubuntu 20.04 LTS
Line Endings: All files must end with a newline character
README.md: A README file is mandatory in the project's root directory
Bash Script Permissions: All Bash scripts must be executable
Shellcheck: Scripts must pass Shellcheck (version 0.7.0) without errors
Script Headers:
First line: #!/usr/bin/env bash
Second line: Comment explaining the script's purpose
Resources:

What is localhost?
What is 0.0.0.0?
What is the hosts file?
Netcat examples
man or help for commands: ifconfig, telnet, nc, cut
Copyright:

Copying and publishing content from this project is strictly prohibited. Plagiarism will result in removal from the program.

Tasks:

Change Your Home IP (mandatory):
Write a Bash script that modifies the hosts file to:
Map localhost to 127.0.0.2
Map facebook.com to 8.8.8.8
Remember to revert changes after completing the task.
Show Attached IPs (mandatory):
Write a Bash script that displays all active IPv4 addresses on the machine.
Port Listening on Localhost (advanced):
Write a Bash script that listens on port 98 on localhost and displays any received text.
Repository:

GitHub repository: alx-system_engineering-devops
Directory: 0x08-networking_basics_2
Please note: This document does not contain the actual code for the tasks. You are expected to complete the tasks yourself based on the provided information and resources.
