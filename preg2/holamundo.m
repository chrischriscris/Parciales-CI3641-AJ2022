#import <Foundation/Foundation.h>
#import <pthread.h>

int main(int argc, const char *argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    NSLog (@"hello world");
    [pool drain];
    return 0;
}
