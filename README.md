# AutoGenerateExample
Use the CRDC data generator in a Github workflow

The interesting bit in this repo is in the .github/workflows directory.  The file *.github/workflows/data_generation.yml* is the GitHub workflow file and triggers the data generation when changes are committed to specific branches.  

**Before you Start**
- The configuration files used by the Bento data generator are found in the *datagen_configs* directory (though that can be changed in the data generator config file).  These **must** be valid configuration files, this workflow doesn't generate them.

- Each repo needs to allow Github Actions to read and write. This can be done in the Settings menu for the repository:  Settings > Actions > General > Workflow Permissions > Read and write permissions

**Variables**
There are a number of variables in the **env** section of the *data_generation.yml* file that can be adjusted to meet the specific needs of the project.  The single exception to this is the **uses: actions/checkout@main** in the Data model checkout step.  That must be changed if your are using a branch other than main as your production data model branch.  If that does not need to be changed, you should only edit the **env** section.

- **CONFIG_DIR**: This is the directory where all of the Bento Data Generator configuration files are stored.
- **CONFIG_FILE**: This is the name of the Bento Data Generator configuration file.
- **WORKING_DIR**:  GitHub actions has a working directory that is usually the name of the repo.  In this example, that's *AutoGenerateExample*.  Note that the owner part of a fully qualified repository name is not needed here.
- **DESTINATION_DIR**: This is the directory/folder in your model repository where the zip file will deposited.  In this example, that's *example_loadsheets*. 
- **REPOSITORY**: This is the full name of the data model repository.  In the example it's *pihltd/AutoGenerateExample*, but for CRDC use it would be something like *CBIIT/ctdc-model*
- **ZIP_FILE**: This is the name of the ZIP archive that will be created.  Do **NOT** include the .zip extention, that will be appended by the workflow.
- **USER_NAME**: This is a git requirement and is the committer's name.
- **USER_EMAIL**: This is also a git requirement and is the email of the committer.
- **COMMIT**: This is the commit statement that will show in GitHub.


## Support scripts
### MDF2DataGenExcel
The Bento Data Generation program supports getting values from CDEs rather than providing them in the Excel sheet.  If using an Excel sheet is preferred, this script will create one with the permissible values from the model filled into the approprate columns.
