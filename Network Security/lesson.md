# 1. Physical layer


## Types of connections

- Oceanic fiber: cheaper because you don't have to cross a country
- Satellite connection
- Microwave links: cheaper when you cannot put a cable in the land
- Laser:
    - Anybody in the middle can look at the data
- Power line communication
- Underground copper/fiber cables
- Cellular networks
- Wifi
- Bluetooth/LPPAN

## Ethernet security

Building an ethernet wiretap is as easy as just plugin the cables in the middle and then plugin them in your computer. There are even ethernet wiretaps solutions. 

But, if something is glued into the network it can be seen. 
The time it takes to travel for a signal into the cable is:

$$
Z_0 = \sqrt{\frac{L}{C}}
$$

So, actually, if someone is tapped into your network this can be seen by a reflection going partially back.

However, another tap can be done by detecting the magnetic field from the cable.

## Just old stories?
Even though there are many security stories in the past the problem is that the network flaws from the past done by state actors, now can be done by other people since the technology has advanced. 

## Physical layer is a lot of things
Physical layer is not only the cables that connect computers. It is also everything that you connect to your device.

> 60% of all the compromises start with a compromised supply chain

## Optical cables

### Refractive index
$$
\text{Refractive index} = \frac{\text{Speed of light in vacuum}}{\text{Speed of light in medium}}
$$

This happens because in vacuum there's nothing stopping the light. But when there's some opposition the light speed is reduced.

- Air: $n = 1.00027$
- Water: $n = 1.33$

When the light changes from to different refractive indices it changes direction and it's like is "bending"

Snell's law:

$$
n_1 \sin \theta_1 = n_2 \sin \theta_2
$$

There's a maximum angle after which it does not refract anymore.

The optical fiber cables have a cover because otherwise the light could escape if the cable is in contact with a surface with a higher refractive index. The cover has a different type of glass to protect the refractive index.

### Security

As there's always a bit of scattering optic cables can be compromised anyway. There are machines that scan the scattering generated light rays.

## Avoiding compromised networks

An easy way to avoid compromised physical networks can be to have all the cables layered inside a pressured pipe. It's a very cheap method an also if sensors are used to monitor the pressure then it can be detected if someone is actually accessing the cable

## Wireless

### Security through Range limitation?

- UHF RFID
- Bluetooth
- WiFi 802.11b
- GSM

# 2. Link layer

How are we going to do addressing?

This layer introduces addresses, MAC addresses. They are tied to hardware. It allows us to talk to individual devices.

Ethernet:

- 48 bits address
- First 24 by manufacturer
- Last 24 unique device identifier
- $2^{48}$ possible mac addresses

This layer also regulates medium access


## Attacks on link layer
**Problem**: A node can start saying that all the IP addresses are in its MAC address. It's an obvious **man in the middle** attack.

**Solution**: Switches are smart and they usually can know some of the devices for sure. So, if a node tries to have all the IP addresses the switch can turn off the port.

**Problem**: A switch memory usually is very small because they have a different memory style that works different in order to serve packets at high speed. An attacker can fill a switch memory really fast. _CAM Table Flood Attack_

**Solution**: There are two possible options:
- Shut down the switch when the memory fills: There's a loss in availability but not in confidentiality
- Broadcast all the packets through all the ports: There's a loss in confidentiality but not in availability.

### Port security
- White listing addresses
- Authentication

### Virtual LAN
It isolates different types of network but still the bandwidth could be saturated. However for compatibility purposes the default VLAN is 1 and sometimes if you tag a packet as for VLAN 1 the switch may remove the header and this could be exploited when the packet is forwarded.

## WiFi 📶
- Independent service set
- Infrastructure basis service set (BSS)
- Extended service set (ESS)

If an attacker has access to an antenna then it has access to all the other members of the network.

Another type of attack is just adding a fake access point. **Evil twin** attack. If the authentication is only at the user level then there's no way to prevent it.



### National Vulnerability Database

Contains all of the known vulnerabilities of a certain software. There are more than 9000 known vulnerabilities.


## Encryption

## WEP Authentication

It was already catastrophically broken already in 1999. Even though it was broken many years prior it still continued in being adopted for many years. 


### Problem 1: Authentication protocol

You have the access point. 

There's the Input Vector (IV) which is supposedly random but can be picked by the client.

$$
\begin{aligned}
    P \oplus K &= C \\
    C \oplus K &= P \\
    C \oplus P &= K
\end{aligned}
$$

### Problem 2: IV space and IV Reuse
$2^{24} = 16$ million

$$
\begin{aligned}
    54 MBps \\
    BC\ 1500\ bytes \rightarrow 4700 N/s \\
    AC\ 400\ bytes 
\end{aligned}
$$

In an hour there will be an IV collision for sure.

### Problem 3: Message bijection + tampering
- CRC is easy to compute
- CRC is entirely linear

I can modify encrypted texts

ARP messages are encrypted but not all the WiFi packets. So this means that we can predict what it is actually in the data.

$$
\begin{aligned}
    C &= \left[M || CRC(M) \right] \oplus RC4(IV || K) \\
    C' &= [(M \oplus T) || CRC(M \oplus T)] \oplus RC4(IV || K) \\
    &= T || CRC(T) \oplus M || CRC(M) \oplus RC4(IV || K) \\
    &= [T || CRC(T)] \oplus C \implies \text{I can send messages already}
\end{aligned}
$$

RC4 was an algorithm designed in the 1980s, it was the industry standard. Somebody the source code of RC4 and multiple vulnerabilities that it was possible to obtain the original key.

> Don't design crypto yourself!

### Problem 4: Retrieving the WEP key


### WEP Conclusion

We should design security protocols in a different way. WEP was partially hardware implemented. A better security protocol design is to have encapsulated protocols so if something is broken you can switch the protocol quite easily.

10 later after WEP, WPA2 starts to rise

WEP still matters because there are many wireless connections that still use this security protocol. 

> The security design of today will still matter in probably  the next two or three decades

When you have a VPN network you are moving the trust from your local network to another network. For example in an airport if you connect to a free-to-access network then your connection is not secured so the most secure thing is to use a VPN network.

## WiFi Protected Access (WPA)

There was a need to create a new wireless security protocol so they created WPA. But the problem was that there was a lot of hardware designed security that could not be changed.

- WPA was just a hot-fix 
- WPA2 solved many of the problems

### Evolution to WPA

1. The authentication protocol

Previously everyone could read all the messages if they had the key. Now everyone had a different key this time. 

To compute the pseudorandom number that is used for the key they use the MAC addresses, IPs... and also the SSID is used as a salt. This means that the more unique an SSID is the more security you have because attackers won't have a specific table for your access point.

2. IV Space and IV Reuse
3. Message Injection/Tampering due to CRC

They increased the IV size and added the MAC address to the key part so two access points would not have the same key.

Now they used MIC in order to check the CRC which is a crypto secure CRC.

### Evolution to WPA2

Here we could design everything from scratch.

3. Message Injection/Tampering due to CRC

For unguided medium with bit flips a block cypher is more secure. Here now all the origin and destination blocks are encrypted in one key.

4. Retrieving the key

Now they are using a block cypher which is more secure. They used AES which is more secure and they use a temporary key.



## GSM

### Types 

- Be in the middle and downgrade the cypher used for encryption
- Passive listening and decrypt the data when required
- Just passive listening and you can ask for a user's location

# Network Layer

Provides a point-to-point connection between two networks

We use Internet Protocol for this

## Enterprise topologies

You need to create a list of importance of difference users. Usually the admins have the highest priority but they usually have a low-priority account. The high priority is only used in certain cases and it is good if two admins work together when using the high priority



