This web-based challenge is essentially a variant of The Password Game - players have to guess a password based on a growing set of complex rules.
We first spent around an hour playing around with the password rules, and we successfully fulfilled all the rules till no.27, only to realise that all rules afterwards were obfuscated.
<br><br>
While we were confused at first, we soon opened up the page source to see if there was anything interesting.
Surprisingly, we found out that instead of generating each rule one by one when the previous one was solved, the script already generated all the rules (including the hidden ones) in the HTML source.
We were then able to ignore the obfuscated rules and directly look into the code logic - apparently all rules after no.27 only check if the first 6 digits of the hash of a particular substring of the "password" is correct.
<br><br>
By writing a simple Python script, we can easily bruteforce the password by generating all possible substrings and comparing their hash value. This only took us around 15 minutes and we successfully obtained the final flag!
<br><br>
Flag: `hkcert23{h0p3_y0u_u53d_th3_s0urc3m4p}`
