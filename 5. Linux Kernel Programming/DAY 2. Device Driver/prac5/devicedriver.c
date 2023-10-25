//app 에서 보낸 read() systeam call 에 data를 전송하는 device driver 샘플 코드
//fops 구조체의 .read 를 추가해서 함수를 등록한다.
//__user 매크로를 사용해서 user 영역의 메모리 공간임을 명시한다.

#include <linux/module.h>
#include <linux/printk.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/device.h>

#define NOD_NAME "deviceFile"

MODULE_LICENSE("GPL");

static int NOD_MAJOR;		
static struct class *cls;   

static int deviceFile_open(struct inode *inode, struct file *filp){
    pr_info("Open Device\n");
    return 0;
}

static int deviceFile_release(struct inode *inode, struct file *filp){
    pr_info("Close Device\n");
    return 0;
}

//read() syscall 에 의해 동작하는 함수
//__user 매크로를 사용해서 user 영역의 메모리 공간임을 명시한다.
static ssize_t deviceFile_read(struct file *filp, char __user *buf, size_t count, loff_t *pos){
	buf[0] = 'H';
	buf[1] = 'I';
	buf[2] = '\n';
	pr_info("Write data!\n");	
	return count;
}

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = deviceFile_open,
    .release = deviceFile_release,
    //.read 
    .read = deviceFile_read,
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
