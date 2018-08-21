本程序主要是满足局域网故障排查，让网络工程师解放双手不再重复工作。

使用前提：

1.需要一个规范的网络规划，ip地址主机使用规则 ，要求全网规则一样才可以进行更改使用，另外这个版本紧紧只有 ssh才可以  telnet的 我没写 因为比较简单
而且一般交换机都支持ssh  大家更改下即可。

2.其中的super密码是 h3c的 去掉代码就可以通用了

3.结合trace数据可以对接前端进行画图以及信息反馈，总体来说就是小聪明，瞎玩。


4.使用案例：
输入源ip地址:10.253.1.139
输入目的ip地址:10.253.2.10


结果：

 1  bogon (10.253.241.97)  1.408 ms
 2  10.253.241.138 (10.253.241.138) [AS 65105]  48.004 ms
 3  *
 4  *
 5  *
 6  *
!Destination not found inside Max Hop Count.

交换机网关到目的主机ip测试结果:

--- Ping statistics for 10.253.2.10 ---
5 packet(s) transmitted, 0 packet(s) received, 100.0% packet loss

交换机网关到目的主机网关测试结果:

--- Ping statistics for 10.253.2.62 ---
5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss
round-trip min/avg/max/std-dev = 1.575/1.792/2.244/0.245 ms
