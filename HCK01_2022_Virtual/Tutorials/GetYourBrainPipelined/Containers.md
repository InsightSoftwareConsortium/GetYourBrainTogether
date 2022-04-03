# GetYourBrainPipelined
Example scripts for setting up a brain processing pipeline


# Running on BIL
Make sure you have a Syslabs.io account and remote token setup as described in the previous tutorial
https://hackmd.io/@biomed-apps/B1B8mQCb5#Singularity


Starting in your home directory. The first task will be to use git to download the files for this tutorial and used them to create a very simple container. The 'interact' command will start a session in an interactive node on the cluster (use 'exit' to close the session).
```
interact
user=`whoami`
git clone https://github.com/InsightSoftwareConsortium/GetYourBrainStraight.git
base="GetYourBrainStraight/HCK01_2022_Virtual/Tutorials/GetYourBrainPipelined"
singularity build --remote example-easy.sif $base/Example-Easy/Singularity
singularity run example-easy.sif
```

You should now see something that looks like:
```
 ____________________
< Hello Example-Easy >
 --------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Use that singularity image to run a command in the container
```
singularity exec example-easy.sif cowsay "Exec Example-Easy"
```

Use the container to run a script and data that we included in the container
```
singularity exec example-easy.sif /opt/scripts/cow_script.sh /data/include/pkg_data.txt
```


Use the container to run a locally defined scripts that access local information
```
mkdir data
echo "Local Data" > data/data.txt
singularity exec -B /bil/users/$user/$base/Example-Easy:/opt/local -B /bil/users/$user/data:/data/input example-easy.sif /opt/local/dragon_script.sh /data/input/data.txt
```

Now build an container that does some example registration. This may take 10min or so.
```
singularity build --remote example-reg.sif $base/Example-Registration/Singularity
mkdir data_input
mkdir data_output
singularity exec -B /bil/users/$user/data_input:/data/input -B /bil/users/jtduda/data_output:/data/output example-reg.sif /opt/scripts/example.sh
```



## Running the examples
A 'Dockerfile' is provided to show how the image may be built. The build process takes a while so instead you may want to use a provided image that was created with the Dockerfile:

docker pull jtduda/python-itk-sitk-ants:0.1.0

Now you will need a directory for input data and for output data. For illustration we will call these /local/data/input and /local/data/output. We will refer to the location of this repo as /local/repo/GetYourBrainPipelined. The example may now be run via:

docker run -v /local/data/input:/data/input -v /local/data/output:/data/output -v /local/repo/GetYourBrainPipelined:/scripts jtduda/python-itk-sitk-ants:0.1.0 /scripts/example.sh

This will run the following python programs:
* save_inputs.py - prepopulate the input directory with some example data
* smoothITK.py - smooth an image using the itk python module
* smoothSimpleITK.py - smooth an image using the SimpleITK python module
* smoothANTs.py - smooth an image using the ants python module
* registrationANTs.py - simple registration using the ants python module
* registrationSimpleITK.py - simple registration using the SimpleITK python module

All outputs will be saved in the /local/data/output directory.

### Singularity
To run via singularity, first pull via:

singularity pull docker://jtduda/python-itk-sitk-ants:0.1.0

To run the example:

singularity exec -B /local/data/input:/data/input -B /local/data/output:/data/output -B /local/repo/GetYourBrainPipelined:/scripts python-itk-sitk-ants_0.1.0.sif /scripts/example.sh


