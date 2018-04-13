
train = {
    "machine_index": 1,

    "train_tfrecords_filename":
        ["/home/rafael/Documents/unicamp/ic/src/data/train/tfr/fs_fnorm/*",
         "/home/panda/ic/data/train/raw_rgb/*",
         "/home/storage_local/panda/data/train/train_raw_rgb.tfrecords"],

    "val_tfrecords_filename":
        ["/home/rafael/Documents/unicamp/ic/src/data/val/tfr/val_fs_fnorm_rgb.tfrecords",
         "/home/panda/ic/data/val/val_raw_rgb.tfrecords",
         "/home/storage_local/panda/data/val/val_raw_rgb.tfrecords"],

    "save_model_dir":
        ["/home/rafael/Documents/unicamp/ic/src/save",
         "home/panda/ic/save"
         "/home/storage_local/panda/save"],

    "load_model_dir":
        [None,
         None,
         None],

    "result_dir":
        [None,
         "/home/panda/ic/results",
         None],

    "writer_dir":
        ["/home/rafael/Documents/unicamp/ic/src/log",
         "/home/panda/ic/log",
         "/home/storage_local/panda/log"],

    "val_result_file":
        ["/home/rafael/Documents/unicamp/ic/src/log/val_results.txt",
         "/home/panda/ic/log/val_results.txt",
         "/home/storage_local/panda/log/val_results.txt"],

    "train_result_file":
        ["/home/rafael/Documents/unicamp/ic/src/log/train_results.txt",
         "/home/panda/ic/log/train_results.txt",
         "/home/storage_local/panda/log/train_results.txt"],

    "status_file":
        ["/home/rafael/Documents/unicamp/ic/src/log/status.txt",
         "/home/panda/ic/log/status.txt",
         "/home/storage_local/panda/log/status.txt"],

    "num_epochs": 500,
    "batch_size": 5,
    "image_height": 135,
    "image_width": 240,
    "input_channels": 3,
    "label_channels": 1,
    "val_epochs": 1
}



eval = {
    "tfrecords_filename": "/home/rafael/Documents/unicamp/ic/src/data/test/tfr/test1_of_1.tfrecords",
    "load_model_dir": "/home/rafael/Documents/unicamp/ic/src/save",
    "num_epochs": 1,
    "batch_size": 1,
    "image_height": 135,
    "image_width": 240,
    "input_channels": 3,
    "label_channels": 1
}
