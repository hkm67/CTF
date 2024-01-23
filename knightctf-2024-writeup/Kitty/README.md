This is another web-based challenge with the follow description:
> Tetanus is a serious, potentially life-threatening infection that can be transmitted by an animal bite.
<br>

The description hinted that the task is about some kind of poisoning attack. Upon a few attempts of different web-based attacks, we discover that it was an SQL injection vulnerability. The final payload was the following:
<br>
```
Username: Admin
Password: "OR 1=1 --//
```
<br>
This successfully logged us in a forum page with a textbox for creating new posts.
<br><br>
 <img src="https://github.com/michaelkhchan/CTF/assets/101359830/52ae7f0d-9770-4784-b37b-1348087a0f60" width=500>
<br><br>

The hints stopped here, and any input submitted will just create a new post. By reviewing the source code, we can see that the script revealed the way to show the flag.
<br><br>
 <img src="https://github.com/michaelkhchan/CTF/assets/101359830/c83da454-763b-4d52-9ca1-3ba2b9cc8aa4" width=500>
<br><br>
Entering "cat flag.txt" into the textbox, and it will return the flag in the newly created post.
<br><br>
Flag: `KCTF{Fram3S_n3vE9_L1e_4_toGEtH3R}`

