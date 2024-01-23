This is some of the first warm-up tasks of the CTF. The challenge's description was: *"Levi Ackerman is a robot!"*, with a website: http://66.228.53.87:5000/.
<br><br>
Given the hints, we can try to visit the website's robots.txt to see if any pages are hidden from search engines and crawlers. Upon reaching http://66.228.53.87:5000/robots.txt, we can see that the following page is disallowed:
<br><br>
`Disallow : /l3v1_4ck3rm4n.html`
<br><br>
By visiting the page, we can obtain the flag for this simple task.
<br><br>
Flag: `KCTF{1m_d01n6_17_b3c4u53_1_h4v3_70}`
