import torch
from torch_geometric.nn import GCNConv
from layers import AttentionModule, TenorNetworkModule

# --------------------------------------------------------------------------------
# Student model
# --------------------------------------------------------------------------------

class Student(torch.nn.Module): 
    def __init__(self, args,device):
        super().__init__()
        self.args = args
        self.device=device
        self.number_labels = 21
        self.feature_count = self.args.tensor_neurons
        self.convolution_1 = GCNConv(self.number_labels, self.args.filters_1)
        self.convolution_2 = GCNConv(self.args.filters_1, self.args.filters_3)
        self.tensor_network = TenorNetworkModule(self.args)
        self.fully_connected_first = torch.nn.Linear(self.feature_count,
                                                     self.args.bottle_neck_neurons)
        self.scoring_layer = torch.nn.Linear(self.args.bottle_neck_neurons, 1)
        self.sigmoid = torch.nn.Sigmoid()    
        
    
    def layermodule(self,features,edge_index):
        features=self.convolution_1(features,edge_index)
        features = torch.nn.functional.relu(features)
        features = torch.nn.functional.dropout(features,
                            p=self.args.dropout,
                            training=self.training)

        features=self.convolution_2(features, edge_index)
        features=features.mean(dim=0,keepdim=True)
        features=torch.transpose(features, 0, 1)

        return features


    def forward(self, data):
        edge_index_1 = data["edge_index_1"].to(self.device)
        edge_index_2 = data["edge_index_2"].to(self.device)
        features_1 = data["features_1"].to(self.device)
        features_2 = data["features_2"].to(self.device)


        features_vector_1=self.layermodule(features_1,edge_index_1)
        features_vector_2=self.layermodule(features_2,edge_index_2)
        return features_vector_1,features_vector_2

    def embedded_forward(self, embedding_vector1, embedding_vector2):
        scores = self.tensor_network(embedding_vector1, embedding_vector2)
        scores = torch.t(scores)

        scores = torch.nn.functional.relu(self.fully_connected_first(scores))
        score = self.sigmoid(self.scoring_layer(scores))
        return score    
        
# --------------------------------------------------------------------------------
# Teacher model(SimGNN) 
# --------------------------------------------------------------------------------

class SimGNN(torch.nn.Module):
    def __init__(self,args,device):
        super(SimGNN,self).__init__()
        self.device=device
        self.args = args
        self.number_labels = 21
        self.setup_layers()
            
    def setup_layers(self):
        """
        Creating the layers.
        """
        self.feature_count = self.args.tensor_neurons
        self.convolution_1 = GCNConv(self.number_labels, self.args.filters_1)
        self.convolution_2 = GCNConv(self.args.filters_1, self.args.filters_2)
        self.convolution_3 = GCNConv(self.args.filters_2, self.args.filters_3)
        self.attention = AttentionModule(self.args)
        self.tensor_network = TenorNetworkModule(self.args)
        self.fully_connected_first = torch.nn.Linear(self.feature_count,
                                                     self.args.bottle_neck_neurons)
        self.scoring_layer = torch.nn.Linear(self.args.bottle_neck_neurons, 1)
        self.sigmoid = torch.nn.Sigmoid()    


    def convolutional_pass(self, edge_index, features):
        """
        Making convolutional pass.
        :param edge_index: Edge indices.
        :param features: Feature matrix.
        :return features: Absstract feature matrix.
        """
        
        features = self.convolution_1(features, edge_index)
        features = torch.nn.functional.relu(features)
        features = torch.nn.functional.dropout(features,
                                               p=self.args.dropout,
                                               training=self.training)
        features = self.convolution_2(features, edge_index)
        features = torch.nn.functional.relu(features)
        features = torch.nn.functional.dropout(features,
                                               p=self.args.dropout,
                                               training=self.training)
        features = self.convolution_3(features, edge_index)
        return features

    def forward(self, data):
        """
        Forward pass with graphs.
        :param data: Data dictiyonary.
        :return score: Similarity score.
        """
        edge_index_1 = data["edge_index_1"].to(self.device)
        edge_index_2 = data["edge_index_2"].to(self.device)
        features_1 = data["features_1"].to(self.device)
        features_2 = data["features_2"].to(self.device)
        abstract_features_1 = self.convolutional_pass(edge_index_1, features_1)
        abstract_features_2 = self.convolutional_pass(edge_index_2, features_2)

        pooled_features_1 = self.attention(abstract_features_1)
        pooled_features_2 = self.attention(abstract_features_2)
        scores = self.tensor_network(pooled_features_1, pooled_features_2)
        scores = torch.t(scores)

        scores = torch.nn.functional.relu(self.fully_connected_first(scores))
        score = self.sigmoid(self.scoring_layer(scores))
        return score,pooled_features_1,pooled_features_2
    
    def embedded_forward(self, embedding_vector1, embedding_vector2):
        scores = self.tensor_network(embedding_vector1, embedding_vector2)
        scores = torch.t(scores)

        scores = torch.nn.functional.relu(self.fully_connected_first(scores))
        score = self.sigmoid(self.scoring_layer(scores))
        return score


