This is a steganography challenge that starts with a zip file "chall.zip" and the description:
> Hunt your way through the challenge and Capture The hidden Flag!!!
<br>

After downloading the zip file, we noticed that the files inside was password protected. We used `zip2john` to create a hash from the zip file, and used John the Ripper (`john`) to brute force the password. The commands were as follow:
```
zip2john chall.zip > chall.hash
john --wordlist=/usr/share/wordlists/rockyou.txt chall.hash
```
With just under 20 seconds, we have cracked the password: `zippo123`.
<br><br><br>
Extracting the zip file returned 999 identical image files of [`You Know What It Is`](https://www.youtube.com/watch?v=dQw4w9WgXcQ), a WAV file and two txt files with the contents as follow:
```
n0t3.txt:
The flag is here somewhere. Keep Searching...

Tips: Use lowercase only

nooope_not_here_gotta_try_harder.txt:
KCTF{f4k3_fl46}
```
<br>
When listening to the WAV file, it was clear that it was a Morse code audio. 

Using an online [Morse Code Audio Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html), we were able to extract the message: `MORSECODETOTHERESCUE!!!`.
<br><br>
We were then stuck here for a while, until we noticed that one of the images, IMG_725, was slightly larger than the others with a later edited date. We then used `steghide` on IMG_725 with the passphrase `morsecodetotherescue!!!` and successfully extracted the "flag.txt".
<br><br>
Flag: `KCTF{3mb3d_53cr37_4nd_z1pp17_4ll_up_ba6df32ce}`
