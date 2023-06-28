NOTE: if anyone is reading this I left out some of the objectives because i knew them well enough I saw no value in taking notes.


### Azure Security Center
Azure security center is a monitoring service that provides threat protection across both Azure and on-prem data centers.
- Provides security recommendations.
- Detect and block malware.
- Analyze and identify potential attacks.
- Just in time access control for ports.
Capabilities
- Policy Compliance
  - Run policies across management groups, subscriptions or tenants.
- Continuous Assessments
  - Assess new and deployed resources to ensure that they are configured properly.
- Tailored recommendations
  - Recommendations based on existing workloads with instructions on how to implement them.
- Threat protection
  - Analyze attempted threats through alerts and impacted resource reports.

### Azure Sentinel
Azure sentinel is a security information management (SEIM) and security automated response (SOAR) solution that provides security and threat intelligence across an enterprise.

### Azure dedicated hosts
Azure dedicated hosts provides physical servers that host one or more Azure virtual machine that is dedicated to a single organization's workload.  
Benefits
- Hardware isolation at the server level.
- Control over maintenance event timings.
- Aligned with Azure hybrid use benefits.

### Defense in depth
- Layered approach to securing computer systems.
- provides multiple levels of protection.

### Network Security Groups (NSGs)
NSGs filter network traffic to and from azure resources on Azure virtual networks
- Set inbound and outbound rules to filter by source and destination IP address, port. and protocols.
- Add multiple rules, as needed, within subscription limits.
- Azure applies default, baseline security rules to new NSGs.
- Override default rules with new, higher priority rules.

### Azure Firewall
A stateful, managed Firewall as a Service (FaaS) that grants/denies server access based on originating IP address, in order to protect network resources.
- Applies inboud and outbound traffic filtering rules.
- Built-in high availability
- Unrestricted cloud scalability.
- Uses Azure monitor logging.
- Azure also has WAF.

### Azure DDoS protection
You can also enable DDoS. It is turned on by default.