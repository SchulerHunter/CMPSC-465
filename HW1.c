#include <stdio.h>
struct MixedData
{
    float Data1;
    double Data2;
    char Data3;
    int Data4[5];
    double Data5[2];
} MixedData;
int main(void) {
    printf("%i", sizeof(MixedData));
}