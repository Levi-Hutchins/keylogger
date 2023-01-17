# Key Logger
## Description
This was one of a series of projects I completed after finishing my first year of computer science. The project was designed to allow me to gain a deeper understanding of how and why keyloggers work. By developing these software tools and gaining an insider mindset I will hopefully now be able to know when and where a key logger might be in use and how to combat that.  

### How does it Work?
- When the program is started it 'listens' for the internet to be started. The type of browser can be modified in the source code.
- Once the internet is running screenshots are taken every 3 seconds and analysed to see if they contain the phrases "Log in" or "Sign In"
- If those phrases are detected within the images the logging will begin and the images will be saved
- Once the program has reached its entered runtime it will encrypt the log file and send an email containing the encrypted data to the destination email.

###
<details><summary>How to Use</summary>
<p>
Enter your desired runtime in the main.py file

#### Command

```
python main.py 
```

</p>
</details>
