An ansible plugin is code that is write so you can use it. To me (as of right now), I dont really understand the difference between a plugin and a module.

There are different kinds of plugins 
- action
- filter
  - This is a jinja 2 filter
- callback
  - the result from the task
  - use case
    - mail
    - slack
    - teams
    - loggers
    - timer is the terminal windows
- lookup
- strategy
- connection