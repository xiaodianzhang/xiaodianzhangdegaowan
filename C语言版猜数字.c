#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
int 随机数(int 最大值) {

    int r = rand() % 最大值 + 1;
    return r;
}

int main() {
    srand((unsigned)time(NULL));
    int 连续输入 = 0;
    int 机会 = 10;
    int 最大值 = 100000;
    int 目标数 = 随机数(最大值);
    int 目标数保存 = 目标数;
    int 玩家输入的数;
    char 缓冲[114514];
    char 余数;
    int 提二 = 0;
    printf("这是一个猜数字游戏（注意：请输入数字）接下来会有一些效果输入对应的数字来获得它\n如果你不想要任何的效果你可以输入一些其他的数字");
    printf("\n\n\n");
    printf("1.额外7次猜测机会\n2.猜测次数变为100000提示变成🤪\n3.得知目标数的奇偶\n4.下一页");
    fgets(缓冲,sizeof(缓冲),stdin);
    if(sscanf(缓冲,"%d",&玩家输入的数) == 1 && 玩家输入的数 == 1){
    机会 += 7;
    }
    if(sscanf(缓冲,"%d",&玩家输入的数) == 1 && 玩家输入的数 == 2){
    提二 = 1;
    机会 = 100000;
    }
    if(sscanf(缓冲,"%d",&玩家输入的数) == 1 && 玩家输入的数 == 3){
    if(目标数 % 2 == 0){
    printf("目标数是偶数\n");
    }else{
    printf("目标数是奇数\n");
    }
    }
    if(sscanf(缓冲,"%d",&玩家输入的数) == 1 && 玩家输入的数 == 114514){
    printf("👁\n");
    机会 = 114514;
    提二 = 2;
    }
    if(sscanf(缓冲,"%d",&玩家输入的数) == 1 && 玩家输入的数 == 4){
    printf("1.你的猜测次数变为30每次你猜之后目标数会再次变化\n你会获得这个目标数是更大了还是更小了的提示");
    fgets(缓冲,sizeof(缓冲),stdin);
    int 选择;
    if(sscanf(缓冲,"%d",&玩家输入的数) == 1 && 玩家输入的数 == 1){
    机会 = 30;
    提二 = 3;
    }
    }
    
    
    
    
   
    
    while (1) {
    
        if(机会 <= 0 && 提二 == 2){
        printf("👁?\n");
        break;
        }
        else if(机会 <= 0) {
            printf("次数用完了🥺目标数是:%d",目标数);
            break;
        }
        
        if(提二 == 2){
        printf("你还有👁次机会");
        printf("猜1到100000之间的数\n");
        }
        else if(提二 != 1 && 提二 != 2){
        printf("你还有%d次机会",机会);
        printf("猜1到100000之间的数\n");
        }else if(提二 == 1){
        printf("你还有🤪次机会");
        printf("猜🤪到🤪的数\n");
        }
        fgets(缓冲,sizeof(缓冲),stdin);
        if(sscanf(缓冲,"%d%c",&玩家输入的数,&余数) == 2 && 余数 == '\n'){
        if(提二 == 0 && 玩家输入的数 > 最大值 || 提二 == 0 && 玩家输入的数 < 1){
        if(连续输入 == 0){
        printf("🤔你输入的数超过了最小值或是最大值");
        }if(连续输入 == 1){
        printf("🤨...你输入的数超过了最小值或是最大值");
        }if(连续输入 == 2){
        printf("🥺你输入的数超过了最小值或最大值");
        }if(连续输入 == 3){
        printf("算了不管你了😵你输入的数超过了最小值或最大值");
        }
        连续输入++;
        continue;
        }
        
        
        
        
        
        
        
        if (提二 == 1 && 玩家输入的数 != 目标数){
        if(玩家输入的数 < 目标数){
        printf("🥺\n");
        }else if(玩家输入的数 > 目标数){
        printf("🤪\n");
        }
        
        }
        else if(提二 == 2){
        if(玩家输入的数 < 目标数){
        printf("👁\n");
        }else if(玩家输入的数 > 目标数){
        printf("👁👁\n");
        }else if(玩家输入的数 == 目标数){
        printf("👁👍\n");
        }
        }
        else if (玩家输入的数 < 目标数) {
            printf("\n小了\n");
        }
        else if (玩家输入的数 > 目标数) {
            printf("\n大了\n");
        }
        else if (玩家输入的数 == 目标数) {
            printf("\n✓\n");
            break;
        }
        }else{
        printf("\n🥺请输入数字🥺\n");
        continue;
        }
        机会--;
        if (连续输入 < 3){
        连续输入 = 0;
        }
        if(提二 == 3){
        目标数保存 = 目标数;
        目标数 = 随机数(最大值);
        if(目标数保存 < 目标数){
        printf("目标数更大了,大了%d",目标数 - 目标数保存);
        }else if(目标数保存 > 目标数){
        printf("目标数更小了,小了%d",目标数保存 - 目标数);
        }else if(目标数保存 == 目标数){
        printf("目标数不变");
    }
    }
    }
    
    
    return 0;

}