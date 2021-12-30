from func_mods import *

cross_check = True      ## Cross-Check parameter is here for safety(so that system cannot go out of memory) Change it if needed

logo = '''

  ___                                                                              
 /                   /    /                /  | /                / /               
(___       ___  ___ (___    ___  ___      (   |   ___       ___ (    ___  ___  ___ 
|    |   )|   )|    |    | |   )|   )      \  )| |___ |   )|   )| |  __/ |___)|   )
|    |__/ |  / |__  |__  | |__/ |  /        \/ |  __/ |__/ |__/|| | /__  |__  |    
                                                                                   

'''

print(logo)

print("It Should be in format Ex -")
print("(2x\u00b2 + 5x - 5) --> 2x^2 + 5x^1 - 5")
print("Spaces are required between terms as shown.")
print("X-Range: Give a No. and it will make x-range from -no. to +no.")
print("Warning: as big you give the range then it will take that much time.")
print("Warning: Don't give too much big range because the images first saves in computer so it could lead to crash system because of out of memory.")
print("Precision: how detailed you want the graph at deafult it is 1 but you can decrease or increase it.")
print("Warning: Don't give too much small no because the images first saves in computer so it could lead to crash system because of out of memory.")
print("But How: Assum if u choose x-range as 400 and precision as 0.1 then total point will be to about 400*2/0.1 = 8000")
print("means you will be ploting 8000 images then saving those images and then making the video of it then they will be deleted so about it before doing too much.")
func = input("Expression: ")
x_range = int(input("X-Range: "))
precision = float(input("Precision: "))

## cross-check for safety(You could make it change but Not Recommended).
if cross_check:
    if x_range > 1000 and precision < 0.5:
        sys.exit(0)

try:
    os.mkdir("tmp")
except:
    shutil.rmtree("tmp")
    os.mkdir("tmp")
func = make_function(make_func_properties(func))
make_plots_images(func, x_range, precision)
make_plot_video()
shutil.rmtree("tmp")