Postmortem: Outage on 19th January 2024
🚨 Oops! Our Servers Took a Siesta! 🚨
Hey there, fellow tech aficionados! Ever had a day where your servers decide to take a little break without giving you a heads-up? Well, on the 19th of January 2024, our Nginx server got a bit too cosy and decided to crash the party, leaving 90% of our users scratching their heads and waiting longer than usual for our services. But fear not, because we're here to spill the beans on what went down and how we fixed it faster than you can say "code monkey"!
Timeline ⏰
12:00 PM: Oh snap! Our monitoring system goes wild with alerts, signalling trouble in server paradise.
12:15 PM: The engineering squad is on the case faster than you can say "404 error"! Investigation mode: activated.
1:00 PM: Cue dramatic music! We uncover the villain behind the chaos - a sneaky bug chilling in our Nginx server config.
1:30 PM: Bug squashed! Server gets a wake-up call and restarts with a vengeance.
2:00 PM: Crisis averted! Our servers are back online, ready to rock and roll like nothing ever happened.
Root Cause and Resolution 🛠️
Root Cause: Turns out our Nginx server was feeling a bit overwhelmed by a misconfigured rate limiting rule, causing it to throw a tantrum and crash.
Resolution: With a swift update to the rate limiting rule, our server learned how to handle traffic spikes like a pro, avoiding future meltdowns.
Corrective and Preventative Measures 🛡️
Tweak the Nginx settings: We gave our Nginx server a little pep talk and adjusted its settings to handle traffic spikes without breaking a sweat.
Bring in the Big Guns - Monitoring System: We beefed up our monitoring system to keep a closer eye on our servers, catching bugs before they have a chance to party crash.
Code Reviews for the Win: Regular code reviews are now part of our routine, ensuring those sneaky bugs don't stand a chance.
Lessons Learned 📚
Testing, Testing, 1-2-3: Thorough testing and code reviews are like sunscreen for your codebase - essential for avoiding those nasty burns.
Eyes on the Prize: Monitoring systems are our trusty sidekicks in the fight against server gremlins, helping us squash bugs before they cause chaos.
Ready, Set, Respond!: A well-oiled incident response plan is the superhero cape every tech team needs, swooping in to save the day when things go haywire.
Conclusion 🎉
So, there you have it! The tale of our server's unexpected siesta on January 19th, 2024. But fear not, dear readers, for every outage is an opportunity to learn and grow. Armed with our newfound wisdom, we march forward, ready to tackle whatever challenges come our way, with a sprinkle of humour and a whole lot of determination!
Read the full postmortem here!

