//sample3 코드와 동일, insmod / rmmod 시 deviceFile 생성해주는 커널 모듈 형식의 device driver 샘플코드
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

//read() syscall 에 의해 동작하는 함수
//__user 매크로를 사용해서 user 영역의 메모리 공간임을 명시한다.
static ssize_t deviceFile_read(struct file *filp, char __user *buf, size_t count, loff_t *pos){
	buf[0]='G';
	buf[1]='O';
	buf[2]='O';
	buf[3]='D';
	buf[4]='!';

	buf[5]='\n';
	pr_info("app msg : %s", buf);
	return count;
}

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = deviceFile_open,
    .release = deviceFile_release,
	.read = deviceFile_read,
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

    pr_info("[Hanjun Cho]\n");

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
    pr_info("[BYE BYE Embedded Developers]\n");
}

module_init(deviceFile_init);
module_exit(deviceFile_exit);
