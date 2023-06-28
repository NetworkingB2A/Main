What is CICD for network automation?
The goal to to bring software development principles into the net devops mind frame.

What is continuous deployment vs continuous delivery?
- Delivery means to deploy all of your code changes to a testing and/or production environment after the build stage. You can schedule the config upgrade when ever.
- Deployment mean that there is no human intervention. when the pipeline is passed the config change is pushed out immediately. No more release day.

How is this done in practice?
network as code
network stored as source control
changes are proposed in code  "branches"
CICD builds test environment, tests code on test environment, then if successful the configuration change will be pushed out to end devices

Tools you will need to preform this ( this is just a list i have come up with, this does not mean you need to follow the tools i have called out)
- Ansible
- CML
- Github(Maybe, might try something else), gogs 
- Drone or Jenkins
- Vagrant is an option as well
  - My understanding is that this will start up a local copy of cisco IOS and you can test out your configuration and verify the change worked how you thought it would.

steps
- create a branch
- update network to code code
- stage and commit your 
- push your commits to the source control
- pushing your commit to the dev branch, Your pipeline push a message to jenkins
- Jenkins is a tool will run the CICD process
  - You can start up a test network
  - push out configuration changes to the test network
  - Verify your change worked
    - This one can be tedious and difficult to do
    - You may have a lot of different tests that you want to run
- Destroy your test network
- if all tests pass, your CICD tool will merge the changes to your production environment
- Depending on your choice of Continues deployment or delivery. this config change will get pushed out right away or on a schedule.
- Once the change is pushed out, you will have your change 


Some notes on pipelines
- Pipeline files are done in yaml
- Not 100% sure on the next part but this is what i saw in the video i watched
- Yaml file contains
  - notify
    - you may use slack, discord, teams, webex, ECT
  - integration
  - delivery
  - deployment
- CICD is not magic. you write out exactly what you want done and the CICD tool will do it
- 


Many steps will be involved for this to happen. (here are some of the steps, need to think about it a bit more before. the steps right now will not be in order)
- need a environment as a "coded network"
- need to have copies of your network 






You need to first create your perfect test environment.
AKA create a digital twin, then copy that XML data you receive and that will be a template that your workflow tool will use to build out the CML topology. (This will be a very tedious process at first but worth it in the end.)


## Github actions
Events
- This is the trigger to start a workflow
Jobs
- Jobs consite of steps and actions
Runners
- This is a container enviroment that will run our code 
- Default github will run this for you, but you have the option to host your own if you would like
Steps
- Steps are a list of actions that must be done
actions

for github the naming convention needs to be 
repo name/.github/workflows/filename.yml



when user updates sharepoint list, event is triggered. 
power automate creates a either an issue or a PR that will update a Json file (might not be json, but it could be) I will also want a check to be done to see if user updated file correctly
I need a PR to be created and I need someone to manually approve it inside of github. once approval and merge is complete. 
CD will take into action and will go to service now to update the fields for the device type.
testing will need to happen to to check see if device type is in snow, or dnac.