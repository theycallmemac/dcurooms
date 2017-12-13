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

