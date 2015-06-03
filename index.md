---
layout: default
---

# Life of a web request. How the Internet works?

![Project image](//img.sieben.fr/internet_is_fascinating.jpg)

The Internet is becoming one of the most important tool that people use to
read, do and share research, messages and ideas. Many people use it as a tool
but not so many really understand how networks and the Internet works, evolve
and keep spreading its influence. The Internet is by itself a very vivid
subject of research related to the domain of distributed systems with very
active and open research mixing industry and academics. Making computers talk
to each others seems like obvious today but network protocols are the results
of a long process mixing engineering and scientific research.

The goal of this project would be to study, understand and recreate all the
protocols that make the Internet what it is.  We would study the Internet's
structure and protocols through experiments and dissecting network activity.
We'll use and write programs to explore what happens at a networking level as
you surf the Web, use a search engine, send emails, use torrents and more. All
these protocols would be tested and played with. At the end, students would be
able to craft a little Internet working within their own network.

The concrete agenda of this project would be split into a core
[project](project.html) that will give student a concrete use case and
several options and side tracks that will be explored as the student progress.

<hr>

## Required material

- Curious students.
- Relatively recent computer (Intel i3,5 or 7 and at least 2GB of RAM)
- Mostly PC running a recent UNIX system (GNU/Linux or MacOSX). For people running windows I can find workarounds using virtualbox.
- If computers are provided can you ensure that I will be able to install software on it and more generally have administrative privileges? That would   help in the very low level part of the networking stack.
- If you have some raspberry pi/Arduino available that would be great. Otherwise I will see if I can bring some with me.

## Agenda (Will change with student interest and progress)

| Day 1  | Presentation & Setup                          |
| Day 2  | [Working on core](project.html)               |
| Day 3  | [Working on core](project.html)               |
| Day 4  | [Working on core](project.html)               |
| Day 5  | [Working on web options](web.html)            |
| Day 6  | [Working on web options](web.html)            |
| Day 7  | [Working on networking options](network.html) |
| Day 8  | [Working on networking options](network.html) |
| Day 9  | [Working on iot/sensing options ](iot.html)   |
| Day 10 | Sum up                                        |

<hr>

## Aims

### What is the problem you are going to solve? / What will be the challenge in this project?

- How computers connect to each others on the other side of the world?
- How computers talk to each others?

### What is the final result you will get? / What will you try to accomplish in the end?

We obtain the same thing at the beginning that at the end. Rather than building
something we are going to dissect a living system. At the end I want to hear a
story. What happen when I press enter while visiting a website. What happen
when I launch a process.

<hr>

## Project Course

### Theoretical concepts

How protocols are constructed. General pictures of how computers works and what
are the different levels.

I'm a teaching assistant so I got all the material from my introduction course
to networks. My objectives is to have a more hand-on experience. Go from
working stuff and then try to dissect the different encapsulation and
understand how they work with each others but always starting from a simple
core project.

### Experiments performed

Dissecting protocols, seeing what are the packets sends on the internet. See
how they evolve how they move. For that we will use wireshark that is a packet
dissector and different virtual machines interconnected in a virtual network
to see how communications happen between machines. The agenda of our different
focus is presented in Agenda.

<hr>

## Science with benefits

### Benefits for the students

- A basic understanding of the processes happening inside the internet and also
  inside their computer.

- Some notion about python and python libraries that might help them later on
  if they continue working in science/tech fields.

### Why should it be featured?

Understanding the Internet and the problematic behind how it works can be
useful for every scientist that want to preserve an open Internet and being
able to solve problems that might occurs while using it to share/talk with
other people with it.

There is an other benefit. The Internet is probably one of the most decoupled
achievement of humanity. It doesn't have a single creator, controler or
regulator. It's an ecosystem mixing scientists, industrials and people.
Understanding the human processes behind this can be relevant to scientist as
well.

<hr>

## Security risks

All experiments will be run on virtual machine or uncriticals machines.
Students should be safe.

## Backup plans

### Hardware issues

As long as I got working and recent machine where I can do whatever I want or
install virtual box, I think I will be fine. One safer bet would be to tell
the students to bring their own devices. Therefore, no matter what is provided
we might have a fallback. I can find dirtier hacks if that fail as well but I
would strongly appreciate having some safety that I will have proper
materials.

### Interest/Understanding issues

In the case where students are not interested and/or don't understand what is
going on I can change subjects relatively quickly to an other aspects of
computing. Because the core project is simple, it can be done quickly. All the
others options are based on motivation and are very diverse in terms of
complexity and time investment. Matching between students and options will be
easy to make. All of them are pretty much independant. I would strongly
appreciate to have students interested in computer science/networking. Worst
case scenario, we could probably team up with the guys in Automating Biology -
An End to End Approach and focus on how to make sharing research easy
with IPython because we will use that in the core project.

### Outperforming issues

Even if the core project can be achieved easily, several options are available
to extend previous work. Those options will be started only after the core
project is completed.

An alliance between the guys in Automating Biology - An End to End Approach
could also be done in case where students are working fast and we have enough
times to propose collaboration with other teams.

<hr>

## The part where I talk about myself with the third pronon

*don't forget to show my head to the people. it's well worth seeing*

<img src="//img.sieben.fr/me.jpeg" alt="Here is my face" style="width: 200px;"/>

Remy LEONE a PhD student working at Telecom Paris Tech in the field of
Wireless Sensors Networks. His research interests are passive monitoring of
networks, active estimation of energy reserve and lifetime expectancy of a
network. For more information go checkout [sieben.fr/phd](sieben.fr/phd).

Student of S3++ in 2007 and member of [Paris Montagne](//paris-montagne.org)
since 2006. These associations spread science and scientific research taste in
young and not so young minds.

<!--
You can know more by looking at http://sieben.fr/about. Happy stalking :)
-->
