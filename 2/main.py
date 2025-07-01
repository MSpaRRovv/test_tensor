import json
import random

def generate_version(template):
    parts = []
    for part in template.split("."):
        if part == "*":
            parts.append(str(random.randint(0, 9)))
        else:
            parts.append(part)
    return ".".join(parts)

def compare_version(v1, v2):
    parts1 = list(map(int, v1.split(".")))
    parts2 = list(map(int, v2.split(".")))

    max_len = max(len(parts1), len(parts2))
    parts1 += [0] * (max_len - len(parts1))
    parts2 += [0] * (max_len - len(parts2))

    for part1, part2 in zip(parts1, parts2):
        if part1 < part2:
            return -1
        elif part1 > part2:
            return 1
    return 0

version = input("Введите версию: ").strip()
config_file = input("Введите имя файла (name.json): ").strip()

with open(config_file) as f:
    templates = json.load(f)

    all_version = []
    for name, template in templates.items():
        versions = sorted([generate_version(template) for _ in range(2)], key=lambda v: [int(p) for p in v.split(".")])
        print(f"{name}: {template} -> {', '.join(versions)}")
        all_version.extend(versions)

    sorted_version = sorted(all_version, key = lambda v: [int(p) for p in v.split(".")])
    older_version = [v for v in sorted_version if compare_version(v, version) == -1]


    print(f"Все остортированные версии: ")
    for versions in sorted_version:
        print(versions)

    print(f"Версии старше {version}: ")
    for version in older_version:
        print(version)
 