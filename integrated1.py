import split_on_silence_main
import try6
import clear_files
import prediction
import tkinter as tk



'''def add_to_path(number, name):
    path = "C:\\Users\\Lakshminagaraj\\Documents\\Pramod\\ML project\\testset_new\\"
    if not os.path.exists(path + number + "\\" + name + "_" + number + ".wav"):
            write_wav(path + "{}\\{}_{}.wav".format(number, name, number), prediction_X[predictions.index(pre)], 22500)
    else:
            write_wav(path + "{}\\{}_{}.wav".format(number, name + str(random.randrange(2, 100000)), number), prediction_X[predictions.index(pre)], 22500)
'''

main_ui = tk.Tk()
main_ui.geometry("1000x500")
main_ui.title("Speech Recognition")
path = "C:\\Users\\Lakshminagaraj\\Documents\\Pramod\\ML project\\SplitOnSilenceFiles"
clear_files.clear(path)
total_files = split_on_silence_main.sos()
tk.Label(main_ui, text = str(total_files) + " files exported").place(relx = 0.25, rely = 0.5, anchor = tk.CENTER)
predictions, prediction_X = prediction.predict()
predictions = list(predictions)
tk.Button(main_ui, text = "See Results", command = prediction.tkWindow).place(relx = 0.75, rely = 0.5, anchor = tk.CENTER)
tk.Button(main_ui, text = 'Done', command = main_ui.destroy).place(relx = 0.5, rely = 0.75, anchor = tk.CENTER)
main_ui.mainloop()


'''name = input("Enter your name")
count = 0
for pre in predictions:
    number = numbers[pre]
    num = num_list[pre]
    ans = input("Was the number {}. Enter y / n: ".format(number))
    if ans == 'y':
        add_to_path(number, name)
        count += 1
    elif ans == 'n':
        number = input("What was the actual number: ")
        add_to_path(number, name)
print("Prediction accuracy: {}".format(count / total_files))'''