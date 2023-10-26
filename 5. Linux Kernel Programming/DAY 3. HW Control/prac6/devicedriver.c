#include <linux/module.h>
#include <linux/printk.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/device.h>
#include <linux/uaccess.h>
#include <linux/gpio.h>
#include <linux/interrupt.h>

#define NOD_NAME "deviceFile"

MODULE_LICENSE("GPL");

static int NOD_MAJOR;
static struct class *cls;

#define BTN 2
#define DEV_NAME "BTN"

static int irq_num;
static int app_pid;
static struct kernel_siginfo sig_info;
static struct task_struct *task;

static irqreturn_t btn_handler(int irq, void* data){
    pr_info("%s pressed!\n", DEV_NAME);

    if( app_pid>0 ){
        task = pid_task(find_vpid(app_pid), PIDTYPE_PID);
        if( task ){
            pr_info("Find app!\n");
            send_sig_info(SIGIO, &sig_info, task);
            pr_info("Send Signal\n");
        }
    }

    return IRQ_HANDLED;
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
            app_pid = (int)arg;
            pr_info("PID : %d\n", app_pid);
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
	
    gpio_request(BTN, "BTN");
    irq_num = gpio_to_irq(BTN);
    gpio_direction_input(BTN);
    int ret = request_irq(irq_num, btn_handler, IRQF_TRIGGER_FALLING, DEV_NAME, NULL);

    return 0;
}

static void __exit deviceFile_exit(void)
{
    free_irq(irq_num, DEV_NAME);
    gpio_free(BTN);

    device_destroy(cls, MKDEV(NOD_MAJOR, 0));
    class_destroy(cls);

    unregister_chrdev(NOD_MAJOR, NOD_NAME);
    pr_info("Unload Module\n");
}

module_init(deviceFile_init);
module_exit(deviceFile_exit);
