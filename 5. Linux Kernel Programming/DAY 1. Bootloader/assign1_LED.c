#include <common.h>
#include <command.h>
#include <stdio.h>
#include <linux/delay.h>
#include <asm/gpio.h>
#include <string.h>

#define LED 18

static void ledon(void){
	gpio_set_value(LED,1);
	printf("LED ON!\n");
}
static void ledoff(void){
	gpio_set_value(LED,0);
	printf("LED OFF!\n");
}

static int do_kfc(struct cmd_tbl *cmdtp, int flag, int argc,
		   char *const argv[])
{
	if( argc > 2 ){
		printf("Usage : kfc option\n");
		return 0;
	}
	
	gpio_request(LED,"LED");
	gpio_direction_output(LED,0);

	char *const num = argv[1];
	if( (*num) == '1' ){
		ledon();
	}
	else if( (*num)=='2' ){
 		ledoff();
	}
	else if( (*num)=='3' ){
		for(int i=0; i<3; i++){
			ledon();
			mdelay(500);
			ledoff();
			mdelay(500);
		}
	}
	else {
		printf("Invalid option. please check kfc command.\n");
	}
	
	gpio_free(LED);
	return 0;
}

U_BOOT_CMD(
	kfc, CONFIG_SYS_MAXARGS, 0, do_kfc,
	"LED WORLD!",
	"\n"
	"kfc 1 : turn on led\n"
	"kfc 2 : turn off led\n"
	"kfc 3 : blink led\n"
	"Embedded GREAT!\n\n"
);