function getCenterOfRoute(route) {
    maxmin = getMaxMins(route);
    x1 = maxmin[0];
    x2 = maxmin[1];
    y1 = maxmin[2];
    y2 = maxmin[3];
    return getCenter(x1, x2, y1, y2);
}

function getCenter(xmin, xmax, ymin, ymax) {
    center = [xmin + ((xmax - xmin) / 2),
             ymin + ((ymax - ymin) / 2)];
    return center;
}

function maxmin(route) {
    mm = [];
    for(r in route) {
        if( r.type = 'Feature') {

        }
    }
    return mm;
}