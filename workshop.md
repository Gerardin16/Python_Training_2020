## Gmail new email alert - Pulling Mechanism
	1. Login into Gmail with user credential(Uname, password)
	2. User credential should come from Configuration file
	3. Create separate component of Configuration Manager
	4. Create other cross cutting components - Logging, Auditing, Configuration
	5. Every 5 minutes once, need to verify any new mail arrives
	6. Upon coming new mail in the inbox, raise an alert notification
	https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10
	http://www.quartz-scheduler.org/
	
## File Watcher and Word repeated Count - Push Mechanism
	1. Create a file watcher in a specific folder
	2. The specific folder name must be specified in a configuration file
	3. Create other cross cutting components - Logging, Auditing, Configuration
	4. As soon as new file arrives, need to identify the repeated word count
   	5.The told word count result should be mail to the recipients defined in the configuration
 
	 http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html
 
 1. Class
 2. Component
 3. Sequence Diga
 4. Activity 
 5. Use case (Optional)


