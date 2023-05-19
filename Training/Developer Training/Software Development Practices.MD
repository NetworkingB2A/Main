# Software development lifecycle
### What is SDLC (Software development lifecycle)?
SDLC is a generic process. The following is the overall stages
- Stage 1 - Planning
  - Can also be called requirement analysis. Identify the problem, get input from stakeholders.
- Stage 2 - Defining
  - What should your program do at the end?  
- Stage 3 - Designing  
  - You turn software specifications into a design specification. Users must have buy in at this stage
- Stage 4 - Building  
  - This is where you start to work on the code.
- Stage 5 - Testing  
  - Test code for bugs or defects.
- Stage 6 - Deployment  
  - This is where you put your software into production.

## Software Development methods
### Waterfall
Waterfall is the older way of designing code. This method follows the SDLC down to a T. The problem is that you do not deliver a product until it is completed. You may spend years writing the code before ever pushing the code into production. if you are halfway done writting the code, you still have delivered 0 product.  
Waterfall does not handle changes well at all. If need to make a change during the coding phase, that might mean you need to take a step backwards and move back into planning.  
Advantages:
- Design errors are highlighted before any code is written
- Good documentation is mandatory for this kind of methodology
Three major challenges for waterfall include
- The serial nature of waterfall
- Value is not achieved until the end
- Quality can often suffer. Re-engineering the applications can be very costly.

### Lean
According to the lean pioneers, an enterprise must focus on three major points to fully embrace the lean philosophy.
- Purpose
- Process
- People
Three main goals for the lean method
- Elimination of waste
  - if something doesn't add value to the final product. Get rid of it
- Just-in-time
  - Don't build something until the customer is ready to buy it.
- Continues improvement
  - Always improve your processes with lessons learned.

### Agile
One key factor of agile, is breaking your work into short sprint(2 weeks is typical). At the end of every sprint, you should have something to deliver to your program.  
You would first create the bare minimum viable product. This may not deliver every part of your whole product, but you just delivered a product to your users that can start to be used right away. At the end of the next sprint you will have another feature, and the next sprint you will have another feature. You will continue to deliver products over and over again, while finding bugs along the way. You may also find out that one of the original goals will need to be scraped. This is no longer a big deal because you may have not spent time writing this code and you just ended up saving yourself a bunch of time.

The Agile Manifesto
- Customer satisfaction is provided through early and continuous delivery of valuable software.
- Changing requirements, even in late development, are welcome.
- Working software is delivered frequently (in weeks rather than months).
- The process depends on close, daily cooperation between business stakeholders and developers.
- Projects are built around motivated individuals, who should be trusted.
- Face-to-face conversation is the best form of communication (co-location).
- Working software is the principal measure of progress.
- Sustainable development requires being able to maintain a constant pace.
- Continuous attention is paid to technical excellence and good design.
- Simplicity—the art of maximizing the amount of work not done—is essential.
- The best architectures, requirements, and designs emerge from self-organizing teams.
- A team regularly reflects on how to become more effective and adjusts accordingly.

## Software testing

There are different types of testing
- Unit testing
  - This is to test out very small bits of your code.
- Integration tests
  - This is to find how your application can work with other applications. 
- Function test or system testing
  - This test will do full end to end testing. Testing everything. This will be the longest phase of your testing.
- Acceptance testing
  - Test if the system is read for delivery.


### Test-Driven Development(TDD)
Developing test before writing code seems backwards but it is a standard when writing code.  
If you write test first you can avoid some unnecessary bug chasing.  
The five steps of TTD
1. Write tests
2. Test fails
3. Write code
4. Test passes
5. Refactor

Robust tests are very important, as they will help you discover the edge cases.
Refactoring your code is important, here are some reasons why
- Better code structure
- Better code readability
- Better design

### Unit testing
Unit testing is the idea of testing out very small parts of your code. The idea is that if you test out every small part of code and that failure happens, you can quickly take a look. Where if you test out all the code at one time, you may need to test to run for 10-20 minutes before the failure happens. running that over and over again could take hours.

Good unit tests should have the following characteristics
- Reliable
- Isolated
- Fast
- Readable

Tested units usually have dependencies to other parts of the system, in order to isolate your unit tests you may need to create a test double. Test doubles is a object that mimics some aspects or functionality of some other object. Types of test doubles include:
- Fake
- Stub
- Mock
- Dummy
- Spy


When creating unit test its a good idea to create your test using the OOB principles.  
Another good idea is to name your test at "test_testmodulename".  
You will need to import unittest and when creating your class you will need to inherit unittest.Testcase from the unittest module.  
If you want to run your test make sure to add the following to your code.
- <code> if \_\_name\_\_ =='\_\_main\_\_':  
&nbsp;&nbsp;&nbsp;&nbsp;unittest.main() </code>

** NOTE go to the following site to learn more info about unit test.  
https://docs.python.org/3/library/unittest.html


Some tools for TDD and unit testing
- pyats
- unittest
### Integration testing
This is the idea of testing units of code with their necessary integrations. A couple different approaches include
- Big bang approach
- Incremental approach
  - Three different directions
    - Top-down approach
    - bottom-up approach
    - sandwich approach

Two different test double types for integration testing
- Driver
- Stub

### System testing
The idea of system testing is to test the application end to end. There are many types of testing for system testing, some of those tests include
- Functionality testing
- Installation testing
- Usability testing
- Security testing
- Performance testing
- Load testing
- Stress testing
- Regression testing
- Storage testing
- Configuration testing: A given system could be running in the cloud, on local computer, remote servers, ect. This testing it to test the different types of configuration.
- Compatibility testing
- Reliability testing: check new versions of code work with old versions.
- Recovery testing
- Procedure testing

### Acceptance testing
This portion of testing is working the the actual end users. Different level of testing here includes
- Alpha testing
- Beta testing
- Contract testing
- Regulation testing
- Operational testing
  

## Code review 
Code review is a way to have other developers look at your code for verification. Some facets for what other developers will be looking for include 
- identify bugs
  - This is the most important part of the code review
- Improve code quality
- make sure standards are being followed
- allows others to be familiar with other parts of the project

Often multiple people are assigned to perform a code review. It is best to verify smaller bits of code, in order to keep it more manageable.

# Design Patterns
## Understanding Design patterns

You write this to show exactly what you are trying to accomplish. A design pattern is a map. This is not code. a set of rules on how you can write code.

take a look at the following book:
Design patterns: element of reusable object-oriented software
ISBN-13: 978:021633610

## Unified Modeling Language
Unified modeling language (UML) was created because programming languages are usually not at a high level of abstraction. UML helps software designers look at a UML glass diagram and understand better how the application is suppose to function.
![UML Diagram](../../images/UML%20diagram.png)


## Architecture patterns
Some of the commonly known software architecture patterns:
- Layered or multitier architecture pattern
  - This is broken up almost like an org chart.
  - There is no rule as to how many layers you can help, but often you will find 4 layers
    - Presentation layer
      - User interface communication
    - Business layer
      - Business rules processing
    - Persistence layer
      - Data persistence handling
    - Database layer
      - Database storage technology
  - You should not skip or jump layers, if a request starts at the presentation layer it must go through business and persistence to get to the database layer.
  - if for some reason you did need a special layer that is optional to use or not, you would create an <i> open-type layer</i>
  - each layer should be designed independently 
- Event-driven architecture pattern
- Microservices architecture pattern
- Model-View-Controller (MVC) architecture pattern
- Space-based architecture

## Software Design Patterns
There are many software design patterns, and you should pick out the correct one for your application. There are three groups in which patterns are divided into. 
- Creational
  - concerned with the class or object creation mechanism
- Structural
  - deals with class or object compositions for maintaining flexibility in larger projects
- Behavioral
  - describes the ways of interaction between classes and objects.

| Creational patterns | Structural patterns | Behavioral Patterns |
|-|-|-|
| Singleton | Adapter | Observer |
| Abstract Factory | Decorator | Interpreter |
| Prototype | Facade | Mediator | 
| Factory Method | Proxy | State|


### Singleton Design pattern
![Singleton Design pattern](../../images/Singleton%20Design.png)

- A pattern that restricts classes to only being instantiated once during the execution of a program.
  - Examples include - Data base connections, configuration values, static values, ect
- A class with a private instance variable representing it's only instance, a public get instance() method to retrieve that object, a constructor to enforce a single-instantiation.
- Extra steps are needed to make a singleton design work. other languages like java and c# will work automatically.
- Example code view Sample code/singleton.py

### Observer Pattern
![Observer Design pattern](../../images/Observer%20Pattern.png)
A pattern where dependent objects are updated or modified by one or more subject objects
- Allows objects to react or respond in response to events.
- Popular in UI systems
- The observer pattern is often used to handle communication between the model and the view in the MVC pattern.

Two classes defined by observer pattern:
- Subject - Which maintains a list of observers and includes methods for attaching, detaching, and notifying observers.
- Observer - Which has a method to receive updates from subjects.
- Example code view Sample code/observer.py

### Model, View, Controller (MVC)
A high-level abstraction where responsibilities are divided up into three loosely coupled components. This design type is often used in web development.
- Model: The component that retrieves and manipulates the data. Often tied to a database.
- View: The component that displays data. It's what the end users see on their devices. 
- Controller: The component that handles logic flow, user interaction, and directs models and views.

Benefits of the MVC pattern:
- Separation of concern
- Multiple views to the same model
- Flexible presentations changes
- Independent testing of components
- Pluggable components

Downsides of the MVC pattern:
- Increased complexity
- Excessive number of change notifications
- View and controller tight coupling
- Separate controller is sometimes not needed

Good to know
- There is typically one controller for each view. 
- One of the primary features of MVC architecture is the separation between the view and the model. This is very important design principle.
- The relationship between the view and a controller is an example of the strategy design pattern.

# Conducting code reviews
Some benefits for a code review
- It helps you create higher-quality software.
- It enables your team to be more cohesive and deliver software projects on time.
- It can help you find defects and inefficient code.

Some good practices for code review
- Use a code review checklist. Make sure you are following your organization standards.
- Review the code not the person.
- Check your ego at the door. Remember people are not reviewing you they are just looking at your code.
- make sure your complete the recommendation and your check those back into the repo.


# Other Notes
Cohesion and loosely coupled 
Here are some design guidelines to consider:
- Acyclic dependencies principle
- Stable dependencies principle
- Single responsibility principle

The concepts that define what OOP enables:
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

A decision on software architecture can be made while studying these characteristics of a system:
- Performance
- Availability
- Modifiability
- Testability
- Usability
- Security