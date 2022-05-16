def convert_labels(image, box):
    '''
    Definition: Parses label files to extract label and bounding box
    coordinates. Converts (x1, y1, x1, y2) KITTI format to
    (x, y, width, height) normalized YOLO format.
    '''
    x1, y1, x2, y2 = box

    def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin

    size = [image['height'], image['width']]
    xmax, xmin = sorting(x1, x2)
    ymax, ymin = sorting(y1, y2)

    dw = 1./size[1]
    dh = 1./size[0]
    
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh

    return (x,y,w,h)