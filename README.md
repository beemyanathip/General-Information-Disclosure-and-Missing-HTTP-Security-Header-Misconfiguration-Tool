# General-Information-Disclosure-and-HTTP-Security-Header-Misconfiguration-Tool

This Python program checks the security and information leakage aspects of a website by sending an HTTP request to the provided URL. 

This function sets up an option parser to accept a URL using the '-u' or '--url' option.
It parses the command-line arguments, and if the URL is provided, it returns it.
Get the URL from the command-line arguments

# Often people who set up servers expose too much information in the UAT environment.
and then forget to turn off that disclosure in the actual use condition (Production Environment), allowing users to know the technology and version numbers of the tools used in website development And it allows attackers to use this information along with other information on the system to attack web applications through Common Vulnerabilities and Exposures (CVE).

Using HTTP Security Header: It is a feature that enhances the security of web applications. Helps users protect against threats from attackers It has the following features:

   -X-Content-Type-Options: This header is used to prevent attacks through MIME type sniffing, which occurs when a website allows users to upload content to the server, and users can change 
    or hide files that may be malicious and then upload them to the server.
   -Content-Security-Policy: This header helps define the source of content that is allowed for a website by restricting the content that a browser can load, such as JavaScript and CSS.
   -Strict-Transport-Security: This header sets the browser to always use HTTPS, even if the user initially entered an HTTP URL. It enforces a secure connection by specifying that HTTP 
    requests should be automatically redirected to HTTPS.
   -X-Frame-Options: This header helps protect users from clickjacking attacks, where attackers can load iframes from their own website onto your website, making users believe your website is 
    not malicious.
   -Referrer-Policy: This header is a new format that helps websites control the data collected by the browser along with document references. Every website should configure this setting.
 
# This function sets up an option parser to accept a URL using the '-u' or '--url' option.
It parses the command-line arguments, and if the URL is provided, it returns it.
Get the URL from the command-line arguments

The program calls the get_url_arguments() function to obtain the URL to be checked. If no URL is provided, it prints a message asking the user to provide a URL using the '-u' option.
Perform an HTTP request to the provided URL

The program sends an HTTP GET request to the provided URL with a timeout of 5 seconds and stores the response in the response variable.
Extract HTTP response headers

It checks if the 'Server' and 'X-Powered-By' headers are present in the response.
If 'Server' header is present and contains any digits, it adds it to the geninfo list.
If 'X-Powered-By' header is present, it also adds it to the geninfo list.
Define a list of security headers to check:

The program creates a list of specific security headers it wants to check for, such as X-Content-Type-Options, Content-Security-Policy, etc.
Check for missing security headers:

The program compares the list of security headers with the headers obtained from the response.
If any of the security headers are missing, it adds them to the missing list.
Display results:

The program prints the results:
If any security headers are missing, it lists the missing headers.
If no security headers are missing, it congratulates by saying there are no missing HTTP security headers
and the final step if there is any server or technology information leakage, it lists that information.

