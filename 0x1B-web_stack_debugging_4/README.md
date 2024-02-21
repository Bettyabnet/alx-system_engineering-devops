## 0x1B. Web stack debugging #4
This Directory contains Puppet manifests for various tasks, including web stack debugging and user management.

# Requirements:
# General
* All files are interpreted on Ubuntu 14.04 LTS.
* All files must end with a new line.
* A README.md file at the root of the project is mandatory.
* Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
* Your Puppet manifests must run without error.
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
* Your Puppet manifests files must end with the extension .pp.
* Files will be checked with Puppet v3.4.
* Additional requirements for specific tasks are documented in the corresponding manifest files.

### Tasks:

# Sky is the limit, let's bring that limit higher (0-the_sky_is_the_limit_not.pp):
* Fixes a web server issue causing failed requests by optimizing the Nginx configuration.
* Repo: GitHub repository: alx-system_engineering-devops, Directory: 0x1B-web_stack_debugging_4, File: 0-the_sky_is_the_limit_not.pp
## User limit (1-user_limit.pp):
* Configures the OS to allow the holberton user to login and open files without encountering an "Too many open files" error message.
* Repo: GitHub repository: alx-system_engineering-devops, Directory: 0x1B-web_stack_debugging_4, File: 1-user_limit.pp
# Instructions:
* Ensure you meet the general requirements.
* Install puppet-lint if not already installed:
* $ apt-get install -y ruby
* $ gem install puppet-lint -v 2.1.1
* Run puppet lint on each manifest file to ensure they pass without errors.
* Run puppet apply on each manifest file to apply the changes.
* Verify the results of the changes according to the task description.
