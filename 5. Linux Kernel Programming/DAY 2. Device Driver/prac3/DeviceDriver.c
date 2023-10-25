//mknod 유틸리티 사용하지 않고, device_create(), class_create() 를 사용해 device File 을 생성한 디바이스 드라이버 샘플 코드
//device.h 를 이용해, 장치파일을 생성, 관리한다.
//read용 api 를 추가 생성하여 fops에 등록하여, cat 명령어를 이용해 메시지를 출력한다.

#include <linux/module.h>
#include <linux/printk.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/device.h>   //device file 관리용 header
     
#define NOD_NAME "deviceFile"

MODULE_LICENSE("GPL");

static int NOD_MAJOR;       //device file 의 major num 를 담을 변수
static struct class *cls;   //device file 생성을 위한 class

static int deviceFile_open(struct inode *inode, struct file *filp){
    pr_info("Open Device\n");
    return 0;
}

static int deviceFile_release(struct inode *inode, struct file *filp){
    pr_info("Close Device\n");
    return 0;
}

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = deviceFile_open,
    .release = deviceFile_release,
};

static int __init deviceFile_init(void)
{
    //register_chrdev() 의 첫번째 매개변수는 major num, 0으로 지정하면, 커널이 동적으로 할당한다.
    //return 값이 major num 이다.
    NOD_MAJOR = register_chrdev(0, NOD_NAME, &fops);  
    if( NOD_MAJOR < 0 ){
        pr_alert("Register File\n");
        return NOD_MAJOR;
    }

    pr_info("Insmod Module\n");

    //device file를 관리해주는 class 생성
    //device file 생성
    cls = class_create(THIS_MODULE, NOD_NAME);
    device_create(cls, NULL, MKDEV(NOD_MAJOR, 0), NULL, NOD_NAME);

    pr_info("Major number %d\n", NOD_MAJOR);
    pr_info("Device file : /dev/%s\n", NOD_NAME);

    return 0;
}

static void __exit deviceFile_exit(void)
{
    //device file 해제
    device_destroy(cls, MKDEV(NOD_MAJOR, 0));
    class_destroy(cls);

    unregister_chrdev(NOD_MAJOR, NOD_NAME);
    pr_info("Unload Module\n");
}

module_init(deviceFile_init);
module_exit(deviceFile_exit);
