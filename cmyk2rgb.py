import torch

def cmyk2rgb(cmyk_tensor):
    # Assuming the input tensor has shape (batch_size, channels, height, width)
    
    # Extracting individual color channels
    c, m, y, k = torch.chunk(cmyk_tensor, 4, dim=0)
    print(cmyk_tensor.shape)
    print(c.shape,m.shape,y.shape,k.shape)
    
    # Calculating RGB values
    r = 1 - c*(1 - k)
    g = 1 - m*(1 - k)
    b = 1 - y*(1 - k)
    
    # Stacking RGB channels
    rgb_tensor = torch.cat([r, g, b], dim=0)
    
    return rgb_tensor