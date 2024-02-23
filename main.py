import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


sender_email = os.environ['email']
password = os.environ['Password']
mailing_list = []

for receiver_email in mailing_list:
  message = MIMEMultipart("alternative")
  message["Subject"] = "Invitation for Annual Sponsorship Meet"
  message["From"] = sender_email
  message["To"] = receiver_email
# Create the plain-text and HTML version of your message

  html = """\
<html>
  <body>
Greetings from Team Octane Racing Electric!<br><br>

We at Octane Racing, are a team of 40+ ambitious engineers from various disciplines of <b>COEP TECHNOLOGICAL UNIVERSITY</b>. We design, manufacture, and race an F1-styled, single-seater, electric vehicle to participate in various national and international competitions conducted by <b>SAE international</b> (Formula Bharat), <b>SAE India</b> (SUPRA), <b>Formula Green</b>, and <b>Formula Imperial</b>. We feel proud to tell you that almost 75% of our car is manufactured in-house!
<br><br>
We have a stellar record when it comes to the results too! The following are the results of our latest competitions –
<br><br>
<b> Formula Bharat 2024-
<ul>
<li>Overall 4th in India, falling just 12 points short of 1st place. </li>

<li>1st place in Cost and Manufacturing. </li>

<li>5th place in Engineering Design.</li>
</ul>
 
<br>
Formula Bharat 2023-
<ul>

<li>Overall 4th in India</li>

<li>2nd in Acceleration</li>

<li>2nd in Autocross</li>

<li>2nd in Endurance</li>

<li>2nd in Skid pad</li>

<li>3rd in MathWorks Modelling</li>

<li>5th in Engineering Design</li>

<li> 7th in Cost and Manufacturing</li>

</ul>
<br>
Formula Imperial 2022-
<ul>
<li>Overall Champions (1st in India)</li>

<li>1st in Cross-Pad</li>

<li>1st in Acceleration</li>

<li>1st in Innovation</li>

<li> 1st in Business Plan</li>

<li>1st in Cost and Manufacturing</li>

<li>Best Driver</li>

<li> Future Award</li>
</ul>
</b><br>
We are associated with <b>Bajaj Auto, TE connectivity, Dhoot Transmission, ANAND Group, XPS, Analog Devices, Tesla, Texas Instruments, Dassault Systemes</b>, and many more.
<br><br>
To celebrate our recent successes, Team Octane Racing Electric has organised a sponsorship and networking event to thank our sponsors for their valuable support and guidance, and to invite renowned companies in the industry to learn from their experience.
<br><br>
We cordially invite you to join us for our <b>Annual Sponsorship Meet</b> on 2nd March 2024 from 10:00 am to 12:30 pm, at Mini Auditorium, COEP TECH, where we will be unveiling our plans and projects for the future, and an electrifying <b>Roadshow</b> of our 2024 racecar, <b>Alectrona 3.0. </b>
<br><br><br>

<a href="videolink">Here's a peek at our Event winning vehicle.</a>

<br><br><br>
Piyush Goyal,<br>
7276772183,<br>
Captain,<br>
Team Octane Racing Electric,<br>
COEP Technological University.<br><br><br>

<span lang="EN-US" style="font-family : Arial Black, sans-serif;color:red">TEAM OCTANE RACING ELECTRIC </span>| <a href=”http://www.coep.org.in/”>COEP TU</a>
<br><br><br>
Email: teamoctaneracing2025@gmail.com | octaneracing@coep.ac.in

<br><br><br> Follow us: <a href = "https://www.facebook.com/TeamOctaneRacing/">fb/TeamOctaneRacing </a> | <a href = "https://www.instagram.com/teamoctaneracingelectric/?hl=en">in/teamoctaneracing</a>

</body>
</html>


"""
  message.attach(MIMEText(html, "html"))

# Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )
