<div id="top"></div>
<h3 align="center">Diffie-Hellman Key Exchange and Man-in-the-Middle Demonstration</h3>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <ul>
      <a href="#about-the-repo">About The Repo</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </ul>
  </ol>
</details>

<!-- ABOUT THE REPO -->
## About The Repo
This repo contains 2 Python files (1 class file and 1 script). [endpoint.py](./endpoint.py) contains
an endpoint class with the methods to generate public and session keys using the
[Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange).
It also contains a class used to simulate a [Man-In-The-Middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attack where the private keys of an endpoint are retrieved via brute force calculations.
[key_exchange.py](./key_exchange.py) simulates a key exchange between 2 endpoints
(Bob and Alice). It also simulates a Man-In-The-Middle
attack (conducted by Mallory) which shows how this key exchange can be broken
when small prime numbers are used.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- BUILT WITH -->
### Built With
These are the requirements for using these scripts:
* [Python 3](https://www.python.org/downloads/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE -->
### Usage
To run the project, place both Python files in the same directory. Then, invoke the
key_exchange.py file from the command line. Adding the ```-q``` option speeds
up the initial calculation of primes, but adds a small chance of the calculated
number not actually being a prime number.

<p align="right">(<a href="#top">back to top</a>)</p>
