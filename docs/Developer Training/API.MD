# Application Programming Interfaces (API)

- Northbound APIs
  - Often a network controller to its management software.
  - Best practices suggest that the traffic should be encrypted using TLS between software and the controller.
- Southbound APIs
  - This would be pushing the configuration to the device from the controller. 

As network engineers we have been using this model of north and southbound aps for years and years. Think of wireless access points and the wireless controller.

## Synchronous vs Asynchronous APIs
Synchronous APIs means that your application is waiting for a response from the API in order to continue the process. You send a command, wait for a response, then send the next command. This works very much like TCP. Synchronous also means slower response times. You man need this type of API communication if you need data from another API before your program can continue. good example would be creating tokens.  
Asynchronous is just the opposite. You send a command, then you send another and another. You never need to wait to find out if the first command was successful. 

# Representational State Transfer (REST) APIs
- REST APIs are often referred to as RESTful API
- RESTful APIs use HTTP methods to gather and manipulate data.



| CRUD Function | Action |
|-|-|
| CREATE | Inserts data inside a database or an application |
| READ | Retrieves data from a database or an application |
| UPDATE | Modifies replaces data in a database or an application |
| Delete | Removes data from a database or an application | 

## RESTful API Fundamentals
### API Types
- Service API
  - An application can call on another application to solve a particular problem.
  - These different applications can work with out interaction from the other app, but this will extend the service for the two apps.
- Information API
  - An application can call on another application to provide information.
- Hardware API
  - An application can call the hardwares API to access the hardware level.

### API Access Types
- Private
  - For internal use only. Used inside a company only.
- Partner
  - APIs that are shared to specific business partners.
- Public
  - API that can be accessed by all.

## RESTful API Authentication

- Basic
  - One of the simplest and most common authentication methods used in APIs.
  - *IMPORTANT NOTE* Basic Auth is sent not encrypted in your program or to the southbound device. You often will use SSL or TLS to encrypt your HTTP call to prevent man in the middle attacks.
  -  Another issue is that the encoded string is sent back and forth in your APIs calls.
- API Keys
  - An API key is a predetermined string that is passed from the client to the server. It is intended to be a pre-shared secret and should not be well known or easy to guess.
  - API keys can be passed to the server in three different ways:
    - String
    - Request header
    - Cookie
  - The string is passed with every call you make.
  - If you are making multiple calls you would want to look into using a cookie or request header.
- Custom Tokens
  - Tokens are a way of authenticating using the REST API. You authenticate once and you receive your token, you use the token to authenticate. 

# HTTP
## HTTP Basics
In order for a HTTP request to be successful, the client need to include four items
- URL (uniform resource locator) 
  - The URL is the location where the service resides on the internet/intranet
  - A URL typically has four components
    - Protocol
      - HTTP
    - Server/Host address
      - first part of the URL the DNS name or ip address
    - Resource
      - Location on the server where the data is stored
    - Parameters
      - a filter or to clarify request
- Method
  - Different kinds of request methods includes  

| Method | Details | CRUD |
|-|-|-| 
| GET | Retrieve data from the server | Read |
| HEAD | Request for header information from a get request |
| POST | Post data or add new data server | Create |
| PUT | Request to ask server to store or update data | Update |
| PATCH | Request server to partially store or update data | Update |
| DELETE | Request server to delete information | Delete |
| TRACE | Request to ask server to return a diagnostic trace |
| OPTIONS | Ask the server for a list of request methods |
| CONNECT | Ask a proxy to make a request to another server |
 
- List of headers
  - The headers contain the meta data about tn HTTP request. 
    - The host name, connection type, The type of data you want to receive, the language, ect
- Body


### HTTP functions calls
| HTTP Function | Action |
|-|-|
| GET | Request data from a destination |
| POST | Submits data to a specific destination |
| PUT | Replaces data at a specific destination |
| Patch | Appends data to a specific destination |
| Delete | Removes data from a specific destination |

### Response codes
The types of response codes you will see
- 1xx (informational) - The request has been successfully received. The server is continuing the process
- 2xx (success) - The request was successful and is completed.
- 3xx (redirection) - Further action must be taken to complete this request.
- 4xx (client error) - The request cannot be understood or is unauthorized.
- 5xx (server error) - The server failed to fulfill a request.

Common response codes
| Status Code | Meaning |
|-|-|
| 100 | Continue |
| 200 | Okay | 
| 301 | Move permanently |
| 302 | Found and redirect |
| 304 | Not modified | 
| 400 | Bad request |
| 401 | Authentication required |
| 403 | Forbidden | 
| 404 | Not found | 
| 405 | Method not allowed |
| 408 | Request timed out | 
| 414 | request URI too large |
| 429 | Too many requests HTTP response headers | 
| 500 | Internal server error |
| 501 | Method not implemented |
| 502 | Bad gateway | 
| 503 | Service unavailable |
| 504 | Gateway timeout | 

### HTTP Headers
There are four distinct types of headers
- General Headers
  - Headers from this category are not specific to any particular kind of message.
  - They are primarily used to communicate information about the message itself and how to process it.
- Request Headers
  - These headers carry information about the resource to be fetched.
  - They also contain the information about the client.
  - Examples
    - Accept-Charset
    - Accept-Datetime
    - Accept-Encoding
    - Accept-Language
- Response Headers
  - These headers hold additional information about the response and the server providing it.
- Entity Headers
  - These headers contain information about the response body.

### HTTPS authentication types   
- Anonymous (no authentication)
- Basic (Base64-encoded)
- Bearer (HTTP implementation of custom token authentication)
- Digest (MD5-hashed credentials)
- Mutual (two-way authentication)
- Other uncommon schemes


### Webhooks
Webhooks are user-defined HTTP callbacks. Also called reverse APIs. When you want an event to happen based on a trigger that occurs.  
ngrok is a free tool that you can use to test out your webhooks.


### REST Constraints
REST defines six architectural constraints that make any web service a truly RESTful API. These are the REST constraints:
- Client/server
  - A client must know the URIs on the server
  - The interaction is where the client initiates requests to the server and the server sends back responses.
- Stateless
  - REST services must be stateless.
  - Each individual request contains all the information that the server needs to preform the request
  - The URI identifies the resource, and the body contains the stat of the resource.
  - A stateless service is easy to scale horizontally, allowing for additional service to be added or removed as necessary.
- Cache
  - Response data must be implicitly or explicitly labeled as cacheable or non-cachable. 
  - Cashing helps to improve the performance of the client side, and helps with scalability of the server.
- Uniform interface
  - Identification of resources
    - These identifiers are stable and do not change across interactions.
  - Manipulation of resources through representations
  - Self-descriptive messages
  - Hypermedia as the engine of application state
- layered system
  - This is the idea that there can be more systems involved than just the client and server.
  - some examples include proxies, load balancers, and so on.
- code on demand
  - This is optional.
  - Sometimes the response can hand back a bit a code that the client can execute.


### REST API Versioning 
There are a few different ways to approach API versioning. Versioning is important because if allows the devs to make changes and update APIs without impacting a customers workflow.  
Different techniques include
- URI path versioning
- Query parameter versioning
- Custom headers
- Content negotiation
  - This way allows you to version a single resource rather then the whole API.


### Pagination
What is pagination?
- instead of all one api call to return all the data in one page, you need to break up that data for a better user experience. 
- There are two popular approaches to pagination
  - offset-based pagination
    - when you set a offset number you are saying which device number you wan to start at.
    - when you set a limit level you say the number of devices you want to receive back.
    - example
      - you have a list of 200 devices. you set an offset of 75 and a limit of 25
      - with out the offset and limit, you would get all 200 devices back. with the offset and limit you would get devices 75 - 100 back
  - keyset-based pagination

### Rate limiting and monetization
Why do you need rate limiting?
-  This need to happen to help with security, business impact and efficiency of the application.
   -  Security
   -  Business impact
   -  Efficiency
Some tips for rate limiting on the client side.
- Avoid constant polling by using webhook to trigger updates.
- Cache your own data when you need to store specialized values or rapidly review very large data sets.
- Query with special filters to avoid re-polling unmodified data.
- Download data during off-peak hours.

API calls can be throttled with:
- HTTP headers: headers like X-RateLimit-Limit and X-RateLimit-Remaining are used to keep track of the numbers of used and remaining API calls for a period of time.
- Message queues: Incoming API calls can be put into a queue, which makes sure the API endpoint itself is not overloaded.
- Software libraries and algorithms: Many libraraies and algorithms have been created for teh purpose of rate limiting, such as leaky bucket, fixed windows, and sliding log.
- Reverse proxies and load balancers: LB and RPs (like NGINX) features rate limiting as a built-in feature.

## Simple Object Access Protocol (SOAP)
- SOAP is used to access web services.
- Features can be added without major updates to the implementation.
- SOAP can use SMTP, TCP or HTTP as a transport protocol. SOAP is used to to exchange data between applications that were build on different programming languages.
  - Using HTTP means that you wont need to open extra firewall ports.
- SOAP is based on XML.
- SOAP messages typically consist of four main components
  - Envelope
    - The envelope encloses the XML data and identifies it as a SOAP message.
  - Header (optional)
  - Body
  - Fault (optional)
    - SOAP Fault Options
      - faultCode : Not optional - Specifies the fault code of an error. Below are the fault codes.
        - VersionMismatch
        - MustUnderstand
        - DataEncodingUnknown
        - Sender
        - Receiver
      - faultString : Not optional - Describes an error
      - faultActor : Optional - Specifies who caused a fault
      - detail : Optional - Applies specific error messages

## Remote-Procedure Calls (RPCs)
RPC is used to execute code or a program on a remote node in a network.
The client sends a call to the server, and then waits for the server to return a reply message. once the reply message is received, the results of the procedures are extracted and teh client execution is resumed. There is no limitation on concurrency, so RPC calls can also be executed asynchronously.  
Some notes to remember:
- Error handling should be handled on the remote server.
- Global variables and side effects are sometimes unknown or hidden to the client.
- You will see a performance hit of the remote procedures compared to the local procedures.
- Authentication should be used, because you may be unsure of the transport security.
Some different types of RPC are:
- JSON-RPC
- XML-RPC

## Random notes
One important bit of info to keep in mind, when using API testing them in code is very important. you don't want to troubleshoot code you created for a long time. testing you API calls will be very important troubleshooting step.  
SOAP vs RESTApi
- SOAP request you have to send a lot of data just for a simple get like message. The body in SOAP is large.
- SOAP can only use XML
- SOAP is chatty, and will send you a lot of data back.
- SOAP does not have a standardized interaction model.
- All queries are sent with POST queries. 
- REST uses HTTP methods natively (GET, POST, PUT, PATCH and DELETE)
- REST has easier to manage security for the API calls
- REST can use data streaming, will can make your program more efficient. 
NEVER put sensitive data in the query string. only ever put this data in the headers for an RESTApi calls.


