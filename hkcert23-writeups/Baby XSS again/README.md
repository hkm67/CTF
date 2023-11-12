This is one of the guided challenges with a very detailed guide [here](https://hackmd.io/@blackb6a/hkcert-ctf-2023-ii-en-4e6150a89a1ff32c#%E5%8F%88%E6%9C%89%E5%AF%B6%E8%B2%9D-XSS--Baby-XSS-again-Web). 
<br><br>
Basically, this challenge simulates a victim that will click on your malicious URL by using bots. However, the bot will only click on the URL if it is from its origin site. Moreover, there is a Content Security Policy restricting the source of scripts. /
To solve this challenge, we will use one of the whitelisted sources `https://pastebin.com ` to hold our payload. We can obtain the flag by redirecting the user to our webhook and extracting the user's cookie through the payload.

Flag: `flag=hkcert23{pastebin_0r_trashbin}`
