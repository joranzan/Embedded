#include "hal_data.h"
#include <stdio.h>

FSP_CPP_HEADER
void R_BSP_WarmStart(bsp_warm_start_event_t event);
FSP_CPP_FOOTER

/*******************************************************************************************************************//**
 * main() is generated by the RA Configuration editor and is used to generate threads if an RTOS is used.  This function
 * is called by main() when no RTOS is used.
 **********************************************************************************************************************/
void delay(int ms){
    R_BSP_SoftwareDelay(ms, BSP_DELAY_UNITS_MILLISECONDS);
}

volatile i2c_master_event_t g_i2c_callback_event;
void sci_i2c_master_callback(i2c_master_callback_args_t *p_args)
{
    g_i2c_callback_event = p_args->event;
}

void hal_entry(void)
{
    uint8_t addr = 0;       //I2C 통신으로 읽어올 주소 값 담을 변수
    uint8_t buf[100] = {0}; //data 담을 변수

    while(1){
        addr = 0x0;         //초 값이 들어 있는 주소 0x0
        R_SCI_I2C_Write(&g_i2c9_ctrl, &addr, 1, true);  //addr에 있는 data를 1byte만 읽자.
                                                        //DS3231은 해당 I2C 통신으로 초 값을 반환함.
        while( g_i2c_callback_event != I2C_MASTER_EVENT_TX_COMPLETE );

        memset(buf, 0, sizeof(buf));
        R_SCI_I2C_Read(&g_i2c9_ctrl, buf, 1, false);    //buf 에 1 byte data를 읽어 저장. 통신 끝
        while( g_i2c_callback_event != I2C_MASTER_EVENT_RX_COMPLETE );

        printf("%s\r\n", buf);
        delay(500);
    }
}
/*******************************************************************************************************************//**
 * This function is called at various points during the startup process.  This implementation uses the event that is
 * called right before main() to set up the pins.
 *
 * @param[in]  event    Where at in the start up process the code is currently at
 **********************************************************************************************************************/
void R_BSP_WarmStart(bsp_warm_start_event_t event)
{
    if (BSP_WARM_START_RESET == event)
    {

    }

    if (BSP_WARM_START_POST_C == event)
    {
        /* C runtime environment and system clocks are setup. */

        /* Configure pins. */
        R_IOPORT_Open (&g_ioport_ctrl, g_ioport.p_cfg);
        R_SCI_UART_Open(&g_uart0_ctrl, &g_uart0_cfg);
        R_SCI_I2C_Open(&g_i2c9_ctrl, &g_i2c9_cfg);
    }
}
