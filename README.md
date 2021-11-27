# ivp_ws21_histo_eq

Group repository for course "Image, Video and Perception" in Winter Semester 2021/22. Topic: "Histogram Equalization"

## Getting Started

**Installation**

- You need a working install of Python >= 3.8. Check your version in the
  terminal with `python --version` (or with `python3 --version` for most Linux
  systems)
- Install [Poetry](https://python-poetry.org/docs/#installation)
- Check Poetry is working by running `poetry --version` in the terminal - you
  should see your Poetry version. If there is an error, was the installation
  successful? Did you restart your machine afterwards?

**Getting the Repo Set Up**

- If you haven't done so already, clone the repo
  - HTTPS: `git clone https://gitlab.tu-ilmenau.de/jofr4759/ivp_ws21_histo_eq.git`
  - SSH: `git clone git@gitlab.tu-ilmenau.de:jofr4759/ivp_ws21_histo_eq.git`
- Navigate into the repo folder with `cd ivp_ws21_histo_eq`
- Run `poetry install` to set up your libraries
- To run code you must use [Poetry](https://python-poetry.org/docs/basic-usage/#using-poetry-run), not your normal Python environment. For this, either prefix your commands with `poetry run`:  
  ```
  poetry run python test.py
  ```
  or run your code in a new poetry shell:  
  ```
  poetry shell
  python test.py
  ```
  Feel free to test your environment with "test.py" - it acts as a Hello World
  so you can check everything is working. 

- Download the [image database](https://cloud.tu-ilmenau.de/s/9ffWqt7G9oLziAk),
  extract the zip archive and put the image files into the folder
  `image_database`. The images will not be committed. 

**Starting to Code**

- Before you start developing, make sure you are on the newest commit on the
  main branch:  
  ```
  git checkout main
  git pull
  ```
- Check that your dependencies are also up to date: `poetry install`
- Create a new branch for your work: `git checkout -b <your-branch-name>`.
  Replace \<your-branch-name\> with something descriptive like "bbhe".
- Create your code. The folders for each algorithm contain a template `process`
  function that you should fill with working code. How you do that in each
  folder is completely up to you. 
- If you need a new library, use [poetry
  add](https://python-poetry.org/docs/cli/#add) like: `poetry add
  image-enhancement`
- Helper functions for testing your code are provided in `utils.py`. 
    - Load images from the database as grayscale like `img =
      utils.load("1002.png")`
    - For reference, you might want to convert all images to grayscale. For
      this, use `utils.apply_to_all` with the `no_processing` module:  
    ```py
    import utils, no_processing
    utils.apply_to_all(no_processing)
    ```  
    This will take a few minutes. You can find the output in
    `processed/no_processing`.
    - To apply your process function to a single image and save the result in
      the `processed` folder, use  
    ```py  
    import utils, bbhe  
    utils.apply(bbhe, "1002.png")  
    ```  
    This is what you should use most of the time to test your processing code. 
- When you've reached a small goal with your code (e.g. you've added the right
  library or improved the comments in your code), [commit your
  changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_committing_changes).
  
- Once you're done working for the day, push your changes to GitLab: `git push`
- Once you've reached your main goal (e.g. implementing a process function for
  bbhe), make sure you've pushed your branch and then [open a merge request on
  our GitLab](https://gitlab.tu-ilmenau.de/jofr4759/ivp_ws21_histo_eq/-/merge_requests/new).  
  Select your branch (e.g. `bbhe`) as source branch and main as the target
  branch. Click on "compare branches and continue", then give the Merge Request
  a descriptive title (e.g. "Add BBHE Algorithm") and briefly describe how
  you've implemented it and what does/doesn't work in the text. Under Reviewers,
  select all other group members as Reviewers.  
  The other group members will get a mail and can [review your
  code](https://docs.gitlab.com/ee/user/project/merge_requests/reviews/). Leave
  comments when you think something can be improved! The last person to approve
  the Merge Request can hit "merge" at the bottom of the request and it will be
  merged to main.  
  The advantage of this Merge Request based workflow is that everyone looks at
  all the code before it becomes "official", which means we're more likely to
  catch errors. Also, there are no problems with multiple people committing to
  main at the same time. 