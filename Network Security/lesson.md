# Physical layer


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

# Link layer

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


### Encryption

### WEP Authentication

You have the access point. 

There's the Input Vector (IV) which is supposedly random but can be picked by the client.

$$
\begin{aligned}
    P \oplus K &= C \\
    C \oplus K &= P \\
    C \oplus P &= K
\end{aligned}
$$

#### Problem 2: IV Reuse
$2^{24} = 16$ million

$$
\begin{aligned}
    54 MBps \\
    BC\ 1500\ bytes \rightarrow 4700 N/s \\
    AC\ 400\ bytes 
\end{aligned}
$$

In an hour there will be an IV collision for sure.

#### Problem 3: Message bijection + tampering
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



