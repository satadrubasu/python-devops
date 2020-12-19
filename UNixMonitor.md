
 
## SWAP Memory  
 - free  
 - cat /proc/swaps ( where swap is in use )  

Swap space in Linux is used when the amount of physical memory (RAM) is full. If the system needs more memory resources and the RAM is full, inactive pages in memory are moved to the swap space. While swap space can help machines with a small amount of RAM, it should not be considered a replacement for more RAM. Swap space is located on hard drives, which have a slower access time than physical memory.
Swap space can be a dedicated swap partition (recommended), a swap file, or a combination of swap partitions and swap files.
 File systems and LVM2 volumes assigned as swap space cannot be in use when being modified. For example, no system processes can be assigned the swap space
 , as well as no amount of swap should be allocated and used by the kernel. 
 
 Use the free and cat /proc/swaps commands to verify how much and where swap is in use.
 


### [Planning ] Swap Memory  

Swap should equal 2x physical RAM for up to 2 GB of physical RAM, and then an additional 1x physical RAM for any amount above 2 GB, but never less than 32 MB.
For systems with really large amounts of RAM (more than 32 GB) you can likely get away with a smaller swap partition (around 1x, or less, of physical RAM).

### [ Adding ] Swap after RAM Upgrade  

Sometimes it is necessary to add more swap space after installation. For example, you may upgrade the amount of RAM in your system from 128 MB to 256 MB, but there is only 256 MB of swap space. It might be advantageous to increase the amount of swap space to 512 MB if you perform memory-intense operations or run applications that require a large amount of memory.
You have three options: create a new swap partition, create a new swap file, or extend swap on an existing LVM2 logical volume. It is recommended that you extend an existing logical volume.

 *https://web.mit.edu/rhel-doc/5/RHEL-5-manual/Deployment_Guide-en-US/s1-swap-adding.htmlSource 
