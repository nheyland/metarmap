# Metarmap

MetarMap with a controller
https://www.youtube.com/watch?v=yWWK8UxB6ag

[Check out the App!](https://apps.apple.com/us/app/mapremote/id1576002389)

## Installation

See below!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please email me for more information

If you like this project and want to collaborate, please contact me!

## Future Goals

Someday youll be able to buy a package containing the strip of LEDs with the Pi already configured, and a set of the 3D printed parts of the project. I am not there yet, but ultimately that is the goal!

## License

Dont make and sell these, its a community project. I worked hard on this, just trying to make it easier for people to make a metar map and not have to pay 700$ for a premade one that does the same thing.

[MIT](https://choosealicense.com/licenses/mit/)

## Simple Setup

1. Build a metarmap using any WS2812B LEDS
   a. Set the GPIO 18 pin to the data LED wire, ground and 5V can go to any corresponding pin on the board
2. Pull this repo into the raspi
3. Create a script to run the boot.py file at startup
4. Add the airports in order into the contstants file
5. Take note of the KEY_IP and in a web browser on another device enter that ip with the port 3333

## Full Instrcutions

There are a ton of ways to make these maps. Ive made 4 versions and concluded this was the best way for me. You can be cheap and spend as little as 50$ start to finish on it, or go big and spend 150$ on it. I have a medium level shopping list HERE() that will make this quick for you, but consider taking some time to plan it out. Read through this before you buy anything, and check off the boxes, then purchase. I have affiliate links in here, but I still kept the cart on the medium side of quality for convience.

Some of this is required. Some is optional, like I said, pick and choose.

1. Shopping list

   - Map
     - Get these printed at staples or a printer service, I highlight recommend getting printed on foamboard, otherwise buy a posterboard and glue to get these printed
       - Sectional from the FAA [HERE](https://www.faa.gov/air_traffic/flight_info/aeronav/productcatalog/vfrcharts/sectional/)
       - Mapbox Studio This is more customizable, choose the print option and set 36x24 with the highest ppi you can get. (Looks best) [HERE](https://www.mapbox.com/mapbox-studio)
   - LEDs

     - As long as you get WS2812b programmable leds (3 wire) it should work, here are some choices
       - 1st place - From alibaba, great quality, favorite, longest shipping [HERE](https://www.aliexpress.com/item/1342959831.html?spm=a2g0o.store_pc_groupList.8148356.30.3b5e60e8KHoRQY)
       - 2nd place - nearly identical to the first but more expensive [HERE](https://amzn.to/2TRrXQL)
       - 3rd place - I hate this kind, it sticks out of the map, you cant have a glass screen, everyone uses it because its easiest [HERE](https://amzn.to/3wAiVov)

   - Frame

     - You can get creative here, make a frame, buy one, go with no bezel, whatever you want. Remember we need about 3/4 of an inch give or take a bit to accomodate for the LED you choose
       - Amazon Basics (2 Pack) they only sell it in a 2 pack but 100% worth it. You can actually use both stacked up and screwed or glued together to avoid a lot of trouble. Or just use one and find a way to make a spacer behind the board. [HERE](https://amzn.to/3wAiVov)

   - Pi

     - Two options, both work, as long as it has wifi it can be used. You will also need an SD card. 16 gb is best.
       - Pi [HERE](https://amzn.to/3wAiVov)
       - Pi Nano [HERE](https://amzn.to/3wAiVov)
       - Sd Card [HERE](https://amzn.to/3wAiVov)

   - Extras
     - Required
       - Hot glue gun HERE()
       - HDMI Cable (lets be honest you probably have one somewhere)
       - Breadboard wires
     - Not Required
       - Screws
       - 3D Printer (if you needed an excuse to buy one here it is) I provide STLs here for the bulbs (flat LEDs (choice 1 & 2 only)) and for the spacers as well
         - Clear Filament
         - Black Filament
         - Want these but dont want the printer? Email me, venmo me and then we can work out shipping the parts once I print them

2. Assembly - Software Part A

   - When I first made my metarmap, I didn't know code. designed this to be as simple as I could... lets see how this goes. In time I will make this much easier.
   - Email me if you have an issue, otherwise I prefer users to make an issue on this github repo, but I understand not everyone uses github.

   One - Lets start with the Pi, we need to set up raspbian os here in order to have the computer understand what is going on, its like a mac or windows OS but for a microcomputer click [HERE](https://www.raspberrypi.org/documentation/installation/) for the step by step guide.

   Two - Once the pi is set up, connect a keyboard and mouse to the computer, as well as an hdmi cable to an external monitor.

   Three - Go through the process of setting up the Pi like you would any computer, connect to the wifi

   Four - Open terminal, we will need to donwload the software from this page, start by typing `pwd`, you should see something like /home/pi

   Five - Clone this repo `git clone https://github.com/nheyland/metarmap.git`

   Six - Confirm, now type `ls`, you should see a few words pop up that represent directories, now including metarmap

   Seven - Type `cd metarmap` we are now working in the repo, type `ls` and you will see the files that run the metarmap

   Eight - Install packages - Type `sudo apt-get install python3-pip` to install our package manager, then type `pip install -r requiremnts.txt`

   Nine - Test the file type in `sudo python3 boot.py` if you see any errors, now is the time to fix them, email me or post them on the issues board in this repo

   Ten - Once you see `IP is set to -> 192.168.0.##` Appear in the window, we have success! Write down that ip address, as we will use it later on to access the interface

   Eleven - Lastly, lets make sure the device always boots up and starts this server, type ` sudo nano /etc/rc.local.`, use the arrow keys to scroll down to just above the exit 0 line, then type `python3 /home/pi/metarmap/boot.py &`

3. Assembly - Hardware
   This is the hard part, building the map.
   - If you need to, glue the map to the foamboard now, trim the edges, make sure it fits in the frame
   - Start by poking small holes at the airports you want to use, take note of the length between the airports and the length of the LED gaps between lights, avoid cutting wires at all costs.
   - Depending on the LED used, poke the LEDs into the board, or instead if using the flat LEDs find a good way to position the lights so the center of the LED shines through the hole. This is where the buld.stl 3d printed file comes into play, it helps carry the light through in a super clean way. Once through, hot glue the led in, trim the 3d printed tip off to be flat with the surface.
   - The LEDs have an arrow on them, that is where the LEDs start, this is known to us as LED 1 (in reality LED 0)
   - Connect the 5V wire (usually red wire) to a 5V pin on the pi, the ground wire (usually black) to a ground pin on the pi, and most importantly, the data wire to the GPIO oin 18 on the pi [heres a diagram](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/4/header_pinout.jpg)
   - If using the amazon basic poster frame or a similar style frame, unscrew those little scres in the back of the board, scre in the spacer stl (if you have a 3d printer) or find a way to create about 1 inch space between the board and the backing of the frame, the wires and pi will live between these. If you want, use cardboard to cover the gap around the spacers to prevent light from leaking out.
   - Make sure the pi is glued to the back of the board safely enough that you can easily access the microusb and the hdmi cable to it.
   - Plug the power source back in, plug the HDMI back in and lets get started with setting our lights!
4. Programming - Software Part B
   - If youve made it this far, congrats, lets light it up and see where we messed up..
   - Remember that IP that we set before? Get it out, we are going to use that IP as our interface now
   - On any web browser, go to that ip with an additional port 3333 `192.168.0.12:3333` but use the ip you wrote down!
   - You should see an interface appear, it will ask for the ip, NOTE: I use cookies to store the IP in the browser. Closing the browser is fine, but when you clear the cookies, we are going to lose the ip! (Not all the work that we are about to do though, that will be saved on the device) For the record, that ip you wrote down is the ip of the site, maybe bookmark it so you dont lose it.
   - click setup on the map and continue from there! You will need to input each airport you want to add in order of the map. The setup process is rather intuitive so just take it from there!

Thats it! Thanks for checking this out!
