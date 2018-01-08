# changelog

---

__entry:__ 10-12-2017
__contributor:__ theycallmemac

---

  - README.md
      - created a README markdown file in the intial commit.
      - made some further ammendments to this.

  - LICENSE
      - added GNU General Public License v3.0 to the repo

  - book_lab.py, book_room.py, check_availability.py, booking.sh
      - uploaded previously existing files to new repo.

  - free_now.py, booking.sh
    - created free_now.py and added support for this in the shell script.

  - CHANGELOG.md
    - created a markdown file to document the changes to the code.

---

---

__entry:__ 11-12-2017
__contributor:__ theycallmemac

---

  - README.md
      - changed to include information on setup and how to run the script.

  - setup.py
    - added to install dcurooms script with it's dependencies.
    - changed license info in the script

  - scripts/dcurooms
    - dcurooms script added with the previous 'free_now.py' capabilities.

  - book_lab.py, book_room.py, check_availability.py, booking.sh, free_now.py, booking.sh
    - removed with a view to add their functionaltiies to dcurooms script.

---

---

__entry:__ 13-12-2017
__contributor:__ theycallmemac

---

 
  - scripts/dcurooms
    - now at v0.2.0 follwoing a number of minor changes.
    - changed the "-f"/"--free" option to "-n"/"--now". This is the purposes of clarity in the command name.
    - script now supports a "-f" or "--free" option which specificially displays rooms that are free as opposed to just the status of all rooms. This option checks the info returned from "-n"/"--now".
    - changed license info which was incorrect.
    - rewrote the get_current_time function to calculate the current week as opposed to it being hardcoded into the program.


  - README.md
    - added to long command information
    - gave usage example to check for free rooms rather than all rooms

---

---

__entry:__ 14-12-2017
__contributor:__ theycallmemac

---

  - .gitignore
    - created to ignore .pyc and .txt files
    - also ignores egg-info aswell as build and dist directories

  - scripts/dcurooms
    - created, just import dcurooms.py script

  - scripts/dcurooms.py
    - now at v0.2.1 following a number of fixes changes.
    - import specific tools rather than entire libraries.
    - functions return information ready for concatenation.
    - fixed error for wen the hour returned from get_current_time was greater or equal to 23.

  - ```__init__.py```
    - added one in each directory for the unittests
    - helps navigate around the project
  - tests/test_free_now.py
    - created unittest to check the return values of dcurooms
    - tests for exit code
    - tests if output is empty (indicating free) or a hardcoded string.

---

---

__entry:__ 16-12-2017
__contributor:__ theycallmemac

---

  - scripts/dcurooms.py
    - now at v0.3.0 due to some minor changes in what the tool can do and it's usage.
    - can now look up specific rooms on any given week and timeslot. 
    - can also lookup a whole builing when provided with this info too.
    - the "-f"/"--free" command now replaced with "-a"/"--available" command. This is due to a feature I plan for the next minor update.
    - bugs most definitely persist in this new addition. Fixes on the way soon.

  - README.md
    - added information on the new lookup commands.
    - changed info on previous commands listed.
  
  - setup.py
    - added url to setup script.

  - tests/test_available_now.py
    - tests the -anc options rather that the previous -fnc options.
    - renamed file and changed some names around the test.
    - fixed issue #2

---

---

__entry:__ 19-12-2017
__contributor:__ theycallmemac

---

  - scripts/dcurooms.py
    - now at v0.4.0 because of some rewrites and added functionality
    - lookup option now supports a lookup when available option, given as "-la"/"--lookup --available"
    - search_dictionary function added and repetitive lines of code removed.
    - now gives error message when room entered which either doesn't exist or is not yet supported by the tool, this fixes #4
    - now at v0.4.1 due to some fixes
    - found that issue #7 pertained to more than just what was detailed initially
    - tool no longer returns any IndexErrors instead returns a message as to what you entered wrong.
    - this fixes #7
    - 
  - README.md
    - added information on the new lookup when available command
  
  - tests/test_available_now.py
    - removed unnecessary lines
    - changed information and created txt file based on new option names from v0.3.0

---

---

__entry:__ 20-12-2017
__contributor:__ theycallmemac

---

  - scripts/dcurooms.py
    - now at v0.4.2
    - Refactored script from 214 lines to 149 lines, removing large blocks of repetitive code
    - this refactoring fixes issue #8

---

---

__entry:__ 21-12-2017
__contributor:__ theycallmemac

---

  - scripts/dcurooms.py
    - made dcurooms compatible with python3.x, thus closing issue #6
    - this was done by using MechanicalSoup instead of mechanize as the former supports python2 and python3
    - script also decides between http.cookiejar and cookielib bepending on which major version of python the script was installed with.

  - setup.py
    - included more info on the versions of python that the dcurooms script supports

---

---

__entry:__ 24-12-2017
__contributor:__ theycallmemac

---

  - scripts/dcurooms.py
    - closes #3, milestone 1.0.0 reached
    - supports the booking of rooms in the Henry Grattan Building and labs in the School of Computing.
    - requires your gmail username and password to send lab booking on behalf of your email.
    - supports both python2 and python3

---
---

__entry:__ 25-12-2017
__contributor:__ theycallmemac

---

  - scripts/dcurooms.py
    - fixed some errors persisting within the booking code, incorrect parameters etc

  - tests/test_available_now.py
    - made changes to test, giving exit status of 0 rather than 1.
    - now run from projects home dir rather from within the test dir
    - this is for the purposes of TravisCI
    
  - .travis.yml
    - added continuous integration in the from of TravisCI
    - sets python as the language, building for 3.4, 3.5 and 3.6 only
    - installs requirements using the txt file found in the home dir
    - runs tests
    - hope to build for 2.7 soon

  - requirements.txt
    dependencies used by dcurooms to be installed using TravisCI

---
---

__entry:__ 03-01-2018
__contributor:__ theycallmemac

---

  - tests/test_builder.py
    - created test_builder.py
    - tests the return value of the build_timetable function in dcurooms.py
    - also tests the validity of the url built

  - tests/test_lookup.py
    - created test_lookup.py
    - tests the output of an incorrect entry
    - also checks the output is nothing when the room is indeed free

  - .travis.yml
    - added new test_builder.py test to scripts section
    - added new test_lookup.py test too

---
---

__entry:__ 04-01-2018
__contributor:__ theycallmemac

---

  - setup.py, scripts/dcurooms.py, tests/test_lookup.py, tests/test_available_now.py, tests/test_builder.py
    - all scripts named here were formatted to conform with pep8
    - this was done using autopep8

---
---

__entry:__ 07-01-2018
__contributor:__ theycallmemac

---
  - setup.py
    - added extra scripts for running tool
  - .travis.tml
    - removed old test
  - index.py, builders.py, controls.py, checks.py
    - split functions among different files. 
    - Fixes almost all issues found using codeclimate
    - much cleaner (in ways), but can be better, I hope to added some more tests following on from this.
  - README.md
    - added codeclimate staus badge
---
