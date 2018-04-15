#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<unistd.h>
#include<dirent.h>

char default_path[1024] = "/proc/";
int s = 0;

typedef struct file_info {
	int pid;
	int ppid;
	char name[1024];
	int flag;
	int rec;
}info;

int my_getpid(char* str) {
	int len = strlen(str);
	char num[10];
	int i, j, ret;
	if (strncmp(str, "pid", 3) == 0) {
		for (i = 0; i < len; i++) {
			if (str[i] >= '0' && str[i] <= '9')
				break;
		}
		for (j = 0; j < len - i; j++) {
			num[j] = str[i + j];
		}
		ret = atoi(num);
	}
	else 
		ret = 0;
	return ret;
}

int my_getppid(char *str) {
	int len = strlen(str);
	char num[10];
	int i, j, ret;
	if (strncmp(str, "PPid", 4) == 0) {
		for (i = 0; i < len; i++) {
			if (str[i] >= '0' && str[i] <= '9')
				break;
		}
		for (j = 0; j < len - i; j++) {
			num[j] = str[i + j];
		}
		ret = atoi(num);
	}
	else
		ret = 0;
	return ret;
}
int child_exist(info *file, int count, int ppid) {
	int i;
	for (i = 0; i < count; i++) {
		if (file[i].flag == 0 && file[i].ppid == ppid)
			return 1;
	}
	return 0;
}
int main() {
	int i, j, k, total, s1, s2, count, t;
	char str[1024], dir[1024];
	struct dirent **namelist;
	strcpy(dir, default_path);
	total = scandir(dir, &namelist, 0, alphasort);
	printf("path = %s, total = %d\n", dir, total);
	for (i = 0; i < total; i++) {
		strcpy(str, namelist[i]->d_name);
		if (str[0] >= '0' && str[0] <= '9') count++;
	}
	printf("½ø³ÌÊý:%d\n", count);
	info file[1024];
	i = 0; t = 0;
	while (i < total) {
		FILE *fp;
		char path[1024], name[1024];
		int pid, ppid;
		strcpy(str, namelist[i]->d_name);
		strcpy(path, default_path);
		if (str[0] >= '0' && str[0] <= '9') {
			strcat(path, str);
			strcat(path, "/status");
			fp = fopen(path, "r");
			while (!feof(fp)) {
				fgets(str, 1024, fp);
				if ((s1 = my_getpid(str)) != 0) pid = s1;
				if ((s2 = my_getppid(str)) != 0) ppid = s2;
				if (strncmp(str, "Name", 4) == 0) {
					for (j = 4; j < strlen(str); j++) {
						if (str[j] >= 'a' && str[j] <= 'z') break;
					}
					for (k = j; k < strlen(str); k++) {
						name[k - j] = str[k];
						name[k - j - 1] = '\0';
					}
					file[t].pid = pid;
					file[t].ppid = ppid;
					strcpy(file[t].name, name);
				}
				fclose(fp);
				t++;
			}
			i++;
		}
		memset(&file->flag, 0, count);
		memset(&file->rec, 0, count);
		print_pstree(file, count, 0, 0);
	}
}