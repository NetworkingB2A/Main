Different data types
- Transit
- Rest



Some Key terms to understand for security:
- Asset: An asset is something you're trying to protect.
- Threat: Anything you are trying to project against is known aas a threat. 
- Vulnerability: A vulnerability is a weakness or gap in protection efforts.
- Risk: Risk is the intersection of assets, threats, and vulnerabilities

Common threats to applications and some mitigation options

|Threat|Mitigation options|
|-|-|
|Buffer overflow|Separate executable memory from non-executable memory, Randomize address spaces for data, use the built-in projection options in new software OSs and languages.
|Man-in-the-middle| Adopt a SSL/TLS strategy for both web and Email, avoid sensitive data in public Wi-Fi or computers
|DoS attack|Use designed protection services.
|Cross-site scripting| Validate and sanitize input data, Employ cookie security such as timeouts encoding the client ip address and so on.
|Phishing| Educate users to avoid falling for the bait, Detect and mark emails and sites as spam.
|Malware| deploy technologies that continually monitor and detect malware that has evaded perimeter defenses
|SQL injection| Use character escaping, use stored procedures as opposed to queries enforce privileges
|Brute force| Lock the system after a specified number of attempts, use two-factor authorization.

OWASP list of top 10 security risks:
1. Injection
2. Broken authentication
3. Sensitive data exposure
4. XML external entities
5. Broken access control
6. Security misconfiguration
7. Cross-site scripting
8. Insecure deserialization
9. Using components with known vulnerabilities
10. Insufficient logging and monitoring

To minimize risks, the following are some of the best practices in the industry:
- Keep software up-to-date
- Install end-user or device security
- Use strong passwords
- Implement multifactor authentication (MFA)
- Install a firewall
- Encrypt data

Data security types
|Data type|How to protect the data|
|-|-|
| Data in motion | Https, Firewalls |
| Data at rest | Full disk encryption, File system encryption, Database encryption |
| Data in use | Full memory encryption, CPU-based key storage, Enclaves, which are guarded and secure memory segments | 

