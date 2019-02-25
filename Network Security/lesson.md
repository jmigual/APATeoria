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
