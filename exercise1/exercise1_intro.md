In this exercise we will setup an environment on your machine. After that you are going to get familiar with Hadoop command line tool and be able to run the commands.

There are two methods to run the exercise:

1. **Manual**. Install the following:
 * java
 * maven
 * hadoop
2. **docker** base image `kristiania/hadoop:latest` (recommended)


### Method 1. Manual.
1. Download java:

    <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>

Accept and choose the installation file depending on your platform.
For windows users, install it on `C:\java` or other place without space in the filename.

For linux users, use apt-get or yum to install java.

2. Download maven (if you don't have it already).

<http://apache.uib.no/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.zip>

Setup your path so maven is available from command line.

Linux: `export PATH=<path_where_you_extracted_zip>/bin:$PATH`

Windows: Open Environmental variables, e.g. http://bit.ly/1iW3PV0  : Find variable "path" and append the `<maven path>/bin`

Check in the command line if `mvn -version` works.
NB! make sure you have both  `java -version` and `mvn version` working.

### Method 2. Docker.
The base image can be obtained from docker hub.
1. Install docker (if you don't have it).
2. Run: `docker run -it kristiania/hadoop /start`
3. You can find hadoop at `/opt/hadoop/latest/`.
4. Run a sample command, for example list: `hadoop fs -ls`

Tasks:
If you are not using docker, just run the commands without logging in to the container.
1. Log in to you docker container:
    * `docker run -it kristiania/hadoop`
    
2. Create a directory:
  * Use `-mkdir` to create a directory. E.g.

  `hadoop fs -mkdir <YOUR_FOLDER>`

  You have created a folder in the hdfs. Try to create the same folder again, you should receive  an error.
3. List files:
   * Use the `-ls` command to list files.

   `hadoop fs -ls`

   Did you see your folder? How would you list the contents of that folder?
4. Copy a local file:
    - create a dummy file:

      `echo "MY text file"> myfile.txt`
    - Copy to hdfs:

       `hadoop fs -copyFromLocal myfile.txt`
5. Move a local file:

   - use the `-moveFromLocal` to move the file you just created to folder you created in 2.
   - use `ls -l` to make sure the local file is not there.

6. Copy the hdfs file to local machine:

   `hadoop fs -copyToLocal myfile.txt tmp/`

7. Check the content of your file:

   Use the `-cat` command, i.e.:

   `hadoop fs -cat myfile.txt`

8. Use the full url:

  `hadoop fs -cat hdfs://localhost/user/root/myfile.txt`
