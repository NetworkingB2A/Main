### What is an SDK?
SDK is a software development kit that allows a user to grab pre-written APIs and communicate and an endpoint. Alternatively in the case of Python, you could create your own class that can call an API and program it the exact way you want it. or you can use an SDK and cut down on coding time and maintenance.  
A good SDK has these qualities
- Is easy to use
- Is well documented
- Has vault-added functionality
- Integrates will with other SDKs
- Has minimal impact on hardware resources
SDKs provide the following advantages
- Quicker integration
- Faster and more efficient development
- Brand control
- Increased security
- Metrics

### Cisco Meraki
Cisco Meraki cloud platform provides several APIs
- Captive Portal API
- Scanning API
- MV Sense Camera API
- Dashboard API
Cisco Meraki dashboard only allows 5 API calls per second per organization, in the first second there is a burst of additional 5 API calls that can be made.  
If you notice your API calls are giving back too much info your may want to take a pagination approach and limit your calls. some options for pagination in Meraki include:
- perPage: The number of entries to be returned.
- startingAfter: A value used to indicate that the returned data will start immediately after this value
- endingBefore: A value used to indicate that the returned data will end immediately before this value.  
If you have large configuration changes that need to happen you can use action batches in order to send multiple configurations request in a single transaction. this will avoid hitting the API limits.  


## Cisco Compute management platforms and API
Cisco UCS
- Cisco UCS manager
  - This is built for cisco ecosystem
  - Built for Cisco server nodes
- Cisco UCS Central
  - manage multiple Cisco UCS Domains from a central point
  - Uses UCS manager apis
- Cisco Intersight
  - cloud hosted management for cisco UCS and Cisco hyperFlex
  - Tight integration with Cisco TAC
Cisco UCS Director
- This is built as a multi-platform tool

### Cisco Collaboration Platforms
Cisco Unified communications manager
Cisco finesse
- Looks like a way to manage your virtual phone
- Any you can manage a group of phones or a team of people.
Cisco webex
Cisco Webex is a group of products that can work together to collaborate with a team or host meetings
- webex meetings
- Webex teams
- webex devices
- webex board
- any others 

### Cisco security Platforms
Cisco firepower
Cisco Amp and cisco threat grid
Cisco umbrella
Cisco ISE