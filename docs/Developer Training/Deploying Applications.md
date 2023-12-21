
## Cloud  

NIST defines cloud as three main category with additional subcategories. They are:
- Essential characteristics
  - Broad network access
  - Rapid elasticity
  - Measured service
  - On-demand self-service
  - Resource Pooling
- Service models
  - SaaS
  - PaaS
  - IaaS
- Deployment models
  - Public
  - Private
  - Hybrid
  - Community

Some benefits of containers include:
- Consistency for deployment automation
- Simplified lightweight image files measured in MB rather then GB
- Providing only what the app needs and nothing else
- Ability to work the same production as in a developer's laptop
- Ability to deploy applications in seconds

Notes about serverless:
- Of course there is still a server. but you dont need to work about the server at all.
- This is the idea that you write code, upload the code to a server and the server just runs the code.
- Works well if you just need a bit of code to run periodically.
- Can also be called function as a service.
- Advantages of serverless deployment
  - Cost
  - Scalability
  - Easier to use and write code for
- Disadvantages of serverless deployment
  - Latency to spin up the service when needed
  - Resource constraints
  - Monitoring and debugging
  - Security and privacy
  - Vendor lock-in

## DevOps
What is DevOps?
A compound of development (Dev) and Operations (Ops), DevOps is the union of people, process, and technology to continually provide value to customers.


DevOps guiding principles
- Culture
  - For DevOps to work, organizational culture must change. 
  - This is the most important and more difficult part of DevOps
- Automation
  - Everything that can be automated should be automated. 
- Lean
  - Reducing wasted efforts and streamlining the process.
- Measurement
  - If you never measure your results, you will never know what to improve or if you are improving.
- Sharing
  - Feedback and sharing is key to reach the ultimate goal.
- Holistic
  - The DevOps process needs to be treated as a whole process, rather than just a couple of smaller tasks.

### Putting devops into practice. The Three ways
First way: Systems and flow  
The following are key characteristics of the first way
- Make work visible
- Reduce batch sizes
- Reduce intervals of work
- Build in quality by preventing defects from being passed downstream 

Second way: Feedback loop
The following are key characteristics of the second way
- Amplify feedback to prevent problems from happening again
- Enable faster detection and recovery
- See problems as they occur and swarm them until they are fixed
- Maximize opportunities to learn and improve

Third way: Continuous Experimentation and Learning
The following are key characteristics of the third way
- Conduct dynamic, disciplined experimentation and risk taking
- Define time to fix issues and make the system better
- When things go wrong, don't point fingers
- Create shared code repositories

### DevOps Implementation
The stages for implementing DevOps generally follows these steps:
- Continuous integrations
  - This part involves merging dev code with production code and introduces automated testing.
- Continuous delivery
  - This stage involves a software package delivery mechanism for releasing code to staging for review and inspection.
- Continuous deployment
  - This stage relies on continuous integration and continuous delivery to automatically replace code into production as soon as it is ready.


### Components of a CI/CD Pipeline
CI/CD - Continuous integration and continuous deployment
CD/CD is the idea of developing, testing and deploying software in small batches. Your feature will be in a usable and being used will be much quicker when deploying in a CI/CD mindset.

What is continuous deployment vs continuous delivery?
- Delivery means to deploy all of your code changes to a testing and/or production environment after the build stage. You can schedule the config upgrade when ever.
- Deployment mean that there is no human intervention. when the pipeline is passed the config change is pushed out immediately. No more release day.

A CI/CD pipeline consists of:
- Source code repository
- Build stage ( source code, dependencies, and static code analytics)
- Test stage ( unit and integration tests, end-to-end tests)
- Deploy stage ( packaging, staging and production)

A Gitlab pipeline consists of:
- Commit: a change in the code
- Job: Runner instructions
- Pipeline: a group of jobs divided into different stages
- Runner: A server or agent that implements each hob separately, which can spin up or down if needed.
- Stages: Parts of a job(for exmaple, build or tests). Multiple jobs inside the same stage are executed in parallel.

