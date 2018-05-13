void forward(int fwdTime, int waitTime) {
	motor[bl] = 10;
	wait1Msec(fwdTime);
	motor[bl] = 0;
	wait1Msec(waitTime);
}

forward(123, 34524);

forward(123)