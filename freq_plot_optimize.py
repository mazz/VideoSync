import freq_plot

def optimize(audio_filepath, delay):  # change to video_path input, delay in sec
    best_scenario = []
    # audio = freq_plot.extract_audio("HipVsRhy.mp4")
    # audio = freq_plot.extract_audio("HipClip.mp4")
    audio = freq_plot.read_audio("GoldWAV.wav")

    # Sample size
    audio_base = audio[44100*21:44100*45]
    audio_sample = audio[44100*(21+delay):44100*45]

    # Bin overlap
    for i in range(99):
        overlap = float(i)/float(100)
        proc_base = freq_plot.process_audio(audio_base, 1024, 1024*overlap)
        proc_sample = freq_plot.process_audio(audio_sample, 1024, 1024*overlap)

        pairs_base = freq_plot.pairs(proc_base)
        pairs_sample = freq_plot.pairs(proc_sample)

        freqs_base = freq_plot.freq_list(pairs_base)
        freqs_sample = freq_plot.freq_list(pairs_sample)

        # Number of freqs summed
        for j in range(5, 15):
            # Matching tolerance of freqs summed
            for k in range(50, 200):
                start_points = freq_plot.find_start(freqs_base, freqs_sample, j, k)
                alignment = freq_plot.best_start(freqs_base, freqs_sample, start_points)







# ===== OPTIMIZE TEST ========

# b0 = freq_plot.read_audio("GoldWAV.wav")
# b1 = b0[44100*21:44100*45]
# b2 = process_audio(b1, 1024, 1024*.75)
# b3 = pairs(b2)
# b5 = freq_list(b3)
# b4 = sorted(b2.items(), key=lambda x: x[1])
# plot_d(b2)

# soundc = extract_audio("HipVsRhy.mp4")
# c0 = read_audio("HipVsRhyWAV.wav")
# c1 = b0[44100*24:44100*45]
# c2 = process_audio(c1, 1024, 1024*.75)
# c3 = pairs(c2)
# c5 = freq_list(c3)
# plot_d(c2)
# compare(c3, b3, 5, 20)


# start_points = find_start(b5, c5, 9, 90)
# print "start points:", start_points
# alignment = best_start(b5, c5, start_points)
# print "alignment: ", alignment


# dist, cost, path = mlpy.dtw_std(r5, s5, dist_only=False)
# dtw.line_start(path[0], path[1], 50)  # c1 is smaller sample
# fig = plt.figure(1)
# ax = fig.add_subplot(111)
# plot1 = plt.imshow(cost.T, origin='lower', cmap=cm.gray, interpolation='nearest')
# plot2 = plt.plot(path[0], path[1], 'w')

# xlim = ax.set_xlim((-0.5, cost.shape[0]-0.5))
# ylim = ax.set_ylim((-0.5, cost.shape[1]-0.5))
# plt.show()


# ========== MLPY TEST ==========================
# dist, cost, path = mlpy.dtw_std(r5, s5, dist_only=False)
# dtw.line_start(path[0], path[1], 50)  # c1 is smaller sample
# fig = plt.figure(1)
# ax = fig.add_subplot(111)
# plot1 = plt.imshow(cost.T, origin='lower', cmap=cm.gray, interpolation='nearest')
# plot2 = plt.plot(path[0], path[1], 'w')

# xlim = ax.set_xlim((-0.5, cost.shape[0]-0.5))
# ylim = ax.set_ylim((-0.5, cost.shape[1]-0.5))
# plt.show()


# ===== FUZZY STRING MATCHING TEST ===========
# r4 = fuzzy_list(r2)
# letters_dictionary = letters_dict(r2, s2)
# r4 = list_from_letters_dict(letters_dictionary, r3)
# s4 = list_from_letters_dict(letters_dictionary, s3)
# print fuzz.partial_ratio(r4, s4)