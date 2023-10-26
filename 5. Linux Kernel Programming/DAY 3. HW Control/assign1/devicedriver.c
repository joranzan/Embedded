#include <linux/module.h>
#include <linux/printk.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/device.h>
#include <linux/uaccess.h>
#include <linux/gpio.h>
#include <linux/delay.h>
#include <linux/timer.h>

#define NOD_NAME "deviceFile"

MODULE_LICENSE("GPL");



static int NOD_MAJOR;
static struct class *cls;

#define LED 14

struct Node{
	int num1;
	int num2;
	int num3;
	int num4;
};

struct Node readData;


static void ledon(void){
    gpio_set_value(LED,1);
}
static void ledoff(void){
    gpio_set_value(LED,0);
}



static int deviceFile_open(struct inode *inode, struct file *filp){
    pr_info("Open Device\n");
    return 0;
}

static int deviceFile_release(struct inode *inode, struct file *filp){
    pr_info("Close Device\n");
    return 0;
}

static ssize_t deviceFile_ioctl(struct file *filp, unsigned int cmd, unsigned long arg){
    pr_alert("command number : %d\n", cmd);
   	
    unsigned int sum;
	unsigned int flickNum;
    int ret;  
    switch(cmd){
        case _IO(0,3):
			ret = copy_from_user(&readData, (void*)arg, sizeof(struct Node));
			pr_info("Recieved 4 Numbers from User\n");

			break;
		case _IO(0,4):

			sum = readData.num1 + readData.num2 + readData.num3 + readData.num4; 
			pr_info("Transfer sum of 4 Numbers to User Space\n");
			ret = copy_to_user((void*)arg, &sum, sizeof(unsigned int));
			break;

		case _IO(0,5):
			ret = copy_from_user(&flickNum, (void*)arg, sizeof(unsigned int));
			pr_info("LED Start\n");
			for(int i=0;i<flickNum;i++){
				ledon();
				msleep(300);
				ledoff();
				msleep(300);
			}
			pr_info("LED Finished\n");
			break;
    }
    return 0;
}

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = deviceFile_open,
    .release = deviceFile_release,
    .unlocked_ioctl = deviceFile_ioctl,
};

static int __init deviceFile_init(void)
{
    NOD_MAJOR = register_chrdev(NOD_MAJOR, NOD_NAME, &fops);
    if( NOD_MAJOR < 0 ){
        pr_alert("Register File\n");
        return NOD_MAJOR;
    }

    pr_info("Insmod Module\n");

    cls = class_create(THIS_MODULE, NOD_NAME);
    device_create(cls, NULL, MKDEV(NOD_MAJOR, 0), NULL, NOD_NAME);

    pr_info("Major number %d\n", NOD_MAJOR);
    pr_info("Device file : /dev/%s\n", NOD_NAME);

    return 0;
}

static void __exit deviceFile_exit(void)
{
    device_destroy(cls, MKDEV(NOD_MAJOR, 0));
    class_destroy(cls);

    unregister_chrdev(NOD_MAJOR, NOD_NAME);
    pr_info("Unload Module\n");
}

module_init(deviceFile_init);
module_exit(deviceFile_exit);
