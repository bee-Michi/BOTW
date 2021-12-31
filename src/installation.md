# Installing

- [Installing](#installing)
- [Genral info:](#genral-info)
  - [Windows](#windows)
    - [Pre requisites:](#pre-requisites)
    - [Installing and running the softwere!](#installing-and-running-the-softwere)
  - [MacOS/OSX](#macososx)
    - [Running from build](#running-from-build)
      - [**Pre requisites:**](#pre-requisites-1)
      - [**Installing and running the softwere:**](#installing-and-running-the-softwere-1)
      - [**MacOS blocking you:**](#macos-blocking-you)
    - [Running from Source](#running-from-source)
      - [**Pre requisites:**](#pre-requisites-2)
      - [**Installing and running the softwere:**](#installing-and-running-the-softwere-2)
  - [GNU/Linux](#gnulinux)
    - [Pre requisites:](#pre-requisites-3)
      - [**Way 1:**](#way-1)
      - [**Way 2:**](#way-2)
      - [**Installing and running the softwere:**](#installing-and-running-the-softwere-3)

# Genral info:

**MacOS/OSX**: There is a unix executable for directly running it, but you can run it form source too.

**Windows**: You need to run it form Source

**GNU/Linux**: There are some .sh file to esaly install evrything.

## Windows

### Pre requisites:

(skip this if you have python alredy installed)

Download the latest release of python [here](https://www.python.org/). Go on downloads and click the download the latest relese. It should pick up your platform autmagiccly, but if not click on:

Downoalds->All releses->Windowns->Stable release->Download windows installer.

Once downloaded click it to install it. **Make shure to click add python 3.10.1 to path**. 

(You can see it at the bottom of the install window)

### Installing and running the softwere!

Download the latest release of BOTW [here](https://github.com/bee-Michi/BOTW/releases). It shloud be the one with the green check mark saying lates near it.

Scroll down untill you see the Source Code zip. Download it.

Once the download is terminated, unzip the file and then (depending on your windows version)

*Windowns 11*: Rigth click on the folder and selcet the open in terminal option.

*Windows 10*: Shif Rigth click on the folder.

Once done type in this command:

```Bash
cd src
python botw.py
```

And enjoy BOTW!

## MacOS/OSX

### Running from build

#### **Pre requisites:**

Nothing, just the build of the program!

#### **Installing and running the softwere:**

Download the latest release of BOTW [here](https://github.com/bee-Michi/BOTW/releases). It shloud be the one with the green check mark saying lates near it.

Scroll down untill you find the MacOS/OSX Build relese .zip file.

Unzip it, and then run the unix executable.

#### **MacOS blocking you:**

If the on launche you recive this alert:

<img src="../img/macos-big-sur-alert-unverified-developer.png" width="150"  height="150">

Then go:

System preferences->Secrity and privay->General->And down you should see open anyway!


### Running from Source

#### **Pre requisites:**

(skip this if you have python alredy installed)

Download the latest release of python [here](https://www.python.org/). Go on downloads and click the download the latest relese. It should pick up your platform autmagiccly, but if not click on:

Downoalds->All releses->MacOS->Stable release->Download the pkg.

Run it, without modifing anything, and you should have it installed.

#### **Installing and running the softwere:**

Download the latest release of BOTW [here](https://github.com/bee-Michi/BOTW/releases). It shloud be the one with the green check mark saying lates near it.

Scroll down untill you see the Source Code zip. Download it.

Once the download is terminated, unzip the file and then rigth click on the the folder, then go down to services, open new terminal with folder and type in these two commands

```Bash
cd src
python3 botw.py
```

And enjoy BOTW!


## GNU/Linux

### Pre requisites:

Now you have two ways of installing BOTW on linux:

**Way 1**: Directly downloading python using your package manager

**Way 2**: Using an install.sh with the source code provided by me


If you are going to use way 2, or have alredy python installed, then skip to the next step. For evryone else:

#### **Way 1:**

Depending on your distro you will have a differnt package manager. Learn more [here](https://itsfoss.com/package-manager/).

Install python using your package manager.

#### **Way 2:**

Download the latest release of BOTW [here](https://github.com/bee-Michi/BOTW/releases). It shloud be the one with the green check mark saying lates near it.

If you are using a popular distro like debian, ubunut, arch, manjaro, gentoo, red hat, fedora or based on this you can use one of the install-(the package-manager).zip (e.g: install-aptget.zip) files. Download, unzip, and run the shell file in sudo mode!

(remeber sudo mode!!!)

#### **Installing and running the softwere:**

**Way 1**: Download the latest release of BOTW [here](https://github.com/bee-Michi/BOTW/releases). It shloud be the one with the green check mark saying latest near it. Scroll down to the zip file and downloaded it.

**Way 2**: Unzip the source code that came with the instalattion!


Once you have compleatly unziped the file go to the unziped folder and do: rigth clickc -> open new termianl at folder.

Then tye these commands:

```Bash
cd src
python3 botw.py
```

Enjoy BOTW!



