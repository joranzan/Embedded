#include <linux/module.h>
#include <linux/printk.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/device.h>
#include <linux/uaccess.h>
#include <linux/gpio.h>

#define NOD_NAME "deviceFile"

MODULE_LICENSE("GPL");

static int NOD_MAJOR;
static struct class *cls;

#define LED 14
#define BTN 2

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

int lev;
int ret;
static ssize_t deviceFile_ioctl(struct file *filp, unsigned int cmd, unsigned long arg){
    switch(cmd){
        case _IO(0,3):
		    pr_info("LED ON\n");
		    ledon();
		    break;
        
	case _IO(0,4):
		    pr_info("LED OFF\n");
		    ledoff();
		    break;

	case _IO(0,5):
		    lev = gpio_get_value(BTN);
		    pr_info("btn = %d\n", lev);
		    ret = copy_to_user((void*)arg, &lev, sizeof(int));
		    break;	

	default :
		    return -EINVAL;
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
    NOD_MAJOR = register_chrdev(0, NOD_NAME, &fops);
    if( NOD_MAJOR < 0 ){
        pr_alert("Register File\n");
        return NOD_MAJOR;
    }

    pr_info("Insmod Module\n");

    cls = class_create(THIS_MODULE, NOD_NAME);
    device_create(cls, NULL, MKDEV(NOD_MAJOR, 0), NULL, NOD_NAME);

    pr_info("Major number %d\n", NOD_MAJOR);
    pr_info("Device file : /dev/%s\n", NOD_NAME);
	
    gpio_request(LED, "LED");
    gpio_direction_output(LED, 0);

    gpio_request(BTN, "BTN");
    gpio_direction_input(BTN);

    return 0;
}

static void __exit deviceFile_exit(void)
{
    gpio_set_value(LED,0);
    gpio_free(LED);
    gpio_free(BTN);

    device_destroy(cls, MKDEV(NOD_MAJOR, 0));
    class_destroy(cls);

    unregister_chrdev(NOD_MAJOR, NOD_NAME);
    pr_info("Unload Module\n");
}

module_init(deviceFile_init);
module_exit(deviceFile_exit);
