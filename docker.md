Usefull docker commands
---

* Starting a hadoop container:

  `docker run -it kristiania/hadoop`

  This will download the latest image and start a container.

  Parameters:
  - `-it` means that you will log in to an interactive shell.
  If you want the container to be removed when you log out, then add `--rm` to the command, i.e.:

   `docker run --rm -it kristiania/hadoop`
* Listing all containers

  `docker ps -a`

* Mounting a volume:

  `docker run -v /Users/user/foo:/hadoop -it kristiania/hadoop /start`

  This will map your local folder /Users/user/foo to a volume in the container at the point /hadoop.


