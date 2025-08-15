# AutoGenerateExample
Use the CRDC data generator in a Github workflow

The interesting bit in this repo is in the .gihub/workflows directory.  The file *data_generation.yml* is the GitHub workflow file and triggers the data generation.  

**Before you Start**
The configuration files used by the Bento data generator are found in the *configs* directory (though that can be changed in the data generator config file).  These **must** be valid configuration files, this workflow doesn't generate them.

In this example, the submission sheets are in the *loadsheets* directory

Hard-coded information because I'm not sure how to do variables in YAML.
- *datagen_config.yml* (bento-data-generator config file):  
-- The paths for each entry have to start with the name of the repo.  For example, this repo is called AutoGenerateExample so all of the paths in that file look like this:
**./AutoGenerateExample/repodirectory/repofile**
-- All of the paths in this file should be changed to reflect where the files are actually stored.
- *data_generation.yml*(Github actions config):
-- Line 4:*branches*  - Currently set to **main**, needs to be set to whatever branch is used to deploy to Data Hub
-- Line 26: *repository* - Needs to be the data model repository
-- Line 27: *path* - Needs to be set to the data model repository name
-- Lines 32&33: *git config* - Needs to be changed to whoever is doing the commits
-- Line 37: *working-directory* - Needs to be set to the repostiory name

**Notes:**
- Each repo needs to allow Github Actions to read and write.  Settings >
 Actions > General > Workflow Permissions > Read and write permissions