from maya import cmds


def getNumCVs(curve):
    """
    :param str curve:
    :return: Number of cvs
    :rtype: int
    """
    # get attributes
    spans = cmds.getAttr("{}.spans".format(curve))
    degree = cmds.getAttr("{}.degree".format(curve))
    form = cmds.getAttr("{}.form".format(curve))

    # get num cvs
    numCVs = spans + degree

    # adjust for closed curve
    if form == 2:
        numCVs -= degree

    return numCVs


def clusterCurve(curve):
    """
    :param str curve:
    :return: Clusters
    :rtype: list
    """
    clusters = []
    numCVs = getNumCVs(curve)

    # Loop over CVs
    for i in range(numCVs):
        cluster = cmds.cluster("{}.cv[{}]".format(curve, i))[-1]
        clusters.append(cluster)

    return clusters
