# AutoGenerateExample
Use the CRDC data generator in a Github workflow

The interesting bit in this repo is in the .github/workflows directory.  The file *.github/workflows/data_generation.yml* is the GitHub workflow file and triggers the data generation when the repo is committed to the **main** branch.  

**Before you Start**
- The configuration files used by the Bento data generator are found in the *datagen_configs* directory (though that can be changed in the data generator config file).  These **must** be valid configuration files, this workflow doesn't generate them.

- Each repo needs to allow Github Actions to read and write.  Settings >
 Actions > General > Workflow Permissions > Read and write permissions

**Notes**
In this example, the submission sheets are deposited in the *example_loadsheets* directory

The workflow YAML file has ard-coded information because I'm not sure how to do variables in YAML. Here's a list of what you can change:

- *datagen_configs/datagen_config.yml* (bento-data-generator config file):  

  - Github Actions is doing the path management, which means the paths for each entry have to start with the name of the repo.  For example, this repo is called AutoGenerateExample so all of the paths in that file look like this: **./AutoGenerateExample/repodirectory/repofile**

  - All of the paths in this file should be changed to reflect where the files are actually stored.

- *.github/actions/data_generation.yml* (Github actions config):

  - Line 4:*branches*  - This list controls which branch the commit triggers the example file creation.  Currently set to **main**, but additional branches can be added.  Be sure to include the branch that is used to deploy to Data Hub.

  - Line 26: *repository* - Needs to be the data model repository

  - Line 27: *path* - Needs to be set to the data model repository name

  - Lines 32&33: *git config* - Needs to be changed to whoever is doing the commits
  - Line 36:  This is the directory that will contain the completed example loadsheets.  Change this if you use a different directory name.

  - Line 37: *working-directory* - Needs to be set to the repostiory name