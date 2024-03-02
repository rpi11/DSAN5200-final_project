# DSAN5200-final_projects

Given that some of the Quarto website file structure might be a little confusing, here are some directions on where editable files live, as well as how to actually deploy the site on your own domains site.

## Files of interest

All relevant files live within the Quarto website directory titled FinalProject/

* data/data.csv - the csv file containing the data
* eda/explore.ipynb - contains Jupyter notebook code to conduct basic exploratory analysis

## How to deploy site

#### TLDR

1. Perform edits
2. Run "quarto render" from within FinalProject/
3. Push edits to DSAN5200-final_project repository
4. Use following command to update with relevant files: ```rm -r public_html/DSAN5200_FinalProject/; mkdir public_html/DSAN5200_FinalProject/; cd DSAN5200-final_project/; git pull; cd ..; cp -r DSAN5200-final_project/FinalProject/_site/* public_html/DSAN5200_FinalProject```
5. Open [your domain].georgetown.domains/DSAN5200_FinalProject/ and press Cmd+Shift+R

#### Performing and pushing edits

Once you are done editing any of the files above, ```cd``` into the FinalProject/ directory and run the command ```quarto render```. This will add files to the _site/ directory, which is where the deployable code lives. After this, you can push the edits to the DSAN5200-final_project repository.

#### Pulling code onto the domains

This is formatted such that you will be able to enter ```[your domain].georgetown.domains/DSAN5200_FinalProject/``` and pull up the website.

First, clone the repository into the highest level of your domain — mine looks like ```[pihlstro@gtown3 ~]$ git clone ...```

Having cloned the repository, still at the highest level of your domains structure run the following command: ```rm -r public_html/DSAN5200_FinalProject/; mkdir public_html/DSAN5200_FinalProject/; cd DSAN5200-final_project/; git pull; cd ..; cp -r DSAN5200-final_project/FinalProject/_site/* public_html/DSAN5200_FinalProject```

The above command will remove and recreate the ```DSAN5200_FinalProject``` directory in the public site, update the version of the repository on your domain, and then copy the site contents to the deployable platform.

One you run this command, you should be able to go to the url specified above to access the final project. If you don't see edits reflected, try Cmd+Shift+R to do a hard refresh.

