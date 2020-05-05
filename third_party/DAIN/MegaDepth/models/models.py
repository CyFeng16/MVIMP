from .HG_model import HGModel


def create_model(opt, pretrained=None):
    model = None

    model = HGModel(opt, pretrained)
    # print("model [%s] was created" % (model.name()))
    return model
