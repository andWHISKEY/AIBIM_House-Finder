"""Data processing utilities."""

import json
import numpy as np
import random
import torch

def set_seed(random_seed=42):
    torch.manual_seed(random_seed)
    torch.cuda.manual_seed(random_seed)
    torch.cuda.manual_seed_all(random_seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # np.random.seed(random_seed)
    random.seed(random_seed)

def process_pair(path):
    """
    Reading a json file with a pair of graphs.
    :param path: Path to a JSON file.
    :return data: Dictionary with data.
    """
    try:
        data = json.load(open(path))
    except:
        print(path)   
    return data


def calculate_normalized_ged(data):
    """
    Calculating the normalized GED for a pair of graphs.
    :param data: Data table.
    :return norm_ged: Normalized GED score.
    """
    norm_ged = data["ged"]/100.0 
    return norm_ged


def transfer_to_torch(data,global_labels):
        """
        Transferring the data to torch and creating a hash table.
        Including the indices, features and target.
        :param data: Data dictionary.
        :return new_data: Dictionary of Torch Tensors.
        """
        new_data = dict()
        edges_1 = data["graph_1"]

        edges_2 = data["graph_2"]

        edges_1 = torch.from_numpy(np.array(edges_1, dtype=np.int64).T).type(torch.long)
        edges_2 = torch.from_numpy(np.array(edges_2, dtype=np.int64).T).type(torch.long)

        features_1, features_2 = [], []

        for n in data["labels_1"]:
            features_1.append([1.0 if global_labels[n] == i else 0.0 for i in global_labels.values()])

        for n in data["labels_2"]:
            features_2.append([1.0 if global_labels[n] == i else 0.0 for i in global_labels.values()])

        features_1 = torch.FloatTensor(np.array(features_1))
        features_2 = torch.FloatTensor(np.array(features_2))

        new_data["edge_index_1"] = edges_1
        new_data["edge_index_2"] = edges_2

        new_data["features_1"] = features_1
        new_data["features_2"] = features_2


        norm_ged = data["ged"]/100.0
        new_data["target"] = torch.from_numpy(1 - np.exp(-norm_ged).reshape(1, 1)).view(-1).float()

        return new_data