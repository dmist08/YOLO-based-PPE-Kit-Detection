import os

# Folder paths
base_dir = "./Dataset/labels"
splits = ["train", "val", "test"]

# Mapping from original class IDs → new class IDs
id_map = {
    0: 0,   # helmet
    2: 1,   # vest
    3: 2,   # boots
    7: 3,   # no_helmet
    10: 5,  # no_boots
}

for split in splits:
    split_dir = os.path.join(base_dir, split)
    if not os.path.exists(split_dir):
        continue

    for fname in os.listdir(split_dir):
        if not fname.endswith(".txt"):
            continue
        path = os.path.join(split_dir, fname)
        with open(path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue
            old_id = int(parts[0])
            if old_id in id_map:
                parts[0] = str(id_map[old_id])
                new_lines.append(" ".join(parts))

        with open(path, "w") as f:
            f.write("\n".join(new_lines))

print("✅ Label remapping complete! Only 6 classes kept (helmet, vest, boots, no_helmet, no_vest, no_boots).")

