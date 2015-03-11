__author__ = 'gsibble'

def determine_routes(recipients):
    groups_of_recipients = []
    group_count = len(recipients) / 25
    if len(recipients) / 25 > 0:
        for groups_of_25 in xrange(0, len(recipients), 25):
            groups_of_recipients.append(recipients[groups_of_25:groups_of_25+25])
    else:
        groups_of_recipients = [recipients]

    if check_routes_of_appropriate_size(groups_of_recipients) == True:
        return groups_of_recipients

    temp_groups_of_recipients = []
    for index, group in enumerate(groups_of_recipients[group_count:]):
        for groups_of_10 in xrange(0, len(group), 10):
            temp_groups_of_recipients.append(group[groups_of_10:groups_of_10+10])
    groups_of_recipients = groups_of_recipients[:group_count]
    for group in temp_groups_of_recipients:
        groups_of_recipients.append(group)
    group_count = group_count + len(temp_groups_of_recipients)

    if check_routes_of_appropriate_size(groups_of_recipients) == True:
        return groups_of_recipients

    temp_groups_of_recipients = []
    for index, group in enumerate(groups_of_recipients[group_count:]):
        for groups_of_5 in xrange(0, len(group), 5):
            temp_groups_of_recipients.append(group[groups_of_5:groups_of_5+5])
    groups_of_recipients = groups_of_recipients[:group_count]
    for group in temp_groups_of_recipients:
        groups_of_recipients.append(group)
    group_count = group_count + len(temp_groups_of_recipients)

    if check_routes_of_appropriate_size(groups_of_recipients) == True:
        return groups_of_recipients

    temp_groups_of_recipients = []
    for index, group in enumerate(groups_of_recipients[group_count-1:]):
        if len(group) > 5:
            for groups_of_1 in xrange(5, len(group), 1):
                temp_groups_of_recipients.append([group[groups_of_1]])
        else:
            for groups_of_1 in xrange(0, len(group), 1):
                temp_groups_of_recipients.append([group[groups_of_1]])
    groups_of_recipients = groups_of_recipients[:group_count-1]
    for group in temp_groups_of_recipients:
        groups_of_recipients.append(group)

    return groups_of_recipients

def check_routes_of_appropriate_size(routes):
    all_routes_acceptable = True
    for route in routes:
        if len(route) not in [25, 10, 5, 1]:
            all_routes_acceptable = False
    return all_routes_acceptable

def determine_ips_for_routes(numbers):
    ip_set = []
    twenty_five_server_count = 0
    ten_server_count = 0
    five_server_count = 0
    one_server_count = 0
    for number_set in numbers:
        if len(number_set) == 25:
            twenty_five_server_count += 1
            ip_set.append(
                {'ip': '10.0.4.' + str(twenty_five_server_count),
                 'recipients': number_set}
            )
        elif len(number_set) == 10:
            ten_server_count += 1
            ip_set.append(
                {'ip': '10.0.3.' + str(ten_server_count),
                 'recipients': number_set}
            )
        elif len(number_set) == 5:
            five_server_count += 1
            ip_set.append(
                {'ip': '10.0.2.' + str(five_server_count),
                 'recipients': number_set}
            )
        elif len(number_set) == 1:
            one_server_count += 1
            ip_set.append(
                {'ip': '10.0.1.' + str(one_server_count),
                 'recipients': number_set}
            )
        else:
            raise ValueError('Invalid number of recipients')
    return ip_set

def check_with_37_numbers():
    routes = determine_routes(range(0, 42))
    print determine_ips_for_routes(routes)

if __name__ == '__main__':
    check_with_37_numbers()