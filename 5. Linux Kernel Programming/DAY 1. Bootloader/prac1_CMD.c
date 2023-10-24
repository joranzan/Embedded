#include <common.h>
#include <command.h>
#include <stdio.h>
#include <linux/delay.h>

static int do_bbq(struct cmd_tbl *cmdtp, int flag, int argc,
		   char *const argv[])
{
	for(int i=0; i<10; i++){
		printf("BBQ!!!\n");
		mdelay(300);
	}
	printf("====FINISH====\n\n");

	return 0;
}

U_BOOT_CMD(
	bbq, CONFIG_SYS_MAXARGS, 0, do_bbq,
	"BBQ Delicious!!!!!!!!!",
	"\n"
	"BBQ!! 10times"
);