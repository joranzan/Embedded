#include <linux/module.h>
#include <linux/printk.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/device.h>
#include <linux/uaccess.h>
#include <asm/io.h>

#define NOD_NAME "deviceFile"

MODULE_LICENSE("GPL");

static int NOD_MAJOR;
static struct class *cls;

static volatile uint32_t *BASE;
static volatile uint32_t *GPFSEL1;
static volatile uint32_t *GPSET0;
static volatile uint32_t *GPCLR0;

static void ledon(void){
    *GPSET0 = (1<<14);
}
static void ledoff(void){
    *GPCLR0 = (1<<14);
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
    switch(cmd){
        case _IO(0,3):
		pr_info("LED ON\n");
		ledon();
		break;
        case _IO(0,4):
		pr_info("LED OFF\n");
		ledoff();
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
	
    BASE = (uint32_t*)ioremap(0xFE200000, 256);
    GPFSEL1 = BASE + (0x04 / 4);
    GPSET0 = BASE + (0x1C / 4);
    GPCLR0 = BASE + (0x28 / 4);
	
    *GPFSEL1 &= ~(0x7 << 12);
    *GPFSEL1 |= (1 << 12);	

    return 0;
}

static void __exit deviceFile_exit(void)
{
    ledoff();	
    iounmap(BASE);
    device_destroy(cls, MKDEV(NOD_MAJOR, 0));
    class_destroy(cls);

    unregister_chrdev(NOD_MAJOR, NOD_NAME);
    pr_info("Unload Module\n");
}

module_init(deviceFile_init);
module_exit(deviceFile_exit);
