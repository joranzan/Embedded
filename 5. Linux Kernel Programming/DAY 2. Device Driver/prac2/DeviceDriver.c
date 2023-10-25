#include <linux/module.h>
#include <linux/printk.h>
#include <linux/init.h>
#include <linux/fs.h>   //fops 구조체 사용을 위한 헤더

#define NOD_MAJOR 100   //device file MAJOR num
#define NOD_NAME "deviceFile"

MODULE_LICENSE("GPL");

//devicefile open 시 호출
static int deviceFile_open(struct inode *inode, struct file *filp){ 
    pr_info("Open Device\n");
    return 0;
}

//devicefile close 시 호출
static int deviceFile_release(struct inode *inode, struct file *filp){ 
    pr_info("Close Device\n");
    return 0;
}

//구조체 지정초기화를 이용한 fops 구조체 초기화
static struct file_operations fops = {  
    .owner = THIS_MODULE,
    .open = deviceFile_open,
    .release = deviceFile_release,
};

static int __init deviceFile_init(void)
{
    int ret = register_chrdev(NOD_MAJOR, NOD_NAME, &fops);  //chrdev를 모듈에 등록
    if( ret < 0 ){
        pr_alert("Register File\n");
        return ret;
    }

    pr_info("Insmod Module\n");
    return 0;
}

static void __exit deviceFile_exit(void)
{
    unregister_chrdev(NOD_MAJOR, NOD_NAME);
    pr_info("Unload Module\n");
}

module_init(deviceFile_init);
module_exit(deviceFile_exit);
