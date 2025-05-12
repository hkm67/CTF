# misc/standard-editor
This is a fun command injection challenge that abuse a wildcard used in the command.

### Challenge Description
There is no description apart from the endpoint.


### Solution
We start with a endpoint that we can connect to with netcat. Once we got in, we can send strings but it only returns a question mark.
<br>
![Pasted image 20250509205502](https://github.com/user-attachments/assets/ea85450b-a19f-40ad-b76a-3238a6e77297)
<br><br>
Upon some testing, and with hints from the name (standard-editor), it is likely a standard `ed` editor in Linux. See the manual [here](https://man.openbsd.org/ed.1).
<br>
![Pasted image 20250509205541](https://github.com/user-attachments/assets/7252fa82-6367-48ba-bba7-767cdee7abf4)
<br>
- Here I have tried different functions within the `ed` context in attempt to execute system commands or read system files. However, all of them are restricted. (Using `!command` or slashes `/` to access directories are disallowed) <br>
<br>

Let's try writing to a file. As hinted in the prompt, the file contents should be printed when we quit the application. We can see that we wrote '123' to `test.txt`, and when we quit with `q`, '123' was printed.
<br>
![Pasted image 20250509205619](https://github.com/user-attachments/assets/ca1c00d5-b92f-48c7-9544-2820f9ae167a)
<br>

What if we just quit directly without writing to a file? 
<br>
![Pasted image 20250509205634](https://github.com/user-attachments/assets/9d18c153-5e78-476a-b258-cc42af5ef6be)
<br>
Hmm, it seems like that the server is using something like `sed '' *` to read and print out the files created in the `ed` editor. Wildcards in commands are easily exploitable if we can write files to the current directory, which we can in the case.
<br>


To test out our hypothesis, let's create a file with the name `--help`, and see how the `sed` command would react to it:
<br>
![Pasted image 20250509205704](https://github.com/user-attachments/assets/96ab2a6d-aeae-492d-b8bd-9ba488f07f3c)
<br>
- Nice! We have successfully used the filename `--help` to pass as an argument for the `sed` command.
<br>

It was then a lot of trial and error, and eventually we can execute system command using `sed`'s `--expression` flag. Since we cannot use slashes (`/`) in our commands, we can create a bash script file that contains any command, and execute it with `sh`.
<br>
![Pasted image 20250509210549](https://github.com/user-attachments/assets/2e4f37e9-9a99-4b76-bfe6-529838ed605a)
<br>

