import os
import sys

def turn_to_numbers(str_values, mult):
    # Turn a list of strings into a list of numbers.
    return [float(number)*mult for number in str_values.split()]

def temporal_regions(file_path, regions, type_opt, output_path):
    '''
        Create temporal regions from a given file.
        Such regions divide a video equally in number of frames.

        :param str file_path: Path to the file containing the list of frames and their specific classes.
        :param int regions: Number of regions intended to divide a video.
        :param str type_opt: Type of region division: either "concat" or "mean"
        :param str output_path: Path to the file where the new dataset (divided into regions) will be placed. Can be none.
        :return: void
    '''
    file_tail = "_temporal_regions_" + type_opt + "_" + str(regions) + ".txt" # Create the tail for the output file.

    if not output_path:
        # If output_path equal to None.
        output_path = file_path[:-4] + file_tail
    else:
        output_path = os.path.join(output_path, os.path.splitext(file_path)[0].split('/')[-1]) + file_tail
    output_file = open(output_path, 'w')
    file_lines = open(file_path, 'r').readlines()

    n_lines = len(file_lines)

    segments = dict()
    rows = dict()

    for index, line in enumerate(file_lines):
        # Get data and save into dictionaries.    
        main_line = line.split()
        output_row = ' '.join(main_line[:2]) # Get the line part that will remain in the output file.
        main_probs = ' ' + ' '.join(main_line[2:])  # Get the predicted probabilities (or features) for the frame.
        file_name = main_line[0]    # The first element of file's line must be the path for the frame.
        
        # Process file name to extract a key.
        # This process is hardcoded and may change according to the dataset being used.
        # Although it may seem useless, it is extremely important to obtain this information.
        # Based on the frame numbers and their classes, we can identify the video length.
        new_key = file_name.split('/')[7] # Get the video identifier.
        frame_number = file_name.split('/')[-1].split('_')[-1].split('.')[0] # Obtain frame's number.
        
        if not segments.has_key(new_key):
            # Add the video identifier to the dictionary.
            segments[new_key] = dict()
            rows[new_key] = dict()
    
        segments[new_key][frame_number] = main_probs # To that specific frame, save its probs.
        rows[new_key][frame_number] = output_row    # Save its file path and class.
        
    for key in segments:
        # Write regions.
        segment_frames = len(segments[key].keys())
        # frames_ordered = [int(frame) for frame in segments[key].keys()]
        frames_ordered = sorted(segments[key].keys())
        
        # In the end, we must have a of frames equal or higher than regions.
        if segment_frames >= regions:            
            per_region = segment_frames / regions # Save the number of frames per region.
        else:
            print "Can't use this, it has the following length: ", segment_frames
            continue

        regions_dict = dict()

        for i in range(regions):
            # Create regions.
            regions_dict[i] = dict()

            for frame in frames_ordered[:per_region]:
                regions_dict[i][frame] = (rows[key][frame], segments[key][frame]) # Attribute a tuple with the frame path, its class, and its features.
            frames_ordered = frames_ordered[per_region:] # Update the frames considering all except those in the new region.

        for indx, key in enumerate(sorted(regions_dict)):
            # Run over regions.

            for ind, key_2 in enumerate(sorted(regions_dict[key].keys())):
                # Run over frames for region.
                sent_to_file = regions_dict[key][str(key_2)][0] # Get the text defining the original path and class.

                if type_opt == 'concat':
                    # If concat, just glue all features in a single row.
                    sent_to_file += regions_dict[key][str(key_2)][1]
                else:
                    # Else, turn features into numbers and save them.
                    features = turn_to_numbers(regions_dict[key][str(key_2)][1], 1)
                    
                for ind2, key_3 in enumerate(sorted(regions_dict)):
                    # Run over regions again.

                    if key_3 != key:
                        n_keys = len(regions_dict[key_3]) # Get the number of frames.
                        k_keys = regions_dict[key_3].keys() # Get the frame identifiers.
                        k_keys.sort()

                        if (ind + 1) < n_keys:
                            # Check if this isn't the last frame for this particular region.
                            # If it is, take the number in the next position from other regions.
                            if type_opt == 'concat':
                                sent_to_file += regions_dict[key_3][str(k_keys[ind + 1])][1] # Concatenate the features from other frames.
                            else:
                                features = [sum(x) for x in zip(features, turn_to_numbers(regions_dict[key_3][str(k_keys[ind + 1])][1], 1))]    # Sum the features from other frames.
                            
                        else:
                            # If it is the last frame of a region, then take the first frame.                            
                            if type_opt == 'concat':
                                sent_to_file += regions_dict[key_3][str(k_keys[0])][1]
                            else:
                                features = [sum(x) for x in zip(features, turn_to_numbers(regions_dict[key_3][str(k_keys[0])][1], 1))]
                            
                if type_opt == 'mean':
                    features = [x/float(regions) for x in features] # Take the mean of all features.
                    sent_to_file += ' ' + ' '.join([str(x) for x in features]) # Arrange to save into the output file.
                
                output_file.write(sent_to_file + "\n")

    output_file.close()

if __name__ == "__main__":

    opt_list = ['concat', 'mean']

    arg_err_msg = "Please, pass a valid path, a window size as argument, and a type option, such as:\n\t- concat\n\t- mean\n"
    n_args = len(sys.argv)

    if n_args >= 4:
        # Get input arguments.
        file_path = sys.argv[1]
        regions = sys.argv[2]
        type_opt = sys.argv[3]
        if n_args == 5:
            output_path = sys.argv[4]
        else:
            output_path = None

        try:
            regions = int(regions)
        except:
            print arg_err_msg + "\nNot a valid window size."
            sys.exit()

        if not os.path.isfile(file_path):
            print arg_err_msg + "\nNot a valid path."
        
        if type_opt in opt_list:
            temporal_regions(file_path, regions, type_opt, output_path)

        else:
            print arg_err_msg + "\nNot a valid type option."

    else:

        if n_args < 4:
            print arg_err_msg + "\nToo few arguments."
        else:
            print arg_err_msg + "\nToo many arguments."
