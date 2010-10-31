def format_alternatives(alts):
    output = "<alternatives>\n"
    for alt in alts:
        output += "\t<alternative id=\"%s\">\n" % alt
        output += "\t\t<active>true</active>\n"
        output += "\t</alternative>\n"
    output += "</alternatives>\n"
    return output

def format_affectations(affectations):
    output = "<alternativesAffectations>\n"
    for alternative, category in affectations.iteritems():
        output += "\t<alternativeAffectation>\n"
        output += "\t\t<alternativeID>%s</alternativeID>\n" % alternative
        output += "\t\t<categoryID>%s</categoryID>\n" % category
        output += "\t</alternativeAffectation>\n"
    output += "</alternativesAffectations>\n"
    return output

def format_criteria(criteria):
    output = "<criteria>\n"
    for criterion in criteria:
        output += "\t<criterion id=\"%s\"></criterion>\n" % criterion
    output += "</criteria>\n"
    return output

def format_categories(categories):
    output = "<categories>\n"
    for category in categories:
        output += "\t<category id=\"%s\">\n" % category
        output += "\t\t<active>true</active>\n"
        output += "\t</category>\n"
    output += "</categories>\n"
    return output

def format_performances_table(perfs_table):
    output = "<performanceTable>\n"
    for alternative, perfs in perfs_table.iteritems():
        output += "\t<alternativePerformances>\n"
        output += "\t\t<alternativeID>%s</alternativeID>\n" % alternative
        for criterion, value in perfs.iteritems():
            output += "\t\t<performance>\n"
            output += "\t\t\t<criterionID>%s</criterionID>\n" % criterion
            output += "\t\t\t<value><real>%s</real></value>\n" % value
            output += "\t\t</performance>\n"
        output += "\t</alternativePerformances>\n"
    output += "</performanceTable>\n"
    return output

def add_xmcda_tags(xml_data):
    output = '<?xml version="1.0" encoding="UTF-8"?>\n'
    output += '<?xml-stylesheet type="text/xsl" href="xmcdaXSL.xsl"?>\n'
    output += '<xmcda:XMCDA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.decision-deck.org/2009/XMCDA-2.0.0 file:../XMCDA-2.0.0.xsd" xmlns:xmcda="http://www.decision-deck.org/2009/XMCDA-2.0.0" instanceID="void">\n'
    output += xml_data
    output += "</xmcda:XMCDA>\n"
    return output