import argparse
import time
import numpy as np
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


if __name__ == '__main__':

    # Parse command-line entries
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_trials', type=int, nargs='+', action='store', dest='num_trials', default=20)
    parser.add_argument('--cue_delay', type=int, nargs='+', action='store', dest='cue_delay', default= 2)
    # parser.add_argument('--cue_duration', type=int, nargs='+', action='store', dest='cue_duration', default=1)

    args = parser.parse_args()

    # Extract command-line parameters
    num_trials = args.num_trials
    cue_delay = args.cue_delay
    # cue_duration = args.cue_duration

    CUE_LIST = ['Rest', 'Left', 'Right', 'Up', 'Down']
    ACTIVE_CUES = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]

    Rand_Cues = np.random.permutation(ACTIVE_CUES)
    Rest_Cues = np.zeros((32,1))

    # print(Rand_Cues)
    # print(Rest_Cues)

    for count_tr in range(len(Rest_Cues)):
        if count_tr % 2 != 0: # the odd trial
            Rest_Cues[count_tr] = Rand_Cues[int(np.floor(count_tr / 2))]

    print(Rest_Cues)

    # Download cue images
    print('Importing cue images...', end='', flush=True)
    cue_images = {}
    #cue_img = tuple(cue_images)


    # for cue in CUE_LIST:
    #     img = mpimg.imread(r"C:\Users\ErikG\OneDrive - University of Central Florida\Erik_Guier\VR 3rd Arm\Code" + "\\" + cue + ".png")
    #     cue_images[cue] = img

    # Define cue images
    Rest_img = mpimg.imread(r"C:\Users\ErikG\OneDrive - University of Central Florida\Erik_Guier\VR 3rd Arm\Code\Rest.png")
    Left_img = mpimg.imread(r"C:\Users\ErikG\OneDrive - University of Central Florida\Erik_Guier\VR 3rd Arm\Code\Left.png")
    Right_img = mpimg.imread(r"C:\Users\ErikG\OneDrive - University of Central Florida\Erik_Guier\VR 3rd Arm\Code\Right.png")
    Up_img = mpimg.imread(r"C:\Users\ErikG\OneDrive - University of Central Florida\Erik_Guier\VR 3rd Arm\Code\Up.png")
    Down_img = mpimg.imread(r"C:\Users\ErikG\OneDrive - University of Central Florida\Erik_Guier\VR 3rd Arm\Code\Down.png")

    print('Starting show...\n', flush=True)

    i = 0
    
    cue_fig = plt.figure()
    plt.ion()
    print(cue_delay)
    cue_times = np.zeros((len(Rest_Cues), 1))
    while i <= len(Rest_Cues) - 1:
        print(i)
        if Rest_Cues[i] == 0:
            # Set up the cue image
            Cue_Name = Rest_img
            #plt.imshow(mpimg.imread(cue_images[cue]))
            plt.clf()
            plt.imshow(Cue_Name)
            plt.axis('off')
            plt.show(block=False)

            # Wait through the delay
            t0 = time.perf_counter()

            while (time.perf_counter() - t0) < cue_delay:
                 cue_fig.canvas.flush_events()

        elif Rest_Cues[i] == 1:
            # Set up the cue image
            Cue_Name = Up_img
            #plt.imshow(mpimg.imread(cue_images[cue]))
            plt.clf()
            plt.imshow(Cue_Name)            
            plt.axis('off')
            plt.show(block=False)

            # Wait through the delay
            t0 = time.perf_counter()
            while (time.perf_counter() - t0) < cue_delay:
                 cue_fig.canvas.flush_events()

        elif Rest_Cues[i] == 2:
            # Set up the cue image
            Cue_Name = Down_img
            #plt.imshow(mpimg.imread(cue_images[cue]))
            plt.clf()
            plt.imshow(Cue_Name)
            plt.axis('off')
            plt.show(block=False)

            # Wait through the delay
            t0 = time.perf_counter()
            while (time.perf_counter() - t0) < cue_delay:
                 cue_fig.canvas.flush_events()

        elif Rest_Cues[i] == 3:
            # Set up the cue image
            Cue_Name = Left_img
            #plt.imshow(mpimg.imread(cue_images[cue]))
            plt.clf()
            plt.imshow(Cue_Name)
            plt.axis('off')
            plt.show(block=False)

            # Wait through the delay
            t0 = time.perf_counter()
            while (time.perf_counter() - t0) < cue_delay:
                 cue_fig.canvas.flush_events()
            # Increment i

        elif Rest_Cues[i] == 4:
            # Set up the cue image
            Cue_Name = Right_img
            #plt.imshow(mpimg.imread(cue_images[cue]))
            plt.clf()
            plt.imshow(Cue_Name)
            plt.axis('off')
            plt.show(block=False)

            # Wait through the delay
            t0 = time.perf_counter()
            while (time.perf_counter() - t0) < cue_delay:
                 cue_fig.canvas.flush_events()
        

        cue_times[i] = t0
        if i>0:
            print(cue_times[i] - cue_times[i-1])
        #increment i
        i += 1


    print("End of experiment")




