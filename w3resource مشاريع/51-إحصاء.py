import cProfile
import pstats

def my_function():
    # الكود المراد تجربته
    for i in range(1000000):
        pass
def hi_world ():
    print("Hi,world" *2000)
    

# عمل ملف شخصي (للتحليل)
profiler = cProfile.Profile()
profiler.enable()
my_function()
profiler.disable()
hi_world()
profiler.enable()
# تكوين شكل إحصائي لفهم الحل من خلال الإحصاء الموجود في ملف ئcprofile
stats = pstats.Stats(profiler)

# تكوين شكل نهائي
stats.print_stats()
